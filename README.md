# Tvshowfinder-Purpose/Problem Statement
This program helps users easily search for TV shows using a keyword—whether that’s a title, a tag, or a year. It solves the problem of finding detailed information about shows without needing to dig through multiple websites. Whether you're trying to remember the name of a show from 2006 or looking for something in a specific genre, this tool streamlines the process.

# Target Audience-
The target audience is TV lovers—students, casual binge-watchers, and young adults who want fast access to info about shows. It’s especially useful for people who are tired of scrolling through streaming platforms or websites with cluttered interfaces.


# Solution + Limitations-
This program uses the TVMaze API to fetch live data about shows based on user input. It returns a show’s name, runtime, status, genre, premiere date, type, and a summary.

# Limitations:
It only returns up to 3 shows max.
You can’t filter by multiple tags, ratings, or streaming platforms.
No clickable interface—just console-based.
It doesn’t store search history or recommend related shows.

# Key Features / Key Components-

Search Input: User types a title, year, or keyword.
API Request: The program sends a query to the TVMaze API.
Data Display: It shows the name, runtime, genres, and more for each matching show.
Error Handling: If no shows are found or something breaks, it gives friendly messages.
List major parts of your program (what the user can do or see).

# Technical Challenges + Future Plans-

# Challenges:
Learning how to work with an API and parse JSON responses.
Figuring out how to handle different search types (title vs. year vs. tag) with one input.
Making sure the program doesn’t crash if results are empty or broken.

# Future Plans:

Add more filters like genre or network.
Build a simple web interface using Flask or HTML/CSS.
Let users save or favorite shows.
Show trailers or where to stream the show.

# Project Timeline-

Day 1: Learn about APIs and install requests.

Day 2: Build basic program to search and display show names.

Day 3: Add more details (genres, summary, etc.).

Day 4: Add error handling and input variations.

Day 5: Polish program and test with different inputs.


# Tools and Resources Used-

[TVMaze API Docs](https://support.techsmart.codes/hc/en-us/articles/1500004956221-5-4-Web-APIs-Teacher-Guide#h_01J04HQ4F267D1VRB7BFJBGG5Z)
Python and the requests library 
TechSmart platform to run code

