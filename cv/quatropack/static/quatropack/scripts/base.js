/*jshint esversion: 6 */

function handle_menu_toggler() {
    let menu_togglers = $('.qp-menu-button>.navbar-toggler')
    
    menu_togglers.click(function() {
        dbg('toggle main menu')
        
        let menu = $('.qp-main-menu')
        
        if (menu_togglers.hasClass('collapsed')) {
            menu_togglers.removeClass('collapsed')
            
            menu.css('display', 'block')
            menu.animate({ opacity: 1 }, 'slow')
        } else {
            menu.animate({ opacity: 0 }, 'slow', function() {
                menu.css('display', 'none')
            })
            menu_togglers.addClass('collapsed')
        }
    })
}

$(function () {
    handle_menu_toggler()
})