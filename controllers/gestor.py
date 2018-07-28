# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------


@auth.requires_login()
def cargos():
	response.title = T("Cargos")
	pl_car = db.cargos
	pl_cargos = SQLFORM.grid(pl_car,searchable=False,details=False,csv=False)
	return locals()




@auth.requires_login()
def usuarios():
	
	def perfil():
		dato = db().select(db.auth_user.id).last()
		tipo = db(dato==db.auth_user.id).select(db.auth_user.tipo).last()
		us = dato.id
		tipo_tip = tipo.tipo
		if tipo_tip == ['All_Users']:
			perfil = 1
		elif tipo_tip == ['Comercial']:
			perfil = 5
		elif tipo_tip == ['Logistica']:
			perfil = 5
		elif tipo_tip == ['Supervisor']:
			perfil = 4
		else:
			perfil = 3
		pass
		db(db.auth_membership.user_id==us).delete()
		lpint = db.auth_membership.insert(user_id=us,group_id=perfil)
		print lpint
		pass	
	response.title = T("Usuarios")
	pl_users = db.auth_user
	if len(request.args) > 0:
		if (request.args[0] == 'new'):
			pl_usuarios = SQLFORM.grid(pl_users,searchable=False,details=False,csv=False,oncreate = lambda f: perfil())
		elif (request.args[0] == 'edit'):
			pl_usuarios = SQLFORM.grid(pl_users,searchable=False,details=False,csv=False,onupdate = lambda f: perfil())
		else:
			print request.args[0]
			pl_usuarios = ''
			pass
	else:
		# print request.args[0]
		pl_usuarios = SQLFORM.grid(pl_users,searchable=False,details=False,csv=False)
	return locals()


@auth.requires_login()
def actividades():
	response.title = T("Actividades Diarias")
	pl_acti = db.pl_actividades
	pl_acti.id.writable = pl_acti.id.readable = False
	lp_actividades = SQLFORM.grid(pl_acti,searchable=False,details=False,csv=False)
	return locals()

@auth.requires_login()
def ciudades():
	response.title = T("Ciudades")
	pl_ciud = db.pl_ciudades
	pl_ciud.id.writable =  pl_ciud.id.readable  = False
	pl_ciudades = SQLFORM.grid(pl_ciud,searchable=False,details=False,csv=False)
	return locals()

@auth.requires_login()
def precios():
	response.title = T("Lista Precios")
	# pl_tbl_lista()
	pl_list = db.pl_lista
	pl_list.id.redable =  pl_list.id.writetable  = False				
	links =  []
	pl_listaprecios = SQLFORM.grid(pl_list,links=links,searchable=False,details=False,csv=False)
	return locals()

@auth.requires_login()
def proveedores():
	response.title = T("Proveedores")
	# pl_tbl_proveedores()
	pl_prove = db.pl_proveedores
	pl_prove.id.redable =  pl_prove.id.writetable  = False				
	links =  []
	pl_proveedores = SQLFORM.grid(pl_prove,links=links,searchable=False,details=False,csv=False)
	return locals()

@auth.requires_login()
def asignacion():
	response.title = T("Asignación De Precios")
	return locals()

@auth.requires_login()
def imagen():
	pl_val = request.vars
	pl_table = db.pl_actividades
	db(pl_table.id==int(pl_val.id)).update(representacion=pl_val.img)
	lp_resul = 'ok'
	return lp_resul