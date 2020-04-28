# Flask study 

#### 해당 폴더에 있는 샘플을 참조하기!

```
1. 폴더 생성 
flask의 경우 css나 js 같은 파일은 static에 저장하여 url_for 등으로 꺼내서 쓰며 html의 경우에는 templates에 저장한다.

2. 데이터 스키마!
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);

entries라는 테이블이 있다면 드롭시킴 / id는 순차적으로 증가되게 autoincrement를 시켰으며, title과 text는 null을 허용하지 않고 문자값을 가져야함!

3. application 셋업 
(.ini 나 .py로 분리하여 생성 로드하는 것이 더 좋음)
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash 
플라스크 관련 사항을 임포트를 먼저해줌!
기본적인 변수를 선언 및 app 및 app.config.from_object 나 from_envvar를 선언

클라이언트에서 세션을 안전하게 보장하기 위해서는 secret_key가 있어야함!!

운영 시스템에서는 디버그 모드 활성화를 시키지 말아야함!

if __name__ == '__main__':
    app.run()
위의 코드를 작성하여 어플리케이션을 위한 서버 실행가능!

python flask.py를 실행시키면 접속가능! 

4. sqlite를 이용한 db생성

sqlite3 /tmp/flaskr.db < schema.sql => sqlite3 명령어를 이용한 스키마 생성..

DB 초기화를 하는 함수를 추가하기 원하면 contextlib 패키지에 있는 contextlib.closing() 함수를 임포트함! 
(__future__ import with_statement를 가장 먼저 써줌)

초기화 시키는 함수는 flaskr.py의 init_db() 함수 참조!

5. db connection 요청

flask에서는 before_request(), after_request(), teardown_request() 데코레이터를 이용가능!

예시는 flaskr.db를 참조!

해당 파일에 g라는 객체가 있는데 g 객체는 각 함수들에 대해서 오직 한번의 리퀘스트에 대해서만 유효한 정보를 저장하고 있음! , 쓰레드 환경에서는 다른 객체에서 위와 같이 사용할 경우 작동이 보장되지 않음!

6. 뷰 함수 

예시 py 파일에는 작성된 글 보여주기, 새로운 글 추가, 로그인, 로그아웃을 추가하였음.

7. 템플릿

html 파일들은 templates라고 지어진 폴더에 저장하여야 플라스크에서 render_template 함수가 올바르게 값을 보내고 에러가 발생하지 않음!

8. 스타일

css파일을 따로 만들었다면 static 폴더에 두고 url_for을 이용하여 불러와서 사용하기!
```

