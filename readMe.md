#StarWars API - ACS1710 Quiz2

##Challenge 1
[]Display the character data from SWAPI. You'll need to include an input that allows us to input the id of a character. Your code will request the data from the API and display it on the page.

For any character you should display:

    [x]name
    [x]height
    [x]mass
    [x]hair_color
    [x]eye_color

Stretch Challenge
[x]Style your work. This is open ended put as much time into this as you like.

[x]Style the form elements and the the output data.

[x]Error Checking for bad requests
Some of the ids are missing or out of bounds. For example people/17 doesn't exist. Solve this challenge by checking for errors and displaying a message when there is a problem.

[x]Stretch Challenge
The homeworld property is a URL to the homeworld at the SWAPI. Make another request and get the homeworld data and display the name of the hoemworld.

[x]Displaying Lists
Every character has a films property that is a list of the films they appeared in. This list is a list of URLs to those films on SWAPI. Loop over this list, make a request to get the data for each film and display the name of each film.