const BG = document.querySelector("body")

function enable(e) {
    let $e = $(e)
    if ($e.hasClass('c_disabled'))
        $e.removeClass('c_disabled')
}

function disable(e) {
    let $e = $(e)
    if (!$e.hasClass('c_disabled')) {
        /*gsap.to($e, { 
            duration: 10,
            className: 'c_contc_disabled',
        })*/
        $e.addClass('c_disabled')
    }
}

function is_disabled(e) {
    return $(e).hasClass('c_disabled')
}

function hacer_RENOVADOR() {
    const $b = $("body")
    const tl = gsap
    
    let indice = -1
    let animando = false
    
    let $i = $("#image")
    let $t = $("#titulo")
    let $d = $("#detalles")
    
    let $proximo_d, $proximo_t, $proximo_i
    
    function empezar() {
        //dbg(`indice = ${indice}`)
        animando = true
        
        const data_actual = DATA[indice%DATA.length]
        const image = data_actual['image']
        
        $proximo_d = $d.clone().html(data_actual['detalles'])
        $proximo_t = $t.clone().html(data_actual['titulo'])
        $proximo_i = $i.clone().css('background-image', 
            `url('${STATIC_URL}ahorra_energia/images/${image}')`)

        $b.css("overflow-x", "hidden")
        $('.j_ctrl_b').addClass('c_disabled')
    }
    
    function terminar() {
        animando = false
        $b.css("overflow-x", "auto")
        
        if (0 === get_indice()) {
            $('.j_ctrl_s').removeClass('c_disabled')
        } else {
            $('.j_ctrl_b').removeClass('c_disabled')
        }
    }
    
    function get_indice() {
        return indice%DATA.length
    }
    
    return {
        set_indice: (i=-1) => {
            indice = i
            //proximo()
        },
        anterior: ()=> {
            if (animando) return
            indice = ((0 === indice) ? DATA.length : indice)-1
            
            empezar()
            
            const al_x = parseInt(window.innerWidth/2)
            
            gsap.set($proximo_d[0], { x: al_x, scale: 0, })
            gsap.set($proximo_t[0], { x: -al_x, scale: 2, opacity: 0})
            gsap.set($proximo_i[0], { left: "100em", })

            tl.to($d[0], {
                duration: 2, 
                x: -2*al_x,
                scale: 0,
            })

            tl.to($t[0], {
                duration: 1,
                x: 2*al_x,
                scale: 2,
                opacity: 0,
            })
          
            tl.to($i[0], {
                duration: 1.5,
                left: "100em", 
            })

            $b.append($proximo_d)
            $b.append($proximo_t)
            $b.append($proximo_i)

            tl.to($proximo_d[0], {
                duration: 1.5, 
                x: 0,
                scale: 1,
                opacity: 1,
                onComplete: ()=> {
                    $d.remove()
                    $d = $proximo_d
                },
            })

            tl.to($proximo_t[0], {
                duration: 2, 
                x: 0,
                scale: 1,
                opacity: 1,
                onComplete: ()=> {
                    $t.remove()
                    $t = $proximo_t
                    
                    terminar()
                }
            })
            
            tl.to($proximo_i[0], {
                duration: 1,
                left: "2em",
                onComplete: ()=> {
                    $i.remove()
                    $i = $proximo_i
                },
            })
        },
        proximo: ()=> {
            if (animando) return
            indice++
            
            empezar()
            
            const al_x = parseInt(window.innerWidth/2)
            
            gsap.set($proximo_d[0], { x: -al_x, scale: 0, })
            gsap.set($proximo_t[0], { x: al_x, scale: 2, opacity: 0})
            gsap.set($proximo_i[0], { left: "100em", })
            
            tl.to($i[0], {
                duration: 1.5,
                left: "100em", 
            })

            tl.to($d[0], {
                duration: 2, 
                x: al_x,
                scale: 0,
            })

            tl.to($t[0], {
                duration: 1,
                x: -2*al_x,
                scale: 0,
            })

            $b.append($proximo_d)
            $b.append($proximo_t)
            $b.append($proximo_i)
            
            tl.to($proximo_i[0], {
                duration: 1,
                left: "2em",
                onComplete: ()=> {
                    $i.remove()
                    $i = $proximo_i
                },
            })

            tl.to($proximo_d[0], {
                duration: 1.5, 
                x: 0,
                scale: 1,
                opacity: 1,
                onComplete: ()=> {
                    $d.remove()
                    $d = $proximo_d
                },
            })

            tl.to($proximo_t[0], {
                duration: 2, 
                x: 0,
                scale: 1,
                opacity: 1,
                onComplete: ()=> {
                    $t.remove()
                    $t = $proximo_t
                    
                    terminar()
                }
            })
        },
    }
}

