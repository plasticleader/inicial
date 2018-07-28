# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------





# @request.restful()
# def ingresar():

#     def GET(*args, **vars):
#         return dict()

#     def POST(*args, **vars):
#         return dict()

#     def PUT(*args, **vars):
#         return dict()

#     def DELETE(*args, **vars):
#         return dict()

#     return locals()



@request.restful()
def ingresar():
	def GET(*args, **vars):
		plre = request.vars
		print plre
		return dict(plre=plre)
	return locals()