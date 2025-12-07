import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Base import InitiateDriver
from TestCases import test_loginTest
import time

class CheckoutSaucedemo(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.browser = InitiateDriver.startBrowser() # ini cara memanggil class dan method 

    # Assertion Page Login/Main Page
    def test_01_success_page_title(self):
        self.assertEqual(self.browser.title, "Swag Labs")
        #print('Assert Success')
    
    def test_02_success_login(self):
        browser = self.browser
        # Fitur Login
        # Isi username dan password
        browser.find_element(By.ID, "user-name").send_keys('standard_user')
        browser.find_element(By.CSS_SELECTOR,'[data-test="password"]').send_keys('secret_sauce')

        # Klik tombol login
        browser.find_element(By.ID, "login-button").click()

        # Verifikasi login berhasil dengan URL assertion
        get_url = browser.current_url
        self.assertIn('/inventory.html', get_url)       

    def test_03_success_add_item(self):
        browser = self.browser
        
        # berhasil menambahkan barang ke card
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
    def test_04_success_checkout(self):
        browser = self.browser
        
        # berhasil masuk ke halaman cart
        browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        # Verifikasi login berhasil dengan URL assertion
        get_url = browser.current_url
        self.assertIn('/cart.html', get_url) 
              
        #click Checkout
        browser.find_element(By.ID, "checkout").click()
        message = browser.find_element(By.CLASS_NAME,"header_secondary_container")
        assert message.text == "Checkout: Your Information"
        
        #input data-data checkout
        browser.find_element(By.ID, "first-name").send_keys('testing')
        browser.find_element(By.ID, "last-name").send_keys('testing')
        browser.find_element(By.ID, "postal-code").send_keys('123456')
        browser.find_element(By.ID, "continue").click()
        
        #Halaman Checkout Overview
        message = browser.find_element(By.CLASS_NAME,"header_secondary_container")
        assert message.text == "Checkout: Overview"
        browser.find_element(By.ID, "finish").click()
        
        #berhasil checkout
        message = browser.find_element(By.CLASS_NAME,"complete-header")
        assert message.text == "Thank you for your order!"
        
        #kembali ke halaman Home
        browser.find_element(By.ID, "back-to-products").click()
        time.sleep(1)
        
    def test_05a_checkout_firstname_empty(self):
        browser = self.browser
    
        # Berhasil masuk ke halaman cart
        browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        # Verifikasi berhasil masuk ke halaman cart
        get_url = browser.current_url
        self.assertIn('/cart.html', get_url) 
            
        # Click Checkout
        browser.find_element(By.ID, "checkout").click()
        time.sleep(1)
            
        #Test hanya First Name yang kosong
        browser.find_element(By.ID, "last-name").send_keys("Doe")
        browser.find_element(By.ID, "postal-code").send_keys("12345")
        browser.find_element(By.ID, "continue").click()
        
        error_message = browser.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        self.assertEqual(error_message.text, "Error: First Name is required")

    def test_05b_checkout_lastname_empty(self):
        browser = self.browser
    
        # Berhasil masuk ke halaman cart
        browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        # Verifikasi berhasil masuk ke halaman cart
        get_url = browser.current_url
        self.assertIn('/cart.html', get_url) 
            
        # Click Checkout
        browser.find_element(By.ID, "checkout").click()
        time.sleep(1)
        
        #Test hanya Last Name yang kosong
        browser.find_element(By.ID, "first-name").send_keys("John")
        browser.find_element(By.ID, "postal-code").send_keys("12345")
        browser.find_element(By.ID, "continue").click()
        
        error_message = browser.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        self.assertEqual(error_message.text, "Error: Last Name is required")

    def test_05c_checkout_postalcode_empty(self):
        browser = self.browser
    
        # Berhasil masuk ke halaman cart
        browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        # Verifikasi berhasil masuk ke halaman cart
        get_url = browser.current_url
        self.assertIn('/cart.html', get_url) 
            
        # Click Checkout
        browser.find_element(By.ID, "checkout").click()
        time.sleep(1)
        
        #Test hanya Postal Code yang kosong
        browser.find_element(By.ID, "first-name").send_keys("John")
        browser.find_element(By.ID, "last-name").send_keys("Doe")
        browser.find_element(By.ID, "continue").click()
        
        error_message = browser.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        self.assertEqual(error_message.text, "Error: Postal Code is required")

    def test_06_remove_item(self):
        browser = self.browser
        browser.find_element(By.ID, "cancel").click()
        browser.find_element(By.ID, "continue-shopping").click()
        
        # berhasil masuk ke halaman cart
        get_url = browser.current_url
        self.assertIn('/inventory.html', get_url) 
        time.sleep(1)
        
        # berhasil menambahkan barang ke card
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        # berhasil masuk ke halaman cart
        browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        
        # Verifikasi login berhasil dengan URL assertion
        get_url = browser.current_url
        self.assertIn('/cart.html', get_url) 
        
        #click remove item
        browser.find_element(By.ID, "remove-sauce-labs-backpack").click()
        
              
        
    @classmethod
    def tearDownClass(self):
        InitiateDriver.closeBrowser()

if __name__ == '__main__':
    
    unittest.main(verbosity=2)