```
1. 템플릿
플라스크는 템플릿엔진으로 jinja2를 사용한다. (플라스크의 풍부한 기능 확정을 위함!)

2.jinja2 설정 

임의로 설정하지 않는 이상 기본값으로 설정되어있음!

자동변환(autoescaping) 기능은 .html , .xml 과 .xhtml 과 같은 모든 템플릿 파일들에 대해서 기본으로 활성화되어 있음
하나의 템플릿은 in/out에 대한 자동변환(autoescape) 기능을 {% autoescape %} 태그를 이용하여 사용할 수 있음
Flask는 기본적으로 Jinja2 컨텍스트(context)를 통해서 전역 함수들과 헬퍼함수들을 제공함

3. 표준 컨텍스트 (해당 변수들은 jinja2에서 기본으로 사용가능!)

config = 현재 설정값을 가지고 있는 객체(flask.config) 

request = 현재 요청된 객체, 해당 변수는 템플릿이 활성화된 컨텍스트에서 용된 것이 아니라면 유효하지 않음

session = 현재 가지고 있는 세션 객체 (flask.session). 변수는 템플릿이 활성화된 컨텍스트에서 요청된 것이 아니라면 유효하지 않음

g = 요청에 한정되어진 전역 변수(flask.g)

url_for() = 제공된 메서드를 사용하여 지정된 끝점에 대한 URL을 생성
(쿼리 인수가 없음이면 건너뜀 , 블루프린트가 활성시 로컬 끝점을 점으로 혼합하여 동일한 블루포인트에 참조 바로가기 가능)

매개변수 - endpoint, values, _external, _scheme, _anchor, _method

flask.get_flashed_messages(with_categories=False, category_filter=[])
(세션에서 플래시 된 메시지를 모두 끌어 와 반환합니다. 기능에 대한 동일한 요청의 추가 호출은 동일한 메시지를 반환, 기본적으로 메시지만 반환되지만 with_categories가 True로 설정된 경우 반환 값은 형식의 튜플 목록이 됌!)

jinja2 작동방식 

위의 변수들은 전역변수가 아님.. 전역변수와의 차이점은 컨텍스트에서 불려진 템플릿에서는 기본적으로 보이지 않는다는 것임! (성능과 명시적 유지를 위해!)

ex) 부르고 싶은 매크로가 있을 때 요청 객체 접근하는 것이 필요함

매크로로 요청 객체를 파라미터로 명시적 전달 / 관심있는 객체에 속성값으로 가지고 있어야함!
매크로로 컨텍스트를 불러와야함! 
({% from '_helpers.html' import my_macro with context %})


4. 표준 필터

tojson() = json 표기법으로 주어진 객체를 변환하는 것임 (스크립트 태그 안에서는 변환(escaping)이 반드시 일어나서는 안되기에 |safe 필터가 script 태그 안에서 비활성화도록 해야함)

ex) <script type=text/javascript>
    doSomethingWith({{ user.username|tojson|safe }});
</script>
(|tojson 필터는 올바르게 슬래쉬들을 변환해 준다.)

5. 자동변환 (autoescaping) - 자동으로 특수 문자들을 변환
ex) HTML (혹은 XML, 그리고 XHTML) 문서 에서 &, >, <, " , ' 에 해당

=> 해당 문자들을 텍스트 그대로 사용하고 싶다면 "entities"라고 불리우는 값들로 변환해야함!

Python 코드에서는, HTML 문자열을 Markup 객체를 통해서 템플릿에 전달되기 전에 래핑한다. 이방법은 일반적으로 권장되는 방법이다.
템플릿 내부에, |safe 필터를 명시적으로 사용하여 문자열을 안전한 HTML이 되도록 한다. ({{ myvariable|safe }})
일시적으로 모두 자동변환(autoescape) 시스템을 해제한다.

ex) 템플릿에서 자동변환(autoescape) 시스템을 비활성화 하려면, {%autoescape %} 블럭 이용

{% autoescape false %}
    <p>autoescaping is disabled here
    <p>{{ will_not_be_escaped }}
{% endautoescape %}

6. 필터 등록하기

jinja_env(진자 어플리케이션 이용) 및 template_filter()를 이용하면 jinja2에서 필터를 등록할 수 있음


ex)@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

def reverse_filter(s):
    return s[::-1]
app.jinja_env.filters['reverse'] = reverse_filter

함수이름을 필터이름으로 사용하려면 데코레이터의 아규먼트는 선택조건 / 필터가 한번 등록되면 jinja2의 내장 필터를 사용하는 것과 똑같이 사용이 가능
ex) {% for x in mylist | reverse %}
{% endfor %}

7. 컨텍스트 프로세서

새로운 변수들을 자동으로 템플릿의 컨텍스트에 주입시키기 위해서 Flask에는 컨텍스트 프로세서들이 존재
컨텍스트 프로세서들은 새로운 값들을 템플릿 컨텍스트에 주입시키기 위해 템플릿이 렌더링되기 전에 실행되어야함 
템플릿 프로세서는 딕셔너리(dictionary) 객체를 리턴하는 함수
딕셔너리의 키와 밸류들은 어플리케이션에서의 모든 템플릿들을 위해서 템플릿 컨텍스트에 통합

ex) @app.context_processor
def inject_user():
    return dict(user=g.user)


user라는 유효변수를 템플릿 내부에 g.user의 값으로 만듬!(컨텍스트 프로세서가)

변수들은 값 제한 x, 컨텍스트 포레서는 템플릿에서 함수들을 사용할 수 있도록 해줌(파이썬이 패싱 어라운드 함수를 지원함으로 인해!)

ex) 
@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)
    return dict(format_price=format_price)

위의 컨텍스트 프로세서는 format_price 함수를 모든 템플릿들에서 사용가능하도록 해줌!
{{ format_price(0.33) }}






```