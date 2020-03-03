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

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

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

// Application 렌더링 하기
(0, _reactDom.render)(appRouting, document.getElementById("app"));

//render(<div>Hello, Electron and React JSX</div>, document.getElementById("app"));