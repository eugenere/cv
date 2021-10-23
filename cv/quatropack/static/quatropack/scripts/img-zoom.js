/*jshint esversion: 6 */

function handle_img_zoom() {
    $(".qp-img-wrapper").click(function() {
        let new_image = $(this).find('img').attr('src')
        dbg(new_image)
        $('#qp-zoomer .modal-body').css('background-image', "url('"+new_image+"')")
        $('#qp-zoomer').modal()
    })
}

$(function () {
    handle_img_zoom()
})