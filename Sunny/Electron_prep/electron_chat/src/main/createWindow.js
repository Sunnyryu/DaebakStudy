import { BrowserWindow } from "electron";
// electron 버전 이 높아지면서 webPreferences를 작성해야 require를 못읽는 오류가 발생하지 않음
let win;
function createWindow() {
    win = new BrowserWindow({
        webPreferences: { 
            nodeIntegration: true
        }
    });
    win.loadURL(`file://${__dirname}/../../index.html`);
    win.on("close", () => {
        win = null;
    });
}

export default createWindow;
