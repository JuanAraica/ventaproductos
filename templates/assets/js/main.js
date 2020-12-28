var descripcion = "";
Document.write();





jQuery(document).ready(function () {

    jQuery(".play-1, .play-2").yu2fvl();

    jQuery(".owl-carousel4").owlCarousel({
        loop: true,
        center: true,
        margin: 20,
        responsiveClass: true,
        nav: true,
        responsive: {
            0: {
                items: 2,

            },
            600: {
                items: 3,

            },
            1000: {
                items: 5,
                nav: true,
                loop: true
            }
        }
    });

    jQuery(".owl-carousel5").owlCarousel({
        loop: true,
        center: false,
        margin: 10,
        responsiveClass: true,
        nav: false,
        responsive: {
            0: {
                items: 2,

            },
            600: {
                items: 3,

            },
            1000: {
                items: 6,
                nav: false,
                loop: true
            }
        }
    });

});

function myFunction(x) {
    x.classList.toggle("change");
}



jQuery(".link-img").click(function () {
    var link = jQuery(this).attr("data-link");
    //alert(link);
    jQuery("#screen").attr("src", link)
});



var count = 0;
jQuery("#toggle-search").click(function () {
    count++;
    //even odd click detect 
    var isEven = function (someNumber) {
        return (someNumber % 2 === 0) ? true : false;
    };
    // on odd clicks do this
    if (isEven(count) === false) {
        //jQuery("#nav-search").css({"display":"block"});
        jQuery("#nav-search").slideDown();
        jQuery("#toggle-search").attr("src", "assets/images/close.png");

    }
    // on even clicks do this
    else if (isEven(count) === true) {
        //jQuery("#nav-search").css({"display":"none"});
        jQuery("#nav-search").slideUp();

        jQuery("#toggle-search").attr("src", "assets/images/search-icon.png");
    }
});

$(document).ready(function () {


    /* Navigation burger onclick side navigation show */
    $('.burger-container').on('click', function () {
        $('.main-navigation').toggle('slow');

        if ($('#myBtn').hasClass('change')) {
            $('body').addClass('stop-scroll');
        } else {
            $('body').removeClass('stop-scroll');
        }
    });


    /* About me slider */
    $('.about-me-slider').slick({
        slidesToShow: 1,
        prevArrow: '<span class="span-arrow slick-prev"><</span>',
        nextArrow: '<span class="span-arrow slick-next">></span>'
    });

    /* Blog slider */
    $('.blog-slider').slick({
        slidesToShow: 2,
        prevArrow: '<span class="span-arrow slick-prev"><</span>',
        nextArrow: '<span class="span-arrow slick-next">></span>',
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 1
            }
        }]
    });

});



var counta = 0;

$(window).scroll(function (e) {


    /* Onscroll number counter */
    var statisticNumbers = $('.single-count');
    if (statisticNumbers.length) {
        var oTop = statisticNumbers.offset().top - window.innerHeight;
        if (counta == 0 && $(window).scrollTop() > oTop) {
            $('.count').each(function () {
                var $this = $(this),
                    countTo = $this.attr('data-count');
                $({
                    countNum: $this.text()
                }).animate({
                        countNum: countTo
                    },

                    {
                        duration: 2000,
                        easing: 'swing',
                        step: function () {
                            $this.text(Math.floor(this.countNum));
                        },
                        complete: function () {
                            $this.text(this.countNum);
                        }
                    });
            });
            counta = 1;
        }
    }

});