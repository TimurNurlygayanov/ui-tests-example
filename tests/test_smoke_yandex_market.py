#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#

import pytest
from pages.yandex import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 48

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'iphone' in title.lower(), msg


def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # Try to enter "смартфон" with English keyboard:
    page.search = 'cvfhnajy'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 48

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'смартфон' in title.lower(), msg


@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine.

        Note: this test case will fail because there is a bug in
              sorting products by price.
    """

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()

    # Convert all prices from strings to numbers
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    print(all_prices)
    print(sorted(all_prices))

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"
