$(document).ready(function () {


    var logo = $(".logo").html();
    var nav = $("nav").html();
    var headerBig = $('<div class="logo-nav"><div class="logo">' + logo + '</div><nav>' + nav + '</nav></div>');
    var headerSmall = $('<div class="logo-nav"><div class="logo logo--small">' + logo + '</div><nav class="burgermenue nav-small"><div class="burgermenue__line burgermenue__line-top"></div><div class="burgermenue__line burgermenue__line-middle"></div><div class="burgermenue__line burgermenue__line-bottom"></div></nav></div><div class="burgermenue__list">' + nav + '</div>');


    function small() {
        $("header").empty().append(headerSmall);
        $(".burgermenue").click(function () {
            $(".burgermenue").toggleClass("burgermenue--active");
            $(".burgermenue__list").toggleClass("show");
            $(".burgermenue__line-top").toggleClass("burgermenue__line-top--active");
            $(".burgermenue__line-middle").toggleClass("burgermenue__line-middle--active");
            $(".burgermenue__line-bottom").toggleClass("burgermenue__line-bottom--active");
        });
    }

    function big() {
        $("header").empty().append(headerBig);
    };


    // Beim Skalieren der Seite
    $(window).resize(function () {
        var screenwidth = $(window).width();
        if (screenwidth <= 1000) {
            small();
        } else {
            big();
        }
    });

    // Beim Laden der Seite
    if ($(window).width() <= 1000) {
        small();
    } else {
        big();
    }


});
