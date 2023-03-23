import requests
import json
from bs4 import BeautifulSoup

url = "https://frontlinesmedia.in/category/job-notifications/"
jobs = {}  # create an empty dictionary to store job titles and links

try:
    for page in range(1, 4):  # scrape first 3 pages
        page_url = url + f"page/{page}/"
        response = requests.get(page_url)  # send a GET request to the page URL

        # Check if the response is OK (status code 200)
        if response.status_code != 200:
            raise Exception(f"Failed to get page {page_url}. Status code: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")  # parse the HTML content using BeautifulSoup
        job_posts = soup.find_all('h3', class_='entry-title td-module-title')  # find all job post titles
        for post in job_posts:
            job_title = post.find('a').text  # extract the job title from the anchor tag
            job_link = post.find('a')['href']  # extract the job link from the anchor tag
            jobs[job_title] = job_link  # add the job title and link to the dictionary

    with open('output.json', 'w') as f:
        json.dump(jobs, f)  # save the dictionary to a JSON file

except Exception as e:
    print(f"Error: {e}")
    
# End of the code
