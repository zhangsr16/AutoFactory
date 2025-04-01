import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.gov.cn/zhengce/zuixin/home.htm")
    # /XPATH
    element = page.query_selector('//html/body/div[3]/div/div/div[2]/div[1]/ul/li[1]/h4/a')
    if element:
        print(element.inner_text())
    # ---------------------END
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
