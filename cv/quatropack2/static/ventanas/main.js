let num_of_ventanas = {
    current: 1,
    added: 1,
}

let first_ventana = $($('.v-ventana')[0]).clone()

function update_sliders() {
    $('#v-slider-h-'+num_of_ventanas.added).slider({
        range: "min",
        value: 120,
        min: 50,
        max: 300,
        slide: function(event, ui) {
            //$(".v-height").val( "$" + ui.value );
            //dbg(ui)
            //dbg(event)
            $(this).closest('.v-ventana').find('.v-image').width(ui.value+'px')
        }
    })
    $('#v-slider-v-'+num_of_ventanas.added).slider({
        orientation: "vertical",
        range: "min",
        value: 200,
        min: 50,
        max: 500,
        slide: function( event, ui ) {
            //$(".v-height").val( "$" + ui.value );
            $(this).closest('.v-ventana').find('.v-image').height(ui.value+'px')
        }
    })
}

$(function() {
    $('body').on("click", '.v-rem', function() {
        let ov = $(this).closest('.v-ventana')
        dbg('rem: '+ov.find('.v-num').text())
        ov.remove()
        num_of_ventanas.current --
    })
    
    $('.v-add').click(function() {
        num_of_ventanas.current ++
        num_of_ventanas.added ++
        let nv = first_ventana.clone()
        nv.find('#v-slider-v-1').attr('id', 'v-slider-v-'+num_of_ventanas.added)
        nv.find('#v-slider-h-1').attr('id', 'v-slider-h-'+num_of_ventanas.added)
        nv.find('.v-num').text(num_of_ventanas.current+"/"+num_of_ventanas.added)
        $('.v-result').append(nv).ready(function() {
            update_sliders()
        })
    })
    update_sliders()
})