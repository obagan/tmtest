import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.command import Command


class TestTimeWeb(unittest.TestCase):
    tariff_map = {
        "year": {
            "name": "Year+",
            "count_disk": "5",
            "count_sites": "1",
            "count_db": "1",
        },
        "optimo": {
            "name": "Optimo+",
            "count_disk": "10",
            "count_sites": "10",
            "count_db": "10",
        },
        "century": {
            "name": "Century+",
            "count_disk": "15",
            "count_sites": "25",
            "count_db": "25",
        },
        "millennium": {
            "name": "Millennium+",
            "count_disk": "25",
            "count_sites": "50",
            "count_db": "∞",
        },
    }

    def setUp(self):
        self.driver = webdriver.Chrome('C:/bin/chromedriver.exe')
        self.current_tariff = "year"

    def test_send_form(self):
        self.driver.get("https://timeweb.com/ru/services/hosting/")

        self.driver.execute_script("scroll(0, 1250);")
        footer = self.driver.find_element_by_class_name('footer')

        # move mouse to footer
        button = self.driver.find_element_by_css_selector('.btn[rel="{}"]'.format(self.current_tariff))
        ActionChains(self.driver).move_to_element(button).perform()
        time.sleep(2)

        button.click()
        time.sleep(2)

        full_name = self.driver.find_element_by_xpath("//div[@name='hosting']//input[@name='full_name']")
        full_name.click()
        full_name.send_keys('test_name')

        email = self.driver.find_element_by_xpath("//div[@name='hosting']//input[@name='email']")
        email.click()
        email.send_keys('test@test.test')

        confirm = self.driver.find_element_by_css_selector('.checkbox label[for="c4"]')
        confirm.click()

        button = self.driver.find_element_by_xpath("//div[@name='hosting']//a[@class='btn flr ph35 mt-5']")
        button.click()
        time.sleep(2)

        time.sleep(2)
        help_closer = self.driver.find_element_by_class_name('ui-button-icon-primary')
        help_closer.click()

        time.sleep(2)

        tariff_link = self.driver.find_element_by_css_selector(".icon-tariff")
        ActionChains(self.driver).move_to_element(tariff_link).perform()
        tariff_link.click()

        tariff_select = self.driver.find_element_by_css_selector('[class="ui-media-body ui-overflow-wrap"]')
        assert tariff_select.text == self.tariff_map[self.current_tariff]['name'], "Invalid tariff name"

        count_sites = self.driver.find_element_by_id('count_sites')
        assert count_sites.text == self.tariff_map[self.current_tariff]['count_sites'], "Invalid sites count"

        count_disk = self.driver.find_element_by_id('count_disk')
        assert count_disk.text == self.tariff_map[self.current_tariff]['count_disk'], "Invalid disk count"

        count_db = self.driver.find_element_by_id('count_db')
        assert count_db.text == self.tariff_map[self.current_tariff]['count_db'], "Invalid db count"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
