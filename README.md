# GG Deals Scraper

This Python script searches for games on GG Deals and extracts the prices from Official Stores and Keyshops.

## Features

*   **Game Search:** Takes a user input for a game title and searches for it on GG Deals.
*   **Price Extraction:** Extracts the price of the game from the search results page.
*   **Compare Prices:** Navigates to the "Compare Prices" page for each game and extracts the prices from Official Stores and Keyshops.
*   **Output:** Prints the title, price, Official Stores Price, and Keyshops Price for each game found.

## Dependencies

*   `requests`
*   `beautifulsoup4`

## Usage

1.  **Install Dependencies:** Install the required libraries using `pip install requests beautifulsoup4`.
2.  **Run the Script:** Execute the Python script. 
3.  **Enter Game Title:** The script will prompt you to enter the game title to search for.

## How It Works

1.  **Search:** The script takes the user input and constructs the search URL for GG Deals.
2.  **Extract Data:** It sends a request to the website, parses the HTML content using BeautifulSoup, and finds the containers holding game information.
3.  **Get Prices:** The script extracts the game title and price from the containers.
4.  **Compare Prices:** It finds the "Compare Prices" link, navigates to that page, and extracts the prices from Official Stores and Keyshops.
5.  **Output:** The script prints the extracted information for each game found.

## Disclaimer

Web scraping should be done responsibly and in accordance with the website's terms of service. Ensure you have the right to scrape data from GG Deals before using this script.
