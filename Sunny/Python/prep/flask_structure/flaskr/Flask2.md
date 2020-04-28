# Flask study 

#### 해당 폴더에 있는 샘플을 참조하기!

##### 어플리케이션 테스트

```
Flask는 Werkzeug 를 통해 테스트 Client 를 제공하여 어플리케이션의 컨텍스트 로컬을 처리하고 테스트할 수 있는 방법을 제공

어플리케이션 테스트로 unittest 사용

해당 폴더의 flaskr_test.py 파일을 참조하기

1. 테스팅 스켈레톤

setUp() 함수는 새로운 테스트 클라이언트 생성 , 새로운 db를 초기화하며, 테스트 함수가 실행되기 전에 먼저 호출

테스트 후 DB 삭제를 위해 tearDown() 함수에서 파일을 닫고 파일시스템에서 제거함

setup 함수가 실행되는 동안 TESTING(flag)가 활성화됨! -> 요청 처리 하는 동안 error catch가 비활성화되어 있는 것은 어플리케이션에 대한 성능 테스트에 대하여 좀 더 나은 오류 리포트를 얻기 위해.. 

해당 테스트 클라이언트는 어플리케이션에 대한 단순한 인터페이스 제공(쿠키를 놓치지 않고 기록)

sqlite3는 File system 기반이므로 임시 db를 생성할 때 tempfile 모듈을 사용하여 초기화 ok 

mkstemp()는 로우-레벨 파일핸들과 임의의 파일이름을 리턴( 임의의 파일이름을 db 이름으로 사용, os.close() 함수를 사용하여 닫기전까지 유지하면 됨)

2. 첫번째 테스트
/으로 접근 했을 때 No entries here so far를 보여주는 지 확인
(flaskr_test.py에 있는 클래스에 새로운 테스트 메소드를 추가함)

unittest에서 테스트를 수행할 함수를 자동적으로 식별 

self.app.get를 사용함으로써 HTTP GET 요청을 주어진 경로에 보낼 수 있음 / 리턴값은 response_class 객체의 값이 될 것임. data 속성을 사용하여 어플리케이션으로부터 넘어온 리턴 값(문자열)을 검사할 수 있음 

3. 입력과 출력 로깅 (flaskr_test.py에 참조)
테스트 클라이언트에서는 어플리케이션의 입력과 출력에 대한 로그를 기록할 수 있어야함. 작업 작동 시 로그인과 로그아웃 페이지 요청들에 폼 데이터(사용자 이름과 암호)를 적용해야 하며, 로그인, 로그아웃 페이지들은 리다이렉트되기 때문에 클라이언트에게 follow_redirects를 설정해줘야함!

로그인과 로그아웃에 대해서 잘 작동하는지, 유효하지 않은 자격증명에 대해서 실패하는 지 쉽게 테스트하고 로깅 가능

4. 메시지 추가 테스트 

메세지를 추가 하게 되면 잘 작동하는지 확인해야만 함. HTML이 사용가능한지 확인

5. 다른 테스팅 기법들 

test_request_context() 함수를 with 구문과 조합하여 요청 컨텍스트를 임시적으로 활성화 하기 위해 사용될 수 있음. request, g, session와 같은 뷰 함수들에서 사용하는 객체들에 접근 할 수 있음 
app = flask.Flask(__name__)

with app.test_request_context('/?name=Peter'):
    assert flask.request.path == '/'
    assert flask.request.args['name'] == 'Peter'

컨텍스트와 함께 바인드된 모든 객체는 같은 방법으로 사용이 가능 

서로 다른 설정구성으로 어플리케이션을 테스트하기 원할경우 이것을 해결하기 위한 좋은 방법은 없음 => 어플리케이션 팩토리을 공부하기 바람.

테스트 요청 컨텍스트를 사용하는 경우 before_request() 함수와 after_request()는 자동으로 호출되지 않음. 

meth:~flask.Flask.teardown_request 함수는 with 블럭에서 요청 컨텍스트를 빠져나올때 실제로 실행된다. 만약 before_request() 함수도 마찬가지로 호출되기를 원한다면, preprocess_request() 를 직접 호출해야 한다.:

ex) app = flask.Flask(__name__)

with app.test_request_context('/?name=Peter'):
    app.preprocess_request()

어플리케이션의 설계방법에 따라 db connection이 필요할 수 있음

after_request() 함수를 호출하려 한다면, process_response() 함수에 응답객체를 전달하여 직접 호출하여야 함

ex)app = flask.Flask(__name__)

with app.test_request_context('/?name=Peter'):
    resp = Response('...')
    resp = app.process_response(resp)
...

6. 컨텍스트 유지시키기

일반적인 요청이 실행되는 경우에도 테스트 검증이 필요해질 경우가 있음..
test_client()를 with 블럭과 함께 사용 가능..
ex) app = flask.Flask(__name__)

with app.test_client() as c:
    rv = c.get('/?tequila=42')
    assert request.args['tequila'] == '42'

test_client()를 with 블럭 없이 사용한다면, request가 더 이상 유효하지 않기 때문에 assert를 실패하게 함.(실제 요청의 바깥에서 사용하려고 했기 때문)

7. 세션에 접근하고 수정

테스트 클라이언트에서 세션에 접근하고 수정하는 일은 매우 유용할 수 있다. 일반적으로 이를 위한 두가지 방법이 있음

세션이 특정 키 값으로 설정이 되어 있고 그 값이 컨텍스트를 통해서 유지된다고 접근 가능한 것을 보장하는 경우 flask.session
with app.test_client() as c:
    rv = c.get('/')
    assert flask.session['foo'] == 42

세션 트렉잭션이라고 부르는 세션에 대한 적절한 호출과 테스트 클라이언트에서의 수정이 가능한지 시물레이션 가능하도록 하고 있음.(트랜잭션의 끝에서 해당 세션은 저장됨.)

# flask.session 프록시의 sess 객체를 대신에 사용하여야 함을 주의
ex) with app.test_client() as c:
        with c.session_transaction() as sess:
            sess['a_key'] = 'a value'

        # once this is reached the session was stored
```

