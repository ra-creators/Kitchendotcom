"use strict";

var tinderContainer2 = document.querySelector(".tinder2");
var allCards2 = document.querySelectorAll(".tinder--card2");
var nope2 = document.getElementById("nope2");
var love2 = document.getElementById("love2");

function initCards2(card, index) { 
  var newCards = document.querySelectorAll(".tinder--card2:not(.removed)");

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards2.length - index;
    card.style.transform =
      "scale(" + (20 - index) / 20 + ") translateY(-" + 30 * index + "px)";
    card.style.opacity = (10 - index) / 10;
  });

  tinderContainer2.classList.add("loaded");
}

initCards2();

allCards2.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on("pan", function (event) {
    el.classList.add("moving");
  });

  hammertime.on("pan", function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    tinderContainer2.classList.toggle("tinder_love2", event.deltaX > 0);
    tinderContainer2.classList.toggle("tinder_nope2", event.deltaX < 0);

    var xMulti = event.deltaX * 0.03;
    var yMulti = event.deltaY / 80;
    var rotate = xMulti * yMulti;

    event.target.style.transform =
      "translate(" +
      event.deltaX +
      "px, " +
      event.deltaY +
      "px) rotate(" +
      rotate +
      "deg)";
  });

  hammertime.on("panend", function (event) {
    el.classList.remove("moving");
    tinderContainer2.classList.remove("tinder_love2");
    tinderContainer2.classList.remove("tinder_nope2");

    var moveOutWidth = document.body.clientWidth;
    var keep = Math.abs(event.deltaX) < 80 || Math.abs(event.velocityX) < 0.5;

    event.target.classList.toggle("removed", !keep);

    if (keep) {
      event.target.style.transform = "";
    } else {
      var endX = Math.max(
        Math.abs(event.velocityX) * moveOutWidth,
        moveOutWidth
      );
      var toX = event.deltaX > 0 ? endX : -endX;
      var endY = Math.abs(event.velocityY) * moveOutWidth;
      var toY = event.deltaY > 0 ? endY : -endY;
      var xMulti = event.deltaX * 0.03;
      var yMulti = event.deltaY / 80;
      var rotate = xMulti * yMulti;

      event.target.style.transform =
        "translate(" +
        toX +
        "px, " +
        (toY + event.deltaY) +
        "px) rotate(" +
        rotate +
        "deg)";
      initCards2();
    }
  });
});

function createButtonListener(love2) {
  return function (event) {
    var cards = document.querySelectorAll(".tinder--card2:not(.removed)");
    var moveOutWidth = document.body.clientWidth * 1.5;

    if (!cards.length) return false;

    var card = cards[0];

    card.classList.add("removed");

    if (love2) {
      card.style.transform =
        "translate(" + moveOutWidth + "px, -100px) rotate(-30deg)";
    } else {
      card.style.transform =
        "translate(-" + moveOutWidth + "px, -100px) rotate(30deg)";
    }

    initCards2();

    event.preventDefault();
  };
}

var nope2Listener = createButtonListener(false);
var love2Listener = createButtonListener(true);

nope2.addEventListener("click", nope2Listener);
love2.addEventListener("click", love2Listener);
