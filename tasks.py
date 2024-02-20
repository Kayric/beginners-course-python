from robocorp.tasks import task
from robocorp import browser

@task
def robot_spare_bin_python():
    """Insert the weekly sales data and export it as PDF"""
    open_the_intranet_website()
    log_in()

def open_the_intranet_website():
    """Navigate to the intranet website"""
    browser.goto("https://robotsparebinindustries.com/")

def log_in():
    """Fill the form and Log in to the intranet"""
    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")
