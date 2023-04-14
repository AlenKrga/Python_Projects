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

job_link = results.find_all("a", class_="card-footer-item")
# Uncomment the following line to print the text of the first job title to the console
#print(job_title[0].text)

# Loop through each job title and print its text to the console
#for job in job_title:
 #   print(job.text)

#Here, the zip function combines the job_link and job_title lists into a single iterator, so that the for loop will iterate over both lists in parallel. Inside the loop, we can access both the link object and the job object at the same time, and print the link href attribute and the job title text.
for link, job in zip(job_link, job_title):
    print(link.get('href'))
    print("\033[32m" + job.text + "\033[0m")


    

