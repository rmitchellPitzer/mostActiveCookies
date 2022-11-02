# Most Active Cookies

Hi! This Github repository contains the files needed for running the Python script most_active_cookie.py and the unit tests most_active_cookie_tests.py. There's also a csv used for testing given to run the tests.

## most_active_cookie.py usage:

most_active_cookie.py takes in a filename argument and a date argument and returns the most active cookie(s) on a given date.
This is done through a set of methods in the CookieInstance class: readInCSV, updateMapOfCookies, findOccurences, returnMax, and runScript.
The CookieInstance class is default initialized with an empty csvFile of type list, empty mapOfCookies of type dictionary, and empty listOfOccurences of type list.
### readInCSV(fileName) 
Takes in a file name/directory, and will read in the contents from the filename, insert the contents into csvFile, and return 0. If there's no file with the name given, it excepts the error and prints out an error, and returns 1.
### updateMapOfCookies() 
Updates the mapOfCookies to contain a set of keys/values, where the keys are the dates and values are the cookies occuring on the dates. This will also return 0.
### findOccurences(date) 
takes in a date, and using bucket sort, sorts the cookies in mapOfCookies occuring on that date by how many times they occur. This will except and return 1 if there are no cookies with the given date. If no error occurs, this then will update the listOfOccurences to contain this bucket sorted list. 
### returnMax()
This method will iterate backwards through listOfOccurences to find the first non empty element, and for every item in the non empty element, print it out. If there were no cookies in the list, it will print out an error message and return 1, otherwise it will return 0.
### runScript(fileName, date)
This method will run the above methods in order using the arguments passed in. Using the 0/1 values returned from the methods, this will determine which methods are ran. This is to ensure we don't run any extra methods when we know there's an invalid filename/invalid date used.


## most_active_cookie_tests.py usage:

This will run from main all the tests in the file. This will test for correct output/incorrect output of each of the methods outlined above. 
### IMPORTANT: 
The directory containing most_active_cookie_tests.py must also contain most_active_cookie.py and the cookie_log.csv file given.

## Thank you so much!
If you have any questions feel free to email me!
