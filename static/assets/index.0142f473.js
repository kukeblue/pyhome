import{d as k,r as m,o as C,a as f,c as F,b as i,w as l,F as b,e as r,f as B,g as d,t as S,h as E,i as x,A as I}from"./vendor.5a33aa9b.js";const D=function(){const o=document.createElement("link").relList;if(o&&o.supports&&o.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))s(e);new MutationObserver(e=>{for(const t of e)if(t.type==="childList")for(const u of t.addedNodes)u.tagName==="LINK"&&u.rel==="modulepreload"&&s(u)}).observe(document,{childList:!0,subtree:!0});function n(e){const t={};return e.integrity&&(t.integrity=e.integrity),e.referrerpolicy&&(t.referrerPolicy=e.referrerpolicy),e.crossorigin==="use-credentials"?t.credentials="include":e.crossorigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function s(e){if(e.ep)return;e.ep=!0;const t=n(e);fetch(e.href,t)}};D();const w=d("\u5F00\u542F"),L=d("\u505C\u6B62"),N=k({setup(v){let o=-1;const n=m(!1),s=m([]),e=()=>{n.value=!n.value,n.value?o=setInterval(a=>{y()},1e3):clearInterval(o)},t=a=>{switch(a.name){case"\u9886\u53D6\u6293\u9B3C\u4EFB\u52A1":r.get("/api/mh/getZgTask");break;case"\u805A\u7CBE\u4F1A\u795E\u6218\u6597\u81EA\u52A8\u670D\u52A1":r.get("/api/mh/startServiceTjJJHS");break}},u=a=>{switch(a.name){case"\u9886\u53D6\u6293\u9B3C\u4EFB\u52A1":r.get("/api/mh/stopZgTask");break;case"\u805A\u7CBE\u4F1A\u795E\u6218\u6597\u81EA\u52A8\u670D\u52A1":r.get("/api/mh/stopServiceTjJJHS");break}},y=async()=>{const a=await r.get("/api/mh/getTaskAndEventStatus");a.data.list&&(s.value=a.data.list)};C(()=>{clearInterval(o)});const g=[{title:"\u540D\u79F0",dataIndex:"name",key:"name"},{title:"\u72B6\u6001",dataIndex:"status",key:"status"},{title:"\u64CD\u4F5C",dataIndex:"operation",key:"operation",slots:{customRender:"operation"}}];return(a,T)=>{const c=f("a-button"),h=f("a-table");return B(),F(b,null,[i(c,{type:"primary",style:{"margin-bottom":"20px"},onClick:e},{default:l(()=>[d(S(n.value?"\u540C\u6B65\u5DF2\u5F00\u542F":"\u542F\u52A8\u540C\u6B65"),1)]),_:1}),i(h,{"row-key":"name",pagination:!1,columns:g,"data-source":s.value},{operation:l(({record:p})=>[E("div",null,[i(c,{class:"m-5",size:"small",type:"primary",onClick:A=>t(p)},{default:l(()=>[w]),_:2},1032,["onClick"]),i(c,{class:"m-5",size:"small",onClick:A=>u(p)},{default:l(()=>[L]),_:2},1032,["onClick"])])]),_:1},8,["data-source"])],64)}}});const _=x(N);_.use(I);_.mount("#app");
