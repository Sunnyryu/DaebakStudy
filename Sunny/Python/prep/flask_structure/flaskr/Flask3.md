# Flask study 

#### 해당 폴더에 있는 샘플을 참조하기!


##### 설정 다루기

```
Flask는 일반적인 경우 어플리케이션이 구동될때에 설정값들을 사용될 수 있어야 하도록 설계

설정값을 독립적으로 로드하는 방법도 있음 (flask 객체의 config !)

1. 설정 기초 연습

config 은 실제로는 dictionary 의 서브클래스이며, 다른 dictionary 처럼 다음과 같이 수정가능

ex)
app = Flask(__name__)
app.config['DEBUG'] = True

확정된 설정값들은 flask 객체로 전달될 수 있으며, 객체를 통해 설정값들을 읽거나 쓸 수 있음.
app.debug = True

한번에 다수의 키들을 업데이트 하기 위해서는 dict.update() 함수를 사용할 수 있음
app.config.update(
    DEBUG=True,
    SECRET_KEY='...'
)

2. 파일을 통한 설정
파일을 통해 설정을 하여, 플리케이션의 패키징과 배포단계에서 다양한 패키지 도구 (Distribute으로 전개하기) 들을 사용할 수 있도록 해주며, 결과적으로 사후에 설정 파일을 수정 할 수 있도록 해줌!

ex) 
app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

yourapplication.default_settings 모듈로부터 불러옴 -> 환경설정 값들을 YOURAPPLICATION_SETTINGS 파일의 내용으로 덮어씌움 -> 리눅스 혹은 os x에서는 서버를 시작하기 전에 쉘의 export 명렁어로 설정 가능

ex)
$ export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
$ python run-app.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader..

 >set YOURAPPLICATION_SETTINGS=\path\to\settings.cfg(윈도우!)

설정 파일은 (실제론) 파이썬 파일.. 오직 대문자로된 값들만 자ㅜㅇ에 실제로 설정 객체에 저장. 반드시 설정 키값들은 대문자로 사용

ex)
# Example configuration
DEBUG = False
SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83

3. 좋은 설정 사례

여러분의 어플리케이션을 함수에 구현하고 (Flask의) 블루프린트에 등록하자. 이러한 방법을 통해 어플리케이션에 대해서 다중인스턴스를 생성하여 유닛테스트를 보다 쉽게 진행 할 수 있다. 필요에 따라 설정값을 전달해주기 위해 이 방법을 사용할 수 있다.

임포트 시점에 설정정보를 필요로 하는 코드를 작성하지 않는다. 만약 여러분이 스스로 설정값에 대해서 오직 요청만 가능하도록 접근을 제한 한다면 필요에 의해 나중에 설정 객체를 재설정 할 수 있다.

4. develop / product

적어도 운영 환경과 개발환경은 독립된 설정값을 가지고 있어야함.
쉬운 방법으론 버전 관리를 통하여 항상 로드되는 기본 설정값을 사용을 함

ex)
app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

위의 방법으로 덮어씌우고 config.py 파일을 추가한 후 그런다음, 여러분은 단지 독립적인 config.py 파일을 추가한 후 YOURAPPLICATION_SETTINGS=/path/to/config.py 를 export 하면 끝남.. (import하여 상속하는 방법도 있음!)

etc) django에서는 명시적으로 설정파일을 장고(Django)의 세계에서는 명시적으로 설정 파일을 from yourapplication.default_settings import import * 를 이용해 파일의 상단에 추가 하여 변경 사항은 수작업으로 덮어쓰기 하는 방법을 많이 사용함 

ex) 설정에서도 클래스와 상속을 사용할 수 있음 

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

app.config.from_object('configmodule.ProductionConfig')을 호출하면 됌!

5. 인스턴스 폴더
flask.instance_path라고 불리는 컨셉의 속성이 있음(인스턴스 폴더)
인스턴스 폴더는 버전 관리와 특정한 배포에 속하지 않도록 설계
(인스턴스 폴더는 런타임에서의 변경 사항 혹은 설정 파일의 변경 사항에 대한 것들을 보관하기에 완벽한 장소)

ex) 인스턴스 폴더를 자동으로 탐지하도록 하기 위해, 명시적인 설정으로 사용하기 위해 경로를 추가! => 반드시 절대경로 !!
app = Flask(__name__, instance_path='/path/to/instance/folder')

(인스턴스 폴더를 제공하지 않는다면..)
초기 모듈 
ex)
/myapp.py
/instance
초기 패키지
/myapp
    /__init__.py
/instance
설치된 모듈 or 패키지 (prefix는 파이썬이 설치된 경로의 prefix)
$PREFIX/lib/python3.X/site-packages/myapp
$PREFIX/var/myapp-instance

ex) 
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('yourapplication.default_settings')
app.config.from_pyfile('application.cfg', silent=True)

ex) 
filename = os.path.join(app.instance_path, 'application.cfg')
with open(filename) as f:
    config = f.read()

# or via open_instance_resource:
with app.open_instance_resource('application.cfg') as f:
    config = f.read()




```



