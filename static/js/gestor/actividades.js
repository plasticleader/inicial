var lp_activ = {
	ready:function () {},
	imagen:function(lp_r,lp_imagen) {
		swal({
		  title: "Confirmación... ",   
		  text: "Seguro(a) desea  asignar la imagen "+lp_r+" a está actividad. ?",
		  icon: "info",
		  buttons: true,
		  dangerMode: true,
		})
		.then((willDelete) => {
		  	if (willDelete) {
			   	$.post('imagen', {id:$('#idInpunt').val(),img:lp_imagen}, function(data, textStatus, xhr) {
					if (data=='ok') {
						swal("Felicidades","Imagen "+lp_r+" asidnada con éxito. Ok para continuar ","success")
							.then((value) => {
								window.location.href='';
						});
						return false;
					}else {
						swal("Confirmación!", "No se pudo asiganar la imagen", "error");	
					}
				});
			}
		});
	},
	asignar:function(lp_r) {
		$('#idInpunt').val(lp_r);
	}
};

lp_activ.ready();