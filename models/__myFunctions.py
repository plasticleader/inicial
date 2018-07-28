# -*- coding: utf-8 -*-

# Funciones ayudantes

hoy = request.now
mes =  hoy.month
dia =  hoy.day
ano = hoy.year
anoMil = str(hoy)[:2]
anoCentecimas = str(hoy)[2:4]
horaActual = str(hoy)[11:13]
minActual = str(hoy)[14:16]



def getImagen(r):
	lu_user = db.auth_user[r].foto
	if lu_user:
		imagen = URL('default','download/%s' %(lu_user))
	else:
		imagen = URL('static','images/inicio.jpeg')
	return imagen


def getActivacion(r):
	activo = r.registration_key
	if (activo==None) | (activo==''):
		activa = XML("""
			<div  id="divUsers_%s">
				<a href="#"  title="Bloquear Usuario" onclick="lp_users.actualizar('B','%s')" class="btn btn-outline-success m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--outline-2x m-btn--pill m-btn--air">
					<i class="flaticon-user-ok"></i>
				</a>
			</div>""" %(r.id,r.id))
	else:
		activa = XML("""
			<div  id="divUsers_%s">
				<a href="#"  title="Activar Usuario" onclick="lp_users.actualizar('A','%s')" class="btn btn-outline-danger m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--outline-2x m-btn--pill m-btn--air">
					<i class="flaticon-lock-1"></i>
				</a>
			</div>""" %(r.id,r.id))
	return activa



def getRepresentacion(r):
	if r.representacion:
		representacion = 	XML("""
			<a href="#" onclick="lp_activ.asignar('%s')" title="Cambiar Icono" data-toggle="modal" data-target="#m_modal_actividades" cla_ss="btn btn-outline-info m-btn m-btn--custom m-btn--icon m-btn--pill m-btn--air"> 
				<img src="%s" width="40">
			</a>
		""" %(r.id,URL('static','images/Iconos/%s' %r.representacion)) ),
	else:
		representacion = XML("""
			<a href="#" onclick="lp_activ.asignar('%s')" title="Agregar Icono" data-toggle="modal" data-target="#m_modal_actividades" class="btn btn-outline-info m-btn m-btn--custom m-btn--icon m-btn--pill m-btn--air">
				<span>
					<i class="flaticon-placeholder"></i>
					<span>Icono</span>
				</span>
			</a>
		"""%(r.id) )
		pass
	return representacion





def plGetEstadoGeneral(pl_r,pl_table):
	estado = pl_r.estado
	id_ = pl_r.id
	if ( (estado==True) | (estado=='True') ):
		activa = XML("""
			<div  id="divEstados_%s">
				<a href="#"  title="Desactivar" onclick="lp_global.modEstado('B','%s','%s','%s')" class="btn btn-outline-success m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--outline-2x m-btn--pill m-btn--air">
					<i class="flaticon-like"></i>
				</a>
			</div>""" %(id_,estado,id_,pl_table))
	else:
		activa = XML("""
			<div  id="divEstados_%s">
				<a href="#"  title="Activar" onclick="lp_global.modEstado('A','%s','%s','%s')" class="btn btn-outline-danger m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--outline-2x m-btn--pill m-btn--air">
					<i class="flaticon-lock-1"></i>
				</a>
			</div>""" %(id_,estado,id_,pl_table))
	return activa


