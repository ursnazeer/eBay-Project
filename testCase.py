import appTestBase.py

'''Defining variables at the start of the test'''
eBayApp = 'com.ebay.mobile'
eBaySearchTab = 'com.ebay.mobile.activities.QuickSearchHandler'
txtUser = 'newuser'
txtPassword = '1234'
txtIphone = 'iPhone 8S'
checkOut = 'com.ebay.mobile.checkout.CheckoutActivity'


'''Test Steps starts executing from here'''
#-----------------------------------------
'''Start of Test'''
#-----------------------------------------

#--------------------------------------------------
testStep = "To check whether the app is installed"
test.log(testStep)
#--------------------------------------------------
checkWhetherAppIsInstalled(self.eBayApp)


#--------------------------------------------------
testStep = "Launch the test app"
test.log(testStep)
#--------------------------------------------------
launchApp(self.eBayApp)


#--------------------------------------------------
testStep = "Login to the test app"
test.log(testStep)
#--------------------------------------------------
appLogin(self.txtUser, self.Password)


#--------------------------------------------------
testStep = "Search an item in the app"
test.log(testStep)
#--------------------------------------------------
itemSearch(self.eBaySearchTab, self.txtIphone)


#--------------------------------------------------
testStep = "Add the iteam to the cart"
test.log(testStep)
#--------------------------------------------------
itemSearch(self.eBaySearchTab, self.txtIphone)


#--------------------------------------------------
testStep = "Purchase the item in the cart"
test.log(testStep)
#--------------------------------------------------
itemPurchase(self.checkOut)


#--------------------------------------------------
testStep = "Close the app to end the test"
test.log(testStep)
#--------------------------------------------------
tearDown()

#--------------------------------------
'''End of Test'''
#--------------------------------------
