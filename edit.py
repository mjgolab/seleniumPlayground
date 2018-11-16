from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
"""
SELENIUM PLAYGROUND 
Messing around with Selenium WebDriver on Leafground's webpage.
Completion of tasks in labels. Working with basic input fields in 'Edit' section.
"""
class SP_Edit():
    # Setup.
    driverLocation = "C:\\Users\\Marcin\\Documents\\PyCharm\\automation\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverLocation

    # Instantiate the web driver. Proceed to the following address.
    driver = webdriver.Chrome(driverLocation)
    driver.get('http://www.leafground.com/')

    # Find an element with an anchor tag and text 'Edit' associated with it. Call the click() method on that object.
    driver.find_element_by_link_text('Edit').click()

    # Find input field with an id of 'email'.
    mail_input_field = driver.find_element_by_id('email')

    # Store sample email address in a variable.
    mail = "someone@example.com"

    # Create a loop that will insert every character of the string one-by-one in that text field, giving it
    # nice automation touch, instead of inserting it all abruptly.
    for characters in mail:
        mail_input_field.send_keys(characters)

    # Find next element and append text to it. Simulate press of a TAB key.
    driver.find_element_by_xpath('//*[@id="contentblock"]/section/div[2]/div/div/input').send_keys("ed the text!", Keys.TAB)

    # Find another input element. Get the property and store it in a variable. Print its result to the console.
    # Cannot use 'find_element_by_name' method here since two input fields share the same property, here: 'username'!
    value = driver.find_element_by_xpath('//*[@id="contentblock"]/section/div[3]/div/div/input').get_property('value')
    print("The default value used in the third input field is {0}.".format(value))

    # Yet another input element. This time clear the text inside.
    driver.find_element_by_xpath('//*[@id="contentblock"]/section/div[4]/div/div/input').clear()

    # Confirm that the last input element is disabled.
    # First method.
    # var = driver.find_element_by_xpath('//*[@id="contentblock"]/section/div[5]/div/div/input').get_attribute('disabled')
    # print("Is the last input element disabled?: {0}.".format(var))
    # Second method.
    var = driver.find_element_by_xpath('//*[@id="contentblock"]/section/div[5]/div/div/input').is_enabled()
    print("Is the last input element enabled to the user?: {0}.".format(var))


var = SP_Edit()