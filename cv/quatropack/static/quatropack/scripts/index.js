/*jshint esversion: 6 */

function init_carouseles() {
    /*
    var glide = new Glide('#examples', {
        type: 'carousel',
        perView: 4,
        focusAt: 'center',
        breakpoints: {
            800: {
                perView: 2
            },
            480: {
                perView: 1
            }
        }
    })

    glide.mount()
    */
    /*
    */
    let conf = {
        rtl: true,
        loop: true,
        autoWidth: false,
        rewind: false,
        dots: false,
        autoplay: true,
        autoplayHoverPause: true,
        autoplayTimeout: 10000,
        items: 5,
        center: true,
        scrollPerPage: true,
        
        animateIn: true,
        animateOut: true,
        
        mouseDrag: true,
        touchDrag: true,
        pullDrag: true,
        nav: true,
        dots: true,
        dotsEach: true,
        navText : ["<<<",">>>"],
        slideBy: 5,
        
    }
    $(".qp-carousel-examples").owlCarousel(conf)
    conf.autoplayTimeout = 3000
    //conf.rtl = false
    conf.scrollPerPage = false
    //conf.slideBy = 1
    conf.mouseDrag = false
    conf.touchDrag = false
    conf.pullDrag = false
    conf.nav = false
    conf.dots = false
    conf.margin = 20
    conf.autoHeight = true

    
    $(".qp-carousel-logotypes").owlCarousel(conf).on('changed.owl.carousel', 
        function(event) {
            //dbg('logotypes shifted')
        }
    )
    //conf.autoplayTimeout = 3000
    conf.items = 3
    conf.autoplay = false
    conf.startPosition = Math.floor(100*Math.random())
    let car_ben = $(".qp-carousel-benefits")
    car_ben.owlCarousel(conf)
    /*
    */
    car_ben.on('changed.owl.carousel', 
        function(event) {
            dbg('.')
            /*
            $(".qp-carousel-benefits").css('zoom', '90%')
            let items = $(".qp-carousel-benefits .active")
            items.css('zoom', '90%').css('filter', 'grayscale(0.5) blur(10px)')
            start_after(500, function() {
                $(items[1]).css('zoom', '120%').css('filter', 'none')
            })
            */
        }
    )
    
    /*
    let benefits = $('.qp-carousel-benefits .active')
    $(benefits, 'img')
        .css('filter', 'grayscale(50%)')
    $(benefits)
        .css('padding', '1.5em')
    $(benefits[1], 'img')
        .css('filter', 'grayscale(0%)')
    $(benefits[1])
        .css('padding', '0')
        */
}

function show_back() {
    //$('.qp-body-back').removeClass('d-none')    
}

