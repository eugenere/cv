/*jshint esversion: 6 */

function init_carouseles() {
    let cfg = {
        rtl: false,
        loop: true,
        autoplay: true,
        autoplayTimeout: 8000,
        items: 5,
        slideBy: 5,
        autoplayHoverPause: false,

        //margin: -19,
        //autoWidth: true,
        //scrollPerPage: true,

        //animateIn: true,
        //animateOut: true,
        
        mouseDrag: false,
        touchDrag: false,
        pullDrag: false,

        nav: false,
        dots: false,
    }
    $(".qp-carousel-products").owlCarousel(cfg)
    cfg.autoplayTimeout = 12000
    //cfg.autoplayHoverPause = false
    $(".qp-carousel-logotypes").owlCarousel(cfg)
}

$(function () {
    init_carouseles()
})