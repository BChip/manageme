webpackJsonp([4],{87:function(e,t,r){try{(function(){"use strict";function n(e){return e&&e.__esModule?e:{default:e}}function a(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function o(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var l=function(){function e(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}return function(t,r,n){return r&&e(t.prototype,r),n&&e(t,n),t}}(),u=function(e,t,r){for(var n=!0;n;){var a=e,o=t,l=r;n=!1,null===a&&(a=Function.prototype);var u=Object.getOwnPropertyDescriptor(a,o);if(void 0!==u){if("value"in u)return u.value;var c=u.get;if(void 0===c)return;return c.call(l)}var i=Object.getPrototypeOf(a);if(null===i)return;e=i,t=o,r=l,n=!0,u=i=void 0}},c=r(1),i=n(c),f=r(57),s=(n(f),r(31)),p=function(e){function t(){a(this,t),u(Object.getPrototypeOf(t.prototype),"constructor",this).apply(this,arguments)}return o(t,e),l(t,[{key:"render",value:function(){return i.default.createElement("div",null,i.default.createElement(s.Link,{to:"/dashboard/reports",className:"pull-right btn btn-primary btn-outline btn-rounded"},"View Reports"),i.default.createElement(s.Link,{to:"/createProject",className:"pull-right btn btn-primary btn-outline btn-rounded"},"Create Project"),i.default.createElement(s.Link,{to:"/createTeam",className:"pull-right btn btn-primary btn-outline btn-rounded"},"Create Team"))}}]),t}(i.default.Component);t.default=p,e.exports=t.default}).call(this)}finally{}},759:function(e,t,r){try{(function(){"use strict";function n(e){return e&&e.__esModule?e:{default:e}}function a(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function o(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var l=function(){function e(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}return function(t,r,n){return r&&e(t.prototype,r),n&&e(t,n),t}}(),u=function(e,t,r){for(var n=!0;n;){var a=e,o=t,l=r;n=!1,null===a&&(a=Function.prototype);var u=Object.getOwnPropertyDescriptor(a,o);if(void 0!==u){if("value"in u)return u.value;var c=u.get;if(void 0===c)return;return c.call(l)}var i=Object.getPrototypeOf(a);if(null===i)return;e=i,t=o,r=l,n=!0,u=i=void 0}},c=r(1),i=n(c),f=r(31),s=r(62),p=r(87),d=n(p),b=function(e){function t(){a(this,t),u(Object.getPrototypeOf(t.prototype),"constructor",this).apply(this,arguments)}return o(t,e),l(t,[{key:"render",value:function(){return i.default.createElement("div",{className:"overview-page",key:"overview"},i.default.createElement(d.default,null),i.default.createElement("h2",null,"My Projects:"),i.default.createElement(s.Jumbotron,null,i.default.createElement(f.Link,{to:"/dashboard/project"},i.default.createElement("h1",null,"Project BlueFox")," "),"Description: Moving on-prem databases to Microsoft Azure.",i.default.createElement("br",null),"Due: December 2017",i.default.createElement("br",null)," ",i.default.createElement("br",null),i.default.createElement("div",{className:"progress"},i.default.createElement("div",{className:"progress-bar progress-bar-success",role:"progressbar","aria-valuenow":"40","aria-valuemin":"0","aria-valuemax":"100",style:{width:"90%"}},"90% Complete (on track)")),i.default.createElement("hr",null),i.default.createElement(f.Link,{to:"/dashboard/project"},i.default.createElement("h1",null,"Project RedTiger")," "),"Description: Convert 1996 VB Project to Windows 10 C# App.",i.default.createElement("br",null),"Due: January 2018",i.default.createElement("br",null)," ",i.default.createElement("br",null),i.default.createElement("div",{className:"progress"},i.default.createElement("div",{className:"progress-bar progress-bar-danger",role:"progressbar","aria-valuenow":"40","aria-valuemin":"0","aria-valuemax":"100",style:{width:"20%"}},"20% Complete (off track)")),i.default.createElement("hr",null)))}}]),t}(i.default.Component);t.default=b,e.exports=t.default}).call(this)}finally{}}});