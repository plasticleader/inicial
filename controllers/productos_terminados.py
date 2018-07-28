# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitatio
# -------------------------------------------------------------------------

@auth.requires_login()
def index():
	response.title = T("Productos Terminados")
	pl_product = db.pl_productos_terminados
	pl_product.id.redable =  pl_product.id.writetable  = False				
	links =  []
	pl_productos_terminados = SQLFORM.grid(pl_product,links=links,searchable=False,details=False,csv=False)
	return locals()