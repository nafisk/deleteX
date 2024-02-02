from playwright.sync_api import sync_playwright

EMAIL = 'nafisrizwank@gmail.com'
PASSWORD = 'Twitternafis566yolo'

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = browser.new_page()

    # Navigate to the Twitter login page
    page.goto("https://twitter.com/i/flow/login")

    # Fill in the email (or username) field
    # You need to replace 'your_email_or_username' with the actual email or username
    page.fill("input[name='text']", EMAIL)

    # Click on 'Next' button
    page.click("span:has-text('Next')")

    # Wait for a couple of seconds for the password field to appear
    page.wait_for_timeout(2000)  # Waits for 2 seconds

    # Check for the password input field
    page.fill("input[name='password']", PASSWORD)
    
    # If there is an additional step to verify with user name
    
    
    
    # Click on 'Next' button
    page.click("span:has-text('Log in')")
   
    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
