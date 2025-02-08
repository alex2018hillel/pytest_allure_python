import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")

    # service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # service = Service("/usr/local/bin/chromedriver")
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()