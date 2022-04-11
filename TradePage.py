from page import BasePage
from locator import TradePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TradePage(BasePage):

    """ Action methods for the trading page are here """
    #navigate to trade page
    def goToTrade(self):
        self.driver.find_element(*TradePageLocators.nav_trade).click()

    """ Click and enter text in the main search box """
    def search_item(self, text):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(TradePageLocators.search_box)).send_keys(text)
        self.driver.find_element(*TradePageLocators.search_box).send_keys(Keys.ENTER)

    """ Search for a specific stat to filter, the minimum and maximum values of that stat """
    def stat_filter(self,text,min,max):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(TradePageLocators.add_filter)).send_keys(text)
        self.driver.find_element(*TradePageLocators.add_filter).send_keys(Keys.ENTER)
        self.driver.find_element(*TradePageLocators.filter_min).send_keys(min)
        self.driver.find_element(*TradePageLocators.filter_max).send_keys(max)

    """ Click search button and wait for the results """
    def clickSearch(self):
        self.driver.find_element(*TradePageLocators.submit).click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(TradePageLocators.results))
