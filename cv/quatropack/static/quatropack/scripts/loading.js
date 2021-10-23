/*jshint esversion: 6 */

$(function () {
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
        let loading = $('.qp-loading')
        loading.animate({ opacity: 0 }, 'slow', function () {
            loading.remove()
            body.css('overflow', 'auto')
        })
    })
})