function init_form() {
    $(".c_form").addClass('c_js_form')
    let file
    
    function close() {
        //submit
        //$('#entregar').click()
        
        dbg($(".c_form *:invalid").length)
        
        if (0 === $(".c_form *:invalid").length) {
            $("#form_cerrador").click()
        }
    }
    
    qsO(".c_archivo_contesto").addEventListener('click', function(event) {
        qsO("#factura").click()
    })
    
    qsO("#factura").addEventListener('change', function(event)
    {
        //dbg(event)
        if (0 < event.target.files.length) {
            file_name = event.target.files[0].name
            dbg('cargar image: '+event.target.files[0].name)
        } else {
            dbg('no files')
            return
        }
        close()
    })
    
    qsO("#factura").addEventListener('click', close)
}

function cargando() {
    const AE_COOKIE = "ae"
    const TIENE_COOKIE = get_cookie(AE_COOKIE)
    const $vista_descargando = $("#vista_descargando")
    const $boton_cookie = $("button", $vista_descargando)
    BG.style.overflow = 'hidden'
    
    function esconder() {
        gsap.to($boton_cookie, {
            opacity: 0
        })
        
        start_after(500, ()=> { 
            gsap.to($vista_descargando, {
                duration: .5,
                top: "90%",
                //bottom: "1%",
                padding: "4%",
                onComplete: ()=> {
                    $vista_descargando.remove()
                    BG.style.overflow = 'auto'
                },
            })
        })
    }
    
    if (TIENE_COOKIE) {
        esconder()
        return
    }
    
    $boton_cookie.click(()=> {
        set_cookie(AE_COOKIE, true)
        esconder()
    }).show()
}

$(()=> {
    dbg("start")
    dbg(STATIC_URL)
    
    const RENOVADOR = hacer_RENOVADOR()
    const FRECUENCIA = 5000
    let lanzador = start_every(FRECUENCIA, RENOVADOR.proximo)
    
    cargando()
    init_form()
    
    let $pausar = $('#pausar>i.fa')
    let pausar = ()=> {
        lanzador.finish()
        $pausar.removeClass('fa-pause').addClass('fa-play')
    }
    
    //pausar()
    
    $("#cargar_factura").click((e)=> {
        if (is_disabled(e.currentTarget)) {
            return
        }
        
        pausar()
        
        let $cargando_factura = $("#cargando_factura")
        
        disable(e.currentTarget)
        $cargando_factura.show()
        
        function close() {
            dbg('close')
            
            gsap.to($cargando_factura, {
                duration: .5,
                top: "50%",
                bottom: "10%",
                opacity: 0,
                onComplete: ()=> {
                    $cargando_factura.hide()
                    enable(e.currentTarget)
                    BG.style.overflow = 'auto'
                },
            })
        }
        
        BG.style.overflow = 'hidden'
        gsap.to($cargando_factura, {
            duration: .5,
            top: 0,
            opacity: 1,
            bottom: 0,
            onComplete: ()=> {
                dbg("forma ha visto")
                
                $(document).keydown(function(e) {
                    if (e.key === "Escape") {
                        dbg('esc')
                        close()
                    }
                })
                
                $("#form_cerrador").click(()=> {
                    close()
                })
            },
        })
    })
    //.click()
    /*
    $('#volver_al_inicio').click((e)=> {
        if (is_disabled(e.currentTarget)) {
            dbg('d')
            enable(e.currentTarget)
        } else {
            dbg('e')
            disable(e.currentTarget)
        }
    })
    */
    $('#pausar').click((e)=> {
        dbg(e.target.innerHTML)
        if (is_disabled(e.currentTarget)) {
            return
        }
        
        if ($pausar.hasClass('fa-pause')) {
        //if ("||" === e.target.innerHTML) {
            dbg('parar')
            pausar()
            return
        }
        
        dbg('continuar')
        lanzador = start_every(5000, RENOVADOR.proximo)
        $pausar.removeClass('fa-play').addClass('fa-pause')
    })
    
    $('#llamar_proximo').click((e)=> {
        dbg(">")
        if (is_disabled(e.currentTarget)) {
            return
        }
        pausar()
        RENOVADOR.proximo()
    })
    
    $('#volver_al_inicio').click((e)=> {
        dbg("i")
        if (is_disabled(e.currentTarget)) {
            return
        }
        pausar()
        RENOVADOR.set_indice()
        RENOVADOR.proximo()
    })
    
    $('#llamar_anterior').click((e)=> {
        dbg("<")
        if (is_disabled(e.currentTarget)) {
            return
        }
        pausar()
        RENOVADOR.anterior()
    })
    
    window.addEventListener("mousemove", (event) => {
        BG.style.backgroundPositionX = -parseInt(event.clientX/100) + "px"
        BG.style.backgroundPositionY = -parseInt(event.clientY/100) + "px"
    })

    /*
    window.addEventListener("touchstart", ()=> {
        RENOVADOR.haz()
    } , false)

    window.addEventListener("click", ()=> {
        dbg(".")
        RENOVADOR.haz()
    })
    */
})


