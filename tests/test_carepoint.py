
from config.settings import BASE_URL
from pages.carepoint_page import CarePointPage


def test_carepoint_website_opens(driver):
    carepoint_page = CarePointPage(driver)
    carepoint_page.open_carepoint(BASE_URL)

    assert carepoint_page.get_page_title() != ""


def test_enter_first_name(driver):
    carepoint_page = CarePointPage(driver)
    carepoint_page.open_carepoint(BASE_URL)

    carepoint_page.enter_first_name("Santhima")

    assert driver.find_element(
        "id", "forms-first-name"
    ).get_attribute("value") == "Santhima"


def test_enter_last_name(driver):
    carepoint_page = CarePointPage(driver)
    carepoint_page.open_carepoint(BASE_URL)

    carepoint_page.enter_last_name("Tester")

    assert driver.find_element(
        "id", "forms-last-name"
    ).get_attribute("value") == "Tester"


def test_enter_email(driver):
    carepoint_page = CarePointPage(driver)
    carepoint_page.open_carepoint(BASE_URL)

    carepoint_page.enter_email("test@example.com")

    email_value = driver.find_element(
        "id", "forms-email"
    ).get_attribute("value")

    assert email_value == "test@example.com"

    print("Email entered successfully!")


def test_submit_button_click(driver):
    carepoint_page = CarePointPage(driver)
    carepoint_page.open_carepoint(BASE_URL)

    carepoint_page.enter_first_name("Santhima")
    carepoint_page.enter_last_name("Tester")
    carepoint_page.enter_email("test@example.com")

    carepoint_page.click_submit()

    # Verify that the page has a valid title and URL
    assert driver.current_url != ""
    assert driver.title != ""

    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)
    print("Submit button test completed.")

def test_invalid_email(driver):
    carepoint_page = CarePointPage(driver)
    carepoint_page.open_carepoint(BASE_URL)

    carepoint_page.enter_first_name("Santhima")
    carepoint_page.enter_last_name("Tester")
    carepoint_page.enter_email("invalid-email")

    carepoint_page.click_submit()

    email_field = driver.find_element(
        "id", "forms-email"
    )

    assert email_field.get_attribute("value") == "invalid-email"
    assert email_field.get_attribute("type") == "email"


def test_missing_first_name(driver):
    carepoint_page = CarePointPage(driver)
    carepoint_page.open_carepoint(BASE_URL)

    carepoint_page.enter_last_name("Tester")
    carepoint_page.enter_email("test@example.com")

    carepoint_page.click_submit()

    first_name = driver.find_element(
        "id", "forms-first-name"
    )

    assert first_name.get_attribute("value") == ""

    page_text = driver.find_element(
        "tag name", "body"
    ).text

    assert "First Name is required" in page_text

def test_missing_phone_number(driver):
    carepoint_page = CarePointPage(driver)
    carepoint_page.open_carepoint(BASE_URL)

    carepoint_page.click_submit()

    page_text = driver.find_element(
        "tag name", "body"
    ).text

    assert "Phone Number is required" in page_text
