# -*- coding: utf-8 -*-

# Definicion de tables encapsuladas


def pl_tbl_actividades():
	db.define_table('pl_actividades',
		Field('codigo'),
		Field('nombre'),
		Field('estado', 'boolean', default=True, represent = lambda id, r: plGetEstadoGeneral(r,1)),
		Field('descripcion'),
		Field('representacion', represent = lambda id, r: getRepresentacion(r)),
		format = '%(nombre)s'
		)
	# db.pl_actividades.estado.writable = False	
	pass

def pl_tbl_ciudades():
	db.define_table('pl_ciudades',
		Field('codigo'),
		Field('nombre'),
		Field('estado', 'boolean', default=True, represent = lambda id, r: plGetEstadoGeneral(r,2)),
		format = '%(nombre)s'
		)
	pass


def pl_tbl_lista():
	db.define_table('pl_lista',
		Field('codigo'),
		Field('nombre'),
		Field('estado', 'boolean', default=True, represent = lambda id, r: plGetEstadoGeneral(r,3)),
		format = '%(nombre)s'
		)
	pass

def pl_tbl_clientes():
	db.define_table('pl_clientes',
		Field('nit'),
		Field('nombre'),
		Field('direccion'),
		Field('contacto'),
		Field('telefono'),
		Field('email'),
		Field('estado', 'boolean', default=True, represent = lambda id, r: plGetEstadoGeneral(r,4)),
		format = '%(nombre)s'
		)
	pass

def pl_tbl_categorias():
	db.define_table('pl_categorias',
		Field('codigo'),
		Field('estado', default=True),
		Field('categoria'),
		auth.signature,
		format = '%(categoria)s'
		)
	pass

def pl_tbl_proveedores():
	db.define_table('pl_proveedores',
		Field('tipo_identificacion','list:string',widget=SQLFORM.widgets.radio.widget),
		Field('identificacion'),
		Field('nombre'),
		Field('estado', 'boolean', default=True, represent = lambda id, r: plGetEstadoGeneral(r,5)),
		Field('direccion'),
		Field('email'),
		Field('telefono'),
		Field('contacto'),
		Field('telefono_contacto'),
		Field('email_contacto'),
		format = '%(nombre)s'
		)
	db.pl_proveedores.tipo_identificacion.requires = [
		IS_IN_SET(('Nit','Cedula')),
		IS_NOT_EMPTY(error_message='Debe seleccionar un tipo identificación'),
	]
	pass

def pl_tbl_productos_terminados():
	# if not hasattr(db,'pl_categorias'):
	# 	pl_tbl_categorias()
	# if not hasattr(db,'pl_proveedores'):
	# 	pl_tbl_proveedores()
	db.define_table('pl_productos_terminados',
		# Field('categoria', 'reference pl_categorias'),
		# Field('proveedor', 'reference pl_proveedores'),
		Field('codigo'),
		Field('producto'),
		Field('estado', 'boolean', default=True, represent = lambda id, r: plGetEstadoGeneral(r,6)),
		# Field('minimo'),
		format = '%(producto)s'
		)
	pass


def pl_tbl_asignacion_precios():
	if not hasattr(db,'pl_lista'):
		pl_tbl_lista()
	if not hasattr(db,'pl_productos_terminados'):
		pl_tbl_productos_terminados()
	db.define_table('pl_asignacion_precios',
		Field('producto', 'reference pl_productos_terminados'),
		Field('lista', 'reference pl_lista'),
		Field('precio'),
		)
	pass


def pl_tbl_bodegas():
	db.define_table('pl_bodegas',
		Field('codigo'),
		Field('bodega'),
		format = '%(bodega)s'
		)
	pass

def pl_tbl_productos_inventario():
	if not hasattr(db,'pl_productos_terminados'):
		pl_tbl_productos_terminados()
	if not hasattr(db,'pl_proveedores'):
		pl_tbl_proveedores()
	if not hasattr(db,'pl_bodegas'):
		pl_tbl_bodegas()
	db.define_table('pl_productos_inventario',
		Field('bodega', 'reference pl_bodegas'),
		Field('producto', 'reference pl_productos_terminados'),
		Field('cantidad','integer'),
		Field('valor_compra','double'),
		Field('valor_venta','double'),
		auth.signature,
		)
	pass

def pl_tbl_movimientos():
	if not hasattr(db,'pl_productos_inventario'):
		pl_tbl_productos_inventario()
	db.define_table('pl_movimientos',
		Field('producto_inventario','reference pl_productos_inventario'),
		Field('cantidad'),
		Field('tipo_movimiento'),
		Field('observacion'),
		auth.signature,
		)
	pass


def lpAllTables():
	pl_tbl_actividades()
	pl_tbl_ciudades()
	pl_tbl_lista()
	pl_tbl_clientes()
	pl_tbl_proveedores()
	pl_tbl_productos_inventario()
	pass