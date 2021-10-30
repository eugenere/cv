$(function () {
    if (!$('.qp-loading').length) {
        return
    }

    $('.qp-loading>.qp-text').animate({ opacity: 1 }, 'slow')
    
    let body = $('body')
    body.css('overflow', 'hidden') 
    
    var size = 100
    var step = .2
    var current = -Math.PI/2

    var canvas = document.createElement('canvas')
    var context = canvas.getContext('2d')

    var image = document.createElement('img')
    
    image.onload = function() {
        var interval_id = setInterval(function (){
            if (current > Math.PI*3/2) {
                dbg("last")
                clearInterval(interval_id)
                
                start_after(1000, function() {
                    let loading = $('.qp-loading')
                    loading.animate({ opacity: 0 }, 'slow', function () {
                        loading.remove()
                        body.css('overflow', 'auto')
                    })
                })
            }
            context.save()
            
            context.beginPath();
            context.moveTo(size,size);
            context.arc(size, size, size*.5, -Math.PI/2, current)
            context.lineTo(size,size);
            context.clip();
            context.drawImage(image, size/2, size/2, size, size);
            
            context.restore()

            current+=step
            dbg(current)
        }, 100)
    }
    
    dbg('.')
    image.src = STATIC_URL+'quatropack2/images/loading.jpg'
    $('.qp-indicator').append(canvas)
})