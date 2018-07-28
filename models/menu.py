# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

# response.menu = [
#     (T('Home'), False, URL('default', 'index'), [])
# ]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        # (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('Gestor'), False, '#', [
            (T('Usuarios'), False, URL('gestor', 'usuarios')),
            (T('Actividades'), False,URL('gestor', 'actividades')),
            (T('Ciudades'), False,URL('gestor', 'ciudades')),
            (T('Listas'), False,URL('gestor', 'precios')),
            (T('Asiganación Precios'), False,URL('gestor', 'asignacion')),
            (T('Clientes'), False,URL('clientes', 'index')),
            (T('Proveedores'), False,URL('gestor', 'proveedores')),
            (T('Proveedores'), False,URL('materiasPrimas', 'index')),
            (T('Productos'), False,URL('productos_terminados', 'index')),
        ]),
        ('Pedidos', False, '#', [
            (T('Download'), False,
             'http://www.web2py.com/examples/default/download'),
            (T('Support'), False,
             'http://www.web2py.com/examples/default/support'),
            (T('Demo'), False, 'http://web2py.com/demo_admin'),
            (T('Quick Examples'), False,
             'http://web2py.com/examples/default/examples'),
            (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
            (T('Videos'), False,
             'http://www.web2py.com/examples/default/videos/'),
            (T('Free Applications'),
             False, 'http://web2py.com/appliances'),
            (T('Plugins'), False, 'http://web2py.com/plugins'),
            (T('Recipes'), False, 'http://web2pyslices.com/'),
        ]),
        (T('Inventario'), False, '#', [
            (T('Online book'), False, 'http://www.web2py.com/book'),
            (T('Preface'), False,
             'http://www.web2py.com/book/default/chapter/00'),
            (T('Introduction'), False,
             'http://www.web2py.com/book/default/chapter/01'),
            (T('Python'), False,
             'http://www.web2py.com/book/default/chapter/02'),
            (T('Overview'), False,
             'http://www.web2py.com/book/default/chapter/03'),
            (T('The Core'), False,
             'http://www.web2py.com/book/default/chapter/04'),
            (T('The Views'), False,
             'http://www.web2py.com/book/default/chapter/05'),
            (T('Database'), False,
             'http://www.web2py.com/book/default/chapter/06'),
            (T('Forms and Validators'), False,
             'http://www.web2py.com/book/default/chapter/07'),
            (T('Email and SMS'), False,
             'http://www.web2py.com/book/default/chapter/08'),
            (T('Access Control'), False,
             'http://www.web2py.com/book/default/chapter/09'),
            (T('Services'), False,
             'http://www.web2py.com/book/default/chapter/10'),
            (T('Ajax Recipes'), False,
             'http://www.web2py.com/book/default/chapter/11'),
            (T('Components and Plugins'), False,
             'http://www.web2py.com/book/default/chapter/12'),
            (T('Deployment Recipes'), False,
             'http://www.web2py.com/book/default/chapter/13'),
            (T('Other Recipes'), False,
             'http://www.web2py.com/book/default/chapter/14'),
            (T('Helping web2py'), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T("Buy web2py's book"), False,
             'http://stores.lulu.com/web2py'),
        ]),
        (T('Reportes'), False, None, [
            (T('Groups'), False,
             'http://www.web2py.com/examples/default/usergroups'),
            (T('Twitter'), False, 'http://twitter.com/web2py'),
            (T('Live Chat'), False,
             'http://webchat.freenode.net/?channels=web2py'),
        ]),
    ]

def is_session():
    return True if auth.is_logged_in() else False

if is_session():
    idUser = auth.user.id
    nameUser = "%s %s" %(auth.user.first_name,auth.user.last_name)
    emailUser = auth.user.email
    cargoUser = auth.user.cargo
    


lpAllTables()


def getTables(lp_r):
    if ( (lp_r=='0') | (lp_r==0)):
        table = db.auth_user
    elif ( (lp_r==1) | (lp_r=='1') ):
        table = db.pl_actividades
    elif ( (lp_r==2) | (lp_r=='2') ):
        table = db.pl_ciudades
    elif ( (lp_r==3) | (lp_r=='3') ):
        table = db.pl_lista
    elif ( (lp_r==4) | (lp_r=='4') ):
        table = db.pl_clientes
    elif ( (lp_r==5) | (lp_r=='5') ):
        table = db.pl_proveedores
    else:
        table = db.pl_productos_terminados
        pass
    return table