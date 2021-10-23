$(function() {
    dbg('start')
    let last_scroll_y = window.scrollY
    $(window).scroll(function(e) {
        //dbg('scroll');
        //dbg(e);
        let is_to_top = last_scroll_y < window.scrollY
        last_scroll_y = window.scrollY
        dbg('scroll', window.scrollY, is_to_top)
    });
})
