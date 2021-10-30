from django.utils.translation import gettext_lazy as _


MACHINE_NAMES = [
    {
        "name":"Super Seal Max",
        "slug":"super_seal_max",
    },
    {
        "name":"Super Seal Touch",
        "slug":"super_seal_touch",
    },
    {
        "name":"Super Seal 100",
        "slug":"super_seal_100",
    },
    {
        "name":"Super Seal 75",
        "slug":"super_seal_75",
    },
    {
        "name":"Super Seal 50",
        "slug":"super_seal_50",
    },
    {
        "name":"Super Seal Junior",
        "slug":"super_seal_junior",
    }, 
]

MACHINES = [
    {
        "name":"Super Seal Max",
        "slug":"super_seal_max",
        "image": "max.png",
        "short": _("La selladora por inducción más rápida del mercado."),
        "desc": _("Pensada para producciones muy altas. El resultado fiable que necesita especialmente adaptado a su proyecto."),
        "speed": 1200,
        "adapted_speed": 95,
    },
    { 
        "name":"Super Seal Touch",
        "slug":"super_seal_touch",
        "image": "touch.png",
        "short": _("La última tecnología de sellado para altas producciones."),
        "desc": _("Pensada para producciones altas y con las últimas tecnologías. Un equipo puntero para sellar y controlar la producción."),
        "speed": 300,
        "adapted_speed": 70,
    },
    {
        "name":"Super Seal 100",
        "slug":"super_seal_100",
        "image": "nn.png",
        "short": _("La automática robusta ajustada a una gran producción."),
        "desc": _("Pensada para producciones altas automáticas. Una inversión amortizada muy rápido y un sellado de garantía."),
        "speed": 100,
        "adapted_speed": 50,
    },
    { 
        "name":"Super Seal 75",
        "slug":"super_seal_75",
        "image": "nn.png",
        "short": _("La automática fiable adaptada a su linea de producción."),
        "desc": _("Pensada para producciones medias automáticas. Una inversión rentable y un resultado asegurado en cada envase."),
        "speed": 50,
        "adapted_speed": 30,
    },
    {
        "name":"Super Seal 50",
        "slug":"super_seal_50",
        "image": "nn.png",
        "short": _("La automática pequeña."),
        "desc": _("Pensada para automatizar pequeñas producciones. Permite arrancar un nuevo producto con una inversión controlada."),
        "speed": 25,
        "adapted_speed": 15,
    },
    {
        "name":"Super Seal Junior",
        "slug":"super_seal_junior",
        "image": "junior.png",
        "short": _("Móvil y ligera. Eficaz y fiable."),
        "desc": _("Pensada para pequeñas producciones o laboratorio. Permite sellar con fiabilidad en cualquier sitio."),
        "speed": 6,
        "adapted_speed": 10,
    },
]

MACHINES_BY_SLUG = {
    "super_seal_junior": dict({
        'details': {
            'images': [
                'junior/7.png',
                'junior/4.png',
                'junior/6.png',
                'junior/1.png',
            ],
        },
        'demensions': {
            'images': [
                'junior/2.png',
                'junior/5.png',
                'junior/4.png',
                'junior/3.png',
            ],
        },
    }, **MACHINES[5]),
    "super_seal_50": MACHINES[4],
    "super_seal_75": MACHINES[3],
    "super_seal_100": MACHINES[2],
    "super_seal_touch": MACHINES[1],
    "super_seal_max": MACHINES[0],
}

PEELING_SHOTS = [
    '0.png',
    '1.png',
    '2.png',
    '3.png',
    '4.png',
    '5.png',
]

PRODUCTS_REV = [
    "5.png",
    "4.png",
    "3.png",
    "2.png",
    "1.png",
    "10.png",
    "9.png",
    "8.png",
    "7.png",
    "6.png",
    "15.png",
    "14.png",
    "13.png",
    "12.png",
    "11.png",
    "20.png",
    "19.png",
    "18.png",
    "17.png",
    "16.png",
    "25.png",
    "24.png",
    "23.png",
    "22.png",
    "21.png",
    "30.png",
    "29.png",
    "28.png",
    "27.png",
    "26.png"
]

