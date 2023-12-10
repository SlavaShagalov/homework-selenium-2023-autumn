from selenium.webdriver.common.by import By


class BasePageLocators:
    @staticmethod
    def by_test_id(id):
        return By.CSS_SELECTOR, f"[data-test-id='{id}']"


class LoginPageLocators(BasePageLocators):
    MAIL_RU_AUTH_BTN = BasePageLocators.by_test_id('oAuthService_mail_ru')
    MAIL_RU_LOGIN_INPUT = (By.NAME, 'username')
    MAIL_RU_ENTER_PASSWORD_BTN = BasePageLocators.by_test_id('next-button')
    MAIL_RU_PASSWORD_INPUT = (By.NAME, 'password')
    MAIL_RU_SUBMIT_BTN = BasePageLocators.by_test_id('submit-button')


class HqPageLocators(BasePageLocators):
    pass


class AudiencePageLocators(BasePageLocators):
    AUDIENCE_TAB = (By.ID, 'tab_audience')
    USERS_TAB = (By.ID, 'tab_audience.users_list')


class CampaignPageLocators:
    CAMPAIGN_TAB = (By.ID, 'dashboardV2.plans')
    GROUPS_TAB = (By.ID, 'dashboardV2.groups')
    ADS_TAB = (By.ID, 'dashboardV2.ads')
    PLAN_CREATION_BTN = BasePageLocators.by_test_id('create-button')

class BudgetPageLocators:
    PAY_MODAL_BTN = (By.CLASS_NAME, 'AccountInfo_payButton__i1QFc')
    PAY_MODAL = (By.ID, '_modal_26')
    PAY_BTN = (By.XPATH, "//div[contains(@class, 'vkuiFormItem')]//button[contains(string(), 'Пополнить счёт')]")
    AMOUNT_INPUT = (By.NAME, 'amount')
    AMOUNT_WITHOUT_VAT_INPUT = (By.NAME, 'amountWithoutVat')
    MIN_AMOUNT_ERR_MSG = (By.XPATH, "//*[contains(@class, 'vkuiFormItem__bottom') and contains(string(), 'минимальная "
                                    "сумма 600,00 ₽')]")
    PAYMENT_METHOD_FORM = (By.XPATH, "//iframe[contains(@title, 'Счёт')]")
    RANGE_DATA_PICKER_WIDGET = (By.XPATH, "//div[contains(@class, 'RangeDatePicker')]")
    RANGE_DATA_PICKER_BTN = (By.XPATH, "//button[contains(@class, 'ActionsBlock_simpleButton__gfmux')]")
   # PERIOD_BTN

