"use strict";

var _electron = require("electron");

var _createWindow = require("./createWindow");

var _createWindow2 = _interopRequireDefault(_createWindow);

var _setAppMenu = require("./setAppMenu");

var _setAppMenu2 = _interopRequireDefault(_setAppMenu);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

_electron.app.on("ready", function () {
    (0, _setAppMenu2.default)();
    (0, _createWindow2.default)();
});
// 이하 생략 


_electron.app.on("window-all-closed", function () {
    if (process.platform !== "darwin") {
        _electron.app.quit();
    }
});

_electron.app.on("activate", function (_e, hasVisibleWindows) {
    if (!hasVisibleWindows) {
        (0, _createWindow2.default)();
    }
});