PRODUCTS = [
    # heinz
    "16.png",
    "17.png",
    "18.png",
    "19.png",
    "20.png",
    
    # repsol
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    
    # azucarera
    "21.png",
    "22.png",
    "23.png",
    "24.png",
    "25.png",
    
    # apache
    "6.png",
    "7.png",
    "8.png",
    "9.png",
    "10.png",
    
    # nutella
    "26.png",
    "27.png",
    "28.png",
    "29.png",
    "30.png",
    
    # adama
    "11.png",
    "12.png",
    "13.png",
    "14.png",
    "15.png",
]

LOGOTYPES = {
    "top": [
        {
            "name": "eni",
            "image": "5.eni.png"
        },
        {
            "name": "british_petroleum",
            "image": "4.british_petroleum.png"
        },
        {
            "name": "repsol",
            "image": "3.repsol.png"
        },
        {
            "name": "shell",
            "image": "2.shell.png"
        },
        {
            "name": "cepsa",
            "image": "1.cepsa.png"
        },
        {
            "name": "procter_and_gamble",
            "image": "15.procter_and_gamble.png"
        },
        {
            "name": "nabisco",
            "image": "14.nabisco.png"
        },
        {
            "name": "calve",
            "image": "13.calve.png"
        },
        {
            "name": "heinz",
            "image": "12.heinz.png"
        },
        {
            "name": "hellmans",
            "image": "11.hellmans.png"
        },
        {
            "name": "bayer",
            "image": "25.bayer.png"
        },
        {
            "name": "adama",
            "image": "24.adama.png"
        },
        {
            "name": "o_basf",
            "image": "23.o_basf.png"
        },
        {
            "name": "brandt",
            "image": "22.brandt.png"
        },
        {
            "name": "probelte",
            "image": "21.probelte.png"
        },
        {
            "name": "dia",
            "image": "35.dia.png"
        },
        {
            "name": "el_corte_ingles",
            "image": "34.el_corte_ingles.png"
        },
        {
            "name": "lidl",
            "image": "33.lidl.png"
        },
        {
            "name": "carrefour",
            "image": "32.carrefour.png"
        },
        {
            "name": "hacendado",
            "image": "31.hacendado.png"
        },
        {
            "name": "kraft",
            "image": "45.kraft.png"
        },
        {
            "name": "danone",
            "image": "44.danone.png"
        },
        {
            "name": "cadbury",
            "image": "43.cadbury.png"
        },
        {
            "name": "unilever",
            "image": "42.unilever.png"
        },
        {
            "name": "nestle",
            "image": "41.nestle.png"
        },
        {
            "name": "soria_natural",
            "image": "55.soria_natural.png"
        },
        {
            "name": "weider",
            "image": "54.weider.png"
        },
        {
            "name": "robis",
            "image": "53.robis.png"
        },
        {
            "name": "best_protein",
            "image": "52.best_protein.png"
        },
        {
            "name": "nutrytec",
            "image": "51.nutrytec.png"
        },
        {
            "name": "cataliment",
            "image": "65.cataliment.png"
        },
        {
            "name": "copusan",
            "image": "64.copusan.png"
        },
        {
            "name": "fragata",
            "image": "63.fragata.png"
        },
        {
            "name": "aceitunas_guadalquivir",
            "image": "62.aceitunas_guadalquivir.png"
        },
        {
            "name": "agro_sevilla",
            "image": "61.agro_sevilla.png"
        },
        {
            "name": "bayer",
            "image": "75.bayer.png"
        },
        {
            "name": "abbott",
            "image": "74.abbott.png"
        },
        {
            "name": "novatis",
            "image": "73.novatis.png"
        },
        {
            "name": "gsk",
            "image": "72.gsk.png"
        },
        {
            "name": "pfizer",
            "image": "71.pfizer.png"
        }
    ],
    "bottom": [
        {
            "name": "chemo",
            "image": "10.chemo.png"
        },
        {
            "name": "total",
            "image": "9.total.png"
        },
        {
            "name": "quimiberica",
            "image": "8.quimiberica.png"
        },
        {
            "name": "chevron",
            "image": "7.chevron.png"
        },
        {
            "name": "esso",
            "image": "6.esso.png"
        },
        {
            "name": "grupo_siro",
            "image": "20.siro.png"
        },
        {
            "name": "cidacos",
            "image": "19.cidacos.png"
        },
        {
            "name": "chovi",
            "image": "18.chovi.png"
        },
        {
            "name": "prima",
            "image": "17.prima.png"
        },
        {
            "name": "ybarra",
            "image": "16.ybarra.png"
        },
        {
            "name": "johnson_and_johnson",
            "image": "30.johnson_and_johnson.png"
        },
        {
            "name": "sara_lee",
            "image": "29.sara_lee.png"
        },
        {
            "name": "fujifilm",
            "image": "28.fujifilm.png"
        },
        {
            "name": "kodak",
            "image": "27.kodak.png"
        },
        {
            "name": "palc",
            "image": "26.palc.png"
        },
        {
            "name": "milka",
            "image": "40.milka.png"
        },
        {
            "name": "hero",
            "image": "39.hero.png"
        },
        {
            "name": "mondelez",
            "image": "38.mondelez.png"
        },
        {
            "name": "martin_braun",
            "image": "37.martin_braun.png"
        },
        {
            "name": "carte_dor",
            "image": "36.carte_dor.png"
        },
        {
            "name": "prosol",
            "image": "50.prosol.png"
        },
        {
            "name": "pepsi",
            "image": "49.pepsi.png"
        },
        {
            "name": "coca_cola",
            "image": "48.coca_cola.png"
        },
        {
            "name": "nutrexpa",
            "image": "47.nutrexpa.png"
        },
        {
            "name": "lanjaron",
            "image": "46.lanjaron.png"
        },
        {
            "name": "la_constancia",
            "image": "60.la_constancia.png"
        },
        {
            "name": "dani",
            "image": "59.dani.png"
        },
        {
            "name": "mccormick",
            "image": "58.mccormick.png"
        },
        {
            "name": "ducros",
            "image": "57.ducros.png"
        },
        {
            "name": "mari_paz",
            "image": "56.mari_paz.png"
        },
        {
            "name": "purina",
            "image": "70.purina.png"
        },
        {
            "name": "labiana",
            "image": "69.labiana.png"
        },
        {
            "name": "campbells",
            "image": "68.campbells.png"
        },
        {
            "name": "gatorade",
            "image": "67.gatorade.png"
        },
        {
            "name": "herbalife",
            "image": "66.herbalife.png"
        },
        {
            "name": "revlon",
            "image": "80.revlon.png"
        },
        {
            "name": "loreal",
            "image": "79.loreal.png"
        },
        {
            "name": "rnb",
            "image": "78.rnb.png"
        },
        {
            "name": "rubio",
            "image": "77.rubio.png"
        },
        {
            "name": "esteve",
            "image": "76.esteve.png"
        }
    ]
}

