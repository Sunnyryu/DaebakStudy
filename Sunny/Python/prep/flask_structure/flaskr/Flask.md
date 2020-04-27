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




```