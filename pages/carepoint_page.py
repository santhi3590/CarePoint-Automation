
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CarePointPage(BasePage):

    # Locators
    FIRST_NAME = (By.ID, "forms-first-name")
    LAST_NAME = (By.ID, "forms-last-name")
    EMAIL = (By.ID, "forms-email")
    SUBMIT_BUTTON = (By.ID, "forms-submit")

    # Open website
    def open_carepoint(self, url):
        self.open_url(url)

    # Get page title
    def get_page_title(self):
        return self.driver.title

    # Enter first name
    def enter_first_name(self, name):
        self.enter_text(self.FIRST_NAME, name)

    # Enter last name
    def enter_last_name(self, name):
        self.enter_text(self.LAST_NAME, name)

    # Enter email
    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    # Scroll to Submit button and click
    def click_submit(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.SUBMIT_BUTTON)
        )

        # Scroll the button into view
        self.driver.execute_script("""
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center',
                behavior: 'instant'
            });
        """, element)

        # Move slightly upward to keep the button visible
        self.driver.execute_script("window.scrollBy(0, -200);")

        # Print button position for debugging
        details = self.driver.execute_script("""
            const b = arguments[0];
            const r = b.getBoundingClientRect();
            const x = r.left + r.width / 2;
            const y = r.top + r.height / 2;
            const top = document.elementFromPoint(x, y);

            return {
                buttonY: r.y,
                buttonBottom: r.bottom,
                viewportHeight: window.innerHeight,
                pageScrollY: window.scrollY,
                documentHeight: document.documentElement.scrollHeight,
                topElement: top ? top.outerHTML : "None"
            };
        """, element)

        print("SUBMIT BUTTON DEBUG:", details)

        # Wait until the button is clickable
        element = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )

        # Click Submit
        element.click()

        self.driver.implicitly_wait(2)

        print("URL after submit:", self.driver.current_url)
        print("Page title after submit:", self.driver.title)
        print("Page text after submit:", self.driver.find_element(
            By.TAG_NAME, "body"
        ).text[-1000:])