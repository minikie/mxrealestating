(function(t){function e(e){for(var a,n,r=e[0],l=e[1],c=e[2],p=0,_=[];p<r.length;p++)n=r[p],i[n]&&_.push(i[n][0]),i[n]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(t[a]=l[a]);d&&d(e);while(_.length)_.shift()();return o.push.apply(o,c||[]),s()}function s(){for(var t,e=0;e<o.length;e++){for(var s=o[e],a=!0,r=1;r<s.length;r++){var l=s[r];0!==i[l]&&(a=!1)}a&&(o.splice(e--,1),t=n(n.s=s[0]))}return t}var a={},i={app:0},o=[];function n(e){if(a[e])return a[e].exports;var s=a[e]={i:e,l:!1,exports:{}};return t[e].call(s.exports,s,s.exports,n),s.l=!0,s.exports}n.m=t,n.c=a,n.d=function(t,e,s){n.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:s})},n.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},n.t=function(t,e){if(1&e&&(t=n(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var s=Object.create(null);if(n.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)n.d(s,a,function(e){return t[e]}.bind(null,a));return s},n.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return n.d(e,"a",e),e},n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},n.p="/";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],l=r.push.bind(r);r.push=e,r=r.slice();for(var c=0;c<r.length;c++)e(r[c]);var d=l;o.push([0,"chunk-vendors"]),s()})({0:function(t,e,s){t.exports=s("56d7")},"39c9":function(t,e,s){"use strict";var a=s("ac7d"),i=s.n(a);i.a},4678:function(t,e,s){var a={"./af":"2bfb","./af.js":"2bfb","./ar":"8e73","./ar-dz":"a356","./ar-dz.js":"a356","./ar-kw":"423e","./ar-kw.js":"423e","./ar-ly":"1cfd","./ar-ly.js":"1cfd","./ar-ma":"0a84","./ar-ma.js":"0a84","./ar-sa":"8230","./ar-sa.js":"8230","./ar-tn":"6d83","./ar-tn.js":"6d83","./ar.js":"8e73","./az":"485c","./az.js":"485c","./be":"1fc1","./be.js":"1fc1","./bg":"84aa","./bg.js":"84aa","./bm":"a7fa","./bm.js":"a7fa","./bn":"9043","./bn.js":"9043","./bo":"d26a","./bo.js":"d26a","./br":"6887","./br.js":"6887","./bs":"2554","./bs.js":"2554","./ca":"d716","./ca.js":"d716","./cs":"3c0d","./cs.js":"3c0d","./cv":"03ec","./cv.js":"03ec","./cy":"9797","./cy.js":"9797","./da":"0f14","./da.js":"0f14","./de":"b469","./de-at":"b3eb","./de-at.js":"b3eb","./de-ch":"bb718","./de-ch.js":"bb718","./de.js":"b469","./dv":"598a","./dv.js":"598a","./el":"8d47","./el.js":"8d47","./en-SG":"cdab","./en-SG.js":"cdab","./en-au":"0e6b","./en-au.js":"0e6b","./en-ca":"3886","./en-ca.js":"3886","./en-gb":"39a6","./en-gb.js":"39a6","./en-ie":"e1d3","./en-ie.js":"e1d3","./en-il":"7333","./en-il.js":"7333","./en-nz":"6f50","./en-nz.js":"6f50","./eo":"65db","./eo.js":"65db","./es":"898b","./es-do":"0a3c","./es-do.js":"0a3c","./es-us":"55c9","./es-us.js":"55c9","./es.js":"898b","./et":"ec18","./et.js":"ec18","./eu":"0ff2","./eu.js":"0ff2","./fa":"8df4","./fa.js":"8df4","./fi":"81e9","./fi.js":"81e9","./fo":"0721","./fo.js":"0721","./fr":"9f26","./fr-ca":"d9f8","./fr-ca.js":"d9f8","./fr-ch":"0e49","./fr-ch.js":"0e49","./fr.js":"9f26","./fy":"7118","./fy.js":"7118","./ga":"5120","./ga.js":"5120","./gd":"f6b4","./gd.js":"f6b4","./gl":"8840","./gl.js":"8840","./gom-latn":"0caa","./gom-latn.js":"0caa","./gu":"e0c5","./gu.js":"e0c5","./he":"c7aa","./he.js":"c7aa","./hi":"dc4d","./hi.js":"dc4d","./hr":"4ba9","./hr.js":"4ba9","./hu":"5b14","./hu.js":"5b14","./hy-am":"d6b6","./hy-am.js":"d6b6","./id":"5038","./id.js":"5038","./is":"0558","./is.js":"0558","./it":"6e98","./it-ch":"6f12","./it-ch.js":"6f12","./it.js":"6e98","./ja":"079e","./ja.js":"079e","./jv":"b540","./jv.js":"b540","./ka":"201b","./ka.js":"201b","./kk":"6d79","./kk.js":"6d79","./km":"e81d","./km.js":"e81d","./kn":"3e92","./kn.js":"3e92","./ko":"22f8","./ko.js":"22f8","./ku":"2421","./ku.js":"2421","./ky":"9609","./ky.js":"9609","./lb":"440c","./lb.js":"440c","./lo":"b29d","./lo.js":"b29d","./lt":"26f9","./lt.js":"26f9","./lv":"b97c","./lv.js":"b97c","./me":"293c","./me.js":"293c","./mi":"688b","./mi.js":"688b","./mk":"6909","./mk.js":"6909","./ml":"02fb","./ml.js":"02fb","./mn":"958b","./mn.js":"958b","./mr":"39bd","./mr.js":"39bd","./ms":"ebe4","./ms-my":"6403","./ms-my.js":"6403","./ms.js":"ebe4","./mt":"1b45","./mt.js":"1b45","./my":"8689","./my.js":"8689","./nb":"6ce3","./nb.js":"6ce3","./ne":"3a39","./ne.js":"3a39","./nl":"facd","./nl-be":"db29","./nl-be.js":"db29","./nl.js":"facd","./nn":"b84c","./nn.js":"b84c","./pa-in":"f3ff","./pa-in.js":"f3ff","./pl":"8d57","./pl.js":"8d57","./pt":"f260","./pt-br":"d2d4","./pt-br.js":"d2d4","./pt.js":"f260","./ro":"972c","./ro.js":"972c","./ru":"957c","./ru.js":"957c","./sd":"6784","./sd.js":"6784","./se":"ffff","./se.js":"ffff","./si":"eda5","./si.js":"eda5","./sk":"7be6","./sk.js":"7be6","./sl":"8155","./sl.js":"8155","./sq":"c8f3","./sq.js":"c8f3","./sr":"cf1e","./sr-cyrl":"13e9","./sr-cyrl.js":"13e9","./sr.js":"cf1e","./ss":"52bd","./ss.js":"52bd","./sv":"5fbd","./sv.js":"5fbd","./sw":"74dc","./sw.js":"74dc","./ta":"3de5","./ta.js":"3de5","./te":"5cbb","./te.js":"5cbb","./tet":"576c","./tet.js":"576c","./tg":"3b1b","./tg.js":"3b1b","./th":"10e8","./th.js":"10e8","./tl-ph":"0f38","./tl-ph.js":"0f38","./tlh":"cf75","./tlh.js":"cf75","./tr":"0e81","./tr.js":"0e81","./tzl":"cf51","./tzl.js":"cf51","./tzm":"c109","./tzm-latn":"b53d","./tzm-latn.js":"b53d","./tzm.js":"c109","./ug-cn":"6117","./ug-cn.js":"6117","./uk":"ada2","./uk.js":"ada2","./ur":"5294","./ur.js":"5294","./uz":"2e8c","./uz-latn":"010e","./uz-latn.js":"010e","./uz.js":"2e8c","./vi":"2921","./vi.js":"2921","./x-pseudo":"fd7e","./x-pseudo.js":"fd7e","./yo":"7f33","./yo.js":"7f33","./zh-cn":"5c3a","./zh-cn.js":"5c3a","./zh-hk":"49ab","./zh-hk.js":"49ab","./zh-tw":"90ea","./zh-tw.js":"90ea"};function i(t){var e=o(t);return s(e)}function o(t){var e=a[t];if(!(e+1)){var s=new Error("Cannot find module '"+t+"'");throw s.code="MODULE_NOT_FOUND",s}return e}i.keys=function(){return Object.keys(a)},i.resolve=o,t.exports=i,i.id="4678"},"56d7":function(t,e,s){"use strict";s.r(e);s("cadf"),s("551c"),s("f751"),s("097d");var a=s("2b0e"),i=s("bb71");s("da64");a["a"].use(i["a"],{iconfont:"md"});var o=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("v-app",{attrs:{app:""}},[s("v-navigation-drawer",{attrs:{fixed:"",app:""},model:{value:t.drawer,callback:function(e){t.drawer=e},expression:"drawer"}},[s("v-list",{attrs:{dense:""}},[s("v-list-tile",[s("v-list-tile-action",[s("v-icon",[t._v("home")])],1),s("v-list-tile-content",[s("v-list-tile-title",[t._v("Home")])],1)],1),s("v-list-tile",[s("v-list-tile-action",[s("v-icon",[t._v("contact_mail")])],1),s("v-list-tile-content",[s("v-list-tile-title",[t._v("Contact")])],1)],1)],1)],1),s("v-toolbar",{attrs:{color:"indigo",dark:"",fixed:"",app:""}},[s("v-toolbar-side-icon",{on:{click:function(e){e.stopPropagation(),t.drawer=!t.drawer}}}),s("v-toolbar-title",[t._v("부동산 보고서")]),s("v-spacer"),s("v-btn",{attrs:{icon:""},on:{click:function(e){return t.setView("positioninfo")}}},[s("v-icon",{attrs:{"flip-horizontal":""}},[t._v("format_list_bulleted")])],1),s("v-btn",{attrs:{icon:""},on:{click:function(e){return t.setView("resultreport")}}},[s("v-icon",[t._v("insert_chart_outlined")])],1),s("v-btn",{attrs:{icon:""},on:{click:function(e){return t.setView("usersettings")}}},[s("v-icon",[t._v("settings")])],1)],1),"positioninfo"==t.selectedView?s("v-content",[s("PositionInfo",{ref:"positionInfoComp",attrs:{userinfo:this.$store.state.userinfo,portfolio_list:this.$store.state.portfolio_list}})],1):t._e(),"resultreport"==t.selectedView?s("v-content",[s("ResultReport",{ref:"resultReportComp",attrs:{results_data:this.$store.state.results_data,userinfo:this.$store.state.userinfo,position_list:this.$store.state.selected_portfolio.position_list}})],1):t._e(),"usersettings"==t.selectedView?s("v-content",[s("UserSettings",{attrs:{results_data:this.$store.state.results_data,userinfo:this.$store.state.userinfo,position_list:this.$store.state.selected_portfolio.position_list}})],1):t._e()],1)},n=[],r=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("v-container",{attrs:{fluid:"","mt-0":"","pb-0":"","pt-0":"","text-xs-center":""}},[t.positionlist_view?s("v-layout",{attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{xs12:""}},[s("v-toolbar",{staticClass:"mb-2",attrs:{dense:""}},[s("v-toolbar-title",[t._v("자산내역")]),s("v-spacer"),s("v-btn",{attrs:{icon:""},on:{click:function(e){return t.add_new_position()}}},[s("v-icon",[t._v("add")])],1)],1),s("v-card",{attrs:{flat:"",elevation:"0"}},[t.position_list.length>0?s("v-list",{attrs:{"two-line":""}},[t._l(t.position_list,function(e,a){return[s("v-list-tile",{key:e.name,attrs:{avatar:"",ripple:""},on:{click:function(s){return t.selecte_position(e)}}},[s("v-list-tile-content",[s("v-list-tile-title",[t._v(t._s(e.name))]),s("v-list-tile-sub-title",{class:{"text-danger":t.addressError}},[t._v(t._s(e.address))]),s("v-list-tile-sub-title",[t._v(t._s(e.book_value)+" 만원")])],1),s("v-list-tile-action",[s("v-list-tile-action-text",[t._v(t._s(e.position_type))])],1)],1),a+1<=t.position_list.length?s("v-divider",{key:a}):t._e()]})],2):t._e(),0==t.position_list.length?s("v-layout",{staticStyle:{height:"calc(100vh - 180px)"},attrs:{column:""}},[s("v-flex",{attrs:{xs12:""}},[s("v-layout",{attrs:{"align-center":"","justify-center":"","fill-height":""}},[s("v-subheader",[t._v("\n                항목이 없습니다.\n              ")])],1)],1)],1):t._e()],1)],1)],1):t._e(),t.positionlist_view?s("v-navigation-drawer",{staticClass:"grey lighten-2",attrs:{height:"500px",absolute:"",temporary:""},model:{value:t.portfolio_drawer,callback:function(e){t.portfolio_drawer=e},expression:"portfolio_drawer"}},[s("v-list",{staticClass:"pa-1"},[s("v-list-tile",{attrs:{avatar:""}},[s("v-list-tile-content",[s("v-list-tile-title",[t._v(t._s(t.userinfo.email))])],1),s("v-btn",{attrs:{icon:""}},[s("v-icon",[t._v("add")])],1)],1)],1),s("v-list",{staticClass:"pt-0",attrs:{dense:""}},[s("v-divider"),t._l(t.portfolio_list,function(e){return s("v-list-tile",{key:e.title,on:{click:function(s){s.stopPropagation(),t.position_list=e.position_list,t.portfolio_drawer=!t.portfolio_drawer,t.selected_portfolio_title=e.title}}},[s("v-list-tile-action",[s("v-icon",[t._v(t._s(e.icon))])],1),s("v-list-tile-content",[s("v-list-tile-title",[t._v(t._s(e.title))])],1)],1)})],2)],1):t._e(),t.positionlist_view?t._e():s("v-layout",{attrs:{row:"",wrap:""}},[s("v-toolbar",{staticClass:"mb-0",attrs:{dense:""}},[s("v-btn",{attrs:{icon:""},on:{click:function(e){t.positionlist_view=!t.positionlist_view}}},[s("v-icon",[t._v("arrow_back")])],1),s("v-spacer"),s("v-btn",{attrs:{icon:""},on:{click:function(e){return t.delete_position()}}},[s("v-icon",[t._v("delete")])],1)],1)],1),t.positionlist_view?t._e():s("v-layout",{staticClass:"pa-2",attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{xs12:""}},[s("v-text-field",{attrs:{label:"이름"},model:{value:t.position_info.name,callback:function(e){t.$set(t.position_info,"name",e)},expression:"position_info.name"}})],1),s("v-flex",{attrs:{xs9:""}},[s("v-text-field",{attrs:{label:"주소",color:"grey",disabled:""},model:{value:t.position_info.address,callback:function(e){t.$set(t.position_info,"address",e)},expression:"position_info.address"}})],1),s("v-flex",{attrs:{xs3:""}},[s("v-layout",{attrs:{row:"","justify-center":""}},[s("v-dialog",{attrs:{persistent:"","max-width":"600px"},scopedSlots:t._u([{key:"activator",fn:function(e){var a=e.on;return[s("v-btn",t._g({attrs:{color:"primary",dark:""}},a),[t._v("수정")])]}}],null,!1,1110201709),model:{value:t.address_dialog,callback:function(e){t.address_dialog=e},expression:"address_dialog"}},[s("v-tabs",{attrs:{dark:"",color:"cyan","show-arrows":""}},[s("v-tabs-slider",{attrs:{color:"yellow"}}),t._e(),s("v-tab",{key:"naverInputTabKey",attrs:{href:"#naverInputTabKey"}},[t._v("Naver")]),s("v-tabs-items",[s("v-tab-item",{key:"directInputTabKey",attrs:{value:"directInputTabKey"}},[s("v-card",[s("v-card-text",[s("v-container",{attrs:{"grid-list-md":""}},[s("v-layout",{attrs:{wrap:""}},[s("v-flex",{attrs:{xs12:"",sm12:"",md12:""}},[s("v-text-field",{attrs:{label:"Address"},model:{value:t.position_info.address,callback:function(e){t.$set(t.position_info,"address",e)},expression:"position_info.address"}})],1),s("v-flex",{attrs:{xs12:"",sm6:"",md4:""}},[s("v-text-field",{attrs:{label:"Legal Dong",required:""},model:{value:t.position_info.legal_dong,callback:function(e){t.$set(t.position_info,"legal_dong",e)},expression:"position_info.legal_dong"}})],1),s("v-flex",{attrs:{xs12:"",sm6:"",md4:""}},[s("v-text-field",{attrs:{label:"Apt Name",hint:"example of helper text only on focus"},model:{value:t.position_info.apt_name,callback:function(e){t.$set(t.position_info,"apt_name",e)},expression:"position_info.apt_name"}})],1),s("v-flex",{attrs:{xs12:"",sm6:"",md4:""}},[s("v-text-field",{attrs:{label:"Private Area",required:""},model:{value:t.position_info.private_area,callback:function(e){t.$set(t.position_info,"private_area",e)},expression:"position_info.private_area"}})],1),s("v-flex",{attrs:{xs12:"",sm6:"",md4:""}},[s("v-text-field",{attrs:{label:"Region Code"},model:{value:t.position_info.region_code,callback:function(e){t.$set(t.position_info,"region_code",e)},expression:"position_info.region_code"}})],1)],1)],1),s("small",[t._v("*indicates required field")])],1),s("v-card-actions",[s("v-spacer"),s("v-btn",{attrs:{color:"blue darken-1",flat:""},on:{click:function(e){t.address_dialog=!1}}},[t._v("Close")])],1)],1)],1),s("v-tab-item",{key:"naverInputTabKey",attrs:{value:"naverInputTabKey"}},[s("v-card",[s("v-card-text",[s("v-container",{attrs:{"grid-list-md":""}},[s("v-layout",{attrs:{wrap:""}},[s("v-flex",{attrs:{xs12:""}},[s("v-text-field",{attrs:{label:"Url",required:""},model:{value:t.position_info.url,callback:function(e){t.$set(t.position_info,"url",e)},expression:"position_info.url"}})],1),s("v-flex",{attrs:{xs12:""}},[s("v-btn",{on:{click:function(e){return t.url_check()}}},[t._v("check")])],1)],1)],1)],1),s("v-card-actions",[s("v-spacer"),s("v-btn",{attrs:{color:"blue darken-1",flat:""},on:{click:function(e){t.address_dialog=!1}}},[t._v("Close")])],1)],1)],1)],1)],1)],1)],1)],1),s("v-flex",{attrs:{xs5:""}},[s("v-text-field",{attrs:{label:"매입가",suffix:"만원"},model:{value:t.position_info.book_value,callback:function(e){t.$set(t.position_info,"book_value",e)},expression:"position_info.book_value"}})],1),s("v-flex",{attrs:{xs1:""}}),s("v-flex",{attrs:{xs5:""}},[s("v-text-field",{attrs:{label:"매매일",type:"date"},model:{value:t.position_info.book_date,callback:function(e){t.$set(t.position_info,"book_date",e)},expression:"position_info.book_date"}})],1),s("v-flex",{attrs:{xs12:""}},[s("v-select",{attrs:{items:["자가","전세","월세"],label:"투자형태"},model:{value:t.position_info_position_type,callback:function(e){t.position_info_position_type=e},expression:"position_info_position_type"}})],1),"전세"==t.position_info.position_type||"월세"==t.position_info.position_type?s("v-flex",{attrs:{xs12:""}},[s("v-card",{staticClass:"pa-2 mb-3",attrs:{color:"blue lighten-5"}},[s("v-flex",{attrs:{xs12:""}},[s("v-checkbox",{attrs:{label:"타인 소유 부동산(보증금을 준 경우)",value:"vertical"},model:{value:t.position_info.rent.is_resident,callback:function(e){t.$set(t.position_info.rent,"is_resident",e)},expression:"position_info.rent.is_resident"}})],1),s("v-container",{attrs:{"grid-list-md":"","pa-0":""}},[s("v-layout",[s("v-flex",{attrs:{xs6:""}},[s("v-text-field",{attrs:{label:"보증금",suffix:"만원"},model:{value:t.position_info.rent.deposit,callback:function(e){t.$set(t.position_info.rent,"deposit",e)},expression:"position_info.rent.deposit"}})],1),"월세"==t.position_info.position_type?s("v-flex",{attrs:{xs6:""}},[s("v-text-field",{attrs:{label:"월세"},model:{value:t.position_info.rent.monthly_payment,callback:function(e){t.$set(t.position_info.rent,"monthly_payment",e)},expression:"position_info.rent.monthly_payment"}})],1):t._e()],1)],1),s("v-container",{attrs:{"grid-list-md":"","pa-0":""}},[s("v-layout",[s("v-flex",{attrs:{xs6:""}},[s("v-text-field",{attrs:{label:"계약일",type:"date"},model:{value:t.position_info.rent.effective_date,callback:function(e){t.$set(t.position_info.rent,"effective_date",e)},expression:"position_info.rent.effective_date"}})],1),s("v-flex",{attrs:{xs6:""}},[s("v-text-field",{attrs:{label:"만기일",type:"date"},model:{value:t.position_info.rent.maturity_date,callback:function(e){t.$set(t.position_info.rent,"maturity_date",e)},expression:"position_info.rent.maturity_date"}})],1)],1)],1)],1)],1):t._e(),s("v-flex",{attrs:{xs12:""}},[s("v-select",{attrs:{"item-value":"loan_type",items:["없음","고정금리","변동금리"],label:"대출"},model:{value:t.position_info_loan_type,callback:function(e){t.position_info_loan_type=e},expression:"position_info_loan_type"}})],1),"고정금리"==t.position_info.loan_type?s("v-flex",{attrs:{xs12:""}},[s("v-card",{staticClass:"pa-2",attrs:{color:"green lighten-5"}},[s("v-container",{attrs:{"grid-list-md":"","pa-0":""}},[s("v-layout",[s("v-flex",{attrs:{xs6:""}},[s("v-text-field",{attrs:{label:"금액",suffix:"만원"},model:{value:t.position_info.loan.amount,callback:function(e){t.$set(t.position_info.loan,"amount",e)},expression:"position_info.loan.amount"}})],1),s("v-flex",{attrs:{xs6:""}},[s("v-text-field",{attrs:{label:"금리",suffix:"%"},model:{value:t.position_info.loan.rate,callback:function(e){t.$set(t.position_info.loan,"rate",e)},expression:"position_info.loan.rate"}})],1)],1)],1),s("v-container",{attrs:{"grid-list-md":"","pa-0":""}},[s("v-layout",[s("v-flex",{attrs:{xs6:""}},[s("v-text-field",{attrs:{label:"계약일",type:"date"},model:{value:t.position_info.loan.effective_date,callback:function(e){t.$set(t.position_info.loan,"effective_date",e)},expression:"position_info.loan.effective_date"}})],1),s("v-flex",{attrs:{xs6:""}},[s("v-text-field",{attrs:{label:"만기일",type:"date"},model:{value:t.position_info.loan.maturity_date,callback:function(e){t.$set(t.position_info.loan,"maturity_date",e)},expression:"position_info.loan.maturity_date"}})],1)],1)],1)],1)],1):t._e()],1)],1)},l=[],c=(s("6b54"),s("28a5"),s("f499")),d=s.n(c),p=(s("7f7f"),{props:["userinfo","portfolio_list"],data:function(){return{positionlist_view:!0,portfolio_drawer:!1,address_dialog:!1,addressError:!0,access_key:"",position_info_position_type:"자가",position_info_loan_type:"없음",position_info:{name:"test name2",asset_type:"apartment",address:"test address",legal_dong:"test dong",apt_name:"test apt",private_area:55.12,region_code:11110,book_value:1e4,book_date:"2018-10-11",position_type:"자가",rent:{deposit:0,monthly_payment:1e3,is_resident:!1,effective_date:"2018-10-11",maturity_date:"2018-10-11"},loan_type:"없음",loan:{amount:0,rate:.03,effective_date:"2018-10-11",maturity_date:"2018-10-11"}}}},methods:{position_info_valiation:function(){var t=this.position_info.name,e=this.$store.state.selected_portfolio.position_list.some(function(e){return e.name==t});return!(e>0)||(console.log("name duplication : "+this.position_info.name),!1)},load_positions_from_key:function(){var t=this,e=this.$store.getters.getCookie("position_token");this.$axios.post(this.$store.state.url_end_point+"/getpositions",{position_token:e}).then(function(e){console.log(e.data);var s=e.data["message"];"success"==s&&(t.$store.state.userinfo=e.data["data"]["userinfo"],t.position_list=e.data["data"]["position_list"],e.data["data"]["results_data"]&&(t.$store.state.results_data=e.data["data"]["results_data"]),t.$store.state.isCalculated=!1,console.log(s))}).catch(function(t){console.log(t)})},add_new_position:function(){console.log("add start ---------------------------------------");var t=JSON.parse(d()(this.$store.state.new_position_info_template)),e=new Date,s=e.toISOString().split("T")[0];t.book_date=s,t.rent.effective_date=s,t.rent.maturity_date=s,t.loan.effective_date=s,t.loan.maturity_date=s,this.position_info=t;var a=0,i=t.name;do{a+=1}while(this.position_list.some(function(t){return t.name==i+a.toString()}));this.position_info.name=i+a.toString(),this.$store.state.selected_portfolio.position_list.push(t),this.$store.state.isCalculated=!1,this.positionlist_view=!1,console.log("add complete ------------------------------------")},selecte_position:function(t){this.positionlist_view=!1,this.position_info=t},delete_position:function(){var t=this.position_info.name;this.position_list=this.position_list.filter(function(e){return e.name!=t}),this.positionlist_view=!0},edit_position:function(){this.$store.state.isCalculated=!1,console.log("edit complete")},clear_position:function(){this.$store.state.isCalculated=!1,this.$store.state.selected_portfolio.position_list=[],console.log("clear complete")},url_check:function(){var t=this;this.$axios.post(this.$store.state.url_end_point+"/parse_position_info",{url:this.position_info.url}).then(function(e){console.log(e.data);var s=e.data["message"];"success"==s&&(t.position_info.address=e.data["address"],t.position_info.legal_dong=e.data["legal_dong"],t.position_info.apt_name=e.data["apt_name"],t.position_info.private_area=e.data["private_area"],t.position_info.region_code=e.data["region_code"],console.log(s),t.address_dialog=!1,t.addressError=!1)}).catch(function(e){console.log(e),t.addressError=!0})}},mounted:function(){this.load_positions_from_key()},computed:{position_list:{get:function(){return this.$store.state.selected_portfolio.position_list},set:function(t){this.$store.state.selected_portfolio.position_list=t}},selected_portfolio_title:{get:function(){return this.$store.state.selected_portfolio.title},set:function(t){this.$store.state.selected_portfolio.title=t}}},watch:{position_info_position_type:function(t){this.position_info.position_type=t},position_info_loan_type:function(t){this.position_info.loan_type=t}},created:function(){var t=this.$store.getters.getCookie("position_token");console.log("positioninfo_vue_created"),console.log(t)}}),_=p,f=s("2877"),u=s("6544"),v=s.n(u),m=s("8336"),b=s("b0af"),h=s("99d9"),x=s("ac7c"),g=s("a523"),y=s("169a"),k=s("ce7e"),j=s("0e8f"),w=s("132d"),C=s("a722"),V=s("8860"),$=s("ba95"),T=s("40fe"),S=s("5d23"),z=s("f774"),q=s("b56d"),O=s("9910"),D=s("e0c7"),I=s("71a3"),L=s("c671"),A=s("fe57"),P=s("aac8"),E=s("9a96"),N=s("2677"),R=s("71d9"),B=s("2a7f"),G=Object(f["a"])(_,r,l,!1,null,null,null),H=G.exports;v()(G,{VBtn:m["a"],VCard:b["a"],VCardActions:h["a"],VCardText:h["b"],VCheckbox:x["a"],VContainer:g["a"],VDialog:y["a"],VDivider:k["a"],VFlex:j["a"],VIcon:w["a"],VLayout:C["a"],VList:V["a"],VListTile:$["a"],VListTileAction:T["a"],VListTileActionText:S["a"],VListTileContent:S["b"],VListTileSubTitle:S["c"],VListTileTitle:S["d"],VNavigationDrawer:z["a"],VSelect:q["a"],VSpacer:O["a"],VSubheader:D["a"],VTab:I["a"],VTabItem:L["a"],VTabs:A["a"],VTabsItems:P["a"],VTabsSlider:E["a"],VTextField:N["a"],VToolbar:R["a"],VToolbarTitle:B["a"]});var F=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("v-container",{attrs:{fluid:"","mt-0":"","pb-0":"","pt-0":"","text-xs-center":""}},[s("div",{attrs:{id:"printArea"}},[s("v-layout",{attrs:{"align-center":"",row:"",wrap:""}},[s("v-container",{attrs:{"grid-list-xs":""}},[s("v-layout",{attrs:{"align-center":"","justify-end":""}},[s("v-flex",{attrs:{xs6:""}},[t._v("생성일 : "+t._s(t.results_data.timestamp))]),s("v-flex",{attrs:{xs3:""}},[s("v-btn",{attrs:{small:""},on:{click:function(e){return t.export_report()}}},[s("v-icon",{staticClass:"icon-flipped"},[t._v("reply")])],1)],1),s("v-flex",{attrs:{xs3:""}},[s("v-btn",{attrs:{small:"",disabled:t.isReportGeneratable},on:{click:function(e){return t.result_update()}}},[t._v("생성")])],1)],1)],1),s("v-snackbar",{attrs:{timeout:2e3,color:t.analysis_request_status,top:!0},model:{value:t.snackbar,callback:function(e){t.snackbar=e},expression:"snackbar"}},[t._v("\n        "+t._s(t.analysis_request_message)+"\n        ")]),s("v-snackbar",{attrs:{timeout:2e3,color:t.export_request_status,top:!0},model:{value:t.export_snackbar,callback:function(e){t.export_snackbar=e},expression:"export_snackbar"}},[t._v(t._s(t.export_request_message))])],1),s("div",{staticClass:"row"},[s("div",{staticClass:"col-xl-3 col-md-3 col-sm-6 col-6 mb-3"},[s("div",{staticClass:"card border-left-primary shadow h-100 py-2"},[s("div",{staticClass:"card-body"},[s("div",{staticClass:"row no-gutters align-items-center"},[s("div",{staticClass:"col mr-2"},[s("div",{staticClass:"text-xs font-weight-bold text-primary text-uppercase mb-1"},[t._v("자산")]),s("div",{staticClass:"h5 mb-0 font-weight-bold text-gray-800"},[t._v(t._s(this.results_data.summary.asset_amount))]),s("div",[t._v("억원")])]),s("div",{staticClass:"col-auto"},[s("i",{staticClass:"fas fa-calendar fa-2x text-gray-300"})])])])])]),s("div",{staticClass:"col-xl-3 col-md-3 col-sm-6 col-6 mb-3"},[s("div",{staticClass:"card border-left-success shadow h-100 py-2"},[s("div",{staticClass:"card-body"},[s("div",{staticClass:"row no-gutters align-items-center"},[s("div",{staticClass:"col mr-2"},[s("div",{staticClass:"text-xs font-weight-bold text-success text-uppercase mb-1"},[t._v("부채")]),s("div",{staticClass:"h5 mb-0 font-weight-bold text-gray-800"},[t._v(t._s(this.results_data.summary.liability_amount))]),s("div",[t._v("억원")])]),s("div",{staticClass:"col-auto"},[s("i",{staticClass:"fas fa-dollar-sign fa-2x text-gray-300"})])])])])]),s("div",{staticClass:"col-xl-3 col-md-3 col-sm-6 col-6 mb-3"},[s("div",{staticClass:"card border-left-success shadow h-100 py-2"},[s("div",{staticClass:"card-body"},[s("div",{staticClass:"row no-gutters align-items-center"},[s("div",{staticClass:"col mr-2"},[s("div",{staticClass:"text-xs font-weight-bold text-success text-uppercase mb-1"},[t._v("순자산")]),s("div",{staticClass:"h5 mb-0 font-weight-bold text-gray-800"},[t._v(t._s(this.results_data.summary.capital_amount))])]),s("div",{staticClass:"col-auto"},[s("i",{staticClass:"fas fa-dollar-sign fa-2x text-gray-300"})])])])])]),s("div",{staticClass:"col-xl-3 col-md-3 col-sm-6 col-6 mb-3"},[s("div",{staticClass:"card border-left-success shadow h-100 py-2"},[s("div",{staticClass:"card-body"},[s("div",{staticClass:"row no-gutters align-items-center"},[s("div",{staticClass:"col mr-2"},[s("div",{staticClass:"text-xs font-weight-bold text-success text-uppercase mb-1"},[t._v("총손익")]),s("div",{staticClass:"h5 mb-0 font-weight-bold text-gray-800"},[t._v(t._s(this.results_data.summary.profit_amount))])]),s("div",{staticClass:"col-auto"},[s("i",{staticClass:"fas fa-dollar-sign fa-2x text-gray-300"})])])])])])]),s("v-divider"),s("div",{staticClass:"row"},[s("div",{staticClass:"col-xl-12 col-lg-12"},[s("div",{staticClass:"card shadow"},[s("div",{staticClass:"card-header py-3"},[s("h6",{staticClass:"m-0 font-weight-bold text-primary"},[t._v("자산 내역")])]),s("div",{staticClass:"card-body pa-0"},[s("v-card",[[s("v-data-table",{staticClass:"elevation-0",attrs:{headers:t.headers,items:t.position_list,"hide-actions":""},scopedSlots:t._u([{key:"items",fn:function(e){return[s("td",[t._v(t._s(e.item.name))]),s("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.book_value))]),s("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.book_date))]),s("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.apt_name))]),s("td",{staticClass:"text-xs-left"},[s("v-progress-linear",{attrs:{value:"50",height:"5",color:e.item.color}})],1),s("td",{staticClass:"text-xs-right"},[s("v-btn",{attrs:{flat:"",icon:"",color:"grey"}},[s("v-icon",[t._v("edit")])],1)],1)]}}])})]],2)],1)])])]),s("v-divider"),s("div",{staticClass:"row"},[s("div",{staticClass:"col-xl-12 col-lg-12"},[s("div",{staticClass:"card shadow"},[s("div",{staticClass:"card-header py-3 d-flex flex-row align-items-center justify-content-between"},[s("h6",{staticClass:"m-0 font-weight-bold text-primary"},[t._v("현금흐름")])]),s("div",{staticClass:"card-body"},[s("div",{staticClass:"chart-area"},[s("canvas",{ref:"myChart"})])])])])]),s("v-divider"),s("div",{staticClass:"row"},[s("div",{staticClass:"col-lg-6"},[s("div",{staticClass:"card shadow"},[s("div",{staticClass:"card-header py-3"},[s("h6",{staticClass:"m-0 font-weight-bold text-primary"},[t._v("메모")])]),s("div",{staticClass:"card-body"},[s("p",[t._v("\n              SB Admin 2 makes extensive use of Bootstrap 4 utility classes in order to reduce CSS bloat\n              and poor page performance. Custom CSS classes are used to create custom components and\n              custom utility classes.\n            ")]),s("p",{staticClass:"mb-0"},[t._v("\n              Before working with this theme, you should become familiar with the Bootstrap\n              framework, especially the utility classes.\n            ")])])])])]),s("hr")],1)])},K=[],U=s("5b20"),M=s.n(U),J=s("6c27"),Q=s.n(J),W={props:["results_data","userinfo","position_list"],data:function(){return{position_stored:!1,snackbar:!1,analysis_request_status:"info",analysis_request_message:"no message",export_snackbar:!1,export_request_status:"info",export_request_message:"no message",headers:[{text:"Name",align:"left",value:"name"},{text:"Price",value:"price"},{text:"Date",value:"date"},{text:"AptName",value:"apt_name"},{text:"Ratio",value:"ratio"},{text:"Action",value:"action",align:"right"}],cashflow_chart:null,chartData:{datacollection:{labels:["January","February"],datasets:[{label:"Data One",backgroundColor:"#f87979",data:[40,21]}]}},options:{responsive:!0,maintainAspectRatio:!1}}},mounted:function(){console.log("report vue mounted"),this.$store.state.isCalculated||(this.chart=new M.a(this.$refs.myChart,{type:"bar",data:{labels:this.results_data.flows.dates,datasets:[{label:"In",backgroundColor:"blue",data:this.results_data.flows.inflows},{label:"out",backgroundColor:"red",data:this.results_data.flows.outflows}]}}))},methods:{export_report:function(){var t=this,e=this.$store.getters.getCookie("position_token"),s=Q()(t.results_data.toString());this.$axios.post(this.$store.state.url_end_point+"/export_report",{report_token:s,position_token:e,results_data:t.results_data}).then(function(e){var a=t.$store.state.url_end_point+"/report/"+s;navigator.clipboard.writeText(a).then(function(){t.export_snackbar=!0,t.export_request_status="success",t.export_request_message="링크 복사됨"})}).catch(function(e){t.snackbar=!0,t.analysis_request_message=e.response,t.analysis_request_status="링크 저장 실패"})},result_update:function(){var t=this,e=this.$store.getters.getCookie("position_token");this.$axios.post(this.$store.state.url_end_point+"/analysis",{email:this.$store.state.userinfo.email,position_token:e,position_list:this.$store.state.selected_portfolio.position_list}).then(function(e){t.$store.state.results_data=e.data.results_data,t.$store.state.isCalculated,t.analysis_request_message="success",t.analysis_request_status="success",t.snackbar=!0}).catch(function(e){400==e.response.status&&(t.snackbar=!0,console.log(e.response.message),t.analysis_request_message=this.response.message,t.analysis_request_status="error"),console.log(e)})},printDiv:function(){this.isHeaderVisible=!1,window.print(),this.isHeaderVisible=!0}},computed:{isHeaderVisible:{get:function(){return this.$store.state.isHeaderVisible},set:function(t){this.$store.state.isHeaderVisible=t}},isReportGeneratable:{get:function(){return 0==this.position_list.length}}},beforeDestroy:function(){this.cashflow_chart&&this.cashflow_chart.destroy()}},X=W,Y=(s("39c9"),s("8fea")),Z=s("8e36"),tt=s("2db4"),et=Object(f["a"])(X,F,K,!1,null,"16ddf32c",null),st=et.exports;v()(et,{VBtn:m["a"],VCard:b["a"],VContainer:g["a"],VDataTable:Y["a"],VDivider:k["a"],VFlex:j["a"],VIcon:w["a"],VLayout:C["a"],VProgressLinear:Z["a"],VSnackbar:tt["a"]});var at=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("v-container",{attrs:{"mt-0":"","pb-0":"","pt-0":"","text-xs-center":""}},[s("v-layout",{attrs:{row:"",wrap:""}},[s("v-flex",{attrs:{xs12:""}},[s("span",[t._v("ID : "+t._s(t.userinfo.email))])]),s("v-flex",{attrs:{xs12:""}},[s("span",[t._v("Saved TimeStamp : "+t._s(t.timestamp))])]),s("v-flex",{attrs:{xs12:""}},[s("v-btn",{attrs:{color:"primary"},on:{click:function(e){return t.store_position()}}},[t._v("Save")])],1),s("v-flex",{attrs:{xs12:""}},[s("transition",{attrs:{name:"fade"}},[t.alert.is_visible?s("div",[s("v-alert",{attrs:{value:!0,type:t.alert.type,transition:"scale-transition"}},[t._v(t._s(t.alert.message))])],1):t._e()])],1)],1)],1)},it=[],ot={props:["results_data","userinfo","position_list"],data:function(){return{alert:{is_visible:!1,type:"success",message:"success"},cookie:"empty",name:"test",access_key:"not generated",timestamp:""}},methods:{makeGuestCookie:function(){var t=new Date;return Q()(t.getTime().toString())},setCookie:function(t,e,s){console.log("setCookie");var a="";if(s){var i=new Date;i.setTime(i.getTime()+24*s*60*60*1e3),a="; expires="+i.toUTCString()}document.cookie=t+"="+(e||"")+a+"; path=/",console.log(this.$store.getters.getCookie("position_token"))},store_position:function(){var t=this;this.position_list.length<1&&(t.alert.is_visible=!0,t.alert.type="warning",t.message="position is empty");var e=this.makeGuestCookie();t.setCookie("position_token",e,7),this.$axios.post(this.$store.state.url_end_point+"/storepositions",{email:t.$store.state.userinfo.email,position_token:e,results_data:t.$store.state.results_data,position_list:this.position_list}).then(function(e){var s=e.data["message"];"success"==s&&(t.position_stored=!0,t.access_key=e.data["access_key"],t.alert.is_visible=!0,t.alert.type="success",t.alert.message=s,t.timestamp=e.data["timestamp"])}).catch(function(e){t.alert.is_visible=!0,t.alert.type="error",t.alert.message="save fail"})}}},nt=ot,rt=s("0798"),lt=Object(f["a"])(nt,at,it,!1,null,null,null),ct=lt.exports;v()(lt,{VAlert:rt["a"],VBtn:m["a"],VContainer:g["a"],VFlex:j["a"],VLayout:C["a"]});var dt={name:"App",components:{PositionInfo:H,ResultReport:st,UserSettings:ct},data:function(){return{drawer:!1,mainstep:0,selectedView:"positioninfo"}},methods:{setView:function(t){this.selectedView=t}}},pt=dt,_t=s("7496"),ft=s("549c"),ut=s("706c"),vt=Object(f["a"])(pt,o,n,!1,null,null,null),mt=vt.exports;v()(vt,{VApp:_t["a"],VBtn:m["a"],VContent:ft["a"],VIcon:w["a"],VList:V["a"],VListTile:$["a"],VListTileAction:T["a"],VListTileContent:S["b"],VListTileTitle:S["d"],VNavigationDrawer:z["a"],VSpacer:O["a"],VToolbar:R["a"],VToolbarSideIcon:ut["a"],VToolbarTitle:B["a"]});var bt=s("2f62");a["a"].use(bt["a"]);var ht=new bt["a"].Store({state:{url_end_point:"http://127.0.0.1:5000",isHeaderVisible:!0,userinfo:{email:"Guest"},selected_portfolio:{title:"default",position_list:[]},position_cookie:"position_token",portfolio_list:[{title:"predefined1",position_list:[{name:"test name4",asset_type:"apartment",address:"test address",legal_dong:"test dong",apt_name:"test apt",private_area:55.12,region_code:11110,book_value:1e4,book_date:"2018-10-11",position_type:"자가",rent:{deposit:0,monthly_payment:1e3,effective_date:"2018-10-11",maturity_date:"2018-10-11"},loan_type:"없음",loan:{amount:0,rate:.03,effective_date:"2018-10-11",maturity_date:"2018-10-11"}},{name:"test name2",asset_type:"apartment",address:"test address",legal_dong:"test dong",apt_name:"test apt",private_area:55.12,region_code:11110,book_value:1e4,book_date:"2018-10-11",position_type:"전세",rent:{deposit:7e3,monthly_payment:1e3,effective_date:"2018-10-11",maturity_date:"2018-10-11"},loan_type:"없음",loan:{amount:5e3,rate:.03,effective_date:"2018-10-11",maturity_date:"2018-10-11"}}]},{title:"predefined2",position_list:[{name:"test name3",asset_type:"apartment",address:"test address",legal_dong:"test dong",apt_name:"test apt",private_area:55.12,region_code:11110,book_value:1e4,book_date:"2018-10-11",position_type:"월세",rent:{deposit:6e3,monthly_payment:1e3,effective_date:"2018-10-11",maturity_date:"2018-10-11"},loan_type:"없음",loan:{amount:5e3,rate:.03,effective_date:"2018-10-11",maturity_date:"2018-10-11"}}]}],new_position_info_template:{name:"부동산",asset_type:"apartment",address:"주소 확인 필요함",legal_dong:"test dong",apt_name:"test apt",private_area:55.12,region_code:11110,book_value:1e4,book_date:"2018-10-11",position_type:"자가거주",rent:{deposit:0,monthly_payment:1e3,effective_date:"2018-10-11",maturity_date:"2018-10-11"},loan_type:"없음",loan:{amount:0,rate:.03,effective_date:"2018-10-11",maturity_date:"2018-10-11"}},results_data:{name:"not calculated",result_date:"Not Calulated",summary:{asset_amount:"-",liability_amount:"-",capital_amount:"-",profit_percent:"-",profit_amount:"-"},flows:{dates:["2018-10-11","2018-10-11"],inflows:[100,100],outflows:[100,100]},comments:{},timestamp:""},isCalculated:!1,mainstep:0},getters:{position_list:function(t){return t.selected_portfolio.position_list},getCookie:function(t){return function(t){for(var e=t+"=",s=document.cookie.split(";"),a=0;a<s.length;a++){var i=s[a];while(" "==i.charAt(0))i=i.substring(1,i.length);if(0==i.indexOf(e)){var o=i.substring(e.length,i.length);return o}}return null}}}}),xt=s("9f7b"),gt=s.n(xt),yt=(s("f9e3"),s("2dd8"),s("bc3a")),kt=s.n(yt);a["a"].use(gt.a),a["a"].config.productionTip=!1,a["a"].prototype.$axios=kt.a,new a["a"]({store:ht,render:function(t){return t(mt)}}).$mount("#app")},ac7d:function(t,e,s){}});
//# sourceMappingURL=app.753ac7d8.js.map