/*
 * Copyright 2021 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import * as _webviewAPI from "vscode-webview";

import ReactDOM from "react-dom";
import React from "react";
import { App } from "./app";

(() => {
  // eslint-disable-next-line no-console
  console.log("Query WebView JavaScript loaded successfully.");
  const vscode = acquireVsCodeApi<string>();
  vscode.postMessage({
    command: "test",
    text: "Foo!",
  });

  window.addEventListener('message', event => {

    const message = event.data; // The JSON data our extension sent

    switch (message.type) {
      case 'config-set':
        console.log(message.config)
        break;
    }
});

  ReactDOM.render(
    React.createElement(App, {}, null),
    document.getElementById("app")
  );
})();
