import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):
    
    def setUp(self):
        # Configurar el WebDriver y abrir la página web
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        
    def test_new_user(self):
        # Acciones de prueba para el registro de un nuevo usuario
        driver = self.driver
        
        # Hacer clic en el enlace "Log In" en el encabezado 
        # Esta deprecado el find_element_by_XPATH ahora se usa como esta abajo
        driver.find_element(By.XPATH,'//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.LINK_TEXT,'Log In').click()
        
        # Hacer clic en el botón "Create an Account"
        create_account_button = driver.find_element(By.XPATH,'//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        
        # Verificar que se muestra la página de creación de una nueva cuenta
        self.assertEqual('Create New Customer Account', driver.title)
        
        # Localizar los elementos de entrada y completar los campos
        first_name = driver.find_element(By.ID,'firstname')
        middlename = driver.find_element(By.ID,'middlename')
        lastname = driver.find_element(By.ID,'lastname')
        email_address = driver.find_element(By.ID,'email_address')
        password = driver.find_element(By.ID,'password')
        confirmation_password = driver.find_element(By.ID,'confirmation')
        news_letter_subscription = driver.find_element(By.ID,'is_subscribed')
        submit_button = driver.find_element(By.XPATH,'//*[@id="form-validate"]/div[2]/button/span/span')
        
        # Verificar que todos los elementos de entrada están habilitados
        self.assertTrue(first_name.is_enabled()
                        and lastname.is_enabled()
                        and middlename.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and confirmation_password.is_enabled()
                        and news_letter_subscription.is_enabled()
                        and submit_button.is_enabled())
        
        # Ingresar los valores en los campos de entrada
        first_name.send_keys('Test')
        middlename.send_keys('Test')
        lastname.send_keys('Test')
        email_address.send_keys('Test@testingmail.com')
        password.send_keys('Test')
        confirmation_password.send_keys('Test')
        
        # Hacer clic en el botón de envío del formulario
        submit_button.click()
        
    def tearDown(self):
        # Realizar acciones de limpieza y cerrar el navegador
        self.driver.implicitly_wait(3)
        self.driver.close()
            
if __name__ == "__main__":
    # Ejecutar las pruebas y generar el informe HTML
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='register_new_user'))
