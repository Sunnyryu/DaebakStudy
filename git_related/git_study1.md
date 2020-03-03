# git rewind 


#### git study


```
깃이란 무엇인가??
쉽게 생각하면 분산버전관리 시스템

사용자 정보 
git config --global user.name sunny
git config --global user.email email

편집기 
git config --global core.editor emacs/vim/notepad++ 이맥스, 빔,노트패드 편집기를 사용가능 ! 

설정확인 
git config --list

도움말 보기
git help <verb> / ex) git help config

깃 저장소만들기

git init => 깃 init을 하여 깃 초기 상태를 만들기 ! 

깃 저장소 가져오기 
git clone <url>

깃 저장소에 파일 추가

git add <file path>
git commit -m "커밋하려는 내용?
git push 후에 깃허브 아이디/패스워드 입력

깃 상태 확인
git status 

깃 파일 추적 
git add README 

파일 무시하기
.gitignore 파일에 제외할 것을 정리함!

깃 staged / unstaged 

단순히 파일이 변경됐다는 사실이 아니라 어떤 내용이 변경됐는지 살펴보려면 git status 명령이 아니라 git diff 명령을 사용해야 한다.

만약 커밋하려고 Staging Area에 넣은 파일의 변경 부분을 보고 싶으면 git diff --staged 옵션을 사용한다. 이 명령은 저장소에 커밋한 것과 Staging Area에 있는 것을 비교한다.

git rm을 사용하여 워킹 디렉토리 뿐만 아니라 추적된 상태의 파일도 삭제함!

깃 파일 이름 변경

git mv file_before file_after 

깃 로그 

특별한 아규먼트 없이 git log 명령을 실행하면 저장소의 커밋 히스토리를 시간순으로 보여준다. 즉, 가장 최근의 커밋이 가장 먼저 나온다. 그리고 이어서 각 커밋의 SHA-1 체크섬, 저자 이름, 저자 이메일, 커밋한 날짜, 커밋 메시지를 보여준다.

ex) git log -p -2
깃 로그 커밋의 diff 결과 최근 2개를 보여준다는 것임!

git log --stat 각 커밋의 통계 정보를 조회할 수 있음!

git log --pretty=oneline
 oneline 옵션은 각 커밋을 한 라인으로 보여준다. 이 옵션은 많은 커밋을 한 번에 조회할 때 유용하다. 추가로 short, full, fuller 옵션도 있는데 이것은 정보를 조금씩 가감해서 보여준다.

 git log --pretty=format => 나만의 포맷으로 결과를 출력하고 싶을 때 사용 
```
![1](https://i.imgur.com/6IV1yD1.png)

```
git log 주요 옵션
```
![2](https://i.imgur.com/lHrtbUz.png)

```
git 조회 제한 조건

git log --since=2.weeks 
(2주 동안 만들어진 커밋을 가져올 수 있음)

```
![3](https://i.imgur.com/ECb0xHo.png)

```
git 되돌리기

git coomit --amend (깃 커밋을 잘못 했을 때 다시 작성할 수 있음!)

--amend 옵션으로 커밋을 고치는 작업이 주는 장점은 마지막 커밋 작업에서 아주 살짝 뭔가 빠뜨린 것을 넣거나 변경하는 것을 새 커밋으로 분리하지 않고 하나의 커밋에서 처리하는 것이다. “앗차, 빠진 파일 넣었음”, “이전 커밋에서 오타 살짝 고침” 등의 커밋을 만들지 않겠다는 말이다.

git reset HEAD <file>을 사용하여 저장된 것을 저장하지 않은 상태로 만들 수 있음 그대신 --hard옵션은 위험할 수 있어 조심해야함!

modified 파일 되돌리기! 
git checkout -- <file> => 워킹 디렉토리에 되돌릴 수 있음!! (최근 커밋된 버전)

git remote
리모트 저장소 확인! 

git remote -v (url을 볼수 있음!)

리모트 저장소가 여러 개 있다면 이 명령은 등록된 전부를 보여준다. 여러 사람과 함께 작업하는 리모트 저장소가 여러개라면 아래와 같은 결과를 얻을 수도 있다. 

 기존 워킹 디렉토리에 새 리모트 저장소를 쉽게 추가할 수 있는데 git remote add <단축이름> <url> 명령을 사용한다

리모트 저장소를 Pull 하거나 Fetch 하기
git fetch <remote>
리모트 저장소에는 있는 데이터를 모두 가져온다. 그러면 리모트 저장소의 모든 브랜치를 로컬에서 접근할 수 있어서 언제든지 Merge를 하거나 내용을 살펴볼 수 있음

git fetch 명령은 리모트 저장소의 데이터를 모두 로컬로 가져오지만, 자동으로 Merge 하지 않는다. 그래서 당신이 로컬에서 하던 작업을 정리하고 나서 수동으로 Merge 해야 한다

쉽게 git pull 명령으로 리모트 저장소 브랜치에서 데이터를 가져올 뿐만 아니라 자동으로 로컬 브랜치와 Merge 시킬 수 있다

리모트 저장소 살펴보기
git remote show <리모트 저장소 이름> 명령으로 리모트 저장소의 구체적인 정보를 확인할 수 있다. origin 같은 단축이름으로 이 명령을 실행하면 아래와 같은 정보를 볼 수 있다


리모트 저장소 이름을 바꾸거나 리모트 저장소를 삭제하기
git remote rename / git remote remove

태그 조회하기 git tag  (-l --list)
 Annotated 태그는 Git 데이터베이스에 태그를 만든 사람의 이름, 이메일과 태그를 만든 날짜, 그리고 태그 메시지도 저장한다
git tag -a (annotated)
-m 을 추가하면 메세지도 저장가능!

git show 명령으로 태그 정보및 커밋 정보 확인가능!

Lightweight 태그

Lightweight 태그는 기본적으로 파일에 커밋 체크섬을 저장하는 것뿐이다. 다른 정보는 저장하지 않는다. Lightweight 태그를 만들 때는 -a, -s, -m 옵션을 사용하지 않는다. 이름만 달아줄 뿐이다.

태그를 공유하려면 git push origin 태그 이름으로 이용!

Git Alias

git config --global alias.ci commit
git ci로만으로도 커밋이 가능하다.



```