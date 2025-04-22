from bs4 import BeautifulSoup
import pandas as pd

# Read HTML file
with open('10_Amazon.in_ Laptops.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all product containers
laptop_divs = soup.find_all('div', {'data-component-type': 's-search-result'})

# Lists to store data
names = []
reviews = []
prices = []

# Loop through each product
for laptop in laptop_divs:
    # Product Name
    name_element = laptop.find('h2')
    name = name_element.text.strip() if name_element else ""

    # Product Rating
    rating_element = laptop.find('span', class_='a-icon-alt')
    review_text = rating_element.text.strip() if rating_element else ""

    # Product Price
    price_element = laptop.find('span', class_='a-price-whole')
    price = price_element.text.strip() if price_element else ""

    # Append to lists
    names.append(name)
    reviews.append(review_text)
    prices.append(price)

# Save to Excel
df = pd.DataFrame({
    'Names': names,
    'Reviews': reviews,
    'Price': prices
})
df.to_excel('10_Amazon_Laptops_Data.xlsx', index=False) 
