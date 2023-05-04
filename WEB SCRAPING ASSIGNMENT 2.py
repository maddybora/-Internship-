#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.naukri.com/"
search_term = "Data Analyst"
location = "Bangalore"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, 'html.parser')

# Find the search fields and enter the search criteria
search_fields = soup.find_all('input', {'class': 'sugInp'})
search_fields[0]['value'] = search_term
search_fields[1]['value'] = location

# Find and click the search button
search_button = soup.find('button', {'class': 'btn'})
response = requests.post(url, data={'skill': search_term, 'location': location})

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the job listings
job_listings = soup.find_all('article', {'class': 'jobTuple bgWhite br4 mb-8'})

# Scrape the job data for the first 10 job listings
jobs_data = []
for job in job_listings[:10]:
    job_title = job.find('a', {'class': 'title'}).text.strip()
    job_location = job.find('li', {'class': 'fleft grey-text br2 placeHolderLi location'}).text.strip()
    company_name = job.find('a', {'class': 'subTitle ellipsis fleft'}).text.strip()
    experience_required = job.find('li', {'class': 'fleft grey-text br2 placeHolderLi experience'}).text.strip()
    jobs_data.append({'Job Title': job_title, 'Job Location': job_location, 'Company Name': company_name, 'Experience Required': experience_required})

# Create a pandas dataframe from the scraped data
df = pd.DataFrame(jobs_data)

# Display the dataframe
print(df)


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.naukri.com/"
search_term = "Data Scientist"
location = "Bangalore"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, 'html.parser')

# Find the search fields and enter the search criteria
search_fields = soup.find_all('input', {'class': 'sugInp'})
search_fields[0]['value'] = search_term
search_fields[1]['value'] = location

# Find and click the search button
search_button = soup.find('button', {'class': 'btn'})
response = requests.post(url, data={'skill': search_term, 'location': location})

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the job listings
job_listings = soup.find_all('article', {'class': 'jobTuple bgWhite br4 mb-8'})

# Scrape the job data for the first 10 job listings
jobs_data = []
for job in job_listings[:10]:
    job_title = job.find('a', {'class': 'title'}).text.strip()
    job_location = job.find('li', {'class': 'fleft grey-text br2 placeHolderLi location'}).text.strip()
    company_name = job.find('a', {'class': 'subTitle ellipsis fleft'}).text.strip()
    jobs_data.append({'Job Title': job_title, 'Job Location': job_location, 'Company Name': company_name})

# Create a pandas dataframe from the scraped data
df = pd.DataFrame(jobs_data)

# Display the dataframe
print(df)


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/"
search_term = "sunglasses"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, 'html.parser')

# Find the search field and enter the search term
search_field = soup.find('input', {'class': '_3704LK'})
search_field['value'] = search_term

# Find and click the search button
search_button = soup.find('button', {'class': '_2KpZ6l _2doB4z'})
search_button.click()

# Scrape the data for the first 100 sunglasses listings
sunglasses_data = []
while len(sunglasses_data) < 100:
    # Find all the sunglasses listings
    sunglasses_listings = soup.find_all('div', {'class': '_2kHMtA'})

    # Scrape the data for each sunglasses listing
    for sunglasses in sunglasses_listings:
        brand = sunglasses.find('div', {'class': '_2WkVRV'}).text.strip()
        product_description = sunglasses.find('a', {'class': '_2mylT6'}).text.strip()
        price = sunglasses.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()
        sunglasses_data.append({'Brand': brand, 'Product Description': product_description, 'Price': price})

        # Break out of the loop if we have scraped 100 sunglasses listings
        if len(sunglasses_data) == 100:
            break

    # Find the next page button and click it
    next_button = soup.find('a', {'class': '_1LKTO3'})
    if next_button:
        response = requests.get(next_button['href'])
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        break

# Create a pandas dataframe from the scraped data
df = pd.DataFrame(sunglasses_data)

# Display the dataframe
print(df)


