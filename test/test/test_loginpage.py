import pytest

from test.pages.base_page import BasePage
from test.pages.login_page import LoginPage
from utilities.screenshot import take_screenshot


@pytest.mark.login
def test_loginpage(browser,setup_logging):
    logger = setup_logging  # Get logger from conftest.py
    logger.info("Starting to test login_page")
    try:
        login_page = LoginPage(browser)
        login_page.enter_name("pramila")
        login_page.enter_email("pramilaeceian@gmail.com")
        login_page.enter_password("Seplnt@2024")
        #login_page.select_gender("Female")
        login_page.select_emplystatus("Student")
        logger.info("Test login_page PASSED")

        screenshot_path = take_screenshot(browser, prefix='success')
        print(f"Screenshot saved to {screenshot_path}")

    except Exception as e:
        logger.error(f"Test failed: {e}")

        screenshot_path = take_screenshot(browser, prefix='error')
        print(f"An error occurred: {e}")
        print(f"Screenshot saved to {screenshot_path}")

        pytest.fail(f"Test failed with exception: {e}")


