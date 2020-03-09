"use strict";
require("babel-register");
const app = require("electron").app;
const path = require("path");
if (process.argv.length < 3) app.exit();
const target = path.join(process.cwd(), process.argv[2])
require(target);
