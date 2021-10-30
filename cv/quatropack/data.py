from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils.translation import gettext as _
from . import models

EXAMPLES = [
    {
        'image': '/static/quatropack/images/examples/1.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/10.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/11.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/12.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/13.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/14.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/15.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/16.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/17.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/18.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/19.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/2.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/20.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/21.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/22.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/23.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/24.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/3.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/4.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/5.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/6.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/7.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/8.png',
        'name': 'example',
    },
    {
        'image': '/static/quatropack/images/examples/9.png',
        'name': 'example',
    },
]

EXAMPLES_1 = [
    {
        'image': '/static/quatropack/images/examples/1_200.png',
        'name': 'automotive',
    },
    {
        'image': '/static/quatropack/images/examples/2_200.png',
        'name': 'beverage',
    },
    {
        'image': '/static/quatropack/images/examples/3_200.png',
        'name': 'chemical',
    },
    {
        'image': '/static/quatropack/images/examples/4_200.png',
        'name': 'cosmetics',
    },
    {
        'image': '/static/quatropack/images/examples/5_200.png',
        'name': 'dairy',
    },
    {
        'image': '/static/quatropack/images/examples/6_200.png',
        'name': 'food',
    },
    {
        'image': '/static/quatropack/images/examples/7_200.png',
        'name': 'household',
    },
    {
        'image': '/static/quatropack/images/examples/8_200.png',
        'name': 'pharmaceutical',
    },
    {
        'image': '/static/quatropack/images/examples/9_200.png',
        'name': 'pharmaceutical',
    },
    {
        'image': '/static/quatropack/images/examples/10_200.png',
        'name': 'pharmaceutical',
    },
]

BENEFITS = [
    {
        'name': _('secure transport'),
        'image': "https://www.enerconind.co.uk/wp-content/uploads/2017/01/SECURE_TRANSPORT_Tick-1.png",
    },
    {
        'name': _('extended shelf life'),
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/05/EXTENDED_SHELF_LIFE_Tick.png',
    },
    {
        'name': _('higher production speeds'),
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/02/HIGHER_PRODUCTION_SPEEDS_Tick-1.png',
    },
    {
        'name': _('tamper evidence'),
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/01/TAMPER_EVIDENCE_1A.png',
    },
    {
        'name': _('stronger seals'),
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/05/Stronger_seals_Tick.png',
    },
]

LOGOTYPES = [
    {
        'image': '/static/quatropack/images/logotypes/1.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/10.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/11.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/12.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/13.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/14.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/15.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/16.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/17.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/18.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/19.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/2.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/20.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/21.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/22.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/23.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/24.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/25.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/26.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/27.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/28.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/29.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/3.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/30.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/31.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/32.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/33.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/34.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/35.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/36.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/37.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/38.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/39.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/4.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/40.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/41.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/42.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/43.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/44.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/45.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/46.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/47.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/48.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/49.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/5.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/50.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/51.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/52.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/53.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/54.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/55.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/56.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/57.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/58.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/59.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/6.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/60.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/61.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/62.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/63.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/64.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/65.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/66.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/7.png',
        'name': 'logo',
    },
    {
        'image': '/static/quatropack/images/logotypes/8.png',
        'name': 'logo',
    },
]

LOGOTYPES_1 = [
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/01/Arla_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/03/Shaws_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/02/Orchard_Valley_Foods_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/05/Mendez_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/05/Chemfix_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/01/Beanies_logo-1-1.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/05/Zipz_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/01/GSK_logo-1.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/02/Wyepak_logo_241x88.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/01/Millers_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/02/Opet_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/06/Clarks_logo.png',
        'name': 'logo',
    },
    {
        'image': 'https://www.enerconind.co.uk/wp-content/uploads/2017/06/Floratine_logo.png',
        'name': 'logo',
    },
]

