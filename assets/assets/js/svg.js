var line1 = $('#line1');
var div1 = $('#step1');
var div2 = $('#step2');

var x1 = div1.offset().left + (div1.width()/2);
var y1 = div1.offset().top + (div1.height()/2);
var x2 = div2.offset().left + (div2.width()/2);
var y2 = div2.offset().top + (div2.height()/2);

line1.attr('x1',x1).attr('y1',y1).attr('x2',x2).attr('y2',y2);