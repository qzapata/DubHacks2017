(function () {
	var values;

	//sets onload function of the page
	window.onload = function() {
		values = new Array();

		document.getElementById("taskText").value = "";
		document.getElementById("eventText").value = "";
		document.getElementById("examText").value = "";

		document.getElementById("taskBtn").onclick = AddTask;
		document.getElementById("eventBtn").onclick = AddEvent;
		document.getElementById("examBtn").onclick = AddExam;
		document.getElementById("crSchedule").onclick = SendData;
	}; 

	function AddTask() {

		
		values.push("task");
		values.push(document.getElementById("taskName").value);
		values.push(document.getElementById("taskStart").value); 
		values.push(document.getElementById("taskEnd").value);

		document.getElementById("taskText").value += document.getElementById("taskName").value + "\n";
	}

	function AddEvent() {
		values.push("event");
		values.push(document.getElementById("eventName").value);
		values.push(document.getElementById("eventStart").value);
		values.push(document.getElementById("eventEnd").value);

		document.getElementById("eventText").value += document.getElementById("eventName").value + "\n";
	}

	function AddExam() {
		values.push("exam");
		values.push(document.getElementById("examName").value);
		values.push(document.getElementById("examStart").value);
		values.push(document.getElementById("examEnd").value);

		document.getElementById("examText").value += document.getElementById("examName").value + "\n";
	}

	function SendData() {
		var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
		console.log(values);
		$.ajax({
	        type: 'post',
	        url: 'get_data',
	        data: {'tasks[]': values,
	     		csrfmiddlewaretoken:csrftoken
	     	},
    	});
	}
}) ();