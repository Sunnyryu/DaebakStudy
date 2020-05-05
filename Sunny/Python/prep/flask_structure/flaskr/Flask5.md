# Flask study 

#### 해당 폴더에 있는 샘플을 참조하기!

##### 요청 컨텍스트

```
1. 요청 컨텍스트

컨텍스트 로컬로 다이빙하기
여러분이 사용자를 리디렉트해야하는 URL을 반환하는 유틸리티 함수를 갖는다고 하자. 그 함수는 항상 URL의 next 인자나 HTTP referer 또는 index에 대한 URL을 리디렉트한다고 가정.

ex)
from flask import request, url_for

def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')
여러분이 볼 수 있는 것처럼, 그것은 요청 객체를 접근, 여러분은 플레인 파이썬 쉘에서 이것을 실행하면, 여러분은 아래와 같은 예외를 볼 것임

>>> redirect_url()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'request'
우리가 현재 접근할 수 있는 요청을 갖고 있지 않기 때문에 그것은 이해가 됌, 그래서 우리는 요청을 만들고 그것을 현재 컨텍스트에 연결시켜야 함, test_request_context 메소드는 우리에게 RequestContext 를 만들어 줄 수 있음.

>>> ctx = app.test_request_context('/?next=http://example.com/')
이 컨텍스트는 두 가지 방식으로 사용될 수 있음, with 절과 함께 사용되거나 push() 와 pop() 메소드를 호출하여 사용됨!

>>> ctx.push()
이 시점부터 여러분은 요청 객체를 가지고 작업할 수 있음.

>>> redirect_url()
u'http://example.com/'
pop 함수를 호출할 때까지

>>> ctx.pop()
요청 컨텍스트는 내부적으로 스택을 유지하기 때문에 여러분은 여러번 push와 pop을 할 수 있다. 이것이 내부적인 리디렉트와 같은 것을 손쉽게 구현한 것임.

2. 컨텍스트가 작동하는 방식
여러분이 플라스크 WSGI 어플리케이션이 내부적으로 동작하는 방식을 살펴보려면, 아래와 대단히 유사한 코드를 찾게될 것임.
ex)
def wsgi_app(self, environ):
    with self.request_context(environ):
        try:
            response = self.full_dispatch_request()
        except Exception, e:
            response = self.make_response(self.handle_exception(e))
        return response(environ, start_response)
request_context() 메소드는 새로운 RequestContext 객체를 반환하고 컨텍스트를 연결하기 위해 with 구문과 조합하여 RequestContext 객체를 사용함. 이 시점부터 with 구문의 끝까지 같은 쓰레드에서 호출되는 모든 것은 요청 글로벌 객체( flask.request 와 기타 다른것들)에 접근할 수 있을 것임.

요청 컨텍스트도 내부적으로 스택처럼 동작, 스택의 가장 상위에는 현재 활성화된 요청이 있음. push() 는 스택의 제일 위에 컨텍스트를 더하고, pop() 은 스택으로부터 제일 상위에 있는 컨텍스트를 제거함. 컨텍스트를 제거하는 pop 동작 시, 어플리케이션의 teardown_request() 함수 또한 실행

주목할 다른 것은 요청 컨텍스트가 들어오고 그때까지 해당 어플리케이션에 어떠한 어플리케이션 컨텍스트가 없었다면, 자동으로 application context 또한 생성할 것이라는 것임.

3.콜백과 오류

각 요청 전에, before_request() 함수들이 수행됨, 이런 함수들 중 하나라도 응답을 반환하면, 다른 함수들은 더 이상 호출되지 않음. 
그러나 어떤 경우라도 반환값은 뷰의 반환값에 대한 대체값으로 처리됨.
before_request() 함수들이 응닶을 반환하지 않는다면, 보통 요청 처리가 시작되고 요청에 맞는 뷰 함수가 응답을 반환하게 됌.
그리고 나서, 뷰의 반환값은 실제 응답 객체로 변환되고 응답 객체를 대체하거나 변경할 준비가 되있는 after_request() 함수로 전달함
요청의 종료 시에는 teardown_request() 함수가 실행된다. 이 함수는 심지어 처리되지 않는 예외의 경우나 before-request 핸들러가 아직 처리되지 않거나 전혀 실해되지 않는 경우에도 항상 발생 (예를 들면, 테스트 환경에서 때때로 before-request 콜백이 호출되지 않기를 원할수도 있음)
자 오류가 발생하면 무슨일이 발생하는가? 운영 환경에서는 예외가 처리되지 않으면, 500 내부 서버 핸들러가 실행됨. 그러나, 개발 환경에서는 예외는 더 진행되지 않고 WSGI 서버로 영향을 끼침. 대화형 디버거와 같은 방식에서는 도움되는 디버깅 정보를 제공할 수 있음.

새로운 teardown 함수는 요청의 마지막에서 반드시 행이 필요한 경우에 대체할 목적으로 사용되는 것을 가정함

4.테어다운(Teardown) 콜백
테어다운 콜백은 특별한 콜백인데 여러 다른 시점에 실행되기 때문임. 엄격하게 말하자면, 그것들이 RequestContext 객체의 생명주기와 연결되있긴 하지만, 그것들은 실제 요청 처리와 독립되있으며, 요청 문맥이 꺼내질 때, teardown_request() 함수는 호출됨.

with 구문이 있는 테스트 클라이언트를 사용하여 요청 문맥의 생명이 범위가 늘었는지 또는 명령줄에서 요청 문맥을 사용할 때를 아는 것이 중요함

ex)
with app.test_client() as client:
    resp = client.get('/foo')
    # the teardown functions are still not called at that point
    # even though the response ended and you have the response
    # object in your hand

# only when the code reaches this point the teardown functions
# are called.  Alternatively the same thing happens if another
# request was triggered from the test client
명령줄에서 이 동작을 보기는 쉬움

ex)
>>> app = Flask(__name__)
>>> @app.teardown_request
... def teardown_request(exception=None):
...     print 'this runs after request'
...
>>> ctx = app.test_request_context()
>>> ctx.push()
>>> ctx.pop()
this runs after request
>>>
before-request 콜백은 아직 실행되지 않고 예외가 발생했더라도,teardown 콜백은 항상 호출된다는 것을 명심해라. 테스트 시스템의 어떤 부분들 또한 before-request 핸들러를 호출하지 않고 일시적으로 요청 문맥을 생성할지도 모름, 절대로 실패하지 않는 방식으로 여러분의 teardown-request 핸들러를 쓰는 것을 보장해라.

5.프록시에서 주의할 점
플라스크에서 제공하는 일부 객체들은 다른 객체에 대한 프록시들임, 이렇게 하는 뒷 배경에는 이런 프락시들이 쓰레들간에 공유되어 있고 그 프락시들이 쓰레드들에 연결된 실제 객체로 필요시에 보이지 않게 디스패치되어야 한다는 것임.

대게 여러분은 그 프락시에 대해서 신경쓰지 않아도 되지만, 이 객체가 실제 프락시인지 알면 좋은 몇 가지 예외의 경우가 있음.

프락시 객체들이 상속받은 타입을 속이지 않아서, 여러분이 실제 인스턴스를 확인한다면, 프락시로 된 인스턴스에서 타입을 확인해야함.(아래의 _get_current_object 를 보라).
객체의 참조가 중요한 경우( 시그널(Signals) 을 보내는 경우)
여러분이 프록시된 감춰진 객체에 접근할 필요가 있다면, _get_current_object() 메소드를 사용할 수 있음.

ex)
app = current_app._get_current_object() my_signal.send(app)

6. 오류 시 컨텍스트 보존
오류가 발생하거나 하지 않거나, 요청의 마지막에서 요청 문맥은 스택에서 빠지게 되고 그 문맥과 관련된 모든 데이타는 소멸됨. 하지만, 개발하는 동안 그것은 예외가 발생하는 경우에 여러분이 더 오랜 시간동안 그 정보를 갖고 있기를 원하기 때문에 문제가 될 수 있음. 

PRESERVE_CONTEXT_ON_EXCEPTION 설정 변수값을 설정하여 그 행동을 좀 더 세밀하게 설정함. 디폴트로 이 설정은 DEBUG 설정과 연결된다. 어플리케이션이 디버그 모드라면, 그 문맥은 보존되지만, 운영 모드라면 보존되지 않음.

어플리케이션이 예외 발생 시 메모리 누수를 야기할 수 있으므로 운영 모드에서 ``PRESERVE_CONTEXT_ON_EXCEPTION``을 강제로 활성화하지 않아야함, 
하지만, 개발 모드에서 운영 설정에서만 발생하는 오류를 디버그하려 할 때 개발 모드로 같은 오류 보존 동작을 얻는 것은 개발하는 동안에는 유용할 수 있음.
```

