## TV Show Finder

**Find TV shows fast using real-time data.**

---

### ✅ Purpose / Problem Statement

Scrolling through endless streaming platforms just to find a show from 2006? Yeah, no thanks. The **TV Show Finder** is a Python-based console tool that allows users to search TV shows by title, tag, or even year—all in one place. It cuts through the clutter of bloated websites and delivers clean info, fast.

---

###  Target Audience

* Binge-watchers who want quick access to TV data
* Students needing a mental break (hello, study sessions!)
* Anyone tired of streaming service overload

---

### Solution + Limitations

**Solution:**

* Uses the TVMaze API to pull real-time TV show info
* Displays up to 3 show results with:

  * Name, Runtime, Status, Genre, Premiered Date, Type, and Summary
* Friendly error messages for invalid or empty results

**Limitations:**

* Only shows 3 results at a time
* Can't filter by multiple tags, ratings, or streaming platforms
* Console-based (no web interface yet)
* Doesn’t store search history or suggest related shows

---

### Key Features

* **User Input**: Accepts flexible inputs like show title, tags, or year
* **API Integration**: Sends request to TVMaze
* **Result Display**: Shows details in a clear format
* **Error Handling**: try-except blocks to prevent crashes or blank data

---

### Technical Challenges

* Parsing JSON data from an unfamiliar API
* Handling unexpected or incomplete user inputs
* Ensuring the app doesn’t break with invalid keywords

---

### Future Plans

* Add filters (genre, rating, network)
* Build a web version using Flask + HTML/CSS
* Add functionality to favorite or bookmark shows
* Show trailers and where to stream the show

---

### Project Timeline

| Day   | Task                                       |
| ----- | ------------------------------------------ |
| Day 1 | Research APIs and set up request library   |
| Day 2 | Build core search and query functionality  |
| Day 3 | Add detailed data output (genre, summary)  |
| Day 4 | Add error handling and user input features |
| Day 5 | Final polish, testing, and documentation   |

---

###  Tools & Resources

* [TVMaze API](https://www.tvmaze.com/api)
* Python + `requests` library
* TechSmart platform

---

### Sample Code Snippet

Here’s a peek at how the program pulls and displays show data using the TVMaze API:

```python
import requests  # Making API calls

API_URL = "https://api.tvmaze.com"
path = "/search/shows"

print("Welcome to the TV Show Search!")
try:
    search = input("Enter a title, tag, or year to search by: ").lower()
    params = { "q": search }
    response = requests.get(API_URL + path, params=params)
    results = response.json()

    for i in range(3):
        print("Name:", results[i]["show"]["name"])
        print("Runtime:", results[i]["show"]["runtime"])
        print("Status:", results[i]["show"]["status"])
        print("Genres:", results[i]["show"]["genres"])
        print("Premiered:", results[i]["show"]["premiered"])
        print("Type:", results[i]["show"]["type"])
        print("Summary:", results[i]["show"]["summary"])
        print()
except IndexError:
    print("No results found. Try a different keyword.")
except Exception:
    print("Oops! Something went wrong. Please try again.")
```
