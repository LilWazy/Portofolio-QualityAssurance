import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self): # ini untuk buka browser dan install sesuai versi browser laptop
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(service=service, options=options)

    def test_a_verify_success_login(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi form password
        time.sleep(1)
        self.browser.find_element(By.ID, "signin_login").click() # klik tombol login
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertIn('....', popup_atas)
        time.sleep(1)
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)

    def test_verify_failed_login_with_email_registered_and_empty_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # tidak mengisi password, diberi string kosong ""
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
    
        # validasi
        self.assertEqual(popup_atas, '....')
        time.sleep(1)
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)

    def test_verify_failed_login_with_empty_email_and_registered_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....") # tidak mengisi form email diberi string kosong ""
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi password
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, '....')
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)
    
    def test_a_verify_failed_login_with_unregistered_email_and_unregistered_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....@gmail.com") # isi form dengan email belum registrasi
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi form dengan pass belum registrasi
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, "....")
        time.sleep(1)
        self.assertEqual(popup_bawah, "....")
        time.sleep(2)

    def test_a_verify_failed_login_with_registered_email_and_unregistered_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi form password salah
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, "....")
        time.sleep(1)
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)

    def test_verify_failed_login_with_empty_email_and_empty_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # tidak mengisi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # tidak mengisi form password
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, '....')
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)

    def test_verify_failed_login_with_max_20_char_email_and_registered_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....@gmail.com") # isi form email max char salah
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi form password
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
    
        # validasi
        self.assertEqual(popup_atas, '....')
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)

    def test_verify_failed_login_with_registered_email_and_max_20_char_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi form password max char salah
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, '....')
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)

    def test_verify_failed_login_with_max_20_char_email_and_max_20_char_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....@gmail.com") # isi form email max char
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi form password max char salah
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, '....')
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)

    def test_verify_failed_login_with_not_valid_email_and_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....") # isi form  dengna invalid email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi form password
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        respon_error_email = self.browser.find_element(By.ID, 'email').get_attribute('validationMessage') # dapetin teks/tulisan validasi email
        time.sleep(2)
        # validasi
        self.assertEqual(respon_error_email,"Please include an '@' in the email address. '....' is missing an '@'.")
        time.sleep(2)

    def test_verify_failed_login_with_max_20_char_email_and_max_20_char_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://....") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("....@gmail.com") # isi form email max char
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("....") # isi form password max char salah
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, '....')
        self.assertEqual(popup_bawah, '....')
        time.sleep(2)

    def tearDown(self): # ini untuk tutup browser
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()