function init_scroll_handler() {
    const ZOOM_LIMIT_MARGINE = 50
    const TOP_SCROLL_ZOOM_LIMIT = 250
    const TO_TOP_ZOOM_LIMIT = 500
    const BOTTOM_SCROLL_ZOOM_LIMIT = 300
    let last_scroll_y = window.scrollY
    let top_zoomed = true
    let bottom_zoomed = false
    let $nav = $(".qp-nav")
    //let init_zoom_value = $nav.css('zoom')
    let init_zoom_value = '150%'//$nav.css('zoom')
    
    let bottom_scroll_zoom = document.documentElement.scrollHeight-
            (document.documentElement.clientHeight+BOTTOM_SCROLL_ZOOM_LIMIT)
    
    /**/
    if (TOP_SCROLL_ZOOM_LIMIT < last_scroll_y) {
        //$nav.css('zoom', '100%')
        $nav.css('font-size', '100%')
        top_zoomed = false
    }
    
    $('.qp-to-top').css('display', TO_TOP_ZOOM_LIMIT < last_scroll_y ? 'block' : 'none')
    
    if (bottom_scroll_zoom + ZOOM_LIMIT_MARGINE < last_scroll_y) {
        $('.qp-footer').animate({ zoom: '150%' }, "slow");
        bottom_zoomed = true
    }
    /**/
    $(window).scroll(function(e) {
        var scrollTop = $(window).scrollTop()
        var intensity = 3.5
        $('img.qp-body-back').css('transform', 'translateY(' + (scrollTop / intensity) + 'px)')
        
        bottom_scroll_zoom = document.documentElement.scrollHeight-
                (document.documentElement.clientHeight+BOTTOM_SCROLL_ZOOM_LIMIT)
        //dbg('scroll');
        //dbg(e);
        let is_to_top = last_scroll_y > window.scrollY
        last_scroll_y = window.scrollY
        //dbg('scroll', window.scrollY, is_to_top)
        
        //nav menu zooming
        if (!top_zoomed && is_to_top && TOP_SCROLL_ZOOM_LIMIT + ZOOM_LIMIT_MARGINE > last_scroll_y) {
            top_zoomed = true
            //dbg("to up")
            //$nav.animate({ zoom: init_zoom_value }, "slow");
            $nav.animate({ 'font-size': '100%' }, "slow");
        }
        else
        if (top_zoomed && !is_to_top && TOP_SCROLL_ZOOM_LIMIT - ZOOM_LIMIT_MARGINE < last_scroll_y) {
            top_zoomed = false
            //dbg("to down")
            init_zoom_value = $nav.css('zoom')
            //$nav.animate({ zoom: '100%' }, "slow");
            $nav.animate({ 'font-size': '100%' }, "slow");
        }
        //to top btn showing
        if (is_to_top && TO_TOP_ZOOM_LIMIT + ZOOM_LIMIT_MARGINE > last_scroll_y) {
            $('.qp-to-top').css('display', 'none')
        }
        else
        if (!is_to_top && TO_TOP_ZOOM_LIMIT - ZOOM_LIMIT_MARGINE < last_scroll_y) {
            $('.qp-to-top').css('display', 'block')
        }
        //bottom zooming
        //dbg(bottom_scroll_zoom, last_scroll_y)
        
        if (!bottom_zoomed && !is_to_top && bottom_scroll_zoom + ZOOM_LIMIT_MARGINE < last_scroll_y) {
            bottom_zoomed = true
            //dbg("to down")
            $('.qp-footer').animate({ zoom: '150%' }, "slow");
        }
        else
        if (bottom_zoomed && is_to_top && bottom_scroll_zoom - ZOOM_LIMIT_MARGINE > last_scroll_y) {
            bottom_zoomed = false
            //dbg("to up")
            $('.qp-footer').animate({ zoom: '100%' }, "slow");
        }
    });
}

function init_anchor_smooth_scrolling() {
    var $root = $('html, body');
    
    //$('a[href^="#"]')
    $('.qp-smooth-scroll').click(function () {
        $root.animate({
            scrollTop: $( $.attr(this, 'href') ).offset().top
        }, 500);

        return false;
    });
}

function init_devices_tab() {
    $('.qp-tabs li:last-child a').tab('show')
}

function show_loading() {
    if (!$('.qp-loading').length) {
        return
    }

    let body = $('body')
    let loading_progress = 0

    body.css('overflow', 'hidden') 

    let progress_starter = start_every(100, function() {
        loading_progress += 4        
        $('.qp-indicator').css('width', loading_progress+'%')
        if (loading_progress >= 40) progress_starter.finish()
    })
    
    start_after(1500, function() {
        $('.qp-loading').remove()
        body.css('overflow', 'scroll')
    })
}


$(function() {
	//dbg("start")
	//init_scroll_handler()
    init_anchor_smooth_scrolling()
    init_carouseles()
    
    if ('true' !== get_arg('is_examples')) {
        init_devices_tab()        
    }
    
    show_loading()
   
    init_scroll_handlers()
    
    $('.qp-menu-toggler').click(function() {
        let toggler = $(this)
        let body = $('body')
        let is_closed = toggler.hasClass('collapsed')
        let menu = $('.qp-main-menu')
        
        if (is_closed) {
            menu.css('display', 'block')
            //menu.fadeTo('slow', '100%')
            menu.animate({ opacity: 1 }, 'slow')
            $('.qp-menu-toggler').removeClass('collapsed')
            //menu.animate({ display: 'block' }, 'slow')
            //body.css('overflow', 'hidden')
        } else {
            /*
            menu.fadeTo('slow', '0', function() {
                menu.css('display', 'none')
            })
            */
            //body.css('overflow', 'scroll')
            //menu.animate({ display: 'none' }, 'slow')
            menu.animate({ opacity: 0 }, 'slow', function() {
                menu.css('display', 'none')
            })
            $('.qp-menu-toggler').addClass('collapsed')
        }
            
    })
	//dbg("inited")
})