"""
LOGOTYPES_TOGETHER = [
    {
        "name": "cepsa",
        "image": "1.cepsa.png"
    },
    {
        "name": "shell",
        "image": "2.shell.png"
    },
    {
        "name": "repsol",
        "image": "3.repsol.png"
    },
    {
        "name": "british_petroleum",
        "image": "4.british_petroleum.png"
    },
    {
        "name": "eni",
        "image": "5.eni.png"
    },
    {
        "name": "esso",
        "image": "6.esso.png"
    },
    {
        "name": "chevron",
        "image": "7.chevron.png"
    },
    {
        "name": "quimiberica",
        "image": "8.quimiberica.png"
    },
    {
        "name": "total",
        "image": "9.total.png"
    },
    {
        "name": "chemo",
        "image": "10.chemo.png"
    },
    {
        "name": "hellmans",
        "image": "11.hellmans.png"
    },
    {
        "name": "heinz",
        "image": "12.heinz.png"
    },
    {
        "name": "calve",
        "image": "13.calve.png"
    },
    {
        "name": "nabisco",
        "image": "14.nabisco.png"
    },
    {
        "name": "pg",
        "image": "15.pg.png"
    },
    {
        "name": "ybarra",
        "image": "16.ybarra.png"
    },
    {
        "name": "prima",
        "image": "17.prima.png"
    },
    {
        "name": "chovi",
        "image": "18.chovi.png"
    },
    {
        "name": "cidacos",
        "image": "19.cidacos.png"
    },
    {
        "name": "grupo_siro",
        "image": "20.siro.png"
    },
    {
        "name": "probelte",
        "image": "21.probelte.png"
    },
    {
        "name": "brandt",
        "image": "22.brandt.png"
    },
    {
        "name": "o_basf",
        "image": "23.o_basf.png"
    },
    {
        "name": "adama",
        "image": "24.adama.png"
    },
    {
        "name": "bayer",
        "image": "25.bayer.png"
    },
    {
        "name": "palc",
        "image": "26.palc.png"
    },
    {
        "name": "kodak",
        "image": "27.kodak.png"
    },
    {
        "name": "fujifilm",
        "image": "28.fujifilm.png"
    },
    {
        "name": "sara_lee",
        "image": "29.sara_lee.png"
    },
    {
        "name": "johnson_and_johnson",
        "image": "30.johnson_and_johnson.png"
    },
    {
        "name": "hacendado",
        "image": "31.hacendado.png"
    },
    {
        "name": "carrefour",
        "image": "32.carrefour.png"
    },
    {
        "name": "lidl",
        "image": "33.lidl.png"
    },
    {
        "name": "el_corte_ingles",
        "image": "34.el_corte_ingles.png"
    },
    {
        "name": "dia",
        "image": "35.dia.png"
    },
    {
        "name": "carte_dor",
        "image": "36.carte_dor.png"
    },
    {
        "name": "braun",
        "image": "37.braun.png"
    },
    {
        "name": "mondelez",
        "image": "38.mondelez.png"
    },
    {
        "name": "hero",
        "image": "39.hero.png"
    },
    {
        "name": "milka",
        "image": "40.milka.png"
    },
    {
        "name": "nestle",
        "image": "41.nestle.png"
    },
    {
        "name": "unilever",
        "image": "42.unilever.png"
    },
    {
        "name": "cadbury",
        "image": "43.cadbury.png"
    },
    {
        "name": "danone",
        "image": "44.danone.png"
    },
    {
        "name": "kraft",
        "image": "45.kraft.png"
    },
    {
        "name": "lanjaron",
        "image": "46.lanjaron.png"
    },
    {
        "name": "nutrexpa",
        "image": "47.nutrexpa.png"
    },
    {
        "name": "coca_cola",
        "image": "48.coca_cola.png"
    },
    {
        "name": "pepsi",
        "image": "49.pepsi.png"
    },
    {
        "name": "prosol",
        "image": "50.prosol.png"
    },
    {
        "name": "nutrytec",
        "image": "51.nutrytec.png"
    },
    {
        "name": "best_protein",
        "image": "52.best_protein.png"
    },
    {
        "name": "robis",
        "image": "53.robis.png"
    },
    {
        "name": "weider",
        "image": "54.weider.png"
    },
    {
        "name": "soria_natural",
        "image": "55.soria_natural.png"
    },
    {
        "name": "mari_paz",
        "image": "56.mari_paz.png"
    },
    {
        "name": "ducros",
        "image": "57.ducros.png"
    },
    {
        "name": "mc_cormick",
        "image": "58.mc_cormick.png"
    },
    {
        "name": "dani",
        "image": "59.dani.png"
    },
    {
        "name": "la_constancia",
        "image": "60.la_constancia.png"
    },
    {
        "name": "agro_sevilla",
        "image": "61.agro_sevilla.png"
    },
    {
        "name": "aceitunas_guadalquivir",
        "image": "62.aceitunas_guadalquivir.png"
    },
    {
        "name": "fragata",
        "image": "63.fragata.png"
    },
    {
        "name": "copusan",
        "image": "64.copusan.png"
    },
    {
        "name": "gataliment",
        "image": "65.gataliment.png"
    },
    {
        "name": "herbalife",
        "image": "66.herbalife.png"
    },
    {
        "name": "gatorade",
        "image": "67.gatorade.png"
    },
    {
        "name": "campbells",
        "image": "68.campbells.png"
    },
    {
        "name": "labiana",
        "image": "69.labiana.png"
    },
    {
        "name": "purina",
        "image": "70.purina.png"
    },
    {
        "name": "pfizer",
        "image": "71.pfizer.png"
    },
    {
        "name": "gsk",
        "image": "72.gsk.png"
    },
    {
        "name": "novatis",
        "image": "73.novatis.png"
    },
    {
        "name": "abbott",
        "image": "74.abbott.png"
    },
    {
        "name": "bayer",
        "image": "75.bayer.png"
    },
    {
        "name": "esteve",
        "image": "76.esteve.png"
    },
    {
        "name": "rubio",
        "image": "77.rubio.png"
    },
    {
        "name": "rnb",
        "image": "78.rnb.png"
    },
    {
        "name": "loreal",
        "image": "79.loreal.png"
    },
    {
        "name": "revlon",
        "image": "80.revlon.png"
    },
]
"""