```
내장된 고유 설정값들 (flask에서 이미 사용중!)
```
![999](https://i.imgur.com/1qFSM8a.png)


##### 시그널 


```
blinker라는 라이브러리도 시그널 기능을 사용할 수 있음

시그널이란  핵심 프레임워크나 다른 플라스크 확장의 어느 곳에서 동작이 발생했을 때 공지를 보내어 어플리케이션을 동작하게 하여 어플리케이션간의 의존성을 분리하도록 도움
(시그널은 특정 시그널 발신자가 어떤 일이 발생했다고 수신자에게 알려줌!)

플라스크에는 여러 시그널이 있고 플라스크 확장은 더 많은 시그널을 제공할 수도 있음
시그널은 수신자에게 무엇인가를 알리도록 의도한 것이지 수신자가 데이터를 변경하도록 권장하지 않아야 함
( request_started 은 before_request() 과 매우 유사함)
모든 시그널은 정해진 순서 없이 실행되며 어떤 데이터도 수정하지 않음..

핸들러 대비 시그널의 큰 장점은 짧은 순간 동안 그 시그널을 안전하게 수신할 수 있음
(일시적인 수신은 단위테스팅에 도움이 됌!)

1. 시그널 수신

시그널은 수신하려면 시그널의 connect() 메소드를 사용할 수 있음
첫번째 인자는 시그널이 송신됐을 때 호출되는 함수고, 선택적인 두번째 인자는 송신자를 지정
중단하려면 disconnect() 메소드를 사용

핵심 플라스크 시그널에 대해서 송신자는 시그널을 발생하는 어플리케이션

. 여러분이 시그널을 수신할 때, 모든 어플리케이션의 시그널을 수신하고 싶지 않다면 받고자하는 시그널의 송신자 지정을 잊지 말기!

단위테스팅에서 어떤 템플릿이 보여지고 어떤 변수가 템플릿으로 전달되는지 이해하기 위해 사용될 수 있는 헬퍼 컨텍스트 매니저가 있음!

ex) 
from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

위의 메소드는 테스트 클라이언트와 쉽게 묶일 수 있음.
with captured_templates(app) as templates:
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert len(templates) == 1
    template, context = templates[0]
    assert template.name == 'index.html'
    assert len(context['items']) == 10

플라스크가 시그널에 새 인자를 알려준다면 호출한 메소드는 실패하지 않을 것이므로 **extra 인자로 수신하도록 하기!

with 블럭의 내용에 있는 어플리케이션 app 이 생성한 코드에서 보여주는 모든 템플릿은 templates 변수에 기록

편리한 헬퍼 메소드도 존재한다(connected_to()). 그 메소드는 일시적으로 그 자체에 컨텍스트 메니저를 가진 시그널에 대한 함수를 수신

컨텍스트 매니저의 반환값을 그런 방식으로 지정할 수 없기 때문에 인자로 템플릿의 목록을 넘겨줘야 함

ex)
from flask import template_rendered

def captured_templates(app, recorded, **extra):
    def record(sender, template, context):
        recorded.append((template, context))
    return template_rendered.connected_to(record, app)

templates = []
with captured_templates(app, templates, **extra):
    ...
    template, context = templates[0]

2. 시그널 생성 

어플리케이션에서 시그널을 사용하고 싶다면 일반적인 사용예는 변경된 Namespace. 클래스에 시그널을 명명

ex)
from blinker import Namespace
my_signals = Namespace()

model_saved = my_signals.signal('model-saved')

3. 시그널 보내기

시그널을 전송하고 싶다면, send() 메소드를 호출하면 된다. 이 메소드는 첫번째 인자로 송신자를 넘겨주고 선택적으로 시그널 수신자에게 전달되는 키워드 인자도 있음
ex)
class Model(object):
    ...

    def save(self):
        model_saved.send(self)

항상 좋은 송신자를 뽑도록 함, 송신자로 self를 넘겨줌, 
임의의 함수에서 시그널을 전송한다면, current_app._get_current_object() 를 송신자로 전달가능
(시그널의 송신자로 절대 current_app 를 넘겨주지 않도록 하고 대신 current_app._get_current_object() 를 사용한다. 왜냐하면 current_app 는 실제 어플리케이션 객체가 아닌 프락시 객체이기 때문)

4. 시그널과 플라스크 요청 컨텍스트 

시그널을 수신할 때 요청 컨텍스트 를 완전하게 지원
Context-local 변수는 request_started 과 request_finished 사이에서 일관성을 유지하므로 여러분은 필요에 따라 flask.g 과 다른 변수를 참조
시그널 보내기 과 request_tearing_down 시그널에서 언급하는 제약에 대해 유의

5. 시그널 수신 기반 데코레이터

connect_via() 데코레이터를 사용하여 시그널을 쉽게 수신

ex)
from flask import template_rendered

@template_rendered.connect_via(app)
def when_template_rendered(sender, template, context, **extra):
    print 'Template %s is rendered with %s' % (template.name, context)

6. 핵심 시그널

플라스크에는 다음과 같은 시그널이 존재

1) flask.template_rendered
시그널은 템플릿이 성공적으로 뿌려졌을 때 송신, template 으로 템플릿과 딕셔너리 형태인 context 로 컨텍스트를 인스턴스로 하여 호출

ex) 
def log_template_renders(sender, template, context, **extra):
    sender.logger.debug('Rendering template "%s" with context %s',
                        template.name or 'string template',
                        context)

from flask import template_rendered
template_rendered.connect(log_template_renders, app)

2) flask.request_started
시그널은 요청 처리가 시작되기 전이지만 요청 컨텍스트는 만들어졌을 때 송신, 요청 컨텍스트가 이미 연결됐기 때문에, 수신자는 표준 전역 프록시 객체인 request 으로 요청을 참조

ex)
def log_request(sender, **extra):
    sender.logger.debug('Request context is set up')

from flask import request_started
request_started.connect(log_request, app)

3) flask.request_finished
시그널은 클라이언트로 응답이 가기 바로 전에 보내짐, response 인자로 응답 객체를 넘겨줌

ex)
def log_response(sender, response, **extra):
    sender.logger.debug('Request context is about to close down.  '
                        'Response: %s', response)

from flask import request_finished
request_finished.connect(log_response, app)

4) flask.got_request_exception

시그널은 요청 처리 동안 예외가 발생했을 때 보내짐, 표준 예외처리가 시작되기 전에 송신되고 예외 처리를 하지 않는 디버깅 환경에서도 보내짐, exception 인자로 예외 자체가 수신자에게 넘어감!

ex)
def log_exception(sender, exception, **extra):
    sender.logger.debug('Got exception during processing: %s', exception)

from flask import got_request_exception
got_request_exception.connect(log_exception, app)

5) flask.request_tearing_down

요청 객체가 제거될 때 보내짐, 요청 처리 과정에서 오류가 발생하더라도 항상 호출, 시그널을 기다리고 있는 함수는 일반 teardown 핸들러 뒤에 호출, 순서 보장 x

ex)
def close_db_connection(sender, **extra):
    session.close()

from flask import request_tearing_down
request_tearing_down.connect(close_db_connection, app)

예외가 있는 경우 이 시그널을 야기하는 예외에 대한 참조를 갖는 exc 키워드 인자를 넘겨줄 것임.

6) flask.appcontext_tearing_down

시그널은 어플리케이션 컨텍스트가 제거될 때 보내짐. 예외가 발생하더라도 시그널은 항상 호출, 일반 teardown 핸들러 뒤에 시그널에 대한 콜백 함수가 호출되지만 순서 보장 x

ex)
def close_db_connection(sender, **extra):
    session.close()

from flask import appcontext_tearing_down
appcontext_tearing_down.connect(close_db_connection, app)

5)번과 마찬가지로 예외에 대한 참조를 exc인자가 넘겨줄것임!

```

