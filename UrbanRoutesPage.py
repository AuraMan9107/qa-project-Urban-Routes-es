from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
from selenium.webdriver import Keys



class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    call_a_taxi_button = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    comfort_rate_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")

    phone_number_field = (By.CLASS_NAME, "np-text")
    phone_number_field_popup = (By.ID, "phone")
    next_button = (By.XPATH, "//button[contains(text(), 'Siguiente')]")
    sms_code_field = (By.ID,"code")
    confirm_phone_button = (By.XPATH, "//button[text()='Confirmar']")

    payment_method_button = (By.CSS_SELECTOR, "div.pp-button.filled")
    add_card_button = (By.CSS_SELECTOR, "div.pp-row.disabled")
    card_number_field = (By.ID, "number")
    cvv_field = (By.NAME, "code")
    add_credit_card_button = (By.CSS_SELECTOR, "button.button.full")
    close_button_popup = (By.XPATH, "//div[contains(@class, 'payment-picker') and contains(@class, 'open')]//div[@class='modal']//div[contains(@class, 'section') and contains(@class, 'active')]//button")

    message_for_driver_field = (By.ID, "comment")
    requirements_button = (By.CLASS_NAME, "reqs-head")
    blankets_and_handkerchief_slider = (By.XPATH, "//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']")
    add_icecream = (By.XPATH,  "//div[contains(text(),'Helado')]/..//div[@class='counter-plus']")

    waiting_order_screen = (By.XPATH, "//div[@class='order shown']")
    waiting_order_screen_title = (By.XPATH, "//div[@class='order shown']//div[@class='order-body']//div[@class='order-header']//div[@class='order-header-title']")
    trip_confirmation = (By.XPATH, "//div[@class='order shown']//div[@class='order-body']//div[@class='order-header']//div[@class='order-number']")
    order_a_taxi_button = (By.CLASS_NAME, 'smart-button-main')

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

    def get_payment_button(self):
        return WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.payment_method_button)
            )

    def click_on_payment_button(self):
        self.get_payment_button().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.add_card_button)
        )

    def click_on_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_number_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.card_number_field)
        )

    def set_card_number(self):
        self.get_card_number_field().send_keys(data.card_number)

    def get_card_code_number(self):
        return WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.cvv_field)
        )
    def set_card_code_number(self):
        self.get_card_code_number().send_keys(data.card_code)

    def get_add_credit_card_button(self):
        return WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.add_credit_card_button)
        )
    def click_on_add_credit_card_button(self):
        self.get_card_code_number().send_keys(Keys.TAB)
        self.get_add_credit_card_button().click()






