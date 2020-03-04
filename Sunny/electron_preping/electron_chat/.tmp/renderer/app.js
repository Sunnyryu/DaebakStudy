"use strict";

var _react = require("react");

var _react2 = _interopRequireDefault(_react);

var _reactDom = require("react-dom");

var _reactRouter = require("react-router");

var _Login = require("./Login");

var _Login2 = _interopRequireDefault(_Login);

var _Signup = require("./Signup");

var _Signup2 = _interopRequireDefault(_Signup);

var _Rooms = require("./Rooms");

var _Rooms2 = _interopRequireDefault(_Rooms);

var _Room = require("./Room");

var _Room2 = _interopRequireDefault(_Room);

var _firebaseBrowser = require("firebase/firebase-browser");

var _firebaseBrowser2 = _interopRequireDefault(_firebaseBrowser);

var _dotenv = require("dotenv");

var _dotenv2 = _interopRequireDefault(_dotenv);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

_dotenv2.default.config();
var API_KEY = "" + process.env.REACT_APP_API_KEY;
console.log(process.env.REACT_APP_API_KEY);
console.log(API_KEY);

// Routing 정의하기
var appRouting = _react2.default.createElement(
    _reactRouter.Router,
    { history: _reactRouter.hashHistory },
    _react2.default.createElement(
        _reactRouter.Route,
        { path: "/" },
        _react2.default.createElement(_reactRouter.Route, { path: "login", component: _Login2.default }),
        _react2.default.createElement(_reactRouter.Route, { path: "signup", component: _Signup2.default }),
        _react2.default.createElement(
            _reactRouter.Route,
            { path: "rooms", component: _Rooms2.default },
            _react2.default.createElement(_reactRouter.Route, { path: ":roomId", component: _Room2.default })
        )
    )
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
_firebaseBrowser2.default.initializeApp(Config);

// Application 렌더링 하기
(0, _reactDom.render)(appRouting, document.getElementById("app"));

//render(<div>Hello, Electron and React JSX</div>, document.getElementById("app"));