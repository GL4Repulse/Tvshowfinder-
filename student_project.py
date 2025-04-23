"""
Data Structures
Student Project
Project Title: TV Show Search with API and Custom Tags
"""

# ---- IMPORT LIBRARIES ---- #
import requests  # Importing the requests module to make API calls

# ---- BASE API URL ---- #
API_URL = "http://api.tvmaze.com/search/shows?q="  # Base URL to search for shows

# ---- TV SHOW DATABASE ---- #
tvshows = [
    {"title": "Ben 10", "year": 2008, "tags": ["cartoon", "action"]},
    {"title": "Invincible", "year": 2021, "tags": ["TVMA", "action", "animation"]},
    {"title": "The Boys", "year": 2019, "tags": ["TVMA", "action"]},
    {"title": "Daredevil Born Again", "year": 2025, "tags": ["TVMA", "action", "Marvel"]}
]

# ---- WELCOME MESSAGE ---- #
print(" Welcome to the TV Show Search! ")
search = input("Enter a title, tag, or year to search by, or type 'quit' to quit: \n").lower()

# ---- MAIN SEARCH LOOP ---- #
# While the user has not entered "quit", continue running the program
while search != "quit":
    search_results = []  # List to store matched results

    # ---- LOCAL SEARCH ---- #
    for tv in tvshows:
        ## -- TITLE MATCH -- ##
        if tv["title"].lower() == search:
            search_results.append(tv)

        ## -- YEAR MATCH -- ##
        elif str(tv["year"]) == search:
            search_results.append(tv)

        ## -- TAG MATCH -- ##
        elif search in [tag.lower() for tag in tv["tags"]]:
            search_results.append(tv)

    # ---- API SEARCH ---- #
    # If no results are found locally, search online using the TVMaze API
    if len(search_results) == 0:
        print("\n No local results found. Searching online...")

        # API request with search query
        response = requests.get(API_URL + search)

        # ---- API ERROR HANDLING ---- #
        if response.status_code == 200:  # Successful API response
            api_data = response.json()

            # If results are returned from the API
            if len(api_data) > 0:
                for result in api_data:
                    show_info = result["show"]
                    search_results.append({
                        "title": show_info["name"],
                        "year": show_info["premiered"].split("-")[0] if show_info["premiered"] else "N/A",
                        "tags": show_info["genres"] if show_info["genres"] else ["N/A"]
                    })
            else:
                print("No results found in the API database.")
        else:
            print(" Error fetching data from API. Please try again later.")

    # ---- DISPLAY SEARCH RESULTS ---- #
    print("\n Search Results for: [" + str(search).upper() + "]")

    ## -- NO RESULTS FOUND -- ##
    if len(search_results) == 0:
        print(" Sorry, no matches found!")
    ## -- DISPLAY MATCHED RESULTS -- ##
    else:
        for result in search_results:
            print(" Title: [" + result['title'] + "]")
            print(" Year: (" + str(result['year']) + ")")
            print(" Tags: " + ", ".join(result['tags']))
            print("-" * 40)

    # ---- PROMPT FOR NEXT SEARCH ---- #
    search = input("\nEnter a title, tag, or year to search by, or type 'quit' to quit: \n").lower()

# ---- EXIT MESSAGE ---- #
print("\n Thanks for using the TV Show Search Program! See you next time! ")

