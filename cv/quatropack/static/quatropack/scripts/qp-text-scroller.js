/*jshint esversion: 6 */

function init_text_scroller(step_timeout, step) {
    let text_scroller = $('.qp-text-scroller')
    let text = text_scroller.text()
    //text_scroller.empty().html('<div>'+text+' '+text+'</div>')
    text_scroller.html('<div>'+text+' '+text+' '+'</div>')
    let current_shift = 0

    text_scroller.ready(function() {
        let inner = $('.qp-text-scroller>div')
        let width = inner[0].scrollWidth/2
        dbg(`${step}/${width}/`)

        function move() {
            //text_scroller.css
            /**/
            /**/
    
            if (Math.abs(current_shift) > width) {
                current_shift = Math.abs(current_shift) - width
                //dbg('reset shift')
                dbg(`${current_shift}/${step}/${width}/`+
                    inner.css('margin-left')+'/'+
                    text_scroller.innerWidth()+'/'+
                    text_scroller.outerWidth()+'/'+
                    text_scroller[0].scrollWidth+'/'+
                    text_scroller.width())
            } else {
                current_shift += step
            }

            inner.css('margin-left', current_shift+'px')
            start_after(step_timeout, move)
        }
        
        move()
    })
}

$(function() {
    init_text_scroller(50, -1)
})
