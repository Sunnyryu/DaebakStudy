import { OAuth } from "oauth";

function createTwitterOAuth() {
  return new OAuth(
    "https://api.twitter.com/oauth/request_token",
    "https://api.twitter.com/oauth/access_token",
    "!!!Consumer Key!!!",
    "!!!Consumer Secret!!!",
    "1.0A",
    null,
    "HMAC-SHA1"
  );
}

export default createTwitterOAuth;
