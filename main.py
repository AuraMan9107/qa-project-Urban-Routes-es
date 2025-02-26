import data
import utils
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from UrbanRoutesPage import UrbanRoutesPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_phone_number_field()
        routes_page.enter_phone_number(data.phone_number)

    def test_fill_sms_code(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_next_button()
        sms_code = utils.retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(sms_code)

    def test_fill_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_payment_button()
        routes_page.set_card_number()
        routes_page.set_card_code_number()
        routes_page.click_on_add_card_button()



        #para los assert tengo que encontrar como se debe ver la tarjeta cuando ya se agrego una tarjeta.
    """
    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.driver.find_element(*routes_page.message_for_driver_field).send_keys(data.message_for_driver)

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.driver.find_element(*routes_page.requirements_button).click()
        routes_page.driver.find_element(*routes_page.blankets_and_handkerchief_slider).click()

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.driver.find_element(*routes_page.add_icecream).click()
        routes_page.driver.find_element(*routes_page.add_icecream).click()  # Segundo clic para pedir 2 helados

    def test_car_search_model_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.driver.find_element(*routes_page.waiting_order_screen_title).is_displayed()

    def test_driver_info_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        trip_number = routes_page.confirm_trip()
        assert trip_number is not None and trip_number.strip() != "", "No se generó el número de viaje."
        
    """

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

