# Heyo

This is a simple Flask API projects. It has 2 main routes
- `/api/postcodes: A POST endpoint that gets you a list of all the locations that have the **placename** you pass.
- `/api/verify_otp: A POST endpoint as well. You pass the **placename** and **postaal_code** to this endpoint to verify if it exists. If it does exist, it returns true and a data object containing the location details. If it does not exist, it returns false.

Enjoy!
