import config

# https://cloud-qa2.sigma.land/login

XPATH_INPUT_EMAIL = "//input[contains(@placeholder, 'Email или телефон')]"
XPATH_INPUT_PASSWORD = "//input[contains(@placeholder, 'Пароль')]"
XPATH_SUBMIT_BUTTON = "//button[contains(., 'Войти')]"

# https://cloud-qa2.sigma.land/subscription
XPATH_CURRENT_CASH_REGISTER = f"//*[contains(text(), '{config.SIGMA_CLOUD_CASH_REGISTER}')]"
XPATH_NEW_CODE_BUTTON = "//button[@data-label=\"Новый код\"]"
XPATH_SECRET_CODE = "//p[@data-testid='registrationCode']"
XPATH_CLOSE_MODAL_WINDOW = "//span[@data-testid='cashboxModalCloseCrossIcon']"
XPATH_USERS = "//div[text()=\"Пользователи\"]"
XPATH_PROFILE = f"//td[contains(text(),'{config.SIGMA_CLOUD_EMAIL}')]"
XPATH_PIN = "//div[@data-label=\" Пин-код от кассы\"]"
