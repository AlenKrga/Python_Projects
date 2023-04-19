# Import the save_webpage function from the pywebcopy library
from pywebcopy import save_webpage

# Set the URL of the webpage to download
url = 'http://some-site.com/some-page.html'

# Set the download folder where the webpage will be saved
download_folder = '/path/to/downloads/'

# Define the keyword arguments to pass to the save_webpage function
kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}

# Call the save_webpage function with the URL, download folder, and keyword arguments
save_webpage(url, download_folder, **kwargs)


#https://stackoverflow.com/questions/31205497/how-to-download-a-full-webpage-with-a-python-script