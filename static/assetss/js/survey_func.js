	/*  Wizard */
	jQuery(function ($) {
		"use strict";
		function exists(ele){
			if (ele !== null && ele !== undefined){return true}else{return false}
		}
		$('form#wrapped').attr('action', '');
		$("#wizard_container").wizard({
			stepsWrapper: "#wrapped",
			submit: ".submit",
			beforeSelect: function (event, state) {
				if ($('input#website').val().length != 0) {
					return false;
				}
				if (!state.isMovingForward)
					return true;
				var inputs = $(this).wizard('state').step.find(':input');
				return !inputs.length || !!inputs.valid();
			}
		}).validate({
			errorPlacement: function (error, element) {
				if (element.is(':radio') || element.is(':checkbox')) {
					error.insertBefore(element.next());
				} else {
					error.insertAfter(element);
				}
			}
		});
		//  progress bar
		$("#progressbar").progressbar();
		$("#wizard_container").wizard({
			afterSelect: function (event, state) {
				$("#progressbar").progressbar("value", state.percentComplete);
				if(window.value === "Yes"){
					$("#verify").removeClass("required");
					$("#verify").addClass("required");
				}else if(window.value === "No"){
					var url = window.location.pathname
					var current = url.split("/")[3]
					window.location.href = "/accounts/test/"+window.next+"/"
					$("#verify").removeClass("required");
					window.scores[window.indicator] = 1;
					localStorage.setItem("scores",JSON.stringify(window.scores));
					
				}else{
					if(exists(window.scores[window.name])){
						window.scores[window.name] = (parseInt(window.scores[window.name]) + parseInt(window.value)) 
					}else{
						window.scores[window.name] = parseInt(window.value)
					}
					console.log(window.scores[window.name]);
					// check if we are on the last answer 
					var old = JSON.parse(localStorage.getItem("quests"));
					var list = old[""+name];
					window.answers[""+name].push(parseInt(window.value));
					if(window.answers[""+name].length == list.length){
					// we have our final answer, let's save
					var old_answers = JSON.parse(localStorage.getItem("answers")) || {};
					var mg = merge(old_answers,window.answers);
					localStorage.setItem("answers",JSON.stringify(mg));
					}

					console.log(window.answers);
				}
				$("#location").text("(" + state.stepsComplete + "/" + state.stepsPossible + ")");
			}
		});
		// Validate select
		$('#wrapped').validate({
			ignore: [],
			rules: {
				select: {
					required: true
				}
			},
			errorPlacement: function (error, element) {
				if (element.is('select:hidden')) {
					error.insertAfter(element.next('.nice-select'));
				} else {
					error.insertAfter(element);
				}
			}
		});
	});

// Summary 
function getVals(formControl, controlType) {
	switch (controlType) {

		case 'question_1':
			// Get the value for a radio
			var value = $(formControl).val();
			// console.log(value);
			window.value = value;
			if(window.value === "Yes"){
				$("#verify").removeClass("required");
				$("#verify").addClass("required");
			}else{
				$("#verify").removeClass("required");
			}
			$("#question_1").text(value);
			break;

		case 'additional_message':
			// Get the value for a textarea
			var value = $(formControl).val();
			$("#additional_message").text(value);
			break;

		case 'question_2':
			// Get the value for a radio
			var name = $(formControl).prop('name');
			var value = $(formControl).val();
			
			var quest = $(".mb-4").text()
			console.log(quest,value);
			window.value = value;
			window.name = name;
			$("#question_2").text(value);
			break;

		case 'additional_message_2':
			// Get the value for a textarea
			var value = $(formControl).val();
			$("#additional_message_2").text(value);
			break;

		case 'question_3':
			// Get name for set of checkboxes
			var checkboxName = $(formControl).attr('name');

			// Get all checked checkboxes
			var value = [];
			$("input[name*='" + checkboxName + "']").each(function () {
				// Get all checked checboxes in an array
				if (jQuery(this).is(":checked")) {
					value.push($(this).val());
				}
			});
			$("#question_3").text(value.join(", "));
			break;
	}
}
