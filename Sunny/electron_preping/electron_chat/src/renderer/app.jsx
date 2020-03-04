import React from "react";
import { render } from "react-dom";
import { Router, Route, hashHistory } from "react-router";
import Login from "./Login";
import Signup from "./Signup";
import Rooms from "./Rooms";
import Room from "./Room";
import firebase from "firebase/firebase-browser";
import dotenv from "dotenv";

dotenv.config();
const API_KEY = `${process.env.REACT_APP_API_KEY}`
console.log(process.env.REACT_APP_API_KEY);
console.log(API_KEY);

// Routing 정의하기
const appRouting = (
    <Router history={hashHistory}>
        <Route path="/">
            <Route path="login" component={Login}/>
            <Route path="signup" component={Signup} />
            <Route path="rooms" component={Rooms}>
                <Route path=":roomId" component={Room} />
            </Route>
        </Route>
    </Router>
);

//Routing 초기화하기

if (!location.hash.length) {
    location.hash = "#/login";
}

//Firebase 초기화하기
var Config = {
    apiKey: process.env.REACT_APP_API_KEY,
    authDomain: "electron-chat-6ca15.firebaseapp.com",
    databaseURL: "https://electron-chat-6ca15.firebaseio.com",
    projectId: "electron-chat-6ca15",
    storageBucket: "electron-chat-6ca15.appspot.com",
    messagingSenderId: "213254139575",
    appId: "1:213254139575:web:dafe37a10ad96d02eee732",
    measurementId: "G-537GN73NK3"
};
// Initialize Firebase
firebase.initializeApp(Config);


// Application 렌더링 하기
render(appRouting, document.getElementById("app"));


//render(<div>Hello, Electron and React JSX</div>, document.getElementById("app"));