DEVICES = [
    {
        "description":"Movilidad y ligereza.\r\nEficacia y fiabilidad.\r\nPensada para pequeñas producciones o laboratorio. Permite sellar con fiabilidad en cualquier sitio.",
        "image":"http://quatropack.com/Quatropack/supersealjunior_files/SupersealJr.png",
        "name":"Super Seal Junior",
        "slug": "super-seal-junior",
    }, 
    {
        "description":"Rendimiento y fiabilidad adaptado a su\r\n\r\nproducción.\r\n\r\n\r\n\r\nProducción elevada y sellado perfecto en cada envase casi sin mantenimiento.",
        "image":"http://quatropack.com/Quatropack/superseal100_files/shapeimage_3.png",
        "name":"Super Seal",
        "slug": "super-seal",
        "subtypes": [ {
                "name": "50",
            }, {
                "name": "75",
            }, {
                "name": "100",
            },
        ]
    }, 
    {
        "description":"Potencia bajo total control.\r\nTodos los datos bajo control para las altas producciones. La mayor potencia en el menor espacio posible. Y un sellado perfecto.",
        "image":"http://quatropack.com/Quatropack/supersealdeluxe_files/shapeimage_3.png",
        "name":"Super Seal Touch",
        "slug": "super-seal-touch",
    }, 
    {
        "description":"La más rápida del mercado.\r\nLas producciones más elevadas garantizando un sellado perfecto de todos los envases gracias a su exclusivo sistema de bobina doble.",
        "image":"http://quatropack.com/Quatropack/supersealmax_files/shapeimage_9.png",
        "name":"Super Seal Max Touch",
        "slug": "super-seal-max-touch",
    },
]

DEVICES_BY_SLUG = {
    "super-seal-junior": DEVICES[0],
    "super-seal": DEVICES[1],
    "super-seal-touch": DEVICES[2],
    "super-seal-max-touch": DEVICES[3],
}

REVIEWS = [
    {
        'person': 'Mark Leverington, Supply Chain Manager at Clarks',
        'phrase': "We chose Enercon’s induction sealing equipment for its reputation within the industry for reliability… We have not had any issues with any of Enercon’s induction sealers since installation – not a single breakdown in over eight years. I wish other machinery would run this well.",
        'images': [
            "https://www.enerconind.co.uk/wp-content/uploads/2017/01/Clarks_syrups.png",
            "https://www.enerconind.co.uk/wp-content/uploads/2017/06/Clarks_logo.png",
            #"https://www.enerconind.co.uk/wp-content/uploads/2017/01/TAMPER_EVIDENCE_1A.png", #404
        ],
    },
    {
        'person': 'Darryl King, Director of Operations for Floratine',
        'phrase': "You can’t put a price tag on dependability. Customer complaints are nearly eliminated and 99% of our problems were solved with the induction sealer – it was a godsend.",
        'images': [
            "https://www.enerconind.co.uk/wp-content/uploads/2017/01/Floratine_product.png",
            "https://www.enerconind.co.uk/wp-content/uploads/2017/06/Floratine_logo.png",
        ],
    },
    {
        'person': 'Paul Banks, Purchasing and Supply Director at Chemfix',
        'phrase': "I would recommend Enercon Industries to other manufacturers, both for product performance and the benefits gained from the use of its sealing equipment.",
        'images': [
            'https://www.enerconind.co.uk/wp-content/uploads/2017/01/Chemfix_product.png',
            'https://www.enerconind.co.uk/wp-content/uploads/2017/05/Chemfix_logo.png',
        ],
    },
    {
        'person': 'Peter Lauritzen, CEO of Arla Foods UK',
        'phrase': "The size and scale of our new dairy reinforces Arla’s leadership within the UK dairy industry and we have drawn a line in the sand when it comes to next generation fresh milk processing.",
        'images': [
            "https://www.enerconind.co.uk/wp-content/uploads/2017/01/Arla_product.png",
            "https://www.enerconind.co.uk/wp-content/uploads/2017/01/Arla_logo.png",
            #"https://www.enerconind.co.uk/wp-content/uploads/2017/05/TAMPER_EVIDENCE.png",
        ],
    },
]
