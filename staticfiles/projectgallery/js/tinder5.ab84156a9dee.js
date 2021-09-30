"use strict";

var tinderContainer5 = document.querySelector(".tinder5");
var allCards5 = document.querySelectorAll(".tinder--card5");
var nope5 = document.getElementById("nope5");
var love5 = document.getElementById("love5");

function initCards5(card, index) { 
  var newCards = document.querySelectorAll(".tinder--card5:not(.removed)");

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards5.length - index;
    card.style.transform =
      "scale(" + (20 - index) / 20 + ") translateY(-" + 30 * index + "px)";
    card.style.opacity = (10 - index) / 10;
  });

  tinderContainer5.classList.add("loaded");
}

initCards5();

allCards5.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on("pan", function (event) {
    el.classList.add("moving");
  });

  hammertime.on("pan", function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    tinderContainer5.classList.toggle("tinder_love5", event.deltaX > 0);
    tinderContainer5.classList.toggle("tinder_nope5", event.deltaX < 0);

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
    tinderContainer5.classList.remove("tinder_love5");
    tinderContainer5.classList.remove("tinder_nope5");

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
      initCards5();
    }
  });
});

function createButtonListener(love5) {
  return function (event) {
    var cards = document.querySelectorAll(".tinder--card5:not(.removed)");
    var moveOutWidth = document.body.clientWidth * 1.5;

    if (!cards.length) return false;

    var card = cards[0];

    card.classList.add("removed");

    if (love5) {
      card.style.transform =
        "translate(" + moveOutWidth + "px, -100px) rotate(-30deg)";
    } else {
      card.style.transform =
        "translate(-" + moveOutWidth + "px, -100px) rotate(30deg)";
    }

    initCards5();

    event.preventDefault();
  };
}

var nope5Listener = createButtonListener(false);
var love5Listener = createButtonListener(true);

nope5.addEventListener("click", nope5Listener);
love5.addEventListener("click", love5Listener);
