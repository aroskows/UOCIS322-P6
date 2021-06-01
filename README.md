# UOCIS322 - Project 6 #
Brevet time calculator with AJAX, MongoDB, and a RESTful API!
Author: Alexa Roskowski
Date: 5/30/21

# DESCRIPTION #

This website takes all the stuff we did in P5 and added an RESTful API
the api exists on a seperate port and will print the open and close times
that you put on the mongodb from the normal brevets caculator. the website 
has three buttons: List All, List Open, and List Close. these will print
the open, close, or both times in the selected form ( JSON or CSV). Additionally,
 there is an input box where you are suppossed to be able to limit the number 
of times that are displayed. 


# notes #

My folder brevetsapp/ all the files are not there instead they are in another
nested folder (brevetsapp/brevets/). my doecker-compose.yml reflects this.

The urls work if they use the port for the restapi. also they url format is:

/listOpen/JSON/top

/listClose/CSV/top

where top is just the number of the times you want to see and assumming that the port is
the port of the resting api
