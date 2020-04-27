# all the imports
from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing


# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '1234'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

#app.config.from_envvar('FLASKR_SETTINGS', silent=True) => app.config.from_object 대신도 가능

# DB를 접속하기 위한 함수(sqlite를 사용)
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()
# closing() 함수는 with 블럭안에서 연결한 커넥션을 유지하도록 도와줌!
# open_resource()는 어플리케이션 객체의 함수 / 영역 밖에서도 기능 지원, with 블럭에서 직접적으로 사용=> 리소스 경로의 파일을 열고 값을 읽을 수 있음!

@app.before_request
def before_request():
    g.db = connect_db()
# 파라미터가 없는 before_request() 함수는 리퀘스트가 실행되기 전에 호출되는 함수
#after_request() 함수는 리퀘스트가 실행된 다음에 호출되는 함수 
#클라이언트에게 전송된 응답을 파라미터로 넘겨줘야함, 함수들은 반드시 사용된 응답 객체 혹은 새로운 응답 객체를 리턴해야함

@app.teardown_request
def teardown_request(exception):
    g.db.close()
#after_request()에서 예외가 발생하면 teardown_request()로 전달되며, 응답객체가 생성된 후 호출 , 이 함수들은 리퀘스트 객체 수정 x, 리턴 값들은 무시
# 만약 request 진행중에 예외사항 발생 시 다시 각 함수들에게 전달되며, 그렇지 않을 경우 None이 전달 

# 작성된 글 보여줌!
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
# 데이터베이스에서 저장된 모든 글을 보여줌! / 어플리케이션 루트에서 대기 -> 요청이 오면 title 컬럼과 text 컬럼에서 자료 검색하여 보여줌!
# id가 가장 최근 항목을 제일 위에서 보여줌! / row는 select 구문에서 명시된 순서대로 정리된 튜플! 


# 새로운 글 추가!
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
# 로그인을 했다면 새로운 글을 보여주게 작성, POST 리퀘스트에만 응답하도록 함! , 실제 폼은 작성된 글 보여주기에 있음


#로그인 페이지 
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
# 로그인이 잘된다면 작성된글 페이지로 리다이렉트를 보냄!


#로그아웃 페이지
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
# 로그아웃 함수는 세션에서 logged_in 키 값에 대하여 로그인 설정에 대한 값을 제거! 그 후에 작성된 글 페이지로 리다이렉트



if __name__ == '__main__':
    app.run()


