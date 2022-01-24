# from select import select
from selenium import webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class AddPrescriptionTest(unittest.TestCase):



    def setUp(self):

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://13.59.2.216")
        self.driver.maximize_window()
        time.sleep(4)

    def test_success(self):
        driver=self.driver


        doctorPortal=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div/a[4]')
        doctorPortal.click()

        email=driver.find_element(By.ID,"form_d_email")
        email.send_keys("pshivangi1999@gmail.com")
        email.send_keys(Keys.RETURN)

        passwd=driver.find_element(By.XPATH,'//*[@id="form_d_pass"]')
        passwd.send_keys("admin@123")
        passwd.send_keys(Keys.RETURN)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)


        login=driver.find_element(By.XPATH,'//*[@id="contact-form"]/div/div[3]/center/div/div/button')
        login.click()
        time.sleep(2)

        addPrescription=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[3]/form/div/button')
        addPrescription.click()
        time.sleep(2)

        drop=Select(driver.find_element(By.XPATH,'//*[@id="patientname"]'))
        time.sleep(1)
        drop.select_by_index(3)
        time.sleep(5)

        chiefComplain=driver.find_element(By.XPATH,'//*[@id="form_p_cc"]')
        chiefComplain.send_keys("Fever")
        chiefComplain.send_keys(Keys.RETURN)


        diagnosis=driver.find_element(By.XPATH,'//*[@id="form_p_cf"]')
        diagnosis.send_keys("High Body temperature")
        diagnosis.send_keys(Keys.RETURN)

        examination=driver.find_element(By.XPATH,'//*[@id="form_p_examination"]')
        examination.send_keys("checked temperature")
        examination.send_keys(Keys.RETURN)

        investigation=driver.find_element(By.XPATH,'//*[@id="form_p_investigation"]')
        investigation.send_keys("none")
        investigation.send_keys(Keys.RETURN)


        advice=driver.find_element(By.XPATH,'//*[@id="form_p_advice"]')
        advice.send_keys("none")
        advice.send_keys(Keys.RETURN)


        notes=driver.find_element(By.XPATH,'//*[@id="form_p_note"]')
        notes.send_keys("none")
        notes.send_keys(Keys.RETURN)

        #add drug
        medicationItem=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[1]/div[1]/input')
        medicationItem.send_keys("Paracetemol")
        medicationItem.send_keys(Keys.RETURN)

        strength=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[1]/div[2]/input')
        strength.send_keys("2")
        strength.send_keys(Keys.RETURN)

        preparation=Select(driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[2]/div[1]/select'))
        preparation.select_by_index('2')
        time.sleep(2)

        route=Select(driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[2]/div[2]/select'))
        route.select_by_index('2')
        time.sleep(2)

        dosage=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[3]/div[1]/input')
        dosage.send_keys("3")
        dosage.send_keys(Keys.RETURN)

        direction=Select(driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[3]/div[2]/select'))
        direction.select_by_index('2')
        time.sleep(2)

        frequency=Select(driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[4]/div[1]/select'))
        frequency.select_by_index('2')
        time.sleep(2)

        duration=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[4]/div[2]/input')
        duration.send_keys("5 days")
        duration.send_keys(Keys.RETURN)


        totalQuantity=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[5]/div[1]/input')
        totalQuantity.send_keys("10")
        totalQuantity.send_keys(Keys.RETURN)
        addPrescriptionBtn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div/div/div/div/div/form/div[5]/div[2]/button')
        addPrescriptionBtn.click()
        
        driver.execute_script("window.scrollTo(0,0);")
        time.sleep(2)

        submitPrescriptionBtn = driver.find_element(By.XPATH,'//*[@id="contact-form"]/button')
        submitPrescriptionBtn.click()
        driver.execute_script("window.scrollTo(0,0);")
        time.sleep(2)
        driver.switch_to.alert.accept()
        self.assertEqual(driver.current_url, "http://13.59.2.216/doctor_dashboard", " Prescription added successfully")


    


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
