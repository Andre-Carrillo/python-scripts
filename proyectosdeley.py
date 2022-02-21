from selenium import webdriver

#START PAGE
driver = webdriver.Chrome('C:\SelleniumDrivers\chromedriver')
driver.get('https://wb2server.congreso.gob.pe/spley-portal/#/expediente/search')
driver.implicitly_wait(5)

#START FILETERER
filter_button = driver.find_element_by_class_name('p-button-outlined')
filter_button.click()
driver.implicitly_wait(5)

def get_comisiones_buttons() -> list:
    comisiones_button = driver.find_elements_by_tag_name('p-dropdown')[1]
    comisiones_button.click()
    return comisiones_button.find_element_by_class_name('ng-trigger').\
                    find_element_by_tag_name('ul').find_elements_by_css_selector('*')
a = get_comisiones_buttons()
print('_'*20)
print([i.text for i in a])
# for i in get_comisiones_buttons():
    # print('f'i)
