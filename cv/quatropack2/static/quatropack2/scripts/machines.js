/*jshint esversion: 6 */

function is_element_showing(element, fully_in_view) {
    var pageTop = $(window).scrollTop();
    var pageBottom = pageTop + $(window).height();
    var elementTop = $(element).offset().top;
    var elementBottom = elementTop + $(element).height();

    if (fully_in_view === true) {
        return ((pageTop < elementTop) && (pageBottom > elementBottom));
    } else {
        return ((elementTop <= pageBottom) && (elementBottom >= pageTop));
    }
}

function handle_speeds() {
    let speed_bars = $('.qp-speed-bar>.progress-bar')
    let states = []

    for(var i = 0; i < speed_bars.length; i++) {
        states.push(false)
    }

    function update_speed_bars() {
        for (let i = 0; i < speed_bars.length; i ++) {
            let sb = $(speed_bars[i])
            let new_state = is_element_showing(sb)

            if (!new_state || states[i]) {
                if (!states[i]) {
                    sb.width(0)
                }

                states[i] = new_state
                continue
            }

            states[i] = new_state
            /*
            dbg(bar.parent().attr('id')+","+i+": "+width)
            */
            sb.animate({
                'width': sb.attr('aria-valuenow')+'%'
            }, 'slow', function() {
                dbg(sb.parent().attr('id')+","+i+": "+sb.width())
            })
            /**/
        }
    }

    $(window).scroll(update_speed_bars)
    update_speed_bars()
}

$(function () {
    handle_speeds()
    $('[data-toggle="tooltip"]').tooltip()
})