##### 블루프린트

```

블루프린트를 가진 모듈화된 어플리케이션

1
플라스크는 어플리케이션 컴포넌트를 만들고 어플리케이션 내부나 어플리케이션간에 공통 패턴을 지원하기 위해 블루프린트(blueprint) 라는 개념을 사용, 블루프린트는 보통 대형 어플리케이션이 동작하는 방식을 단순화하고 어플리케이션의 동작을 등록하기 위한 플라스크 확장에 대한 중앙 집중된 수단을 제공할 수 있음. Blueprint 객체는 Flask 어플리케이션 객체와 유사하게 동작하지만 실제로 어플리케이션은 아님, 다만 어플리케이션을 생성하거나 확장하는 방식에 대한 블루프린트임.


어플리케이션을 블루프린트의 집합으로 고려, 이 방식은 대형 어플리케이션에 있어서 이상적임.
프로젝트는 어플리케이션 객체를 인스턴스화하고, 여러 확장을 초기화하고, 블루프린트의 묶음을 등록할 수 있음.
어플리케이션 상에 URL 접두어와/또는 서브도메인으로 블루프린트를 등록, URL 접두어와/또는 서브도메인에 있는 파라메터는 블루프린트에 있는 모든 뷰 함수에 걸쳐있는 공통 뷰 인자(기본값을 가진)가 됌.
어플리케이션에 여러 URL 규칙을 가진 블루프린트를 여러번 등록,
블루프린트를 통해 템플릿 필터, 정적 파일, 템플릿, 그리고 다른 유틸리티를 제공, 블루프린트는 어플리케이션이나 뷰 함수를 구현하지 않아도 됌.
플라스크 확장을 초기화할 때 이런 경우 중 어떤 경우라도 어플리케이션에 블루프린트를 등록함.
플라스크에 있는 블루프린트는 끼우고 뺄수 있는 앱이 아니다 왜냐하면 블루프린트는 실제 어플리케이션이 아니기 때문임. 
그것은 어플리케이션에 등록될 수 있는 동작의 집합인데 심지어 여러번 등록될 수 있음,
왜 복수의 어플리케이션 객체를 가지지 않는가 -> 여러분은 그렇게(어플리케이션 디스패칭 을 살펴봐라)할 수 있지만, 어플리케이션은 분리된 설정을 가질것 이고 WSGI 계층에서 관리될 것임.

대신에 블루프린트는 플라스크 레벨에서 분리를 제공하고, 어플리케이션 설정을 공유하며, 그리고 등록된 것을 가지고 필요에 따라 어플리케이션 객체를 변경할 수 있음. 
이것의 단점은 일단 전체 어플리케이션 객체를 제거할 필요없이 어플리케이션이 생성됐을 때 여러분은 블루프린트를 해지할 수 없음.

2. 블루프린트의 개념
블루프린트의 기본 개념은 어플리케이션에 블루프린트이 등록될 때 실행할 동작을 기록한다는 것
플라스크는 요청을 보내고 하나의 끝점에서 다른 곳으로 URL을 생성할 때 뷰 함수와 블루프린트의 연관을 맺음

3.첫번째 블루프린트
아래는 가장 기본적인 블루프린트의 모습! 이 경우에 우리는 정적 템플릿을 간단하게 그려주는 블루프린트를 구현하기를 원할 것임.
ex)
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)

@simple_page.route 데코레이터와 함수를 연결할 때 블루프린트는 어플리케이션에 있는 그 함수를 등록하겠다는 의도를 기록할 것임, 게다가 블루프린트는 Blueprint 생성자(위의 경우에는 simple_page) 에 들어가는 그 이름을 가지고 등록된 함수의 끝점 앞에 붙일 것임.

4.블루프린트 등록하기
아래와 같이 등록
ex)
from flask import Flask
from yourapplication.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

여러분이 어플리케이션에 등록된 규칙을 확인한다면, 여러분은 아래와 같은 것을 찾을 것임.

ex)

[<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
 <Rule '/' (HEAD, OPTIONS, GET) -> simple_page.show>]

첫 규칙은 명시적으로 어플리케이션에 있는 정적 파일에 대한 것임. 다른 두 규칙은 
simple_page 블루프린트의 show 함수에 대한 것이먀, 볼 수 있는 것 처럼, 블루프린트의 이름이 접두어로 붙어있고 점 (.) 으로 구분되있음.

하지만 블루프린트는 또한 다른 지점으로 마운트 될 수 있음

ex)
app.register_blueprint(simple_page, url_prefix='/pages')
그리고 물론 말할 것도 없이, 아래와 같은 규칙이 생성됨 

[<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/pages/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
 <Rule '/pages/' (HEAD, OPTIONS, GET) -> simple_page.show>]

무엇보다 모든 블루프린트이 복수로 적용되는 것에 적절한 응답을 주지는 않지만 여러분은 블루프린트를 여러번 등록할 수 있음. 사실 한번 이상 블루프린트를 마운트할 수 있다면 제대로 블루프린트이 동작하느냐는 블루프린트를 어떻게 구현했으냐에 달려있음.

5.블루프린트 리소스
블루프린트는 리소스 또한 제공할 수 있으며, 때때로 여러분은 단지 리소스만을 제공하기 위해 블루프린트를 사용하고 싶을 수도 있음.

6. 블루프린트 리소스 폴더
보통 어플리케이션처럼, 블루프린트는 폴더안에 포함되도록 고려함, 다수의 블루프린트이 같은 폴더에서 제공될 수 있지만, 그런 경우가 될 필요도 없고 보통 권고하지 않음.

폴더는 보통 __name__ 인 Blueprint 에 두번째 인자로 생각됨. 이 인자는 어떤 논리적인 파이썬 모듈이나 패키지가 블루프린트과 상응되는지 알려주며, 그것이 실제 파이썬 패키지를 가리킨다면 그 패키지 (파일 시스템의 폴더인) 는 리소스 폴더임
그것이 모듈이라면, 모듈이 포함되있는 패키지는 리소스 폴더가 될 것이다. 리소스 폴더가 어떤것인지 보기 위해서는 Blueprint.root_path 속성에 접근할 수 있음.

ex)
>>> simple_page.root_path
'/Users/username/TestProject/yourapplication'

이 폴더에서 소스를 빨리 열기 위해서 여러분은 open_resource() 함수를 사용할 수 있음.

with simple_page.open_resource('static/style.css') as f:
    code = f.read()

7.정적 파일
블루프린트는 static_folder 키워드 인자를 통해서 파일시스템에 있는 폴더에 경로를 제공하여 정적 파일을 가진 폴더를 노출할 수 있음. 그것은 절대 경로이거나 블루프린트 폴더에 대해 상대 경로일 수 있음.

ex)

admin = Blueprint('admin', __name__, static_folder='static')

기본값으로 경로의 가장 오른쪽 부분이 웹에 노출되는 곳이며, 폴더는 여기서 static 이라고 불리기 때문에 블루프린트 위치 + static 으로 될 것임. 블루프린트이 /admin 으로 등록되있다고 하면 정적 폴더는 /admin/static 으로 될 것임.

끝점은 bluepirnt_name.static 으로 되고 여러분은 어플리케이션의 정적 폴더에 한 것 처럼 그 끝점에 URL을 생성할 수 있음.

ex)
url_for('admin.static', filename='style.css')

8.템플릿
여러분이 블루프린트이 템플릿을 노출하게 하고 싶다면 Blueprint 생성자에 template_folder 인자를 제공하여 노출할 수 있음.

ex)
admin = Blueprint('admin', __name__, template_folder='templates')

정적 파일에 관해서, 그 경로는 절대 경로일 수 있고 블루프린트 리소스 폴더 대비 상대적일 수 있음. 
템플릿 폴더는 템플릿 검색경로에 추가되지만 실제 어플리케이션의 템플릿 폴더보다 낮은 우선순위를 갖음. 
그런 방식으로 여러분은 블루프린트이 실제 어플리케이션에서 제공하는 템플릿을 쉽게 오버라이드 할 수 있다.

그러므로 yourapplication/admin 폴더에 블루프린트이 있고 'admin/index.html' 를 뿌려주고 template_folder 로 templates 를 제공한다면 여러분은 yourapplication/admin/templates/admin/index.html 같이 파일을 생성해야 할 것임.

9. URL 만들기
하나의 페이지에서 다른 페이지로 링크하고 싶다면 보통 블루프린트명을 접두어로 하고 점 (.) 으로 URL 끝점을 구분하는 것처럼 url_for() 함수를 사용할 수 있음.

ex)
url_for('admin.index')

추가적으로 여러분이 블루프린트의 뷰 함수에 있거나 뿌려진 템플릿에 있고 같은 블루프린트의 다른 끝점으로 링크를 걸고 싶다면, 점을 접두어로 하여 끝점에 붙여서 상대적인 리디렉션을 사용할 수 있음.

ex)
url_for('.index')

예를 들면 현재 요청을 어떤 다른 블루프린트의 끝점으로 보내는 경우에 admin.index 로 링크할 것임.

```

