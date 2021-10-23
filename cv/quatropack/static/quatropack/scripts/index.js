/*jshint esversion: 6 */

function handle_scrolling() {
    const BORDER = 376
    let header = $('.qp-header')

    if (BORDER > window.scrollY) {
        header.addClass('qp-header-dark')
    }

    $(window).scroll(function (e) {
        if (BORDER < window.scrollY) {
            if (header.hasClass('qp-header-dark')) {
                header.removeClass('qp-header-dark')
            }
        } else {
            if (!header.hasClass('qp-header-dark')) {
                header.addClass('qp-header-dark')
            }
        }
    })
}

function handle_products_peeled() {
    let qImage = $(".qp-products-peeled>.qp-image")
    let images_names = ['5.png', '1.png', '3.png']
    qImage.css('background-image', 
        "url('"+STATIC_URL+'quatropack/images/products-peeled/'+
                images_names[Math.floor(Math.random()*images_names.length)]+"')")
    
    /*
    let current_image = -1
    let finisher
    const SPEED = 1500
    
    function next() {
        current_image = (current_image + 1) % images_number
        
        products_peeled.animate({ opacity: 0 }, 'slow', function () {
            products_peeled.css('background-image', "url('"+peeling_shots_images[current_image]+"')")
            products_peeled.animate({ opacity: 1 }, 'slow', function () {
                if (finisher) finisher.finish()
                finisher = start_after(SPEED, next)
            })
        })
    }

    next()
    */
}

$(function () {
    handle_products_peeled()
    handle_scrolling()
})