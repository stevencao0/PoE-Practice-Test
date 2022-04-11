from locator import *
from element import BasePageElement

# Defines the actions you can do on a webpage (i.e. click a button, enter text in a text box, close the browser)
# This is the actual code that interacts with the web page
class BasePage(object):
  def __init__(self, driver):
      self.driver = driver