##### 어플리케이션 에러 로깅
```
1. 에러 로깅 

1)서버 에러가 발생시킬 수 있는 상황 

클라이언트가 request를 일찍 없애 버렸는데 여전히 어플리케이션이 입력되는 데이타를 읽고 있는 경우.
데이타베이스 서버가 과부하로 인해 쿼리를 다룰 수 없는 경우.
파일시스템이 꽉찬 경우
하드 드라이브가 크래쉬된 경우
백엔드 서버가 과부하 걸린 경우
여러분이 사용하고 있는 라이브러에서 프로그래밍 에러가 발생하는 경우
서버에서 다른 시스템으로의 네트워크 연결이 실패한 경우

# 기본적으로 어플리케이션이 운영 모드에서 실행되고 있다면, Flask는 매우 간단한 페이지를 보여주고 logger 에 예외를 로깅

2. 메일로 에러 발송하기

Flask는 파이썬에 빌트인된 로깅 시스템을 사용 / 실제로 에러가 발생 시, 우리가 원하는 메일을 보내주며, 예외가 발생 시 Flask 로거가 메일을 보내는 것을 설정하는 방법을 보여줌!
ex)
ADMINS = ['yourname@example.com']
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler('127.0.0.1',
                               'server-error@example.com',
                               ADMINS, 'YourApplication Failed')
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

메일 송신자로부터 모든 관리자에게 메일을 보내는 새로운 SMTPHandler를 생성함 (단지 에러와 더 심각한 메세지를 보내라고 핸들러에게 말함..)

3. 파일에 로깅하기

Flask는 자체적으로 코어 시스템에서 어떠한 주의사항도 발생하지 않음

로깅 시스템에 의해 제공되는 핸들러가 있음..

FileHandler (파일 시스템 내 파일에 메세지 남김)
RotatingFileHandler (파일 시스템 내 파일에 메세지를 남기며 특정 횟수를 순환)
NTEventLogHandler (윈도 시스템의 시스템 이벤트 로그에 로깅/ 윈도에 디플로이를 한다면 이 방법을 사용함)
SysLogHandler(유닉스 syslog에 로그를 보냄)

4. 포그 포맷 다루기

로그 기록은 더 많은 정보를 저장함. 
왜 에러가 발생했는니나 더 중요한 어디서 에러가 발생했는지 등의 더 많은 정보를 포함하도록 로거를 설정할 수 있음

포매터는 포맷 문자열을 가지고 초기화될 수 있음. 자동으로 역추적이 로그 진입점에 추가 되어진다는 것을 주목.

ex1 이메일)
from logging import Formatter
mail_handler.setFormatter(Formatter('''
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s

Message:

%(message)s
'''))

ex2 파일로깅)
from logging import Formatter
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))

포매터를 더 커스터마이징 하려면 포매터를 상속 받을 수 있음

format() : 실제 포매팅을 다룸, LogRecord 객체를 전달하면 포매팅된 문자열을 반환해야함

formatTime() : called for asctime 포매팅을 위해 호출, 다른 시간 포맷을 원한다면 이 메소드를 오버라이드 할 수 있음

formatException() : 예외 포매팅을 위해 호출, exc_into 튜플을 전달하면 문자열을 반환해야함, 보통 기본으로 사용해도 괜찮으며, 오버라이드를 할 필요는 없음 

getLogger() 함수를 가지고 로거들을 얻고 핸들러를 첨부하기 위해 얻은 로거들을 반복하여 여러분이 관심있어 하는 로거들을 만드는 것을 추천

ex)
from logging import getLogger
loggers = [app.logger, getLogger('sqlalchemy'),
        getLogger('otherlibrary')]
for logger in loggers:
    logger.addHandler(mail_handler)
    logger.addHandler(file_handler)

5. 어플리케이션 에러 디버깅(디버깅을 위한 설정으로 배포할 때..)

한에 관련된 문제를 해결하기 위해서는 배포환경에 설정된 것과 동일한 사용자 계정에서 실행되어야함.

제품화된 운영 호스트에서 debug=True 를 이용하여 Flask에 내장된 개발 서버를 사용하면 설정 문제를 해결하는데 도움이되지만, 이와같은 설정은 통제된 환경에서 임시적으로만 사용해야 함을 명심하자. debug=True 설정은 운영환경 혹은 제품화되었을때는 절대 사용해서는 안됨..

6. 디버거로 작업 

flask는 독자적인 디버거 제공, 여러가지 파이썬 디버거를 사용할 떄에는 간섭현상이 발생하므로 주의해야함

debug - 디모그 모드 사용 / 예외 잡을 수 있는 여부
use_debugger - flask 내부 디버거를 사용할지 여부
use_reloader - 예외발생시 프로세스를 포크하고 리로드 할지 여부

debug 옵션은 다른 두 옵션이 어떤 값을 갖던지 무조건 True여야함(예외는 잡아야함 )

config.yaml을 이용해서 유용한 설정패턴을 사용하는 것이 가능

ex)
FLASK:
    DEBUG: True
    DEBUG_WITH_APTANA: True

ex)
if __name__ == "__main__":
    # To allow aptana to receive errors, set use_debugger=False
    app = create_app(config="config.yaml")

    if app.debug: use_debugger = True
    try:
        # Disable Flask's debugger if external debugger is requested
        use_debugger = not(app.config.get('DEBUG_WITH_APTANA'))
    except:
        pass
    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0')


```