BENEFITS = [
    {
        "title": _("Prevenir fugas"),
        "image": "1.png",
        "text": _("El  sellado  por  inducción  garantiza  un  envase  estanco  que puede soportar una considerable presión. Esto asegura que su  producto  no  sufrirá  fugas  durante  su  almacenamiento, durante  el  transporte  o  antes  de  su  uso  por  el  consumidor. Muchos  de  nuestros  clientes  empezaron  a  termosellar  sus envases  por  inducción  para  prevenir  escapes  y  mermas, terminando  con  los  envases  mal  cerrados,     las  pegatinas adhesivas o el sellado con cola que no son estancos.  Casi  todos  los  supermercados  y  también  los  comercios online (incluido Amazon) exigen alguna forma de protección contra fugas, como un sellado por inducción."),
    },
    {
        "title": _("Alargar caducidad"),
        "image": "2.png",
        "text": _("Protegido   en   un   ambiente   hermético,   el   producto   se conserva  dentro  del  envase  en  unas  condiciones  óptimas durante   más   tiempo.   Problemas   como   la   oxidación acelerada,  la  degradación  del  producto  por  humedad,  o  la aparición   de   hongos   o   gérmenes   en   la   superficie   son comunes en envases no estancos.  En  algunos  casos,  nuestros  clientes  han  logrado  extender  la vida útil de sus productos hasta 12 semanas.")
    },
    {
        "title": _("Mantener frescura"),
        "image": "3.png",
        "text": _("Todas  las  propiedades  del  producto  se  mantienen  durante más tiempo. En un ambiente donde nada entra y nada sale, se  guardan  cuidadosamente  los  aromas  intensos  y  perdura el color en toda su viveza. Un envase perfectamente cerrado por inducción preserva las texturas únicas y el sabor especial que distinguen un producto de los demás.")
    },
    {
        "title": _("Evidenciar manipulación"),
        "image": "4.png",
        "text": _("El  sellado  por  inducción  proporciona  clara  evidencia  de manipulación  a  sus  clientes,  ya  que  el  disco  de  aluminio debe   ser   retirado   para   acceder   al   producto.   Esto   es especialmente importante para la seguridad y la tranquilidad de  los  consumidores,  que  necesitan  saber  con  certeza  que son los primeros en abrir ese envase. Un disco sellado intacto consigue clientes satisfechos.")
    },
    {
        "title": _("Reducir coste unitario"),
        "image": "5.png",
        "text": _("Ahorrar   dinero   es   otra   de   las   razones   por   las   que   los fabricantes  se  pasan  al  sellado  de  tapones  por  inducción. Cómo pueden ahorrar dinero es algo que puede conseguirse de muchas formas. 1.Ahorros en energía  2.Aumento de la velocidad de producción de la línea 3.Reducción de las devoluciones por fugas 4.Caducidades más largas y mejor gestión del stock 5.Reducción del mantenimiento 6.Reducción de los tiempos de paradas de linea 7.Reducción del peso del envase y del tapón")
    },
    {
        "title": _("Evitar falsificaciones"),
        "image": "6.png",
        "text": _("El   sellado   por   inducción   proporciona   a   sus   usuarios protección  contra  falsificaciones,  ya  que  un  sello  intacto puede  demostrar  a  los  clientes  que  el  producto  no  ha  sido modificado.   Nuevos   sellos   con   holograma   o   logotipo personalizado   hacen   que   copiar   su   producto   sea extremadamente   complicado.   La   protección   contra falsificaciones  es  popular  en  especial  para  productos  de  un elevado  valor,  o  para  productos  fácilmente  imitables.  Nuevo discos  termosellables  más  avanzados,  con  opciones  como láminas  de  aluminio  con  grabados,  tintas  que  cambian  de color,  microimpresiones,  códigos  impresos  o  electrónicos (RFID), colores personalizados y tintas con ADN añadido son lo último en  prevención contra falsificaciones.")
    },
    {
        "title": _("Respeta medio ambiente"),
        "image": "7.png",
        "text": _("Pasándose  al  sellado  por  inducción,  muchos  fabricantes pueden también reducir el grosor del aluminio y la cantidad de plástico usado en el tapón y la botella, convirtiéndolo en una  opción  de  envasado  más  respetuosa  con  el  medio ambiente  y  reducir  su  huella  de  carbono.  En  comparación con  otros  sistemas  de  sellado  utiliza  menos  energía,  lo  que hace del sellado por inducción una solución más respetuosa con el medio ambiente.")
    },
    {
        "title": _("Exportar más lejos"),
        "image": "8.png",
        "text": _("Un envase que protege mejor nos ha permitido llevar el producto más lejos y abrir nuevos mercados en óptimas condiciones. ¡Largas semanas en contenedores expuestos al sol, a la humedad o al frío se soportan mucho mejor dentro de un envase bien sellado!")
    },
    {
        "title": _("Aumentar facturación"),
        "image": "9.png",
        "text": _("Los  envases  si  están  sellados  atraen  a  más  clientes  y  aumenta  el volumen   de   negocio.   Ya   sean   nuevos   productos   a   clientes existentes  o  el  acceso  a  clientes  que  no  quieren  nada  sin  sellar, integrar  una  selladora  por  inducción  en  su  producción  puede permitirle vender más. ")
    },
    {
        "title": _("Imagen de marca"),
        "image": "10.png",
        "text": _("Ni manipulado, ni falsificado, ni abierto. La garantía que se ofrece al cliente  es  total  y  refuerza  la  imagen  de  nuestra  marca.  Un  sistema adoptado por la mayoría de grandes fabricantes a nivel mundial y todas las primeras marcas.")
    },
    {
        "title": _("Mantenimiento cero"),
        "image": "11.png",
        "text": _("Cero,  o  casi  cero.  La  más  reciente  gama  de  selladoras  por inducción  están  todas  refrigeradas  por  aire  y  no  necesitan prácticamente  ningún  mantenimiento  o  consumibles  para seguir funcionando de manera efectiva y eficiente. De hecho, algunos  de  nuestros  clientes  describen  sus  máquinas  con más  de  20  años  de  antigüedad  con  la  expresión  ‘como nueva’. Los  mínimos  costes  de  mantenimiento  y  la  reducción  de  los tiempos de parada de la línea de producción son dos de las razones   por   las   que   nuestra   gama   de   selladoras   por inducción  Enercon  es  la  elección  número  uno  en  todo  el mundo. Pocos repuestos y una larga vida útil la convierten en una inversión muy rentable.")
    },
    {
        "title": _("Mayor productividad"),
        "image": "12.png",
        "text": _("La  tecnología  de  sellado  por  inducción  recibe  frecuentes alabanzas  por  parte  de  los  jefes  de  fábrica  por  aumentar  la productividad en comparación con otros sistemas de sellado. Son  capaces  de  trabajar  a  alta  velocidad  y  eliminan  la necesidad  de  tocar  o  manipular  el  envase.  Pueden  ponerse en  marcha  y  comenzar  a  sellar  instantáneamente.  Es  muy sencillo  integrar  una  máquina  termoselladora  por  inducción en  una  línea  de  producción  ya  existente.  Simplemente  se necesita  un  metro  lineal  de  cinta  transportadora  libre.  Y como las máquinas ya vienen probadas y ajustadas, la puesta en marcha y formación se hace en apenas un par de horas.  Es  un  método  de  sellado  muy  flexible  ya  que  se  pueden sellar  muchos  diámetros  diferentes  con  la  misma  máquina, sin gastar un euro más. ¡Nadie sabe qué envases tendrá que sellar en el futuro!")
    },
]