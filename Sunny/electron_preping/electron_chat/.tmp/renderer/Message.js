"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.default = Message;

var _react = require("react");

var _react2 = _interopRequireDefault(_react);

var _Avatar = require("./Avatar");

var _Avatar2 = _interopRequireDefault(_Avatar);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var MEDIA_BODY_STYLE = {
    color: "#888",
    fontSize: ".9em"
};

var TIME_STYLE = {
    marginLeft: 5
};

var TEXT_STYLE = {
    whiteSpace: "normal",
    wordBreak: "break-word"
};

function Message(props) {
    var _props$message = props.message,
        text = _props$message.text,
        time = _props$message.time,
        writtenBy = _props$message.writtenBy;

    var localeString = new Date(time).toLocaleString();
    return _react2.default.createElement(
        "div",
        { className: "list-group-item" },
        _react2.default.createElement(
            "div",
            { className: "media-object pull-left" },
            _react2.default.createElement(_Avatar2.default, { user: writtenBy })
        ),
        _react2.default.createElement(
            "div",
            { className: "media-body" },
            _react2.default.createElement(
                "div",
                { style: MEDIA_BODY_STYLE },
                _react2.default.createElement(
                    "span",
                    null,
                    writtenBy.displayName
                ),
                _react2.default.createElement(
                    "span",
                    { style: TIME_STYLE },
                    localeString
                )
            ),
            _react2.default.createElement(
                "p",
                { style: TEXT_STYLE },
                text
            )
        )
    );
}