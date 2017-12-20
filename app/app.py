# -*- coding: utf-8 -*-


from flask import abort, Response, Flask, render_template, redirect, url_for
from os import path, getenv


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('dados'))


@app.route('/dados')
def dados():
    campi = {
        'presencial': [
            { 'caption': u'CÂMPUS ÁGUAS LINDAS',         'href': u'/planilhas/presencial/CÂMPUS ÁGUAS LINDAS.csv'         },
            { 'caption': u'CÂMPUS ANÁPOLIS',             'href': u'/planilhas/presencial/CÂMPUS ANÁPOLIS.csv'             },
            { 'caption': u'CÂMPUS APARECIDA DE GOIÂNIA', 'href': u'/planilhas/presencial/CÂMPUS APARECIDA DE GOIÂNIA.csv' },
            { 'caption': u'CÂMPUS CIDADE DE GOIÁS',      'href': u'/planilhas/presencial/CÂMPUS CIDADE DE GOIÁS.csv'      },
            { 'caption': u'CÂMPUS FORMOSA',              'href': u'/planilhas/presencial/CÂMPUS FORMOSA.csv'              },
            { 'caption': u'CÂMPUS GOIÂNIA',              'href': u'/planilhas/presencial/CÂMPUS GOIÂNIA.csv'              },
            { 'caption': u'CÂMPUS GOIÂNIA OESTE',        'href': u'/planilhas/presencial/CÂMPUS GOIÂNIA OESTE.csv'        },
            { 'caption': u'CÂMPUS INHUMAS',              'href': u'/planilhas/presencial/CÂMPUS INHUMAS.csv'              },
            { 'caption': u'CÂMPUS ITUMBIARA',            'href': u'/planilhas/presencial/CÂMPUS ITUMBIARA.csv'            },
            { 'caption': u'CÂMPUS JATAÍ',                'href': u'/planilhas/presencial/CÂMPUS JATAÍ.csv'                },
            { 'caption': u'CÂMPUS LUZIÂNIA',             'href': u'/planilhas/presencial/CÂMPUS LUZIÂNIA.csv'             },
            { 'caption': u'CÂMPUS SENADOR CANEDO',       'href': u'/planilhas/presencial/CÂMPUS SENADOR CANEDO.csv'       },
            { 'caption': u'CÂMPUS URUAÇU',               'href': u'/planilhas/presencial/CÂMPUS URUAÇU.csv'               },
            { 'caption': u'CÂMPUS VALPARAÍSO',           'href': u'/planilhas/presencial/CÂMPUS VALPARAÍSO.csv'           }
        ],
        'ead': [
            { 'caption': u'CÂMPUS ÁGUAS LINDAS',         'href': u'/planilhas/ead/CÂMPUS ÁGUAS LINDAS.csv'         },
            { 'caption': u'CÂMPUS ANÁPOLIS',             'href': u'/planilhas/ead/CÂMPUS ANÁPOLIS.csv'             },
            { 'caption': u'CÂMPUS APARECIDA DE GOIÂNIA', 'href': u'/planilhas/ead/CÂMPUS APARECIDA DE GOIÂNIA.csv' },
            { 'caption': u'CÂMPUS CIDADE DE GOIÁS',      'href': u'/planilhas/ead/CÂMPUS CIDADE DE GOIÁS.csv'      },
            { 'caption': u'CÂMPUS FORMOSA',              'href': u'/planilhas/ead/CÂMPUS FORMOSA.csv'              },
            { 'caption': u'CÂMPUS GOIÂNIA',              'href': u'/planilhas/ead/CÂMPUS GOIÂNIA.csv'              },
            { 'caption': u'CÂMPUS GOIÂNIA OESTE',        'href': u'/planilhas/ead/CÂMPUS GOIÂNIA OESTE.csv'        },
            { 'caption': u'CÂMPUS INHUMAS',              'href': u'/planilhas/ead/CÂMPUS INHUMAS.csv'              },
            { 'caption': u'CÂMPUS ITUMBIARA',            'href': u'/planilhas/ead/CÂMPUS ITUMBIARA.csv'            },
            { 'caption': u'CÂMPUS JATAÍ',                'href': u'/planilhas/ead/CÂMPUS JATAÍ.csv'                },
            { 'caption': u'CÂMPUS LUZIÂNIA',             'href': u'/planilhas/ead/CÂMPUS LUZIÂNIA.csv'             },
            { 'caption': u'CÂMPUS SENADOR CANEDO',       'href': u'/planilhas/ead/CÂMPUS SENADOR CANEDO.csv'       },
            { 'caption': u'CÂMPUS URUAÇU',               'href': u'/planilhas/ead/CÂMPUS URUAÇU.csv'               },
            { 'caption': u'CÂMPUS VALPARAÍSO',           'href': u'/planilhas/ead/CÂMPUS VALPARAÍSO.csv'           }
        ],
        'fic': [
            { 'caption': u'CÂMPUS ÁGUAS LINDAS',         'href': u'/planilhas/fic/CÂMPUS ÁGUAS LINDAS.csv'         },
            { 'caption': u'CÂMPUS ANÁPOLIS',             'href': u'/planilhas/fic/CÂMPUS ANÁPOLIS.csv'             },
            { 'caption': u'CÂMPUS APARECIDA DE GOIÂNIA', 'href': u'/planilhas/fic/CÂMPUS APARECIDA DE GOIÂNIA.csv' },
            { 'caption': u'CÂMPUS CIDADE DE GOIÁS',      'href': u'/planilhas/fic/CÂMPUS CIDADE DE GOIÁS.csv'      },
            { 'caption': u'CÂMPUS FORMOSA',              'href': u'/planilhas/fic/CÂMPUS FORMOSA.csv'              },
            { 'caption': u'CÂMPUS GOIÂNIA',              'href': u'/planilhas/fic/CÂMPUS GOIÂNIA.csv'              },
            { 'caption': u'CÂMPUS GOIÂNIA OESTE',        'href': u'/planilhas/fic/CÂMPUS GOIÂNIA OESTE.csv'        },
            { 'caption': u'CÂMPUS INHUMAS',              'href': u'/planilhas/fic/CÂMPUS INHUMAS.csv'              },
            { 'caption': u'CÂMPUS ITUMBIARA',            'href': u'/planilhas/fic/CÂMPUS ITUMBIARA.csv'            },
            { 'caption': u'CÂMPUS JATAÍ',                'href': u'/planilhas/fic/CÂMPUS JATAÍ.csv'                },
            { 'caption': u'CÂMPUS LUZIÂNIA',             'href': u'/planilhas/fic/CÂMPUS LUZIÂNIA.csv'             },
            { 'caption': u'CÂMPUS SENADOR CANEDO',       'href': u'/planilhas/fic/CÂMPUS SENADOR CANEDO.csv'       },
            { 'caption': u'CÂMPUS URUAÇU',               'href': u'/planilhas/fic/CÂMPUS URUAÇU.csv'               },
            { 'caption': u'CÂMPUS VALPARAÍSO',           'href': u'/planilhas/fic/CÂMPUS VALPARAÍSO.csv'           }
        ]
    }
    return render_template('dados.html', campi=campi)


@app.route('/planilhas/<tipo>/<planilha>.csv')
def download_csv(tipo, planilha):
    def read_csv(planilha):
        # verifica o tipo
        if tipo != 'presencial' and tipo != 'ead' and tipo != 'fic':
            abort(404)
        filename = u'%s/planilhas/%s/%s.csv' % (getenv('APP_ROOT', default='..'), tipo, planilha)
        # verifica se existe a planilha
        if not path.exists(filename):
            abort(404)
        # retorna o generator para cada linha
        with open(filename, 'rb') as filecsv:
            for line in filecsv:
                yield line
    return Response(read_csv(planilha=planilha), mimetype='text/csv')
