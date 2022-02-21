from selenium import webdriver
# import os

# os.environ['PATH'] += r'C:\SelleniumDrivers'
# print(os.environ['PATH'])
driver = webdriver.Chrome('C:\SelleniumDrivers\chromedriver')


driver.get('https://www.congreso.gob.pe/CuadrodeComisiones/')
driver.implicitly_wait(5)

selector = driver.find_element_by_name('fld_78_Comision')
selector.click()
driver.implicitly_wait(2)

selector_options = selector.find_elements_by_tag_name('option')
selector_options[0].click()