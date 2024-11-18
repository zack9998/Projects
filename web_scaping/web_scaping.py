import requests
from bs4 import BeautifulSoup  # Import libraries for sending requests and parsing HTML content

# Send a GET request to the website and store the response
response = requests.get("https://books.toscrape.com/")

# Parse the HTML content of the response using BeautifulSoup with an HTML parser
soup = BeautifulSoup(response.content, "html.parser")

# Find all the 'article' tags (each article represents a book) and store them in the 'books' variable
books = soup.find_all("article")

# Loop through each book found in the 'books' list
for book in books:
    # Extract the book title from the 'a' tag inside the 'h3' tag
    title = book.h3.a["title"]
    
    # Extract the rating of the book from the 'class' attribute of the 'p' tag
    rating = book.p["class"][1]

    # Extract the price of the book
    price = book.find('p', class_='price_color').text
    
    # Print the book title and its rating
    print(f"Title: {title} | Rating: {rating} stars | Price: {price}" )
    print("thanks")
