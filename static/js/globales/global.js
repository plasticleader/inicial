var lp_global = {
	ready:function() {
		// $(".modal").modal({
		// 	keyboard: false,
		// 	backdrop: false
		// });
	},
	crearVentana:function(header,url,tmn) {
		// ejemplo agragar tamaño con clase  
		// Pequeño = mod_al-sm
		// Grande = mod_al-lg 3134716641 // Eugenio Medez
		//
		$("#lpModalTitulo").html(header);
		// $('#id="lpModalGeneral').removeClass('modal-dialog mod_al-sm');
		$('#lpModalGeneral').addClass('modal-dialog '+tmn+' ');


		if (url) {
			lp_global.enviarUrl("lpModalBody",url,false);
		}

		$("#lpModalGeneral").modal({
			keyboard: false,
			backdrop: false
		});
	},
	
	:function(pl_op,pl_estado,pl_id,pl_table) {
		if (pl_op=='B') {
			op = 'Desactivar';
			opd = 'Desactivado'
		}else{
			op ='Activar'
			opd = 'Activado'
		}

		swal({
		  title: "Confirmación... ",   
		  text: "Seguro(a) desea  "+op+" estado. ?",
		  icon: "info",
		  buttons: true,
		  dangerMode: true,
		})
		.then((willDelete) => {
		  	if (willDelete) {
			   	$.post('../global/pl_modEstado', {id:pl_id,estado:pl_estado,table:pl_table}, function(data, textStatus, xhr) {
					$("#divEstados_"+pl_id).html(data);
					swal("Confirmación!", "Estado "+opd+" Exitosamente!", "success");
				});
			}
		});
	},
	cerrarVentana: function(){
		$("#lpModalGeneral").modal('hide');
	},
	enviarUrl: function(identificador,url,funcion){
		$(identificador).load(url,funcion);
	},
	// mymodal: function(titulo,cuerpo,tamanio,btn_cancelar,callback_cancelar,btn_ok,callback_ok){
	// 	//console.log(titulo,cuerpo,tamanio,btn_cancelar,callback_cancelar,btn_ok,callback_ok); 
	// 	$("#modal-tn-titulo").html(titulo);
		
		
	// 	if(tamanio){
	// 		$(".modal-dialog").attr('style', 'width: 90%');
	// 	}else{
	// 		$(".modal-dialog").removeClass('modal-lg');
	// 	}

	// 	if(btn_cancelar){
	// 		$("#btn_modal_cancelar").show();
	// 	}

	// 	if(callback_cancelar){
	// 		$("#btn_modal_cancelar").unbind('click');
	// 		$("#btn_modal_cancelar").click(function(){
	// 			eval(callback_cancelar);
	// 			$('#obs').val('');
	// 			$('#oculto').hide();
	// 		});
	// 	}
	// 	if(btn_ok){
	// 		$("#btn_modal_ok").html(btn_ok).show();
	// 	}

	// 	if(callback_ok){
	// 		$("#btn_modal_ok").unbind('click');
	// 		$("#btn_modal_ok").click(function(){
	// 			eval(callback_ok);
	// 		});
	// 	}
		
	// 	if (cuerpo) {
	// 		tpl.load_ajax("#modal-tn-body",cuerpo,false);
	// 	}
	// 	$("#modal-tn").modal({
	// 		keyboard: false,
	// 		backdrop: false
	// 	});
	// },
	// mymodalClose: function(){
	// 	$("#modal-tn").modal('hide');
	// },
	// load_ajax: function(selector,url,callback){
	// 	$(selector).load(url,callback);
	// },
	valida_campo: function(campo,mensaje,focus,callback){
		if( $.trim( $('#'+campo).val() ) == '' ){
			if(window.sweetAlert){
				if(focus){
					callback += "$('#"+campo+"').focus();";
				}
				swal({
					title: "Ooops...",
					text: mensaje,
					type: "warning",
					showCancelButton: false,
					closeOnConfirm: true,
					showLoaderOnConfirm: false, 
					confirmButtonText: "Ok",
					confirmButtonColor: "#e60000",
					callback: eval(callback),
				});
			}else{
				alert(mensaje);
			}
			
			return true;			
		}
		return false;
	},
};

lp_global.ready();