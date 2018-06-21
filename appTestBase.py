import os
import unittest
from time import sleep
from appium import webdriver


'''Class to run tests against eBay app'''
class eBayApp(unittest.TestCase):

    '''Function to setup the test app on the device'''
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'Samsung Max'
        desired_caps['appPackage'] = 'com.ebay.mobile'
        desired_caps['appActivity'] = 'com.ebay.mobile.activities.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    '''Function to Tear down the test'''
    def tearDown(self):
        self.driver.quit()

    '''Function to check if the app has been installed'''
    def checkWhetherAppIsInstalled(self, appName): 
        self.driver.is_app_installed(appName)
        print("%s APP HAS BEEN INSTALLED" %appName)

    '''Function to launch  the app'''	
    def launchApp(self, appName):
	driver.launch_app()
	el = driver.find_element_by_name(appName)
	assertIsNotNone(el)

    '''Function to Login to the app'''
    def appLogin(self, userName, passWord):
        self.driver.findElement(userId).sendKeys(userName)
        self.driver.findElement(password).sendKeys(passWord)
        self.driver.findElement(login_Button).click()

    '''Function to scroll the app''' 
    def scrollApp(self, dragElement, tapElement):
        element_to_drag = self.driver.find_element_by_xpath(dragElement)
        element_to_tap = self.driver.find_element_by_xpath(tapElement)
	sleep(2)
   
    '''Function to search an item'''
    def itemSearch(self, searchTab, itemName):
        self.driver.find_element_by_xpath(searchTab).click()
        sleep(1)
        self.driver.getKeyboard().sendKeys(itemName)
        self.driver.pressKeyCode(66)

    '''Function to add an item to the cart'''
    def addToCart(self, addItem):
        self.driver.find_element_by_class_name(addItem).click()
        sleep(1)

    '''Function to purchase an item in the cart'''
    def itemPurchase(self, itemCheckout):
        self.driver.find_element_by_class_name(itemCheckOut).click()
        sleep(3)
         
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(eBayApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
