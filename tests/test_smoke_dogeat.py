import pytest

from pages.dogeat import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)
    search_text = 'Royal Canin'

    page.search = search_text
    page.quick_search_results.wait_until_visible()
    page.search_button.click()
    page.wait_page_loaded()

    assert page.search_item_titles.count() == 24

    wrong_titles = []

    for product_name in page.search_item_titles.get_text():
        if search_text.lower() not in product_name.lower():
            wrong_titles.append(product_name)

    assert not wrong_titles, f"Wrong {len(wrong_titles)} product(s) found!"


@pytest.mark.parametrize(
    "track_number, expected_result", [
        pytest.param('1234567890', "Не удалось получить данные статуса отправления.", id="Invalid track"),
        pytest.param('1234567891', "Заказ в пути!", id="Valid track"),
    ]
)
def test_track_order(web_browser, track_number, expected_result):
    """ Make sure track order works as expected """
    page = MainPage(web_browser)

    page.track_order.click()
    page.track_order_dialog.wait_until_visible()
    page.track_order_input = track_number
    page.track_order_search.click()

    assert expected_result == page.track_order_result.wait_until_any_text_present(), "Incorrect track order result"
