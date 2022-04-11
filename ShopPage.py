from page import BasePage
from locator import ShopPageLocators

from element import BasePageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage(BasePage):
    """ Action methods for the shop page are here """
    def click_category_button(self):
        """ The * in '*MainPageLocators.CATEGORY_BUTTON' is same as  (By.CLASS_NAME, "category") """
        element = self.driver.find_element(*MainPageLocators.CATEGORY_BUTTON)
        element.click()

    def navigate_all_categories(self):
        categories = self.driver.find_elements(By.XPATH,".//div[@class='category']")

        self.driver.find_element(*MainPageLocators.CATEGORY_BUTTON).click()
        print(self.driver.current_url)
        self.driver.back()

    def typeSearch(self, text):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(ShopPageLocators.shop_search_box)).send_keys(text)


    def searchSubmit(self):
        self.driver.find_element(*ShopPageLocators.search_box_submit).click()

    def goToSpecials(self):
        self.driver.find_element(*ShopPageLocators.nav_specials).click()

    def goToNew(self):
        self.driver.find_element(*ShopPageLocators.nav_new).click()

    def goToStashTabs(self):
        self.driver.find_element(*ShopPageLocators.nav_stashtabs).click()

    def goToBundles(self):
        self.driver.find_element(*ShopPageLocators.nav_bundles).click()

    def goToArmour(self):
        self.driver.find_element(*ShopPageLocators.nav_armour).click()

    def goToBackAttachment(self):
        self.driver.find_element(*ShopPageLocators.nav_backAttachments).click()

    def goToWeapon(self):
        self.driver.find_element(*ShopPageLocators.nav_weapon).click()

    def goToPortals(self):
        self.driver.find_element(*ShopPageLocators.nav_portals).click()

    def goToSkillEffects(self):
        self.driver.find_element(*ShopPageLocators.nav_skillEffects).click()

    def goToChar(self):
        self.driver.find_element(*ShopPageLocators.nav_character).click()

    def goToFootprints(self):
        self.driver.find_element(*ShopPageLocators.nav_footprints).click()

    def goToGuildHideout(self):
        self.driver.find_element(*ShopPageLocators.nav_guildHideout).click()

    def goToGuild(self):
        self.driver.find_element(*ShopPageLocators.nav_guild).click()

    def goToPets(self):
        self.driver.find_element(*ShopPageLocators.nav_pets).click()

    def goToHideout(self):
        self.driver.find_element(*ShopPageLocators.nav_hideout).click()

    def goToAccountFeatures(self):
        self.driver.find_element(*ShopPageLocators.nav_accFeatures).click()

    def goToSupporterPacks(self):
        self.driver.find_element(*ShopPageLocators.nav_supporterPacks).click()
