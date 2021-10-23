let empezar = () => {
    dbg("start animacion")
    let $actual = $(".c_contesto")
    let $proximo = $actual.clone()
    let $padre = $actual.parent()
    let $body = $('body')
    
    let $cap_actual = $(".c_caption")
    let $cap_proximo = $actual.clone()
    
    $body.css("overflow-x", "hidden")
    
    let height = $padre.height()
    
    $actual.addClass("j_contesto_anterior")
    $proximo.addClass("j_contesto_proximo")
    
    
    gsap.to(".j_contesto_anterior", {
        duration: 1, 
        x: window.innerWidth/2,
        scale: 0,
    })
    gsap.to(".c_caption", {
        duration: 1, 
        x: window.innerWidth/2,
        scale: 0,
    })

    $padre.append($proximo)
    //gsap.set(".j_contesto_proximo", { y: -480 })
    //$padre.height(height)
    
    let pasos = 0
    
    gsap.to(".j_contesto_proximo", {
        duration: 1, 
        x: 0,
        scale: 1,
        startAt: {
            x: -window.innerWidth/2,
            scale: 0,
        },
        onComplete: ()=> {
            $(".j_contesto_anterior").remove()
            $(".c_contesto").removeClass("j_contesto_proximo")
            gsap.set(".c_contesto", { y: 0 })
            
            $body.css("overflow-x", "auto")
            dbg(pasos)
        },
        onUpdate: () => {
            pasos++
        },
    })
}


$(function()
{
    dbg("start")
    
    $('.j_enviar').hide()
    dbg(qsO("#factura"))
    if (!qsO("#factura")) {
        dbg("factura not found")
    } else {
        qsO("#factura").addEventListener('change', function(event)
        {
            //dbg(event)
            dbg('cargar image: '+event.target.files[0].name)
            $('.j_enviar').click()
        })
    }
    
    $('.c_galeria').click(empezar)
    
    if (false)
        start_after(1500, function ()
        {
            gsap.to("#logo", 
            {
                duration: 1, 
                x: 100,
                //opacity: 1,
                scale: 1.2,
                /*
                startAt: 
                {
                    //x: 0, 
                    opacity: 0,
                    scale: 0,
                },
                */
                function ()
                {
                    dbg("onComplete")
                }
            })
            dbg("test.1")
        })

    const galeria = qsO('.c_galeria')
    galeria.style.backgroundImage = 'url(/static/nueva_vista/images/1.jpg)';
    
    const bg = document.querySelector("body")

    window.addEventListener("mousemove", (event) => {
        //dbg(event)
        bg.style.backgroundPositionX = -parseInt(event.clientX/100) + "px"
        bg.style.backgroundPositionY = -parseInt(event.clientY/100) + "px"
        //bg.style.backgroundPositionX = -event.clientX/10 + "px"
        //bg.style.backgroundPositionY = -event.clientY/10 + "px"
    });
})


