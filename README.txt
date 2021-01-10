In this project, I have created basically 3 endpoints:

  1- '/signup' ['POST]                          - It is used for signing up for the users. It will 5 parameters, if not provided, it will throw an error.

  2- '/users' ['GET]                            - It will show number of users that have signed up so far.

  3- '/covid-data-and-sending-mail' ['POST]     - It will show the covid data of a particular country of a particular days.
  
Note: Test the endpoints through postman.

Request Payloads are in json format

1- '/signup'
		{
		"firstname":"",
		"lastname": "",
		"password": "",
		"email": "",
		"country": ""
		}
2- '/covid-data-and-sending-mail'
		{
		  "email": "",
		  "country": "" #optional.  If not provided, it will automatically take the user's country.
		  "days": "" # optional. If not provided it will show last 15days of data.
		}
   