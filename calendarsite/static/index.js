(function () {
	var values;
	//returns the dom element for the given id
	//
	//id: string id of an existing dom element
	function $(id) {
		return document.getElementById(id);
	}

	//sets onload function of the page
	window.onload = function() {
		values = {
			"task": new Array(),
			"event": new Array(),
			"exam": new Array()
		};

		$("taskText").value = "";
		$("eventText").value = "";
		$("examText").value = "";

		$("taskBtn").onclick = AddTask;
		$("eventBtn").onclick = AddEvent;
		$("examBtn").onclick = AddExam;
		$("crSchedule").onclick = SendData;
	}; 

	function AddTask() {
		var val = {
			"name": $("taskName").value,
			"time": $("taskStart").value,
			"duedate": $("taskEnd").value
		};

		values["task"].push(val);
		$("taskText").value += val["name"] + "\n";
	}

	function AddEvent() {
		var val = {
			"name": $("eventName").value,
			"time": $("eventStart").value,
			"duedate": $("eventEnd").value
		};

		values["event"].push(val);
		$("eventText").value += val["name"] + "\n";
	}

	function AddExam() {
		var val = {
			"name": $("examName").value,
			"time": $("examStart").value,
			"duedate": $("examEnd").value
		};

		values["exam"].push(val);
		$("examText").value += val["name"] + "\n";
	}

	function SendData() {
		console.log(values);
		$.ajax({
	        type: 'POST',
	        url: '/get_data/',
	        data: {'tasks[]': values},
    	});
	}
}) ();