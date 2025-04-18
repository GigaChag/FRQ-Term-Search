"""
frq_term_search.py

easy term searching in college board frqs
usefulish for matching scoring guides with specific units to prepare.

By Andrew Segerlind
"""


import selenium
from selenium import webdriver
import toml


def main():
    config = read_config_toml()

    driver = webdriver.Chrome()

    loop_through_years(driver, config)


def read_config_toml():
    pass


def loop_through_years(driver: webdriver, config: list):
    """Iterates through a desired number of years of college board frqs and opens their acordian menus"""
    pass