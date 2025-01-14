import requests
from bs4 import BeautifulSoup

def search_games(query):
    # Construct the URL with the user input
    base_url = "https://gg.deals/search/"
    params = {
        'platform': 1,
        'title': query,
        'type': 1
    }
    
    # Send the request to the website
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return
    
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the container that holds each item
    containers = soup.find_all(class_="game-info-wrapper d-flex column-wrapper")
    
    # Iterate over the containers and extract title and price
    for container in containers:
        title_elem = container.find(class_="game-info-title title")
        price_elem = container.find(class_="price-inner numeric")
        
        title = title_elem.text.strip() if title_elem else "Not available"
        price = price_elem.text.strip() if price_elem else "Not available"
        
        # Proceed only if a price is available
        if price:
            print(f"Title: {title}")
            print(f"Price: {price}")
            
            # Use the specific CSS selector to find the "Compare Prices" button
            compare_link_elem = container.select_one('.game-info-wrapper.d-flex.column-wrapper .game-cta > a[aria-label="Compare Prices"]')
            if compare_link_elem:
                compare_url = "https://gg.deals/" + compare_link_elem['href']
                
                # Request the "Compare Prices" page
                compare_response = requests.get(compare_url)
                if compare_response.status_code == 200:
                    compare_soup = BeautifulSoup(compare_response.text, 'html.parser')
                    
                    # Extract the first two prices
                    price_elements = compare_soup.select('.relative.d-flex.flex-wrap.game-header-price.game-price-anchor-link.game-price-anchor .price-inner.numeric')
                    official_store_price = price_elements[0].text.strip() if len(price_elements) > 0 else "No price available"
                    keyshop_price = price_elements[1].text.strip() if len(price_elements) > 1 else "No price available"
                    
                    print(f"Official Stores Price: {official_store_price}")
                    print(f"Keyshops Price: {keyshop_price}")
                else:
                    print("Failed to retrieve the Compare Prices page")
            else:
                print("No Compare Prices link available")
            
            print("-" * 40)

# User input for search
user_query = input("Enter the game title to search for: ").strip()
search_games(user_query)
