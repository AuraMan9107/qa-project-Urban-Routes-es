import data
import utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from UrbanRoutesPage import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono

        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_call_a_taxi_button()
        routes_page.click_on_comfort_rate_icon()
        assert routes_page.is_comfort_selected()

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_phone_number_field()
        routes_page.enter_phone_number(data.phone_number)
        assert routes_page.is_correct_phone_number_popup().get_attribute("value") == data.phone_number

    def test_fill_sms_code(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_next_button()
        sms_code = utils.retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(sms_code)


    def test_fill_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_payment_button()
        routes_page.click_on_add_card_button()
        routes_page.set_card_number()
        routes_page.set_card_code_number()
        routes_page.click_on_add_credit_card_button()
        routes_page.click_on_close_button()
        assert routes_page.card_is_added()

    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_for_driver()
        assert routes_page.get_message_for_driver_field().get_attribute("value")== data.message_for_driver

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_blankets_and_handkerchief_slider()
        assert routes_page.is_blankets_and_handkerchief_selected()

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_ice_cream_option()
        routes_page.click_on_ice_cream_option() #Segundo click para pedir dos helados
        assert routes_page.two_ice_cream_added()

    def test_car_search_model_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_request_a_taxi_button()
        routes_page.get_waiting_order_screen()
        routes_page.get_order_number()
        assert routes_page.get_order_number()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