# In[4]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set the webdriver path and options
driver_path = 'path/to/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # To run the code in headless mode

# Create a new webdriver instance
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Open the naukri.com webpage
url = 'https://www.naukri.com/'
driver.get(url)

# Find the search field and enter the search term
search_field = driver.find_element_by_xpath('//input[@class="sugInp"]')
search_field.send_keys('Data Scientist')

# Click the search button
search_button = driver.find_element_by_xpath('//button[@class="btn"]')
search_button.click()

# Apply the location filter
location_filter = driver.find_element_by_xpath('//label[@for="chk-Delhi/NCR-cityType-"]/i')
location_filter.click()

# Apply the salary filter
salary_filter = driver.find_element_by_xpath('//label[@for="chk-3-6 Lakhs-ctcFilter-"]/i')
salary_filter.click()

# Get the HTML content of the page
html = driver.page_source

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Scrape the data for the first 10 job results
job_data = []
job_listings = soup.find_all('article', {'class': 'jobTuple bgWhite br4 mb-8'})
for job in job_listings[:10]:
    job_title = job.find('a', {'class': 'title fw500 ellipsis'}).text.strip()
    job_location = job.find('li', {'class': 'fleft grey-text br2 placeHolderLi location'}).text.strip()
    company_name = job.find('a', {'class': 'subTitle ellipsis fleft'}).text.strip()
    experience_required = job.find('li', {'class': 'fleft grey-text br2 placeHolderLi experience'}).text.strip()
    job_data.append({'Job Title': job_title, 'Job Location': job_location, 'Company Name': company_name, 'Experience Required': experience_required})

# Create a pandas dataframe from the scraped data
df = pd.DataFrame(job_data)

# Display the dataframe
print(df)

# Quit the webdriver instance
driver.quit()


# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the Flipkart website
url = "https://www.flipkart.com/"

# Search term
search_term = "sneakers"

# Create a dictionary for the search parameters
params = {
    "q": search_term,
    "otracker": "search",
    "otracker1": "search",
    "marketplace": "FLIPKART",
    "as-show": "on",
    "sort": "",
}

# Send a request to the website and get the response
response = requests.get(url, params=params)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the product containers on the page
product_containers = soup.find_all("div", {"class": "_2kHMtA"})

# Create empty lists to store the scraped data
brands = []
descriptions = []
prices = []

# Loop through each product container and extract the data
for product in product_containers:
    # Find the brand name
    brand = product.find("div", {"class": "_2WkVRV"}).text.strip()
    brands.append(brand)

    # Find the product description
    description = product.find("a", {"class": "_2mylT6"}).text.strip()
    descriptions.append(description)

    # Find the product price
    price = product.find("div", {"class": "_30jeq3 _1_WHN1"}).text.strip()
    prices.append(price)

    # Break the loop when we have scraped data for 100 sneakers
    if len(brands) >= 100:
        break

# Create a pandas dataframe with the scraped data
sneakers_df = pd.DataFrame(
    {
        "Brand": brands,
        "Product Description": descriptions,
        "Price": prices,
    }
)

# Print the dataframe
print(sneakers_df.head())


# In[6]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the Amazon website
url = "https://www.amazon.in/"

# Search term
search_term = "Laptop"

# Create a dictionary for the search parameters
params = {
    "k": search_term,
}

# Send a request to the website and get the response
response = requests.get(url, params=params)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the filter for CPU Type and select "Intel Core i7"
cpu_filter = soup.find("ul", {"aria-label": "Processor Type"}).find_all("li")
for cpu in cpu_filter:
    if "Intel Core i7" in cpu.text:
        cpu.find("input").click()
        break

# Send another request to the website with the selected filter
response = requests.get(url, params=params)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the product containers on the page
product_containers = soup.find_all("div", {"class": "s-include-content-margin s-border-bottom s-latency-cf-section"})

# Create empty lists to store the scraped data
titles = []
ratings = []
prices = []

