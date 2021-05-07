from pages.base import WebPage
from pages.elements import WebElement


class TopMenuMixin(WebPage):
    track_order = WebElement(css_selector="ul.top-menu li.track")
    pay_order = WebElement(css_selector="ul.top-menu li.payorder")


class MiddleMenuMixin(WebPage):
    search = WebElement(id='search-input')
    search_button = WebElement(css_selector=".search-form .search-form__btn")


class ModalMixin(WebPage):
    track_order_dialog = WebElement(css_selector="#modal-track div.modal-content")
    track_order_input = WebElement(css_selector="#modal-track input")
    track_order_search = WebElement(css_selector="#modal-track form button")
    track_order_result = WebElement(css_selector="#modal-track .trackdelivery__report")
