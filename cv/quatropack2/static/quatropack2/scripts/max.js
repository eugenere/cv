/*jshint esversion: 6 */

function handle_parallax() {
    /*
    $('.qp-img-wrapper>img').on("scroll", function(event) {
        dbg('1')
        dbg(this)
        dbg(event)
    })
    
    $('.qp-img-wrapper').scroll(function(event) {
        dbg('2')
        dbg(this)
        dbg(event)
    })
    */
        /*
        dbg('3')
        dbg(img)
        dbg(img.offset().top)
        dbg(img.position().top)
        dbg(img.scrollTop())
        dbg(event)
        dbg('---')
        dbg(window.scrollY)
        */
    //window.addEventListener('scroll', function(event) {
    /*
	$(window).scroll(function(event) {
        let img = $($('.qp-img-wrapper')[5])
        
        //dbg('-------')
        $.each($('.qp-img-wrapper'), function(n, el) {
            let $el = $(el)
            //$el.height()*2/3 
            let diff = el.getBoundingClientRect().top + 1.5*$el.height() - window.innerHeight/2
            let offs = Math.round(diff/5)+'px'
            //dbg(`${n}:${diff}/${offs}`)
            $el.css('margin-top', offs)
        })
    })
    */
}

$(function () {
    dbg('start')
    handle_parallax()
    $("#video-intro")[0].currentTime = 35
})