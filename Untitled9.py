#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send a GET request to the Wikipedia homepage and get the response
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# Find all header tags (h1 to h6) in the parsed HTML content
header_tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

# Create a list to store the text content of each header tag
header_text = []

# Iterate over each header tag and append its text content to the list
for tag in header_tags:
    header_text.append(tag.get_text())

# Create a Pandas DataFrame from the header_text list
df = pd.DataFrame({"Header Tags": header_text})

# Display the DataFrame
print(df)


# In[2]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send a GET request to the IMDB Top Rated Movies page and get the response
url = "https://www.imdb.com/chart/top"
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# Find all the movie tags in the parsed HTML content
movie_tags = soup.find_all("td", class_="titleColumn")

# Create empty lists to store the data for each movie
names = []
ratings = []
years = []

# Iterate over each movie tag and extract its name, rating, and year of release
for tag in movie_tags[:50]: # top 50 movies
    # Extract the name of the movie
    name = tag.find("a").get_text()
    names.append(name)
    
    # Extract the year of release of the movie
    year = tag.find("span", class_="secondaryInfo").get_text()
    year = year.strip("()") # Remove the parentheses from the year
    years.append(year)
    
    # Extract the rating of the movie
    rating = tag.find_next_sibling("td", class_="ratingColumn").get_text().strip()
    ratings.append(rating)

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame({"Name": names, "Rating": ratings, "Year of Release": years})

# Display the DataFrame
print(df)


# In[3]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send a GET request to the IMDB Top Rated Indian Movies page and get the response
url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# Find all the movie tags in the parsed HTML content
movie_tags = soup.find_all("td", class_="titleColumn")

# Create empty lists to store the data for each movie
names = []
ratings = []
years = []

# Iterate over each movie tag and extract its name, rating, and year of release
for tag in movie_tags[:50]: # top 50 Indian movies
    # Extract the name of the movie
    name = tag.find("a").get_text()
    names.append(name)
    
    # Extract the year of release of the movie
    year = tag.find("span", class_="secondaryInfo").get_text()
    year = year.strip("()") # Remove the parentheses from the year
    years.append(year)
    
    # Extract the rating of the movie
    rating = tag.find_next_sibling("td", class_="ratingColumn").get_text().strip()
    ratings.append(rating)

# Create a Pandas DataFrame from the extracted data
df = pd.DataFrame({"Name": names, "Rating": ratings, "Year of Release": years})

# Display the DataFrame
print(df)


# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the HTML content of the webpage
url = 'https://presidentofindia.nic.in/former-presidents.htm'
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table containing the list of former presidents
table = soup.find('table', {'class': 'tablepress'})

# Find all the rows in the table
rows = table.find_all('tr')

# Extract the data from the rows
presidents = []
for row in rows[1:]:
    # Extract president's name
    name = row.find('td', {'class': 'column-1'}).text.strip()

    # Extract president's term of office
    term = row.find('td', {'class': 'column-2'}).text.strip()

    # Append the president's data to the list of presidents
    presidents.append((name, term))

# Create a data frame from the president data
df = pd.DataFrame(presidents, columns=['Name', 'Term of Office'])

# Print the data frame
print(df)


# In[10]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# function to scrape data from url and return a BeautifulSoup object
def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# scrape top 10 ODI teams data and create a data frame
url_teams = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
soup_teams = get_soup(url_teams)
teams_table = soup_teams.find('table', class_='table')
teams_rows = teams_table.tbody.find_all('tr')
teams_data = []
for row in teams_rows[:10]:
    team = row.find('span', class_='u-hide-phablet').text.strip()
    matches = row.find_all('td')[2].text.strip()
    points = row.find_all('td')[3].text.strip()
    rating = row.find_all('td')[4].text.strip()
    teams_data.append([team, matches, points, rating])
teams_df = pd.DataFrame(teams_data, columns=['Team', 'Matches', 'Points', 'Rating'])

# scrape top 10 ODI batsmen data and create a data frame
url_batsmen = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'
soup_batsmen = get_soup(url_batsmen)
batsmen_table = soup_batsmen.find('table', class_='table')
batsmen_rows = batsmen_table.tbody.find_all('tr')
batsmen_data = []
for row in batsmen_rows[:10]:
    batsman = row.find('td', class_='table-body__cell name').a.text.strip()
    team = row.find('span', class_='table-body__logo-text').text.strip()
    rating = row.find('td', class_='table-body__cell u-text-right rating').text.strip()
    batsmen_data.append([batsman, team, rating])
batsmen_df = pd.DataFrame(batsmen_data, columns=['Batsman', 'Team', 'Rating'])

