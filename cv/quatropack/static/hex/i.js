const CELLS_NUM = 40
const ROWS_NUM = 7
let ANIMATION_SPEED = 250
let XR_SPEED = 70
let YR_SPEED = 50

function init_cells() {
    var $grid = $('#grid')
    var $row = $grid.find('.grid-row')
    var cell_html = $row.first().html()
    var row_html = $row.empty()[0].outerHTML
    
    $grid.empty()
    
    dbg(CELLS_NUM, cell_html, row_html)
    
    
    for (let r = 0; r < ROWS_NUM; r++) {
        $row = $(row_html)
        
        for (let c = 0; c < CELLS_NUM; c++) {
            let $cell = $(cell_html)
            let $back = $cell.find('.grid-back')
            let ofs = Math.floor(r/2)
            $back.css('background-position-x', `${c*5.5+r*2.7-ofs*5.5}%`)
            $back.css('background-position-y', `${r*23}%`)
            $row.append($cell)
        }
        
        $grid.append($row)
    }
}

function start_hex_animation(t, next_back) {
    var src_width = t.width()
    /*
    dbg(t.css("background-image"))
    dbg(t.find('.back').css('background-image'))
    dbg(t.find('img').attr('src'))
    dbg(src_width)
    var im_num = Math.floor(100*Math.random())%EXAMPLE_IMAGES.length
    dbg(im_num)
    var im_path = EXAMPLE_IMAGES[im_num]
    dbg(im_path)
    */
    t.animate({ width: 0, marginLeft: src_width/2+'px' },
        function() {
            t.css("background-image", "url('"+next_back+"')")
            t.animate({ width: src_width+'px', marginLeft: 0 }, ANIMATION_SPEED)
        })
}

$(function() {
    dbg('start')
    
    init_cells()
    $('#start').click(function() {
        dbg('click start')
        var BACK_IMAGES = [
            'back.png',
            'back2.png',
            'back3.png',
            'back4.png',
        ]
        var im_num = Math.floor(100*Math.random())%BACK_IMAGES.length
        
        var rows = $('.grid-row')
        //dbg(`click first ${cells.length}`)
        for (var r = 0, rows_number = rows.length; r < rows_number; r++)  {
            setTimeout(function(_r) {
                return function() {
                    //dbg(`_r:${_r}`)
                    var cells = $(rows[_r]).find('.hexagon>.grid-back')
                    
                    for (var c = 0, cells_number = cells.length; c < cells_number; c++)  {
                        setTimeout(function(_c) {
                            return function() {
                                //dbg(`_c:${_c}`)
                                start_hex_animation($(cells[_c]), BACK_IMAGES[im_num])
                            }
                        }(c), c*XR_SPEED)
                    }
                }
            }(r), r*YR_SPEED)
        }
    })
})
