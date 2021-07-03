import time
import pytest

import csv_page, dispense_page

from csv_page import read_all_test_data, get_testcase_test_data

from selenium.webdriver import Chrome

#Open a Terminal and issue the command pytest test.py::<TEST CASE NAME> -s
#Example: pytest test.py::test_upload_csv -s

@pytest.fixture()
def get_driver_webdriver():
    global driver

    driver = Chrome(executable_path='C:\\chromedriver.exe')

    driver.get("http://localhost:8080/")
    driver.maximize_window()       

    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()

#User Story #3
def test_upload_csv(get_driver_webdriver):
    driver = get_driver_webdriver

    time.sleep(2)
    #Upload csv
    csv_page.upload_csv(driver, r"C:\AutoRepo\Oppenheimer\Repo\test.csv")
    csv_page.click_refresh_tax_relief(driver)
    time.sleep(2)
    csv_page.verify_record_show(driver)
    csv_page.verify_table_display(driver)
    return

#User Story #4
#run_verify_tax_relief is not a test case
def run_verify_tax_relief(get_driver_webdriver, test_data):
    driver = get_driver_webdriver
    natid = test_data['nat_id']
    relief = test_data['tax_relief']

    a = csv_page.check_record_show(driver)
    if a == 0:
        csv_page.upload_csv(driver, r"C:\AutoRepo\Oppenheimer\Repo\test.csv")
        csv_page.click_refresh_tax_relief(driver)
        time.sleep(2)
    #AC2 Verify Natid display $ from 5th Character
    csv_page.verify_natid(driver, natid)
    #Verify Tax Relief is calculated correctly
    csv_page.verify_tax_relief(driver, natid, relief)
    return

test_data_list = read_all_test_data("data")

#AC3 Age Group
@pytest.mark.parametrize("test_data", get_testcase_test_data('1001001', test_data_list))
def test_tax_relief_under_18(get_driver_webdriver, test_data):
    run_verify_tax_relief(get_driver_webdriver, test_data)

@pytest.mark.parametrize("test_data", get_testcase_test_data('1002002', test_data_list))
def test_tax_relief_under_35_above_18(get_driver_webdriver, test_data):
    run_verify_tax_relief(get_driver_webdriver, test_data)

@pytest.mark.parametrize("test_data", get_testcase_test_data('1003003', test_data_list))
def test_tax_relief_under_50_above_35(get_driver_webdriver, test_data):
    run_verify_tax_relief(get_driver_webdriver, test_data)

@pytest.mark.parametrize("test_data", get_testcase_test_data('1004004', test_data_list))
def test_tax_relief_under_75_above_50(get_driver_webdriver, test_data):
    run_verify_tax_relief(get_driver_webdriver, test_data)

@pytest.mark.parametrize("test_data", get_testcase_test_data('1005005', test_data_list))
def test_tax_relief_above_76(get_driver_webdriver, test_data):
    run_verify_tax_relief(get_driver_webdriver, test_data)

#AC5 Relief below $50 will be given as $50
@pytest.mark.parametrize("test_data", get_testcase_test_data('1006006', test_data_list))
def test_tax_relief_total_below_50(get_driver_webdriver, test_data):
    run_verify_tax_relief(get_driver_webdriver, test_data)

#AC6 Relief has more than 2 decimal place truncated
@pytest.mark.parametrize("test_data", get_testcase_test_data('1007007', test_data_list))
def test_tax_relief_truncate_2_decimal(get_driver_webdriver, test_data):
    run_verify_tax_relief(get_driver_webdriver, test_data)

#User Story #5
def test_dispense_tax(get_driver_webdriver):
    driver = get_driver_webdriver

    time.sleep(2)
    dispense_page.verify_dispense_btn(driver, "rgba(220, 53, 69, 1)")
    dispense_page.click_dispense_btn(driver)
    time.sleep(2)
    dispense_page.verify_cash_dispense(driver)
    return