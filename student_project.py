"""
Data Structures
Student Project
Project Title: TV Show Search with API and Custom Tags
"""

# ---- IMPORT LIBRARIES ---- #
import requests  # Importing the requests module to make API calls
import pp 
# ---- BASE API URL ---- #
API_URL = "https://api.tvmaze.com"  # Base URL to search for shows
path = "/search/shows"
# ---- WELCOME MESSAGE ---- #
print(" Welcome to the TV Show Search! ")
try:
    search = input("Enter a title, tag, or year to search by, or type 'quit' to quit: \n").lower()
    params ={
        "q": search
    }
    response = requests.get(API_URL+path, params=params)
    results = response.json()
    #name of show runtime stauts gernre
    for i in range (3):
        print("Name: " +  str (results[i]["show"]["name"]))
        print("Runtime: " + str (results[i]["show"]["runtime"]))
        print("Status: " + str (results[i]["show"]["status"]))
        print("Genres: " + str (results[i]["show"]["genres"]))
        print("Premiered: " + str (results[i]["show"]["premiered"]))
        print("Type: " + str (results[i]["show"]["type"]))
        print("Summary: " + str (results[i]["show"]["summary"]))
        print()
except IndexError:
    print ("No Results")
except Exception:
    print ("Sorry this does not exist please pick another title")