var login = {
	ready:function() {
		$('#m_login_signin_submit').click(function(event) {
			var email = $('#emailIngreso').val();
			var pass = $('#passwordIngreso').val();
			if (email=='') {
				swal("Campo Vacio","Debe ingresar un usuario","info")
					.then((value) => {
					   $('#emailIngreso').focus();
				});
				return false;
			}else if (pass=='') {
				swal("Campo Vacio","Debe ingresar un password","info")
					.then((value) => {
					   $('#passwordIngreso').focus();
				});
				return false;
			}else{
				$.post('../ingresoUsuario', {email:email,contrasena:pass}, function(data, textStatus, xhr) {
					if (data=='usuario') {
					swal("Usuario Invalido","Verifique el usuario ingresado","error")
						.then((value) => {
						   $('#emailIngreso').focus();
					});
					return false;
					}else if (data=='invalido') {
						swal("Información Invalida","Usuario/Password errados","error")
							.then((value) => {
							   $('#emailIngreso').focus();
						});
						return false;
					}else{
						swal("Bienvenido(a)","A Plasticos Linea Lider\n Click en ok para continuar.","success")
							.then((value) => {
							window.location.href = '../index';   
						});
					}
				});
				return false;
			}
		});	
	},
};
login.ready();
