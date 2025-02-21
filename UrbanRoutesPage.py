from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    call_a_taxi_button = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    comfort_rate_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    selected_tariff = (By.XPATH, "//div[@class='tariff-picker shown']//div[@class='tariff-cards']//div[@class='tcard active']//div[@class='tcard-title']")

    phone_number_field = (By.CLASS_NAME, "np-text")
    phone_number_field_popup = (By.ID, "phone")
    next_button = (By.CLASS_NAME, "button full")
    sms_code_field = (By.ID,"code")
    confirm_phone_button = (By.XPATH, "//div[@class='section active']//form//div[@class='buttons']//button[@type='submit']")

    payment_method_button = (By.CLASS_NAME, ".pp-button")
    add_card_button = (By.CSS_SELECTOR, ".pp-plus-container")
    card_number_field = (By.ID, "number")
    cvv_field = (By.NAME, "code")
    confirm_credit_card = (By.XPATH, "//div[@class='pp-buttons']//button[@type='submit']")
    close_button_popup = (By.XPATH,
        "//div[@class='payment-picker open']//div[@class='modal']//div[@class='section active']//button[@class='close-button section-close']")

    message_for_driver_field = (By.ID, "comment")
    requirements_button = (By.CLASS_NAME, "reqs-head")
    blankets_and_handkerchief_slider = (By.XPATH, "//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']")
    add_icecream = (By.XPATH,  "//div[contains(text(),'Helado')]/..//div[@class='counter-plus']")
    order_wait_screen = (By.XPATH, "//div[@class='order shown']")
    order_wait_screen_title = (By.XPATH, "//div[@class='order shown']//div[@class='order-body']//div[@class='order-header']//div[@class='order-header-title']")
    trip_confirmation = (By.XPATH, "//div[@class='order shown']//div[@class='order-body']//div[@class='order-header']//div[@class='order-number']")
    book_cab_button = (By.CLASS_NAME, 'smart-button-main')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(
           EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_call_a_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.call_a_taxi_button))

    def click_on_call_a_taxi_button(self):
        self.get_call_a_taxi_button().click()


    def get_comfort_rate_icon(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_rate_icon))

    def click_on_comfort_rate_icon(self):
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.comfort_rate_icon)
            ).click()

    def get_phone_number_field(self):
            WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.phone_number_field)
        ).click()

    def enter_phone_number(self, phone_number):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.phone_number_field_popup)
            ).send_keys(phone_number)

    def click_on_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def enter_sms_code(self, code):
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.sms_code_field)
            ).send_keys(code)
            self.driver.find_element(*self.confirm_phone_button).click()

    def add_credit_card(self, card_number, cvv):
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.payment_method_button)
            ).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.add_card_button)
            ).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.card_number_field)
            ).send_keys(card_number)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.cvv_field)
            ).send_keys(cvv)
            self.driver.find_element(*self.confirm_credit_card).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.close_button_popup)
            ).click()

    def confirm_trip(self):
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.book_cab_button)
            ).click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.order_wait_screen)
            )
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.trip_confirmation)
            ).text


