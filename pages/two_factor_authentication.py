from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import Base
from tests import conftest


class TwoFactorAuthentication(Base):
    _enter_passcode_button = (By.CSS_SELECTOR, '.passcode-label .positive.auth-button')
    _passcode_field_locator = (By.CSS_SELECTOR, '.passcode-label input[name="passcode"]')
    _duo_iframe_locator = (By.ID, 'duo_iframe')
    _error_message_locator = (By.CSS_SELECTOR, '.message.error')

    def enter_passcode(self, passcode):
        self.selenium.switch_to_frame('duo_iframe')
        self.selenium.find_element(*self._enter_passcode_button).click()
        self.selenium.find_element(*self._passcode_field_locator).clear()
        self.selenium.find_element(*self._passcode_field_locator).send_keys(passcode)
        self.selenium.find_element(*self._enter_passcode_button).click()
        self.selenium.switch_to_default_content()

    @property
    def is_error_message_displayed(self):
        if self.is_element_present(*self._duo_iframe_locator):
            self.selenium.switch_to_frame('duo_iframe')
            is_message_shown = self.selenium.find_element(*self._error_message_locator).is_displayed()
            self.selenium.switch_to_default_content()
            return is_message_shown
        return False

    def wait_for_passcode_to_change(self, secret_seed, current_passcode):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: conftest.passcode(secret_seed) != current_passcode)
