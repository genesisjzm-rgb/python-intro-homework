#BOOK SEARCH CLI TOOL

## Features
- Search for books by title using an interactive menu.
- Connects directly to the Open Library API with error handling.
- Cleans up the data so missing or "N/A" publication years don't break the program.
- Uses Matplotlib to generate and save a chart of the publication years.

### Question Addressed
* **Question:** What is the distribution of first publication years for the books returned in a specific search?

### Chart Description & Main XTakeaway
* **What the chart shows:** A histogram that plots out how many books from the search results were published in different years.
* **Main takeaway:** It makes it really easy to see at a glance whether a search term brings up mostly or classics or more modern books, showing the overall time spread of the results.

### Why This Chart Type?
* **Chart Type:** Histogram
* **Rationale:** I went with a histogram because it's great for showing numerical data like years grouped together. It makes it super easy to spot trends and see where the concentrations of publication dates fall.

## How to Run
1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