# Loop through each product container and extract the data
for product in product_containers:
    # Find the product title
    title = product.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).text.strip()
    titles.append(title)

    # Find the product rating
    rating = product.find("span", {"class": "a-icon-alt"}).text.split()[0]
    ratings.append(rating)

    # Find the product price
    price = product.find("span", {"class": "a-price-whole"}).text
    prices.append(price)

    # Break the loop when we have scraped data for 10 laptops
    if len(titles) >= 10:
        break

# Create a pandas dataframe with the scraped data
laptops_df = pd.DataFrame(
    {
        "Title": titles,
        "Ratings": ratings,
        "Price": prices,
    }
)

# Print the dataframe
print(laptops_df.head())


# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the URL and headers
url = 'https://www.amazon.in/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Set the search keyword and filters
search_term = 'laptop'
filters = {'rh': 'n:976392031,p_n_feature_four_browse-bin:1485945031,p_n_feature_thirteen_browse-bin:12598161031,p_n_feature_five_browse-bin:1389401031,p_n_operating_system_browse-bin:14850604031,p_n_feature_fifteen_browse-bin:12598162031|12598163031|12598164031,p_n_condition-type:8609960031,p_n_feature_two_browse-bin:1485947031,p_n_feature_eleven_browse-bin:12598160031,p_n_feature_twelve_browse-bin:12598161031,p_n_feature_fourteen_browse-bin:12598162031|12598163031|12598164031,p_n_feature_two_browse-bin:12598151031,p_n_feature_browse-bin:1485945031'}

# Send a GET request with the search term and filters
response = requests.get(url, headers=headers, params={'k': search_term, **filters})

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the first 10 laptop containers with Intel Core i7 processors
laptops = soup.find_all('div', {'data-component-type': 's-search-result'})

# Initialize empty lists to store the laptop details
titles = []
ratings = []
prices = []

# Loop through the laptop containers and scrape the required details
for laptop in laptops[:10]:
    title = laptop.find('h2').text.strip()
    rating = laptop.find('span', {'class': 'a-icon-alt'})
    if rating:
        rating = rating.text.split()[0]
    else:
        rating = 'N/A'
    price = laptop.find('span', {'class': 'a-price-whole'})
    if price:
        price = price.text.replace(',', '')
    else:
        price = 'N/A'
    titles.append(title)
    ratings.append(rating)
    prices.append(price)

# Create a Pandas DataFrame with the scraped data
df = pd.DataFrame({'Title': titles, 'Rating': ratings, 'Price (INR)': prices})

# Print the DataFrame
print(df)


# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the Jagran Josh website and get its HTML content
url = 'https://www.jagranjosh.com/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Click on the "GK" option and then click on "List of all Prime Ministers of India"
gk_url = soup.find('a', text='GK')['href']
response = requests.get(gk_url)
soup = BeautifulSoup(response.content, 'html.parser')
pm_url = soup.find('a', text='List of all Prime Ministers of India')['href']

# Scrape the data from the Prime Ministers page
response = requests.get(pm_url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'table4'})

data = []
for row in table.findAll('tr')[1:]:
    name = row.find('td').text.strip()
    born_dead = row.findAll('td')[1].text.strip()
    term = row.findAll('td')[2].text.strip()
    remarks = row.findAll('td')[3].text.strip()
    data.append({'Name': name, 'Born-Dead': born_dead, 'Term of office': term, 'Remarks': remarks})

# Create a Pandas DataFrame from the scraped data
df = pd.DataFrame(data)
print(df)


# In[9]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.motor1.com/features/433597/most-expensive-cars-sold-2021/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

cars = []

table = soup.find('table', {'class': 'table table-responsive table-striped table-bordered'})

for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    car_name = cells[0].text.strip()
    car_price = cells[1].text.strip()
    cars.append([car_name, car_price])

df = pd.DataFrame(cars, columns=['Car Name', 'Price'])

print(df)


# In[ ]:




