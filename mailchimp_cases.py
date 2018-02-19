from mailchimp_setting import driver
from mailchimp_setting import MailSetUp
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import pdb
from time import sleep
from mailchimp_setting import log
from selenium.common.exceptions import TimeoutException


class mailchimp(MailSetUp):

    # def read_data(self):

    #     with open('/home/alqama/workspace/MailChimp_ALL_ Contacts_edit.csv', newline='') as File:
    #         reader = csv.reader(File)
    #         for row in reader:
    #             return(row)

    def test_01_login(self):

        username = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'username')))
        username.send_keys('zayalabs')

        password = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'password')))
        password.send_keys('Zaya123456$')

        LogIn = driver.find_element_by_xpath(
            '//*[@id="login-form"]/fieldset/div[4]/button')
        LogIn.click()

    def test_02_search(self):

        search = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, '//body/div[2]/div[1]/div/nav[2]/ul/li[1]/a/span')))
        search.click()
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'global-search')))

        with open('/home/alqama/workspace/autotest-englishduniya/mailchimp/MailChimp_ALL_ Contacts_edit.csv', newline='') as File:
        # with open('/home/alqama/workspace/MailChimp_ALL_ Contacts_edit.csv', newline='') as File:
            reader = csv.reader(File)

            for row in reader:
                id = row
                sleep(3)
                search_field.clear()
                search_field.send_keys(id)
                log.info('searching id {}'.format(id))
                search_field.send_keys(Keys.ENTER)
                sleep(2)
                search_result = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="search-results-data"]/div/ul')))
                results = search_result.find_elements_by_tag_name('li')
                number_of_results = len(results)
                print('number of results for id {} counting outside whileloop are {}'.format(
                    id, number_of_results))
                # log.info('number of results for id {} are {}'.format(id ,number_of_results))
                

                if number_of_results > 1:
                    print('result more than 1 going to wile loop')
                    while number_of_results > 1:

                        print('number of results for id {} are {}'.format(
                            id, number_of_results))
                        log.info('number of results for id {} are {}'.format(
                            id, number_of_results))
                        
                        view_profile = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="search-results-data"]/div/ul/li[2]/div[2]/div/div[2]/div')))
                        view_profile.click()

                        try :

                            delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                                (By.ID, 'delete-member')))
                            delete.click()

                            confirm_delete = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                                (By.CSS_SELECTOR, '#confirm-delete > div.dijitDialogPaneContent > div > div > span')))
                            confirm_delete.click()
                            print('Deleted 1 result for id {}'.format(id))
                            log.info('Deleted 1 result for id {}'.format(id))

                            sleep(3)
                            home_monkey = WebDriverWait(driver, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, '#freddielink > img')))
                            home_monkey.click()
                            # pdb.set_trace()
                            search = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                                (By.XPATH, '//body/div[2]/div[1]/div/nav[2]/ul/li[1]/a/span')))
                            search.click()

                            search_field = WebDriverWait(driver, 10).until(
                                EC.visibility_of_element_located((By.ID, 'global-search')))
                            # search_field.click()
                            search_field.clear()
                            search_field.send_keys(row)
                            search_field.send_keys(Keys.ENTER)
                            sleep(2)
                            search_result = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="search-results-data"]/div/ul')))
                            results = search_result.find_elements_by_tag_name('li')
                            number_of_results = len(results)
                            print('Final count for id {} is {}'.format(
                                id, number_of_results))
                            log.info('Final count for id {} is {}'.format(
                                id, number_of_results))
                            print('done wit wile loop')
                            

                        except TimeoutException :
                            
                            print('Delete button not present for id {}'.format(id))
                            log.info('Delete button not present for id {}'.format(id))
                            sleep(3)
                            home_monkey = WebDriverWait(driver, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, '#freddielink > img')))
                            home_monkey.click()
                            # pdb.set_trace()
                            search = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                                (By.XPATH, '//body/div[2]/div[1]/div/nav[2]/ul/li[1]/a/span')))
                            search.click()
                            search_field = WebDriverWait(driver, 20).until(
                                EC.presence_of_element_located((By.ID, 'global-search')))
                            sleep(3)
                            break

                else:
                    print('For id {} number of search-result is 1'.format(id))
                    log.info('For id {} number of search-result is 1'.format(id))


if __name__ == '__main__':
    unittest.main()
