"use strict";

gsap.registerPlugin(ScrollTrigger);
var tops = gsap.utils.toArray('.anim-top');
tops.forEach(function (top) {
  gsap.from(top, {
    y: "30",
    opacity: 0,
    duration: 2,
    scrollTrigger: {
      trigger: top,
      start: "top 90%",
      end: "bottom 10%",
      toggleActions: "restart complete restart reverse"
    }
  });
});
var downs = gsap.utils.toArray('.anim-down');
downs.forEach(function (down) {
  gsap.from(down, {
    y: "-30",
    opacity: 0,
    duration: 2,
    scrollTrigger: {
      trigger: down,
      start: "top 90%",
      end: "bottom 10%",
      toggleActions: "restart complete restart reverse"
    }
  });
});
var textsToRight = gsap.utils.toArray('.anim-right');
textsToRight.forEach(function (text) {
  gsap.from(text, {
    x: "30",
    opacity: 0,
    duration: 2,
    scrollTrigger: {
      trigger: text,
      start: "top 85%",
      end: "bottom 15%",
      toggleActions: "restart complete restart reverse"
    }
  });
});
var textsToLeft = gsap.utils.toArray('.anim-left');
textsToLeft.forEach(function (text) {
  gsap.from(text, {
    x: "-30",
    opacity: 0,
    duration: 2,
    scrollTrigger: {
      trigger: text,
      start: "top 85%",
      end: "bottom 15%",
      toggleActions: "restart complete restart reverse"
    }
  });
});
gsap.from('.footer-section', {
  scrollTrigger: {
    trigger: ".footer-section",
    toggleActions: "restart complete restart reverse"
  },
  y: '20',
  opacity: 0,
  duration: 2
});