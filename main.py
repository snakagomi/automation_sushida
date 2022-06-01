from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

CHROME_DRIVER = webdriver.Chrome(ChromeDriverManager().install())


def main():
    CHROME_DRIVER.get('http://typingx0.net/sushida/play.html?soundless')
    sleep(10)
    actions = ActionChains(CHROME_DRIVER)
    actions.move_by_offset(250, 300)
    actions.click()
    actions.perform()


if __name__ == '__main__':
    main()
