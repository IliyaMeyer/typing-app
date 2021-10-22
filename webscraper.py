import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from keylogger import Keylogger
from data_processing import DataProcessing


class WebScraper:

    def __init__(self):
        self.driver = webdriver.Chrome()

    """
    returns True if the element exists in the dom, False otherwise
    """
    def does_exist(self, identifier_type, element_identifier):
        try:
            self.driver.find_element(identifier_type, element_identifier)
        except NoSuchElementException:
            return False
        return True

    """
    removes element from browser, waiting 10 seconds max if it is not present
    returns True if removal was successful, false otherwise
    """
    def remove_element(self, identifier_type, element_identifier):
        repeats = 0
        while not self.does_exist(identifier_type, element_identifier):
            time.sleep(1)
            repeats += 1
            if repeats >= 10:
                return False
        self.driver.execute_script("""
                var element = arguments[0];
                element.parentNode.removeChild(element);
                """, self.driver.find_element(identifier_type, element_identifier))
        return True

    """
    opens the browser
    """
    def open_driver(self):
        self.driver.get('https://10fastfingers.com/typing-test/english')

        cookie_field_id = 'CybotCookiebotDialog'
        advert_video_id = 'primis_container_div'
        footer_id = 'fs-sticky-footer'
        ad_unit_id = 'ads-speedtest-view-container'

        self.remove_element(By.ID, cookie_field_id)
        self.remove_element(By.ID, advert_video_id)
        self.remove_element(By.ID, footer_id)
        self.remove_element(By.ID, ad_unit_id)

        print('ready')

        # temp code start
        keylogger = Keylogger()
        keylogger.run_keylogger(duration_after_first_press=60)
        # temp code end

        while not self.does_exist(By.XPATH, '//*[@id="accuracy"]/td[1]'):
            time.sleep(1)
        print('done :)')

        data_processing = DataProcessing(keylogger.screen_input)
        data_processing.show_graph()


def main():
    scraper = WebScraper()
    scraper.open_driver()


if __name__ == '__main__':
    main()
