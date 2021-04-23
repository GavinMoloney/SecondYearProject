from selenium import webdriver
from selenium.webdriver.common import keys

# Launch and open the browser
my_chrome_browser = webdriver.Chrome(executable_path=r"c:\\webdriver\\chromedriver.exe")


# Go and get the HTML
app_url = "http://127.0.0.1:8000/create/"
my_chrome_browser.get(app_url)

my_chrome_browser.implicitly_wait(2)

if my_chrome_browser.current_url != app_url:
    print("Wrong page loaded")
else:

    print("Worked!")

#check the page title
expexted_title = "Create a new account"
actual_title = my_chrome_browser.title

#assert
assert expexted_title in actual_title

#verify
if expexted_title != actual_title:
    print("Error")
else:
    userid_element = my_chrome_browser.find_element_by_name("username")
    email_element = my_chrome_browser.find_element_by_name("email")
    password_element = my_chrome_browser.find_element_by_name("password1")
    password_conf_element = my_chrome_browser.find_element_by_name("password2")

    if userid_element.is_displayed() and email_element.is_displayed() and password_element.is_displayed() and password_conf_element.is_displayed():
        btn_element = my_chrome_browser.find_elements_by_class_name("btn-red")
        btn_element.submit()

        userid_element.send_keys("kameltest")
        email_element.send_keys("Kameltest@gmail.com")
        password_element.send_keys("Test123")
        password_conf_element.send_keys("Test123")

        button_element = my_chrome_browser.find_elements_by_class_name("btn")
        button_element.submit()

        assert "http://127.0.0.1:8000/create/" in my_chrome_browser.title

    else:
        print("Missing elements cannot proceed!")

#close browsers
my_chrome_browser.close()
my_chrome_browser.quit()