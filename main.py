from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.spotify.com/mx/")

driver.find_element_by_id("header-login-link").click()

driver.find_element_by_class_name("btn-facebook").click()

driver.find_element_by_name("email").send_keys("nokoayzack@gmail.com")
driver.find_element_by_name("pass").send_keys("Metallica#1")
driver.find_element_by_name("login").click()
driver.find_element_by_id("nav-link-play").click()
driver.implicitly_wait(10)

while(True):
    driver.find_element_by_class_name("navBar-link").click()
    driver.find_element_by_class_name("inputBox-input").clear()
    driver.find_element_by_class_name("inputBox-input").send_keys(input("Canción: "))

    driver.implicitly_wait(3)

    driver.find_element_by_link_text('CANCIONES').click()
    driver.find_element_by_class_name("tracklist-name").click()
    driver.find_element_by_class_name("more").click()
    context_elements = driver.find_elements_by_class_name("react-contextmenu-item")
    context_elements[2].click()
