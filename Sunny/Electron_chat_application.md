## Electron study

#### Electron 

```
채팅 어플리케이션 테스트 (Single Page Application을 이용하기~)

로그인 페이지 <-> 가입 페이지 / 메인 페이지!

리액트도 함께 활용하기
```

```react
import React from "react";

export class MyComponent extends React.Component {

    constructor(props){
        super(props);
        // 컴포넌트 상태(클릭 횟수 정의)
        this.state = {
            clickCount: 0
        };
        this.handleOnClick = this.handleOnClick.bind(this);
    }
    //button 요소를 클릭했을 때의 처리
    handleOnClick() {
        //상태(클릭 횟수 변경)
        this.setState({
            clickCount: this.state.clickCount + 1
        });
    }
    render() {
        const { clickCount } = this.state;
        return {
            <div>
                <span>click count: </span>
                <span>{clickCount}</span>
                <button onClick={this.handleOnClick}>click me</button>
            </div>
        };
    }
}
```

```
React 컴포넌트는 clickCount(<클릭 횟수>) 관리 / button 요소를 클릭할 때마다 clickCount를 1씩 증가시킴, 컴포넌트의 상태는 state라는 객체로 표현 
상태 변경 시 setState라는 이름의 메서드를 사용!

render() 메서드 내부에서는 JSX 기법이라는 리액트 표기 방법을 사용해서 해당 컴포넌트가 어떤 DOM 요소를 표현하는 지 선언 

setState() 메서드가 실행 시 render 메서드가 호출되어 컴포넌트를 다시 렌더링함! / 리액트는 가상 DOM이라는 기능 활용!!

Angular나 vue도 사용할 수 있음
```

```

개발 프로젝트 만들기 

npm init / npm install electron --save-dev 

Photon Kit은 일렉트론 전용으로 개발된 css 프레임워크임! (UI 구성에 낫베드)
npm install connors/photon --save
npm install react react-dom react-router --save
npm install babel-cli babel-preset-es2015 babel-preset-react --save-dev

nodeIntegration: node 통합 여부 옵션 <electron 5.0.0 이상에서 require을 알 수 없다는 에러가 발생하여>
new BrowserWindow 선언할 때 webPreferences에 nodeIntegration을 true 값으로 선언하면 된다

window = new BrowserWindow({
        webPreferences: {
            nodeIntegration: true
        },
        width: 400, 
        height: 600
 });

React 컴포넌트에서 link to라고 작성된 부분은 react-router를 통해 HTML <a> 태그로 변환합니다!

npm run watch로 Babel 트랜스파일러 실행 => npm start로 Electron시작

현재 공부하는 책에서는 react 및 electron 버전이 구 버전인 부분으로 인해서 신 버전에는 바뀐게 많기에.. 나중에 토이 프로젝트 시 .. 주의!

signup 컴포넌트의 메인 처리는 handleOnSubmit() 메서드가 함!, firebase.auth().createUserWithEmailAndPassword() 메서드로 사용자가 입력한 정보 전달해서, Firebase에 사용자 계정 생성 / Login 컴포넌트에서 사용한 signInWithEmailAndPassword() 메서드 처럼ㅇPromise 반환 / then으로 사용자 계정 생성에 성공할 때의 롤백을 작성함! 

Rooms 컴포넌트의 fetchRooms() 메서드로 목록에 출력할 채티앙들을 추출합니다
.ref("/chatrooms") JSON 트리의 chatrooms 객체 참조
.limitToLast(20) 최근 20개의 데이터만 추출하게한정
.once("value") 쿼리 실행 / 이 쿼리 1회 평가

componentDidMount() => 리액트 컴포넌트가 브라우저의 dom 트리에 마운트 되는 시점에 한 번만 실행하는 처리
Rooms 컴포넌트의 handleOnSubmit() 메서드는 Firebase 데이터베이스에 새로운 채팅방 처리임!
db.ref.push => 트리에 새로 생성한 채팅방의 참조를 저장
newRoomRef.update(...) 값을 변경 데이터베이스의 갱신 처리가 성공적으로 되면 fetchRoom으로 목록을 다시 추출하고 newRoomRef.key를 채팅방 ID로 사용해서 채팅 상세 화면으로 이동!

컴포넌트 마운트 때 룸아이디 매개 변수가 변경 됄 때 fetchRoom 메소드 호출하여 파이어베이스 통신하게 됨!

this.stream.on("child_added", item => {}) on메서드는 대상 쿼리 결과가 변화될 때 마다 콜백 함수를 실행하는 기능을 가지고 있음 ! / 차일드 에디드는 요소가 추가되었을 때 라는 의미임! 

```