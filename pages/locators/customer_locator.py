from selenium.webdriver.common.by import By


first_name_field_loc = (By.ID, "firstname")
last_name_field_loc = (By.ID, "lastname")
email_field_loc = (By.ID, "email_address")
password_field_loc = (By.ID, "password")
password_confirmation_loc = (By.ID, "password-confirmation")
button_create_an_account = (By.CSS_SELECTOR, ".action.submit.primary")
success_message_loc = (By.XPATH, "//div[@class='message-success success message']/div")
error_message_password_8symbols_loc = (By.XPATH, "//div[@id='password-error']")
