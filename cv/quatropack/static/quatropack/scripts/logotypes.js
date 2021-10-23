/*jshint esversion: 6 */

function handle_logotypes2_2() {
    let cells_all = $(".qp-carousel-logotypes2 tr>td")
    let cells_top = $(".qp-carousel-logotypes2 tr:first-child>td")
    let cells_bottom = $(".qp-carousel-logotypes2 tr:last-child>td")
    let pos = 0
    
    function update() {
        function update_cell(e, image_url) {
            let cell = $(e)
            
            cell.animate({ opacity: 0 }, 'slow', function () {
                cell.css('background-image', "url('"+image_url+"')")
                cell.animate({ opacity: 1 }, 'slow')
            })
        }
        for (let i = 0; i < 5; i ++) {
            start_after(i*200, function () {
                update_cell(cells_top[i], logotypes_top[pos+4-i])
                start_after(100, function () {
                    update_cell(cells_bottom[i], logotypes_bottom[pos+4-i])
                })
            })
        }
        pos = (5+pos)%40
        
        start_after(12000, update)
    }
    update()
}

function handle_logotypes2() {
    let cells_all = $(".qp-carousel-logotypes2 tr>td")
    let cells_top = $(".qp-carousel-logotypes2 tr:first-child>td")
    let cells_bottom = $(".qp-carousel-logotypes2 tr:last-child>td")
    let pos = 0
    let finisher
    
    function update() {
        function update_cell(e, image_url) {
            let cell = $(e)
            
            cell.animate({ opacity: 0 }, 'slow', function () {
                cell.css('background-image', "url('"+image_url+"')")
                cell.animate({ opacity: 1 }, 'slow')
            })
        }
        for (let i = 0; i < 5; i ++) {
            update_cell(cells_top[i], logotypes_top[pos+4-i])
            update_cell(cells_bottom[i], logotypes_bottom[pos+4-i])
        }
        pos = (5+pos)%40
        
        if (finisher) finisher.finish()
        finisher = start_after(12000, update)
    }
    update()
}

$(function () {
    handle_logotypes2_2()
})