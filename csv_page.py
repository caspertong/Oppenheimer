import time
import pytest
import csv

def scroll_to_element(driver, elem, scroll_to=0):
    if scroll_to == 0:
        driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'center',behavior:'auto'})", elem)
    elif scroll_to == 1:
        driver.execute_script("arguments[0].scrollIntoView({block:'start',inline:'center',behavior:'auto'})", elem)
    else:
        driver.execute_script("arguments[0].scrollIntoView({block:'end',inline:'center',behavior:'auto'})", elem)

def upload_csv(driver, filepath):
    try:
        #csv = open_csv(filepath)
        el = driver.find_element_by_xpath("//input[@class='custom-file-input']")
        scroll_to_element(driver, el)
        el.send_keys(filepath)
        print("Upload csv successful")
    except Exception:
        print("Failed to Upload csv")
        pytest.fail("Failed to Upload csv")


def click_refresh_tax_relief(driver):
    try:
        el = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
        scroll_to_element(driver, el)
        el.click()
        print("Click on Refresh Tax Relief Button Successful")
    except Exception:
        print("Failed to click the Refresh Tax Relief Button")
        pytest.fail("Failed to click the Refresh Tax Relief Button")

def check_record_show(driver):
    try:
        el = driver.find_element_by_xpath("//caption[text()='List of working class heroes and their tax relief']")
        scroll_to_element(driver, el)
        if el:
            print("List showing Working Class Herors")
            return 1
        else:
            print("List of working class did not show")
            return 0
    except Exception:
        pytest.fail("Failed to verify list of working class")

def verify_record_show(driver):
    try:
        el = driver.find_element_by_xpath("//caption[text()='List of working class heroes and their tax relief']")
        scroll_to_element(driver, el)
        if el:
            print("Verified List showing Working Class Herors")
        else:
            print("List of working class did not show")
            pytest.fail("List of working class did not show")
    except Exception:
        pytest.fail("Failed to verify list of working class")

def verify_table_display(driver):
    try:
        el_nat = driver.find_element_by_xpath("//th[text()='NatId']")
        el_ref = driver.find_element_by_xpath("//th[text()='Relief']")
        scroll_to_element(driver, el_nat)
        if el_nat:
            if el_ref:
                print("Verified both NatId and Relief displayed")
            else:
                print("Relief did not display")
                pytest.fail("Relief did not display")
        else:
            print("Natid did not display")
            pytest.fail("Natid did not display")
    except Exception:
        pytest.fail("Failed to verify Natid and Relief")


def verify_natid(driver, natid):
    try:
        el_nat = driver.find_element_by_xpath("//td[text()='"+natid+"']")
        if el_nat:
            print("Verified Natid are display in $ from the 5th character")
        else:
            print("Natid did not display with $ from the 5th character")
            pytest.fail("Natid did not display with $ from the 5th character")
    except Exception:
        pytest.fail("Failed to verify Natid with $ on the 5th character")

def verify_tax_relief(driver, natid, relief):
    try:
        el_ref = driver.find_element_by_xpath("//td[text()='"+natid+"']/following-sibling::*")
        if el_ref.text == relief:
            print("Verified Relief calculated displayed correctly")
        else:
            print("Relief displayed is incorrect. Actual: "+el_ref.text+" Expected: "+relief)
            pytest.fail("Relief displayed is incorrect. Actual: "+el_ref.text+" Expected: "+relief)
    except Exception:
        pytest.fail("Failed to verify tax relief")

def read_all_test_data(test_data_file_name):
    td = []
    csv.register_dialect('myDialect',
                         delimiter=',',
                         escapechar="\\",
                         skipinitialspace=True)
    with open(test_data_file_name + '.csv', 'r', encoding='utf-8') as csvFile:
        reader = csv.DictReader(csvFile)
        for lines in reader:
            td.append(lines)
    return td

def get_testcase_test_data(testcase_id, test_data_list):
    list_data = []
    for line in test_data_list:
        if (line['natid'] == testcase_id):
            list_data.append(line)
    return list_data