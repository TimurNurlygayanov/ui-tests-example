from config import MAIN_URL
from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from pages.mixin import MiddleMenuMixin, TopMenuMixin, ModalMixin


class MainPage(MiddleMenuMixin, TopMenuMixin, ModalMixin, WebPage):
    def __init__(self, web_driver, url=MAIN_URL):
        super().__init__(web_driver, url)

    search_item_titles = ManyWebElements(css_selector='#goods div.product-item a.product-item__link')
    quick_search_results = WebElement(css_selector='.search-form .search-form__result_full')
