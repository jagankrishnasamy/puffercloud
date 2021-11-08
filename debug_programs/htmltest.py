from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Jagan\Documents\ECE 29401\puffercloud\chromedriver.exe')
driver.get("https://www.cloudlab.us/login.php")

username = driver.find_element_by_name("uid")
password = driver.find_element_by_name("password")
username.send_keys("krish133")
password.send_keys("<Enter Password>")
driver.find_element_by_id("quickvm_login_modal_button").click()

driver.get("https://www.cloudlab.us/user-dashboard.php#profiles")

with open("page_source.html", "w") as f:
    f.write(driver.page_source)