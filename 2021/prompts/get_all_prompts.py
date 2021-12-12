#!/usr/bin/env python

"""
Download all the prompts from Advent of Code. Use responsibly
"""

import bs4
from bs4 import BeautifulSoup
import click
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass
import os


@click.command()
@click.option('--output-dir', type=click.Path(), required=True)
@click.option('--driver-path', type=click.Path(), default='/usr/local/bin/chromedriver')
def download_prompts(output_dir, driver_path):

    driver = webdriver.Chrome(service=Service(driver_path))

    # login
    driver.get('https://adventofcode.com')
    driver.find_element(By.LINK_TEXT, "[Log In]").click()
    driver.find_element(By.LINK_TEXT, "[GitHub]").click()

    # github login
    user_name_input = driver.find_element(By.CSS_SELECTOR, 'input[name=login]')
    user_name = input('GitHub username: ')
    user_name_input.send_keys(user_name)
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[name=password]')
    password = getpass.getpass()
    password_input.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'input[name=commit]').click()

    # get all links
    driver.get('https://adventofcode.com')
    days_links = []
    elms = driver.find_elements(By.CSS_SELECTOR, 'pre.calendar>a')
    for elm in elms:
        days_links.append(elm.get_property('href'))

    # go through and download links
    for link in days_links:
        driver.get(link)
        day = driver.current_url.split('/')[-1]
        soup = BeautifulSoup(driver.page_source, "html.parser")
        first_article = soup.find('article')
        html = str(first_article)
        for x in first_article.next_siblings:
            if type(x) == bs4.element.NavigableString:
                continue
            if 'day-success' in x.get_attribute_list('class'):
                break
            html += str(x)
        output_file = os.path.join(output_dir, f'day_{day}_prompt.html')
        os.makedirs(output_dir, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(html)


if __name__ == '__main__':
    download_prompts()

