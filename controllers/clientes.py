# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitatio
# -------------------------------------------------------------------------

@auth.requires_login()
def index():
	response.title = T("Lista Clientes")
	pl_listClientes = db.pl_clientes
	pl_listClientes.id.redable =  pl_listClientes.id.writetable  = False				
	links =  []
	pl_listaClientes = SQLFORM.grid(pl_listClientes,links=links,searchable=False,details=False,csv=False)
	return locals()