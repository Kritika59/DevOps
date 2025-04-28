from selenium import webdriver
import pytest

# Sample Selenium test with pytest
@pytest.fixture
def setup():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(executable_path="path/to/chromedriver")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_example_com(setup):
    driver = setup
    driver.get("https://www.example.com")
    
    # Perform some actions and assertions
    assert "Example Domain" in driver.title

    # You can add more tests/assertions here
