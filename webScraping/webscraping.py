# Import the requests module and the BeautifulSoup class from the bs4 module
import requests
from bs4 import BeautifulSoup

# Define the URL of the web page to scrape
url = 'https://realpython.github.io/fake-jobs/'

# Use the requests module to get the HTML content of the web page
html = requests.get(url)

# Uncomment the following line to print the HTML content to the console
# print(html.text)

# Create a BeautifulSoup object from the HTML content
s = BeautifulSoup(html.content, 'html.parser')

# Find the element on the web page with the ID "ResultsContainer"
results = s.find(id="ResultsContainer")

# Find all the elements on the web page with the tag <h2> and class "title is-5"
job_title = results.find_all("h2", class_="title is-5")

# Uncomment the following line to print the text of the first job title to the console
# print(job_title[0].text)

# Loop through each job title and print its text to the console
for job in job_title:
    print(job.text)
