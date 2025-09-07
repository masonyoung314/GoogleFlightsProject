# GoogleFlightsProject
This project uses SerpApi's Google flights API to solve my problem of wanting a cheap flight from Amsterdam to Tenerife to see my girlfriend on Christmas. To do so, I call the API with my parameters 3 times per day (6AM, 2PM, and 10PM), returning the cheapest flight each day and then adding that to a list of the cheapest flights found any given day, and resetting the next day. At 11:59:59, the program outputs the cheapest of the three flights that day and then resets the list for the next day. 

If you would like to use this project in your own related project, simply request an API key from SerpApi, and put it in a .env file. Then, update the params section to fit your starting location and arrival. 

In the future I will potentially add the ability to alter some of the parameters to fit the user upon start. In addition, I would like to make the conditionals more strict and only return the cheapest flight that also fits my scheduling constraints (especially the time of the day).
