import pytest
from selenium import webdriver
import logging
from webdriver_manager.microsoft import IEDriverManager

@pytest.fixture(scope="session", autouse=True)
# Set up logging configuration
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("test_log.log"),  # Logs to a file
            logging.StreamHandler()               # Also prints to the console
        ]
    )
    logger = logging.getLogger("TestLogger")
    return logger
# Define a pytest command-line option to specify the browser type

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser option: chrome or firefox"
    )

# Set up a fixture for browser instance based on the command-line argument
@pytest.fixture(scope="function")
def browser(request,setup_logging):
    logger = setup_logging
    browser_type = request.config.getoption("--browser").lower()

    # Log the browser type being used
    logger.info(f"Selected browser: {browser_type}")

    # Initialize the WebDriver based on the selected browser
    try:
        if browser_type == "chrome":
            logger.info("Starting Chrome browser")
            driver = webdriver.Chrome()
        elif browser_type == "firefox":
            logger.info("Starting Firefox browser")
            driver = webdriver.Firefox()
        elif browser_type == "ie":
            logger.info("Starting Internet Explorer browser")
            driver = webdriver.Ie(IEDriverManager().install())
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

        # Log successful browser startup
        logger.info(f"{browser_type.capitalize()} browser started successfully")

    except Exception as e:
        logger.error(f"Failed to start {browser_type} browser: {e}")
        raise


    #request.cls.driver = driver
    # Provide the browser driver instance to the tests
    yield driver


    # Clean up by closing the browser after the test
    logger.info(f"Closing {browser_type} browser")
    driver.quit()
    logger.info(f"{browser_type.capitalize()} browser closed")






