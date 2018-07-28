# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# 16889068  or 016889068 
# fijo 9250478
def pl_modEstado():
	lp_val = request.vars
	if ((lp_val.estado=='True') | (lp_val.estado==True)):
		val_lp = False
	else:
		val_lp = True
		pass
	lp_table = getTables(int(lp_val.table))
	print lp_table
	db(lp_table.id==int(lp_val.id)).update(estado=val_lp)
	lp_retorno = plGetEstadoGeneral(lp_table[lp_val.id],lp_val.table)
	return lp_retorno