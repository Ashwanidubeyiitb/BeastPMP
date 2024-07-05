$(document).ready(function () {

	var current_fs, next_fs, previous_fs; //fieldsets
	var opacity;
	var current = 1;
	var steps = $("fieldset").length;

	setProgressBar(current);

	$(".next").click(function () {
		current_fs = $(this).parent();
		next_fs = $(this).parent().next();

		var name = $('#name').val();
		var roll_no = $('#roll_no').val();
		var department = $('#department').val();
		var degree = $('#degree').val();
		var sop = $('#t04').val();
		var email = $('#email_id').val();
		if(name != "" && roll_no!= "" && department != "---" && degree != "---" && sop != "" && email != ""){

		//Add Class Active
		$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

		//show the next fieldset
		next_fs.show();
		//hide the current fieldset with style
		current_fs.animate({ opacity: 0 }, {
			step: function (now) {
				// for making fielset appear animation
				opacity = 1 - now;

				current_fs.css({
					'display': 'none',
					'position': 'relative',
				});
				next_fs.css({ 'opacity': opacity });
			},
			duration: 500
		});
		setProgressBar(++current);

	}
	else{
		alert("You need to fill all the details");
	}
	});

	$(".previous").click(function () {

		current_fs = $(this).parent();
		previous_fs = $(this).parent().prev();

		//Remove class active
		$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

		//show the previous fieldset
		previous_fs.show();

		//hide the current fieldset with style
		current_fs.animate({ opacity: 0 }, {
			step: function (now) {
				// for making fielset appear animation
				opacity = 1 - now;

				current_fs.css({
					'display': 'none',
					'position': 'relative'
				});
				previous_fs.css({ 'opacity': opacity });
			},
			duration: 500
		});
		setProgressBar(--current);
	});

	function setProgressBar(curStep) {
		var percent = parseFloat(100 / steps) * curStep;
		percent = percent.toFixed();
		$(".progress-bar")
			.css("width", percent + "%")
	}

	$("#submit-btn").click(function (event) {
		// Prevent default form submission (prevents accidental reload)
		event.preventDefault();

		const preferenceIds = [
			"#preference_1",
			"#preference_2",
			"#preference_3",
			"#preference_4",
			"#preference_5"
		];

		$("#error-message").text(""); // Assuming you have an element with this ID

		// Check if all preferences are filled
		let allFilled = true;
		let allNumeric = true;
		for (const id of preferenceIds) {
			const value = $(id).val();
			console.log("value : ", $.isNumeric(value));
			if(!value){
				allFilled = false;
				break;
			}
		}

		for (const id of preferenceIds){
			const val = $(id).val();
			if (!$.isNumeric(val)) {
				allNumeric = false;
				break; // Exit loop if any is empty
			}
		}
		
		console.log("allFilled : ", allFilled);

		if (allFilled && allNumeric) {
			// form = $("#msform")[0]
			// Submit the form (assuming you have a form with ID "msform")
			$("#msform").submit();
		} 
		else if(!allFilled) {
			// Display error message in the designated div
			$("#error-message")
			.text("You have not filled all preference fields.")
			.css({
				"background-color": "red",
				"width": "400px",
				"margin": "20px auto",
				"color": "white",
				"font-family": "Arial, Helvetica, sans-serif",
				"font-size": "large",
				"padding": "10px 20px",
				"border-radius": "2px",
			});

		}
		else if(!allNumeric) {
			// Display error message in the designated div
			$("#error-message")
			.text("All preference fields are not numbers")
			.css({
				"background-color": "red",
				"width": "400px",
				"margin": "20px auto",
				"color": "white",
				"font-family": "Arial, Helvetica, sans-serif",
				"font-size": "large",
				"padding": "10px 20px",
				"border-radius": "2px",
			});
		}
	});

});