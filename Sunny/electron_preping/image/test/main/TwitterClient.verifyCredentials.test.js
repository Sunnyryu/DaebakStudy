import createTwitterOAuth from "../../src/main/createTwitterOAuth";
import createTwitterClient from "../../src/main/createTwitterClient";

const client = createTwitterClient(
  createTwitterOAuth(),
  "!!!Access Token!!!",
  "!!!Access Token Secret!!!"
);

client.verifyCredentials().then(data => {
  console.log(data);
}).catch(error => {
  console.log(error);
});
