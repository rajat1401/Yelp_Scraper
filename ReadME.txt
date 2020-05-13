To set a custom location and/or search keyword, edit the notebook.py file where the call to get_businesses() function
is made in the last line. 

The code works by manually building the URL (as per the keywords entered) and parses the response of the resulting
page to json and extracts the required data. For each listing we extract :-
1) Name 
2) Address
3) Categories (refers to tags. e.g. if it's a ["Chinese", "Mexican"] restaurant) 
4) Zip_Code
5) Phone Number
6) Rating (1-5)
7) URL