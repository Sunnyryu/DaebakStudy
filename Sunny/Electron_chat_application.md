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



```