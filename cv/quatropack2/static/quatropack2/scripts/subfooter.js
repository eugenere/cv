$(function() {
    //var text = $('#qp-info-field').text() + ', jq ready'
    //$('#qp-info-field').text(text)
    var messages = [
        "Es muy sencillo instalar en su línea una selladora por inducción",
        "Solo un metro libre en su línea actual y podría sellar todos sus envases",
        "En menos de un mes podría estar sellando sus envases",
        "Con una inversión muy pequeña podría sellar sus productos",
        "Con una sola máquina podría sellar todos sus productos",
        "Prevenir fugas y alargar la caducidad es sencillo",
        "Mejorar la imagen de mi marca no es complicado"
    ]
    $('#subtitle-text').text(messages[Math.floor(Math.random()*messages.length)])
})