# scrape top 10 ODI bowlers data and create a data frame
url_bowlers = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'
soup_bowlers = get_soup(url_bowlers)
bowlers_table = soup_bowlers.find('table', class_='table')
bowlers_rows = bowlers_table.tbody.find_all('tr')
bowlers_data = []
for row in bowlers_rows[:10]:
    bowler = row.find('td', class_='table-body__cell name').a.text.strip()
    team = row.find('span', class_='table-body__logo-text').text.strip()
    rating = row.find('td', class_='table-body__cell u-text-right rating').text.strip()
    bowlers_data.append([bowler, team, rating])
bowlers_df = pd.DataFrame(bowlers_data, columns=['Bowler', 'Team', 'Rating'])

# print the data frames
print('Top 10 ODI teams:')
print(teams_df.to_string(index=False))
print('\nTop 10 ODI batsmen:')
print(batsmen_df.to_string(index=False))
print('\nTop 10 ODI bowlers:')
print(bowlers_df.to_string(index=False))


# In[13]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# function to scrape data from url and return a BeautifulSoup object
def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# scrape top 10 ODI women's teams data and create a data frame
url_women_teams = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
soup_women_teams = get_soup(url_women_teams)
women_teams_table = soup_women_teams.find('table', class_='table')
women_teams_rows = women_teams_table.tbody.find_all('tr')
women_teams_data = []
for row in women_teams_rows[:10]:
   


# In[15]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# send a request to the webpage
url = 'https://www.cnbc.com/world/?region=world'
page = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# find all the news articles on the page
articles = soup.find_all('div', class_='Card-titleContainer')

# create empty lists to store the data
headlines = []
times = []
news_links = []

# loop through each article and extract the data
for article in articles:
    # extract the headline
    headline = article.find('a', class_='Card-title').text
    headlines.append(headline)

    # extract the time
    time = article.find('time')['datetime']
    times.append(time)

    # extract the news link
    news_link = article.find('a', class_='Card-title')['href']
    news_links.append(news_link)

# create a DataFrame from the data
df = pd.DataFrame({
    'Headline': headlines,
    'Time': times,
    'News Link': news_links
})

# display the DataFrame
print(df)


# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# send a request to the webpage
url = 'https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles'
page = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# find all the articles on the page
articles = soup.find_all('div', class_='pod-listing')

# create empty lists to store the data
paper_titles = []
authors = []
published_dates = []
paper_urls = []

# loop through each article and extract the data
for article in articles:
    # extract the paper title
    paper_title = article.find('a', class_='pod-listing-header__link').text
    paper_titles.append(paper_title)

    # extract the authors
    author_list = article.find('ul', class_='pod-listing-authors')
    author_list_items = author_list.find_all('li')
    author_names = []
    for item in author_list_items:
        author_name = item.find('a').text
        author_names.append(author_name)
    authors.append(", ".join(author_names))

    # extract the published date
    published_date = article.find('div', class_='pod-listing-info__details').find_all('span')[1].text
    published_dates.append(published_date)

    # extract the paper URL
    paper_url = article.find('a', class_='pod-listing-header__link')['href']
    paper_urls.append(paper_url)

# create a DataFrame from the data
df = pd.DataFrame({
    'Paper Title': paper_titles,
    'Authors': authors,
    'Published Date': published_dates,
    'Paper URL': paper_urls
})

# display the DataFrame
print(df)


# In[17]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# send a request to the webpage
url = 'https://www.dineout.co.in/delhi-restaurants'
page = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# find all the restaurants on the page
restaurants = soup.find_all('div', class_='restnt-info cursor')

# create empty lists to store the data
restaurant_names = []
cuisines = []
locations = []
ratings = []
image_urls = []

# loop through each restaurant and extract the data
for restaurant in restaurants:
    # extract the restaurant name
    restaurant_name = restaurant.find('div', class_='restnt-name ellipsis').text.strip()
    restaurant_names.append(restaurant_name)

    # extract the cuisine
    cuisine = restaurant.find('div', class_='restnt-desc ellipsis').text.strip()
    cuisines.append(cuisine)

    # extract the location
    location = restaurant.find('div', class_='restnt-loc ellipsis').text.strip()
    locations.append(location)

    # extract the rating
    rating = restaurant.find('div', class_='restnt-rating rating-stars').text.strip()
    ratings.append(rating)

    # extract the image URL
    image_url = restaurant.find('div', class_='restnt-img img-with-border')['style']
    image_url = image_url.replace("background-image: url('", "")
    image_url = image_url.replace("')", "")
    image_urls.append(image_url)

# create a DataFrame from the data
df = pd.DataFrame({
    'Restaurant Name': restaurant_names,
    'Cuisine': cuisines,
    'Location': locations,
    'Ratings': ratings,
    'Image URL': image_urls
})

# display the DataFrame
print(df)


# In[ ]:




