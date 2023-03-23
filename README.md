# Job Listings Scraper

This is a Python script that scrapes job listings from a website and saves them to a JSON file. It uses the Requests library to send HTTP requests to the website and the BeautifulSoup library to parse the HTML content.

## Installation

To use this script, you need to have Python 3.x installed on your system. You can download the latest version of Python from the official website: "https://www.python.org/downloads/"

You also need to install the Requests and BeautifulSoup libraries. You can install them using pip, the Python package manager, by running the following command in your terminal:

```bash
pip install requests beautifulsoup4
```

## Usage

```python
To run the script, open your terminal and navigate to the directory where the jobscraper.py file is located. Then run the following command:
```
This will start the scraping process and save the job listings to a jobs.json file in the same directory.

You can customize the website URL and the number of pages to scrape by editing the url and range variables in the jobscraper.py file.

## Automating with Github Actions
To automate the scraping process and run the script daily, you can use Github Actions. A sample workflow file is included in the '.github/workflows' directory that runs the script at 9am and 6pm IST every day and pushes the changes to the repository.

To use this workflow, you need to configure the python workflow from the actions sections in the repository tabs. 

## Contributing
Contributions are welcome! If you find any bugs or issues with the script, please open a Github issue or submit a pull request.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.
