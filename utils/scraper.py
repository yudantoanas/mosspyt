import os
import pathlib

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from git import Repo, GitCommandError
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scrape(url, prefix):
    driver = webdriver.Chrome()
    driver.get(url)
    username = driver.find_element(By.ID, 'login_field')
    password = driver.find_element(By.ID, 'password')
    load_dotenv()
    username.send_keys(os.getenv("GH_USERNAME"))
    password.send_keys(os.getenv("GH_PASSWORD"))
    password.send_keys(Keys.ENTER)

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'assignment-repo-list-item'))
    )

    html = driver.page_source
    page = BeautifulSoup(html, "html.parser")

    # init paths to temp store clone repo directories
    data = {
        "paths": [],
        "fileNames": [],
    }

    # find username elements
    items = page.find_all("div", {"class": "assignment-repo-list-item"})
    for element in items:
        # extract username
        username = element.find("img")['alt'].replace('@', '')

        # generate repo url
        url = f"{prefix}-{username}.git"

        # clone repo
        try:
            Repo.clone_from(url, f"clone/{username}")
        except GitCommandError as e:
            print(e)
            continue

        # open repo page
        driver.get(url)
        html = driver.page_source
        repo_page = BeautifulSoup(html, "html.parser")

        # find file elements
        files = repo_page.find("table").find_all(
            "td", {"class": "react-directory-row-name-cell-large-screen"}
        )

        for file in files:
            # extract file name
            file_name = file.get_text()
            extension = pathlib.Path(file_name).suffix

            # select only .ipynb and .py file
            if extension == '.ipynb' or extension == '.py':
                # store file path
                data["paths"].append(f"{username}/{file_name}")
                data["fileNames"].append(file_name)

    # close driver
    driver.quit()

    return data
