# TV Show Finder

# Purpose / Problem Statement
The TV Show Finder is a Python-based tool that allows users to search for TV shows using a keyword—such as a title, tag, or year. It addresses the common problem of browsing multiple cluttered websites just to find basic show info. Whether you're trying to recall a show from 2006 or looking for something in a specific genre, this tool simplifies the search process.

# Target Audience
This program is designed for:

TV lovers and binge-watchers

Students looking for quick entertainment

Young adults who want fast, clean access to show data without navigating bloated streaming services or search engines

# Solution + Limitations

# Solution:

Utilizes the TVMaze API to fetch real-time show data

Displays name, runtime, status, genre, premiere date, type, and summary

User-friendly error handling for no results or invalid input

# Limitations:

Displays only up to 3 shows

Cannot filter by multiple tags, ratings, or platforms

No clickable interface—currently runs in the console

Does not save search history or suggest related shows

# Key Features
Search Input: User enters a keyword, title, or year

API Request: Sends query to TVMaze API

Data Display: Outputs details like name, genre, and summary

Error Handling: Friendly messages if no results or failures occur

# Technical Challenges + # Future Plans

# Challenges:

Learning how to integrate and parse data from an external API

Handling different input types (titles vs. years vs. tags)

Avoiding crashes with incomplete or empty data

# Future Plans:

Add filters (e.g. genre, network, rating)

Build a web interface with Flask and HTML/CSS

Let users save or favorite shows

Display trailers and streaming availability

# Project Timeline
Day	Task
Day 1	Research APIs and set up requests library
Day 2	Build search functionality and basic output
Day 3	Add detailed show info (genre, summary, etc.)
Day 4	Implement error handling and flexible input
Day 5	Final polish, testing, and documentation

# Tools & Resources
[TVMaze API](https://support.techsmart.codes/hc/en-us/articles/1500004956221-5-4-Web-APIs-Teacher-Guide#h_01J04HQ4F267D1VRB7BFJBGG5Z)

Python + requests library

TechSmart platform (for code execution)


