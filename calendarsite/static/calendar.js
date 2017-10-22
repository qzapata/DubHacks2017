(function () {
	// Client ID and API key from the Developer Console
	var CLIENT_ID = 'romP_lpHbCil7P5xS9h1Vzl';

	// Array of API discovery doc URLs for APIs used by the quickstart
	var DISCOVERY_DOCS = ["https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest"];

	// Authorization scopes required by the API; multiple scopes can be
	// included, separated by spaces.
	var SCOPES = "https://www.googleapis.com/auth/calendar.readonly";

	var authorizeButton = document.getElementById('export');

	/**
	*  On load, called to load the auth2 library and API client library.
	*/
	function handleClientLoad() {
		gapi.load('client:auth2', initClient);
	}

		/**
		*  Initializes the API client library and sets up sign-in state
		*  listeners.
		*/
	function initClient() {
		gapi.client.init({
		  discoveryDocs: DISCOVERY_DOCS,
		  clientId: CLIENT_ID,
		  scope: SCOPES
		}).then(function () {
		  // Listen for sign-in state changes.
		  gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);

		  // Handle the initial sign-in state.
		  updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
		  authorizeButton.onclick = handleAuthClick;
		});
	}

	/**
	*  Called when the signed in status changes, to update the UI
	*  appropriately. After a sign-in, the API is called.
	*/
	function updateSigninStatus(isSignedIn) {
		if (isSignedIn) {
		  authorizeButton.style.display = 'none';
		  signoutButton.style.display = 'block';
		  export();
		} else {
		  authorizeButton.style.display = 'block';
		  signoutButton.style.display = 'none';
		}
	}

	/**
	*  Sign in the user upon button click.
	*/
	function handleAuthClick(event) {
		gapi.auth2.getAuthInstance().signIn();
	}

	function export() {
		for var i = 0; i < data.length; i += 3
		{
			var start = data[i];
			var end = data[i + 1];
			var name = data[i + 2];
			var event = {
  'summary': name,
  'location': '',
  'description': '',
  'start': {
    'dateTime': start + '-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': end + '-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    ''
  ],
  'attendees': [

  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}
			gapi.client.calendar.get
			event = service.events().insert(calendarId=gapi.client.calendar.get().calendarId, body=event).execute()
		}
	}

	var data;
	window.onload = function () {
		var data = {{ papel|safe }};
		console.log(data);
		$('#calendar').fullCalendar({
    		weekends: true
		});
	};


}) ();