from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

from git import Repo, GitCommandError


class Scraper:
    def __init__(self, rdpHost, rdpPort, localDir):
        # Initialize the WebDriver with the existing Chrome instance
        self.driver = webdriver.Chrome(
            # Set up ChromeOptions and connect to the existing Chrome rdp
            options=Options().add_experimental_option(
                "debuggerAddress", f'{rdpHost}:{rdpPort}'
            )
        )

        self.localDir = localDir

    def openUrl(url):
        self.driver.get(url)
        time.sleep(3)

        html = self.driver.page_source
        page = BeautifulSoup(html, "html.parser")

        return page

    def play(assignmentUrl, repoPrefix):
        page = openUrl(assignmentUrl)

        # init paths to temp store cloned repo directories
        paths = []

        # find username elements
        usernameElements = page.find_all("div", {"class": "pb-1"})
        for element in usernameElements:
            # extract username
            username = element.find("span").get_text().strip()

            # generate repo url
            url = f"{repoPrefix}-{username}.git"

            # clone repo
            try:
                Repo.clone_from(url, f"{self.localDir}/{username}")
            except GitCommandError as e:
                raise GitCommandError(e)

            # open repo page
            repoPage = openUrl(assignmentUrl)

            # find file elements
            files = repoPage.find("table").find_all(
                "td", {"class": "react-directory-row-name-cell-large-screen"}
            )

            for file in files:
                # extract file name
                fileName = file.get_text()

                # select only .ipynb and .py file
                if ".ipynb" in fileName or ".py" in fileName:
                    # store file path
                    paths.append(f"{sourceDir}/{username}/{fileName}")
                    continue

        # close driver
        driver.quit()

        return paths
