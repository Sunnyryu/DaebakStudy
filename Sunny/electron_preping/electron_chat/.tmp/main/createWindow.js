"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});

var _electron = require("electron");

// electron 버전 이 높아지면서 webPreferences를 작성해야 require를 못읽는 오류가 발생하지 않음
var win = void 0;
function createWindow() {
    win = new _electron.BrowserWindow({
        webPreferences: {
            nodeIntegration: true
        }
    });
    win.loadURL("file://" + __dirname + "/../../index.html");
    win.on("close", function () {
        win = null;
    });
}

exports.default = createWindow;