from selenium import webdriver

browsers = ["chrome", "firefox", "edge"]

for browser in browsers:

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    driver.get("YOUR_DEMO_WEBSITE_URL")

    print(browser, driver.title)

    driver.quit()