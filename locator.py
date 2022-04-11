from selenium.webdriver.common.by import By
#Put all the locators for the pages here
#This is so when someone changes a locator path, you don't need to go through every single code to make changes to the new xpath



class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""
    pass

class TradePageLocators(object):
    """A class for Trade Page locators. All trade page locators should
    come here"""
    search_box = (By.CLASS_NAME, "multiselect__input")
    submit = (By.CLASS_NAME, "search-btn")
    add_filter = (By.XPATH,"//*[@placeholder='+ Add Stat Filter']")
    filter_min = (By.XPATH,"//*[@id='trade']/div[4]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]")
    filter_max = (By.XPATH,"//*[@id='trade']/div[4]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[2]/input[2]")
    nav_trade = (By.ID, "nav-trade")
    results = (By.CLASS_NAME,"itemName")

class HomePageLocators(object):
    nav_home = (By.ID, "nav-home")

class ShopPageLocators(object):
    shop_search_box = (By.CLASS_NAME,"search-text")
    nav_shop = (By.ID, "nav-shop")
    nav_specials = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]")
    nav_new = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[3]")
    nav_stashtabs = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[4]")
    nav_bundles = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[5]")
    nav_armour = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[6]")
    nav_backAttachments = (By.XPATH,"html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[7]")
    nav_weapon = (By.XPATH,"html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[8]")
    nav_portals = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[9]")
    nav_skillEffects = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[10]")
    nav_character = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[11]")
    nav_footprints = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[12]")
    nav_guild = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[13]")
    nav_guildHideout = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[14]")
    nav_pets = (By.XPATH,"html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[15]")
    nav_hideout = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[16]")
    nav_accFeatures = (By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[17]")
    nav_supporterPacks = (By.XPATH,"//*[@id='shopBottopBanner']")
    search_box_submit = (By.CLASS_NAME,"search-button")


class ForumPageLocators(object):
    nav_forum = (By.ID, "nav-forum")
