import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url=sys.argv[1]
print("Testolino is running")
driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://'+ url+ ':5000/');
time.sleep(1) # Let the user actually see something!
region_box = driver.find_element_by_id('comboA')
region_box.send_keys( Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER )
time.sleep(1) # Let the user actually see something!a
instance_box = driver.find_element_by_id('comboA')
instance_box.send_keys( Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER )
time.sleep(1) # Let the user actually see something!a
table = driver.find_element_by_tag_name("table");
driver.quit()
print('testolino is ended without error')