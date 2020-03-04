"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.default = Avatar;

var _react = require("react");

var _react2 = _interopRequireDefault(_react);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var AVATAR_STYLE = {
    width: 32,
    textAlign: "center",
    fontSize: 24
};

function Avatar(props) {
    var photoURL = props.user.photoURL;

    if (photoURL) {
        // photoURL이 설정된 경우, img 요소 출력하기
        return _react2.default.createElement("img", { className: "img-rounded", src: photoURL, style: AVATAR_STYLE });
    } else {
        // photoURL이 설정되지 않은 경우, 대체 icon 출력하기
        return _react2.default.createElement(
            "div",
            { style: AVATAR_STYLE },
            _react2.default.createElement("span", { className: "icon icon-user" })
        );
    }
}