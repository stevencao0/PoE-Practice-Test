from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from TradePage import TradePage
from ShopPage import ShopPage
import unittest
import time

""" All test units will be here """
class  mainTest(unittest.TestCase):

# setup is called every time for each test
    def setUp(self):
        PATH = "C:/Users/Steven/Desktop/Coding-Practice/PoETest/chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.pathofexile.com/")


    def shop(self):
        self.driver.find_element(By.ID, "nav-shop").click()

        print(self.driver.current_url)
        assert self.driver.current_url == 'https://www.pathofexile.com/shop'

        shopPage = ShopPage(self.driver)
        shopPage.navigate_all_categories()
        assert True

#Tests navigation buttons to the correct pages
    def navigation_bar(self):
        self.driver.find_element(By.ID, "nav-home").click()
        assert self.driver.current_url == 'https://www.pathofexile.com/'
        self.driver.find_element(By.ID, "nav-game").click()
        assert self.driver.current_url == 'https://www.pathofexile.com/game'
        self.driver.back()
        self.driver.find_element(By.ID, "nav-forum").click()
        assert self.driver.current_url == 'https://www.pathofexile.com/forum'
        self.driver.back()
        self.driver.find_element(By.ID, "nav-events").click()
        assert self.driver.current_url == 'https://www.pathofexile.com/events'
        self.driver.back()
        self.driver.find_element(By.ID, "nav-trade").click()
        assert self.driver.current_url == 'https://www.pathofexile.com/trade'
        self.driver.back()
        self.driver.find_element(By.ID, "nav-shop").click()
        assert self.driver.current_url == 'https://www.pathofexile.com/shop'

# Trade Page Tests   ----------------------------------------------------------------------------------------------------------------
#Tests search function
    def search_item(self):
        tradePage = TradePage(self.driver)
        tradePage.goToTrade()
        tradePage.search_item('Headhunter')
        tradePage.clickSearch()

        assert "Headhunter" in self.driver.page_source

#Tests search function with additional filters
    def search_item_with_filters(self):
    #    tradePage = Pages.TradePage(self.driver)
        tradePage = TradePage(self.driver)
        tradePage.goToTrade()
        tradePage.stat_filter('+# total to Level of Socketed Bow Gems','1','1')
        tradePage.clickSearch()

        assert "+1 total to Level of Socketed Bow Gems" in self.driver.page_source

    def tearDown(self):
        self.driver.close()
# Shop Page Tests   ----------------------------------------------------------------------------------------------------------------
    def shopNavigation(self):
        self.driver.find_element(By.ID, "nav-shop").click()
        shopPage = ShopPage(self.driver)
        shopPage.goToSpecials()

        assert self.driver.current_url == 'https://www.pathofexile.com/shop/category/specials'
        self.driver.back()
        shopPage.goToArmour()
        assert self.driver.current_url == 'https://www.pathofexile.com/shop/category/armour-effects'

#Tests search box in Shop Page and confirm results
    def test_shopSearch(self):
        self.driver.find_element(By.ID, "nav-shop").click()
        shopPage = ShopPage(self.driver)
        shopPage.goToStashTabs()
        shopPage.typeSearch("map")
        shopPage.searchSubmit()
        assert self.driver.current_url =='https://www.pathofexile.com/shop/category/stash-tabs?search=map'
        assert WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="MapTab"]/div[1]/a/img'))).is_displayed()



# __name__ == __main__ would happen if this file is being runned directly,
# else, the stuff happening in __name__ -- __main__ would not run, when its being imported or being used by another.
if __name__ == "__main__":
    unittest.main()
