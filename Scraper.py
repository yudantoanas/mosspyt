from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

from git import Repo, GitCommandError


def scraper(rdpPort, assignmentUrl, repoUrl):
    # Set up ChromeOptions and connect to the existing browser
    c_options = Options()
    c_options.add_experimental_option("debuggerAddress", f'localhost:{rdpPort}')

    # Initialize the WebDriver with the existing Chrome instance
    driver = webdriver.Chrome(options=c_options)

    # Now, you can interact with the already opened Chrome browser
    driver.get(assignmentUrl)
    html = driver.page_source
    page = BeautifulSoup(html, "html.parser")

    # Init temp storage
    paths = []

    # Find github usernames
    usernameElements = page.find_all("div", {"class": "pb-1"})

    for usernameElement in usernameElements:
        # scrape user name
        username = usernameElement.find("span").get_text().strip()

        # generate repo url
        url = f"{repoUrl}-{username}"

        # clone repo using GitPython
        try:
            Repo.clone_from(url + ".git", f"./sources/{username}")
        except GitCommandError as e:
            print(e)

        # open repo page
        driver.get(url)
        time.sleep(1)

        # scrape each repo page
        html = driver.page_source
        page = BeautifulSoup(html, "html.parser")

        # scrape file name
        tableElement = page.find("table")
        fileElements = tableElement.find_all(
            "td", {"class": "react-directory-row-name-cell-large-screen"}
        )

        # loop through file list and select only .ipynb file
        for fileElement in fileElements:
            file = fileElement.get_text()
            if ".ipynb" in file or ".py" in file:
                # store file path
                paths.append(f"sources/{username}/{file}")
                continue

    # close driver
    driver.quit()

    return paths
