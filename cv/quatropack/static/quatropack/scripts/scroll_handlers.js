/*jshint esversion: 6 */

function create_scroll_handler_for_footer() {
    const BOTTOM_SCROLL_ZOOM_LIMIT = 300
    const ZOOM_LIMIT_MARGINE = 50
    
    let last_scroll_y = window.scrollY
    
    let info = $('.qp-footer .qp-info')
    let footer = $('.qp-footer')
    let bottom_scroll_zoom = document.documentElement.scrollHeight-
            (document.documentElement.clientHeight+BOTTOM_SCROLL_ZOOM_LIMIT)
    let bottom_zoomed = bottom_scroll_zoom + ZOOM_LIMIT_MARGINE < last_scroll_y

    if (bottom_zoomed) {
        info.css('font-size', '150%')
        //footer.css('height', '2.5em')
    } else {
        info.css('font-size', '100%')
        //footer.css('height', '1.5em')
    }
    
    return {
        update: function() {
            let is_to_top = last_scroll_y > window.scrollY
            last_scroll_y = window.scrollY
            
            if (!bottom_zoomed && !is_to_top && bottom_scroll_zoom + ZOOM_LIMIT_MARGINE < last_scroll_y) {
                bottom_zoomed = true
                info.animate({ fontSize: '150%' }, "slow")
                //footer.animate({ height: '2.5em' }, "slow")
                dbg('footer bigger')
            }
            else
            if (bottom_zoomed && is_to_top && bottom_scroll_zoom - ZOOM_LIMIT_MARGINE > last_scroll_y) {
                bottom_zoomed = false
                info.animate({ fontSize: '100%' }, "slow")
                //footer.animate({ height: '1.5em' }, "slow")
                dbg('footer smaller')
            }
        }
    }
}

function create_scroll_handler_for_header() {
    const ZOOM_LIMIT_MARGINE = 10
    const TOP_SCROLL_ZOOM_LIMIT = 70
    let last_scroll_y = window.scrollY
    
    let brand = $(".qp-nav .qp-brand")
    let nav = $(".qp-nav")
    let gamburger = $(".qp-nav .icon-bar")
    let head_big = TOP_SCROLL_ZOOM_LIMIT > last_scroll_y
    
    if (head_big) {
        nav.css('border-bottom-color', 'white')
        brand.css('font-size', '140%')
        gamburger.css('zoom', '130%')
    } else {
        nav.css('border-bottom-color', 'gray')
        brand.css('font-size', '100%')
        gamburger.css('zoom', '100%')
    }
    
    return {
        update: function() {
            if (TOP_SCROLL_ZOOM_LIMIT + ZOOM_LIMIT_MARGINE < window.scrollY && head_big) {
                nav.css('border-bottom-color', 'gray')
                brand.animate({ fontSize: '100%' }, "slow")
                gamburger.animate({ zoom: '100%' }, "slow")
                head_big = false
                //dbg('head smaller')
            } else if (TOP_SCROLL_ZOOM_LIMIT - ZOOM_LIMIT_MARGINE > window.scrollY && !head_big){
                nav.css('border-bottom-color', 'white')
                brand.animate({ fontSize: '140%' }, "slow")
                gamburger.animate({ zoom: '130%' }, "slow")
                head_big = true
                //dbg('head bigger')
            }
        }
    }
}

function create_scroll_handler_for_to_top() {
    const ZOOM_LIMIT_MARGINE = 50
    const TO_TOP_ZOOM_LIMIT = 400
    let last_scroll_y = window.scrollY
    
    if (TO_TOP_ZOOM_LIMIT > last_scroll_y) {
        $('.qp-to-top').css('display', 'none')
    } else {
        $('.qp-to-top').css('display', 'block')
    }
    
    return {
        update: function() {
            let is_to_top = last_scroll_y >= window.scrollY
            last_scroll_y = window.scrollY
            
            if (is_to_top && TO_TOP_ZOOM_LIMIT + ZOOM_LIMIT_MARGINE > last_scroll_y) {
                $('.qp-to-top').css('display', 'none')
            }
            else
            if (!is_to_top && TO_TOP_ZOOM_LIMIT - ZOOM_LIMIT_MARGINE < last_scroll_y) {
                $('.qp-to-top').css('display', 'block')
            }
        }
    }
}

function create_scroll_handlers_manager() {
    let scroll_handlers = []
    return {
        add: function(scroll_handler) {
            scroll_handlers.push(scroll_handler)
            //scroll_handler.update()
        },
        run: function() {
            handlers_count = scroll_handlers.length
            $(window).scroll(function(e) {
                for(let i = 0; i < handlers_count; i++) {
                    scroll_handlers[i].update()
                }
            })
        }
    }
}


function init_scroll_handlers() {
    scroll_handlers_manager = create_scroll_handlers_manager()
    scroll_handlers_manager.add(create_scroll_handler_for_to_top())
    //scroll_handlers_manager.add(create_scroll_handler_for_header())
    scroll_handlers_manager.add(create_scroll_handler_for_footer())
    scroll_handlers_manager.run()
}

