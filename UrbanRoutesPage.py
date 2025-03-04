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
    selected_tariff = (By.XPATH, '//button[@data-for="tariff-card-4"]')

    phone_number_field = (By.CLASS_NAME, "np-text")
    phone_number_field_popup = (By.ID, "phone")
    next_button = (By.XPATH, "//button[text()='Siguiente']")
    sms_code_field = (By.ID,"code")
    confirm_phone_button = (By.XPATH, "//button[text()='Confirmar']")

    payment_method_button = (By.CSS_SELECTOR, "div.pp-button.filled")
    add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.ID, "number")
    cvv_field = (By.NAME, "code")
    add_credit_card_button = (By.XPATH, "//button[text()='Agregar']")
    close_button_popup = (By.XPATH, "//div[contains(@class, 'payment-picker') and contains(@class, 'open')]//div[@class='modal']//div[contains(@class, 'section') and contains(@class, 'active')]//button")
    added_card = (By.ID, "card-1")

    message_for_driver_field = (By.ID, "comment")

    blankets_and_handkerchief_option = (By.XPATH,  "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    blanket_and_handkerchief_checkbox = (By.XPATH,'//span[@class="slider round"]')

    add_icecream = (By.XPATH,  "//div[contains(text(),'Helado')]/..//div[@class='counter-plus']")
    ice_cream_count = (By.XPATH, "//div[@class='counter-value' and text()='2']")

    order_a_taxi_button = (By.CLASS_NAME, 'smart-button-main')
    waiting_order_screen = (By.XPATH, "//div[@class='order shown']")
    trip_confirmation = (By.XPATH, "//div[@class='order shown']//div[@class='order-body']//div[@class='order-header']//div[@class='order-number']")




    def __init__(self, driver):
        self.driver = driver

#Metodos para configurar una dirección

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

#Metodos para tocar el botón "pedir un taxi"

    def get_call_a_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.call_a_taxi_button))

    def click_on_call_a_taxi_button(self):
        self.get_call_a_taxi_button().click()

#Metodos para seleccionar la tarifa Comfort

    def get_comfort_rate_icon(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_rate_icon)
        )

    def click_on_comfort_rate_icon(self):
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.comfort_rate_icon)
            ).click()

    def is_comfort_selected(self):
        return WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(self.selected_tariff)
        )

#Metodos para llenar la tarjeta de número de teléfono

    def get_phone_number_field(self):
            WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.phone_number_field)
        ).click()

    def enter_phone_number(self, phone_number):
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.phone_number_field_popup)
            ).send_keys(phone_number)

    def is_correct_phone_number_popup(self):
        return WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.phone_number_field_popup)
        )

    def click_on_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def enter_sms_code(self, code):
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.sms_code_field)
            ).send_keys(code)
            self.driver.find_element(*self.confirm_phone_button).click()

      #Métodos para agregar una tarjeta de credito

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
        self.get_card_code_number().send_keys(data.card_code+Keys.TAB)

    def get_add_credit_card_button(self):
        return WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.add_credit_card_button)
        )
    def click_on_add_credit_card_button(self):
        self.get_card_code_number().send_keys(Keys.TAB)
        self.get_add_credit_card_button().click()

    def get_close_button(self):
        return WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.close_button_popup)
        )
    def click_on_close_button(self):
        self.get_close_button().click()

    def card_is_added(self):
        return WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.added_card)
        )

#Métodos para escribir un mensaje al conductor

    def get_message_for_driver_field(self):
        return WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.message_for_driver_field)
        )

    def set_message_for_driver(self):
        self.get_message_for_driver_field().send_keys(data.message_for_driver)


#Métodos para elegir la opción de manta y pañuelos

    def get_blankets_and_handkerchief_slider(self):
        self.driver.find_element(*self.blankets_and_handkerchief_option).click()

    def is_blankets_and_handkerchief_selected(self):
        return WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(self.blanket_and_handkerchief_checkbox)
        )

#Métodos para agregar helados

    def get_ice_cream_option(self):
        return WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.add_icecream)
        )

    def click_on_ice_cream_option(self):
        self.get_ice_cream_option().click()

    def two_ice_cream_added(self):
        return WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.ice_cream_count)
        )


#Métodos para pedir el taxi, después de llenar los requerimientos

    def get_request_a_taxi_button(self):
        return WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.order_a_taxi_button)
        )

    def click_on_request_a_taxi_button(self):
        self.get_request_a_taxi_button().click()


#Métodos para ver la información del conductor

    def get_waiting_order_screen(self):
        return WebDriverWait(self.driver,5).until(
            EC.presence_of_element_located(self.waiting_order_screen)
        )


    def get_order_number(self):
        return WebDriverWait(self.driver,50).until(
            EC.presence_of_element_located(self.trip_confirmation)
        )




















