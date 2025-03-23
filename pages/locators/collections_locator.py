from selenium.webdriver.common.by import By


first_name_field_loc = (By.ID, "firstname")
last_name_field_loc = (By.ID, "lastname")
email_field_loc = (By.ID, "email_address")
password_field_loc = (By.ID, "password")
password_confirmation_loc = (By.ID, "password-confirmation")
button_create_an_account = (By.CSS_SELECTOR, ".action.submit.primary")
success_message_loc = (By.XPATH, "//div[@class='message-success success message']/div")
error_message_password_8symbols_loc = (By.XPATH, "//div[@id='password-error']")


style_menu_loc = (By.XPATH, "(//div[@class='filter-options-title'])[2]")
style_menu_tee_loc =(By.XPATH, "((//div[@class='filter-options-content'])[2]/ol/li/a)[8]")
size_menu_loc = (By.XPATH, "(//div[@class='filter-options-title'])[1]")
size_menu_XL_loc =(By.XPATH, "//a/div[contains(text(), 'XL')]")
climate_menu_loc = (By.XPATH, "(//div[@class='filter-options-title'])[1]")
climate_menu_indoor_loc =(By.XPATH, "((//div[@class='filter-options-content'])/ol/li/a)[2]")
color_menu_loc = (By.XPATH, "(//div[@class='filter-options-title'])[1]")
color_menu_blue_loc = (By.XPATH, "(//div[@class='filter-options-content']/div/div/a/div)[2]")
color_tee_first_wight_loc =  (By.XPATH, "(//div[@class='swatch-attribute color']/div/div)[3]")


now_shopping_by_number_loc = (By.XPATH, "//strong[@data-count='4']")
message_add_to_comparison_list_loc = (
    By.XPATH, "//div[contains(@data-bind, 'html: $parent.prepareMessageForHtml(message.text)')]")
filter_current_items_loc = (By.CSS_SELECTOR, ".filter-current .items .item")
filter_label_loc = (By.CSS_SELECTOR, ".filter-label")
filter_value_loc = (By.CSS_SELECTOR, ".filter-value")
button_comparison_list_loc = (By.XPATH, "//div[@class='message-success success message']/div/a")
product_items_loc = (By.XPATH, "//button/span[contains(text(), 'Add to Cart')]")
