"""
frq_term_search.py

easy term searching in college board frqs
usefulish for matching scoring guides with specific units to prepare.

By Andrew Segerlind
"""


import selenium
import selenium.webdriver
import selenium.webdriver.chrome
import toml


def main():
    config = read_config_toml()

    driver = selenium.webdriver.chrome()
    