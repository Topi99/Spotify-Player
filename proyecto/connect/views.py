from django.shortcuts import render
from django.views import View
from selenium import webdriver
import getpass

class Index(View):
    driver = webdriver.Chrome("/home/topi/Documentos/Tec/Segundo/Orga/proyecto/proyecto/connect/chromedriver")
    driver.get("https://www.spotify.com/mx/")

    driver.find_element_by_id("header-login-link").click()

    driver.find_element_by_class_name("btn-facebook").click()

    driver.find_element_by_name("email").send_keys(input("Ingresa tu correo: "))
    driver.find_element_by_name("pass").send_keys(getpass.getpass())
    driver.find_element_by_name("login").click()
    driver.find_element_by_id("nav-link-play").click()
    driver.implicitly_wait(10)



    def get(self, request, song):

        self.driver.find_element_by_class_name("navBar-link").click()
        self.driver.find_element_by_class_name("inputBox-input").clear()
        self.driver.find_element_by_class_name("inputBox-input").send_keys(song.replace("-"," "))

        self.driver.implicitly_wait(3)

        self.driver.find_element_by_link_text('CANCIONES').click()
        self.driver.find_element_by_class_name("tracklist-name").click()
        self.driver.find_element_by_class_name("more").click()
        context_elements = self.driver.find_elements_by_class_name("react-contextmenu-item")
        context_elements[2].click()

        return render(request, 'connect/index.html')
