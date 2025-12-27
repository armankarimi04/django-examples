// import 'vite/modulepreload-polyfill';
// import _ from 'lodash';

function component() {
  const element = document.createElement('div');
  // element.innerHTML =  _.join(['Hello', 'lodash'], ' ');
  element.innerHTML = 'Hello';
  return element;
}
document.body.appendChild(component());

console.log("frontend/index.js");