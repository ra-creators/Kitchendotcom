"use strict";

var tinderContainer4 = document.querySelector(".tinder4");
var allCards4 = document.querySelectorAll(".tinder--card4");
var nope4 = document.getElementById("nope4");
var love4 = document.getElementById("love4");

function initCards4(card, index) { 
  var newCards = document.querySelectorAll(".tinder--card4:not(.removed)");

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards4.length - index;
    card.style.transform =
      "scale(" + (20 - index) / 20 + ") translateY(-" + 30 * index + "px)";
    card.style.opacity = (10 - index) / 10;
  });

  tinderContainer4.classList.add("loaded");
}

initCards4();

allCards4.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on("pan", function (event) {
    el.classList.add("moving");
  });

  hammertime.on("pan", function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    tinderContainer4.classList.toggle("tinder_love4", event.deltaX > 0);
    tinderContainer4.classList.toggle("tinder_nope4", event.deltaX < 0);

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
    tinderContainer4.classList.remove("tinder_love4");
    tinderContainer4.classList.remove("tinder_nope4");

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
      initCards4();
    }
  });
});

function createButtonListener(love4) {
  return function (event) {
    var cards = document.querySelectorAll(".tinder--card4:not(.removed)");
    var moveOutWidth = document.body.clientWidth * 1.5;

    if (!cards.length) return false;

    var card = cards[0];

    card.classList.add("removed");

    if (love4) {
      card.style.transform =
        "translate(" + moveOutWidth + "px, -100px) rotate(-30deg)";
    } else {
      card.style.transform =
        "translate(-" + moveOutWidth + "px, -100px) rotate(30deg)";
    }

    initCards4();

    event.preventDefault();
  };
}

var nope4Listener = createButtonListener(false);
var love4Listener = createButtonListener(true);

nope4.addEventListener("click", nope4Listener);
love4.addEventListener("click", love4Listener);
