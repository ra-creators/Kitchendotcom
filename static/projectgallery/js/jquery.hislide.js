(function ($) {
    var slide = function (ele, options) {
        var $ele = $(ele);
        var setting = {
            speed: 1000,
            interval: 2000,

        };
        $.extend(true, setting, options);
        var states = [{
                $zIndex: 1,
                height: 225,
                width: 400,
                $opacity: 0.4
            },
            {
                $zIndex: 2,
                height: 270,
                width: 480,
                $opacity: 0.7
            },
            {
                $zIndex: 3,
                height: 297,
                width: 528,
                $opacity: 1
            },
            {
                $zIndex: 2,
                height: 270,
                width: 480,
                $opacity: 0.7
            },
            {
                $zIndex: 1,
                height: 225,
                width: 400,
                $opacity: 0.4
            },
        ];

        var $lis = $ele.find('li');
        var timer = null;


        $ele.find('.hi-next').on('click', function () {
            next();
        });
        $ele.find('.hi-prev').on('click', function () {
            states.push(states.shift());
            move();
        });
        $ele.on('mouseenter', function () {
            clearInterval(timer);
            timer = null;
        }).on('mouseleave', function () {
            autoPlay();
        });

        move();
        autoPlay();


        function move() {
            $lis.each(function (index, element) {
                var state = states[index];
                $(element).css('zIndex', state.$zIndex).finish().animate(state, setting.speed).find('img').css('opacity', state.$opacity);
            });
        }


        function next() {

            states.unshift(states.pop());
            move();
        }

        function autoPlay() {
            timer = setInterval(next, setting.interval);
        }
    }

    $.fn.hiSlide = function (options) {
        $(this).each(function (index, ele) {
            slide(ele, options);
        });

        return this;
    }
})(jQuery);