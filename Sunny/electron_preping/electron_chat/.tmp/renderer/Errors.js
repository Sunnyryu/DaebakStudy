"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.default = Errors;

var _react = require("react");

var _react2 = _interopRequireDefault(_react);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var ERRORS_STYLE = {
    padding: 10,
    marginBottom: 30,
    borderRadius: 5,
    color: "#E62626",
    backgroundColor: "#FFDDDF"
};

function Errors(props) {
    var errorMessages = props.errorMessages;

    if (!errorMessages || !errorMessages.length) {
        return null;
    }
    return _react2.default.createElement(
        "div",
        { style: ERRORS_STYLE },
        errorMessages.map(function (e) {
            return _react2.default.createElement(
                "div",
                { key: e },
                e
            );
        })
    );
}