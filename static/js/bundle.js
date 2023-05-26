(function(modules) {
  var installedModules = {};
  function __webpack_require__(moduleId) {
if(installedModules[moduleId]) {
	return installedModules[moduleId].exports;
	}
	var module = installedModules[moduleId] = {
			i: moduleId,
 			l: false,
		exports: {}
 		};
modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
module.l = true;
return module.exports;
	}
	__webpack_require__.m = modules;
  __webpack_require__.c = installedModules;
	__webpack_require__.d = function(exports, name, getter) {
if(!__webpack_require__.o(exports, name)) {
	Object.defineProperty(exports, name, { enumerable: true, get: getter });
	}
 	};
__webpack_require__.r = function(exports) {
		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
		Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
		}
 		Object.defineProperty(exports, '__esModule', { value: true });
	};
__webpack_require__.t = function(value, mode) {
	if(mode & 1) value = __webpack_require__(value);
  if(mode & 8) return value;
	if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
  var ns = Object.create(null);
		__webpack_require__.r(ns);
	  Object.defineProperty(ns, 'default', { enumerable: true, value: value });
 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
		  return ns;
 	};
__webpack_require__.n = function(module) {
	var getter = module && module.__esModule ?
 			function getDefault() { return module['default']; } :
			function getModuleExports() { return module; };
		__webpack_require__.d(getter, 'a', getter);
		return getter;
	};


  /******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./sources/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./sources/index.js":
/*!**************************!*\
  !*** ./sources/index.js ***!
  \**************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("\n\n//# sourceURL=webpack:///./sources/index.js?");

/***/ })

/******/ });