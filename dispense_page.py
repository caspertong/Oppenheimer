import time
import pytest

def scroll_to_element(driver, elem, scroll_to=0):
    if scroll_to == 0:
        driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'center',behavior:'auto'})", elem)
    elif scroll_to == 1:
        driver.execute_script("arguments[0].scrollIntoView({block:'start',inline:'center',behavior:'auto'})", elem)
    else:
        driver.execute_script("arguments[0].scrollIntoView({block:'end',inline:'center',behavior:'auto'})", elem)

def click_dispense_btn(driver):
    try:
        el = driver.find_element_by_xpath("//a[@href='dispense']")
        scroll_to_element(driver, el)
        el.click()
        print("Click on Dispense Button Successful")
    except Exception:
        print("Failed to click on the Dispense Button")
        pytest.fail("Failed to click on the Dispense Button")

def verify_dispense_btn(driver, color):
    try:
        el = driver.find_element_by_xpath("//a[@href='dispense']")
        scroll_to_element(driver, el)
        if el.text == 'Dispense Now':
            print("Verified Dispense Now word displayed")
        else:
            print("Dispense Now word did not display")
            pytest.fail("Dispense Now word did not display")
        dis_color =  el.value_of_css_property("background-color")
        if dis_color == color:
            print("Verified Dispense Now Color is Red RGBA: "+dis_color)
        else:
            print("Dispense Now color not matched. Actual: "+dis_color+" Expected: "+color)
            pytest.fail("Dispense Now color not matched. Actual: "+dis_color+" Expected: "+color)
    except Exception:
        pytest.fail("Failed to Dispense Now Text or Color")

def verify_cash_dispense(driver):
    try:
        el = driver.find_element_by_xpath("//div[text()='Cash dispensed']")
        scroll_to_element(driver, el)
        if el:
            print("Cash Dispense displayed")
        else:
            print("Cash Dispense did not displayed")
            pytest.fail("Cash Dispense did not displayed")
    except Exception:
        pytest.fail("Failed to verify cash dispense")