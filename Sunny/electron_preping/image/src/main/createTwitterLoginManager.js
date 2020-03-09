import path from "path";
import fs from "fs";
import { app, shell, ipcMain, BrowserWindow } from "electron";
import createTwitterOAuth from "./createTwitterOAuth";
import createTwitterClient from "./createTwitterClient";

class TwitterLoginManager {

  constructor() {
    this.oauth = createTwitterOAuth();
    // 토큰 저장 위치 지정
    this.credentialPath = path.join(app.getPath("userData"), ".twitter_credentials");
  }

  getAccessToken() {
    return new Promise((resolve, reject) => {
      this.oauth.getOAuthRequestToken((error, requestToken, requestTokenSecret) => {
        if (error) {
          return reject(error);
        }
        // 권한 부여 화면을 브라우저에 출력하기
        shell.openExternal(`https://api.twitter.com/oauth/authorize?oauth_token=${requestToken}`);

        // PIN 코드 입력 전용 화면 출력하기
        const pincodeWindow = new BrowserWindow({
          width: 400,
          height: 120,
          maximizable: false,
          minimizable: false,
          resizable: false
        });
        ipcMain.once("SEND_PIN", (e, { pincode }) => {
          // 입력한 PIN 코드를 접근 토근, 접근 토큰 시크릿으로 변환하기
          this.oauth.getOAuthAccessToken(requestToken, requestTokenSecret, pincode, (error, accessToken, accessTokenSecret) => {
            if (error) {
              return reject(error);
            }
            resolve({ accessToken, accessTokenSecret });
            pincodeWindow.removeAllListeners("close");
            pincodeWindow.close();
          });
        });
        ipcMain.once("CANCEL_PIN", () => pincodeWindow.close());
        pincodeWindow.on("close", () => reject("user_cancel"));
        pincodeWindow.loadURL(`file://${__dirname}/../../pincodeWindow.html`);
      });
    });
  }
  
  init() {
    const loginAndVerify = () => {
      return this.getAccessToken().then(credentials => {
        this.saveCredentials(credentials);
        return this.verify();
      });
    };
    const credentials = this.loadCredentials();
    if (!credentials) {
      // 토큰이 저장되지 않은 경우
      return loginAndVerify();
    } else {
      return this.verify().catch(() => {
        // 저장된 토큰이 정상적이지 않은 경우
        return loginAndVerify();
      });
    }
  }

  loadCredentials() {
    try {
      this.credentials = JSON.parse(fs.readFileSync(this.credentialPath, "utf-8"));
      return this.credentials;
    } catch (e) {
      this.credentials = null;
      return null;
    }
  }

  saveCredentials(credentials) {
    this.credentials = credentials;
    fs.writeFileSync(this.credentialPath, JSON.stringify(this.credentials), "utf-8");
  }

  createClient() {
    return createTwitterClient(this.oauth, this.credentials.accessToken, this.credentials.accessTokenSecret);
  }

  verify() {
    return this.createClient().verifyCredentials();
  }
}

function createTwitterLoginManager() {
  return new TwitterLoginManager();
}

export default createTwitterLoginManager;
