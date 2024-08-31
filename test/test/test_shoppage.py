import pytest
from test.pages.shop_page import ShopPage
from utilities.screenshot import take_screenshot


@pytest.mark.shop
def test_shopping(browser, setup_logging):
    logger = setup_logging  # Get logger from the logging fixture
    logger.info("Starting shopping page test")

    shop_page = ShopPage(browser)

    shop_page.launch_shop()

    shop_page.assert_shop_page_title()

    screenshot_path = take_screenshot(browser, prefix='success')
    print(f"shoppgae Screenshot saved to  {screenshot_path}")









