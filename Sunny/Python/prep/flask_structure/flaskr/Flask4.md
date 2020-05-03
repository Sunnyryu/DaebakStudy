# Flask study 

#### 해당 폴더에 있는 샘플을 참조하기!

##### 플러거블 뷰

```
플러거블 뷰는 클래스 기반으로한 Django 프레임워크의 제네릭 뷰에 영향을 받은 플러거블 뷰(끼워넣는 뷰?)

1. 기본원칙
db에 있는 객체의 목록을 읽어서 템플릿에 보여주는 함수를 가진다고 고려!

ex)
@app.route('/users/')
def show_users(page):
    users = User.query.all()
    return render_template('users.html', users=users)

위의 예를 클래스로 바꾸자면

ex)
from flask.views import View

class ShowUsers(View):

    def dispatch_request(self):
        users = User.query.all()
        return render_template('users.html', objects=users)

app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))

flask.views.View 의 서브클래스를 만들고 dispatch_request() 를 구현해야함, 클래스를 as_view() 클레스 메소드를 사용해서 실제 뷰 함수로 변환해야함
( 함수로 전달하는 문자열은 뷰가 가질 끝점(end-point)의 이름임)

ex2)
from flask.views import View

class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

class UserView(ListView):

    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return User.query.all()

동작하는 방식은 요청이 들어올 때마다 클래스의 새 인스턴스가 생성되고 dispatch_request() 메소드가 URL 규칙으로부터 나온 인자를 가지고 호출, 클래스 그 자체로는 as_view() 함수에 넘겨지는 인자들을 가지고 인스턴스화됨!

ex)
class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name
    def dispatch_request(self):
        return render_template(self.template_name)

아래의 뷰 함수를 등록 가능해짐!
app.add_url_rule('/about', view_func=RenderTemplateView.as_view(
    'about_page', template_name='about.html'))

2. 메소드 힌트

끼워넣을 수 있는 뷰는 route()나  더 낫게는 methods() 속성 정보를 제공할 수 잇음

ex)
class MyView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            ...
        ...

app.add_url_rule('/myview', view_func=MyView.as_view('myview'))

3. 메소드 기반 디스패치

RESTful API에서 각 HTTP 메소드별로 다른 함수를 수행하는 것은 굉장히 도움이 됌!
flask.views.MethodView 로 여러분은 그 작업을 쉽게 할 수 있으며, 각 HTTP 메소드는 같은 이름을 가진 함수(소문자)로 연결

ex)
from flask.views import MethodView

class UserAPI(MethodView):

    def get(self):
        users = User.query.all()
        ...

    def post(self):
        user = User.from_form_data(request.form)
        ...

app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))

클래스에 정의된 메소드 기반으로 자동 설정


4.데코레이팅 뷰

뷰 클래스 그 자체는 라우팅 시스템에 추가되는 뷰 함수가 아니기 때문에, 클래스 자체를 데코레이팅하는 것은 이해x, 수동으로 as_view() 함수의 리턴값을 데코레이팅해야함!

ex)
def user_required(f):
    """Checks whether user is logged in or raises error 401."""
    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)
    return decorator

view = user_required(UserAPI.as_view('users'))
app.add_url_rule('/users/', view_func=view)

ex2)
class UserAPI(MethodView):
    decorators = [user_required]

호출하는 입장에서는 자체로 암시적이기 때문에, 여러분이 뷰의 개별 메소드에 일반적인 뷰 데코레이터를 사용할수 없다는 것을 명시!
5. 메소드 뷰 API

웹 API는 보통 HTTP 메소드와 매우 밀접하게 동작하는데 MethodView 기반의 API를 구현할때는 더욱 의미가 들어맞음!
URL        | Method | Description
/users/    |GET     | 전체 사용자 정보 목록 얻기
/users/	   |POST	|새로운 사용자 정보 생성
/users/<id>|GET	    | 단일 사용자 정보 얻기
/users/<id>|PUT	    |단일 사용자 정보 갱신
/users/<id>|DELETE  |단일 사용자 정보 삭제

ex)
class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            # return a list of users
            pass
        else:
            # expose a single user
            pass

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass

이것을 어떻게 라우팅 시스템으로 연결하는가? 두가지 규칙을 추가하고 명시적으로 각 메소드를 언급

ex)
user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
app.add_url_rule('/users/<int:user_id>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])

유사하게 보이는 여러 API를 갖고 있다면, 등록하는 메소드를 추가하도록 아래처럼 리팩토링할 수 있음

ex)
def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])

register_api(UserAPI, 'user_api', '/users/', pk='user_id')
``

##### 어플리케이션 컨텍스트

```



```