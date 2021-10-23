function dbg(msg){
	console.log(msg)
}

function page_map_init(){
	var uluru = {lat: 37.978970, lng: -1.122921};
	var page_map = new google.maps.Map(document.getElementById('page-map'), {
		zoom: 15,
		center: uluru,
		mapTypeId: 'satellite',
	});
	var marker = new google.maps.Marker({
		position: uluru,
		map: page_map,
	});
}

function ui_init(){
	$("#floorArea").spinner({
		step: 0.1,
		numberFormat: "n"
    })
	$('.my-chkbox').checkboxradio()
	$('#doCalc').click(function(){
		dbg('calc')
		var area = $('#floorArea').val()
		var opt1 = $('#checkbox-1').is(':checked')
		var opt2 = $('#checkbox-2').is(':checked')
		$('#output').val('calculated for: ' + area + ' Sq.m' + (opt1?' + opt1':'') + (opt2?' + opt2':''))
	})
}
	  
$(function(){
	dbg('start init')
	ui_init()
	dbg('initialized ok')
})
