import requests
from bs4 import BeautifulSoup
import csv

# URL of the website
url = "https://scrapeme.live/shop/"
response = requests.get(url,verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product containers
products = soup.find_all('li', class_="product")

# Open a CSV file to write data
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(["Product Name", "Price", "Product Link"])
    
    # Loop through each product and extract details
    for product in products:
        # Extract the product name
        name = product.find('h2', class_="woocommerce-loop-product__title").get_text(strip=True)
        
        # Extract the product price
        price = product.find('span', class_="woocommerce-Price-amount").get_text(strip=True)
        
        # Extract the product link
        link = product.find('a', class_="woocommerce-LoopProduct-link")['href']
        
        # Write the data to the CSV file
        writer.writerow([name, price, link])
        
        # Print extracted details
        print(f"Product Name: {name}")
        print(f"Price: {price}")
        print(f"Product Link: {link}")
        print("-----")

print("Data has been successfully written to 'products.csv'.")