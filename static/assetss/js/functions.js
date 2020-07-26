(function ($) {

	"use strict";
	function exists(ele){
		if (ele !== null && ele !== undefined){return true}else{return false}
	}
	// Preload
	$(window).on('load', function () { // makes sure the whole site is loaded
		$('[data-loader="circle-side"]').fadeOut(); // will first fade out the loading animation
		$('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
		$('body').delay(350).css({
			'overflow': 'visible'
		});
	})
	
	// Submit loader mask 
	// This will be used when the person finally submits a form
	$('form#wrapped').on('submit', function () {
		if(exists(window.scores[window.name])){
			window.scores[window.name] = (window.scores[window.name] +parseInt(window.value)) 
		}else{
			window.scores[window.name] = parseInt(window.value);
		}
		window.scores[window.name] = window.scores[window.name]
		localStorage.setItem("scores",JSON.stringify(window.scores));
		console.log(window.scores);
		var form = $("form#wrapped");
		form.validate();
		if (form.valid()) {
			$("#loader_form").fadeIn();
		}
		var url = window.location.pathname
		var current = url.split("/")[3]
		window.location.href = "/accounts/test/"+window.next+"/"
	});
	
	// Float labels
	var floatlabels = new FloatLabels( 'form', {
		    style: 2
	});
	
})(window.jQuery); 