/* Vave Workflow Store — scroll reveals and micro-interactions adapted from
   the owner's Vave Automations HQ motion engine. No tracking or remote calls. */
(function(){
'use strict';
if(!document.body)return;
const reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)');
const noMotion=()=>Boolean(reduced&&reduced.matches);
const selectors='.hero,.sec-head,.product,.step,.affiliate-hero,.affiliate-list article,.newsletter,.faq details,.card,.grid>.card';
let observer=null;
const seen=new WeakSet();
function revealVisible(){
  document.querySelectorAll('.motion-reveal').forEach(el=>el.classList.add('is-visible'));
  document.body.classList.remove('motion-ready');
}
if(!noMotion()&&typeof IntersectionObserver==='function'){
  observer=new IntersectionObserver(entries=>{
    for(const entry of entries){
      if(entry.isIntersecting){
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    }
  },{threshold:.045,rootMargin:'0px 0px 45px 0px'});
  document.body.classList.add('motion-ready');
  function wire(){
    let previousParent=null,order=0;
    document.querySelectorAll(selectors).forEach(el=>{
      if(seen.has(el))return;
      seen.add(el);
      const parent=el.parentElement;
      if(parent!==previousParent){previousParent=parent;order=0;} else order++;
      el.style.setProperty('--motion-delay',Math.min(order,5)*55+'ms');
      el.classList.add('motion-reveal');
      const rect=el.getBoundingClientRect();
      if(rect.bottom<=0 || rect.top<window.innerHeight*.72){el.classList.add('is-visible');return;}
      observer.observe(el);
    });
  }
  wire();
  if(typeof MutationObserver==='function'){
    let pending=false;
    const mo=new MutationObserver(records=>{
      if(!records.some(record=>record.addedNodes.length))return;
      if(pending)return;
      pending=true;
      requestAnimationFrame(()=>{pending=false;wire();});
    });
    mo.observe(document.querySelector('#products-grid')||document.body,{childList:true,subtree:true});
  }
}else{revealVisible();}
if(reduced&&reduced.addEventListener){
  reduced.addEventListener('change',()=>{
    if(noMotion()){
      observer?.disconnect();observer=null;revealVisible();
    }
  });
}
const header=document.querySelector('header');
if(header){
  const progress=document.createElement('div');
  progress.className='vave-scroll-progress';
  progress.setAttribute('aria-hidden','true');
  header.appendChild(progress);
  let scheduled=false;
  function update(){
    scheduled=false;
    const max=Math.max(1,document.documentElement.scrollHeight-innerHeight);
    progress.style.transform='scaleX('+Math.max(0,Math.min(1,scrollY/max))+')';
  }
  addEventListener('scroll',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(update);}},{passive:true});
  addEventListener('resize',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(update);}},{passive:true});
  update();
}
document.addEventListener('pointerdown',event=>{
  if(noMotion()||event.pointerType!=='mouse')return;
  const button=event.target.closest('.button,.head-link,.product button,.back,.primary,.secondary');
  if(!button||button.disabled)return;
  const rect=button.getBoundingClientRect();
  const ripple=document.createElement('span');
  ripple.className='motion-ripple';
  ripple.style.left=(event.clientX-rect.left)+'px';
  ripple.style.top=(event.clientY-rect.top)+'px';
  button.appendChild(ripple);
  ripple.addEventListener('animationend',()=>ripple.remove(),{once:true});
},{passive:true});
})();
