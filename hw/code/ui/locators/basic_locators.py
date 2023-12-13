from selenium.webdriver.common.by import By


class BasePageLocators:
    GO_TO_CABINET_BTN = By.CLASS_NAME, 'ButtonCabinet_primary__KQnu7'
    OPTIONS = (By.XPATH, f"//*[contains(concat(' ', @class, ' '), ' vkuiCustomSelectOption ')]")

    @staticmethod
    def by_css_selector(selector, id):
        return By.CSS_SELECTOR, f"[{selector}='{id}']"

    @staticmethod
    def by_option(text):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']"


class LoginPageLocators(BasePageLocators):
    MAIL_RU_AUTH_BTN = BasePageLocators.by_css_selector('data-test-id', 'oAuthService_mail_ru')
    MAIL_RU_LOGIN_INPUT = (By.NAME, 'username')
    MAIL_RU_ENTER_PASSWORD_BTN = BasePageLocators.by_css_selector('data-test-id', 'next-button')
    MAIL_RU_PASSWORD_INPUT = (By.NAME, 'password')
    MAIL_RU_SUBMIT_BTN = BasePageLocators.by_css_selector('data-test-id', 'submit-button')


class RegistrationPageLocators(BasePageLocators):
    CREATE_CABINET_BTN = BasePageLocators.by_css_selector('data-testid', 'create-new')


class CreateCabinetPageLocators(BasePageLocators):
    AGENCY_RADIO = (By.XPATH, f".//*[text()='Агентство']")
    PHYSICAL_RADIO = BasePageLocators.by_css_selector('data-testid', 'physical')
    COUNTRY_SELECT = BasePageLocators.by_css_selector('data-testid', 'country')
    CURRENCY_SELECT = BasePageLocators.by_css_selector('data-testid', 'currency')
    EMAIL_FIELD = BasePageLocators.by_css_selector('data-testid', 'email')
    TERMS_CHECK = (By.CLASS_NAME, "registration_offerTitle__BqyqW")
    SUBMIT_BTN = BasePageLocators.by_css_selector('data-testid', 'create-button')
    EMAIL_ERROR = (By.CLASS_NAME, 'vkuiFootnote')
    TERMS_ERROR = (By.CLASS_NAME, 'vkuiFootnote')
    FORM_ERROR = (By.CLASS_NAME, 'vkuiFormStatus--mode-error')


class HqPageLocators(BasePageLocators):
    pass


class AudiencePageLocators(BasePageLocators):
    # Navigate
    AUDIENCE_TAB = (By.ID, 'tab_audience')
    USERS_TAB = (By.ID, 'tab_audience.users_list')

    # Create
    CREATE_AUDIENCE_BTN = BasePageLocators.by_css_selector('data-testid', 'create-audience')
    AUDIENCE_TITLE_INPUT = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    ADD_SRC_BTN = (By.XPATH, "//button[contains(., 'Добавить источник')]")

    KEYWORDS_TITLE_INPUT = (By.XPATH,
                            "//div[contains(@class, 'ModalRoot_overlay')][contains(., 'Ключевые фразы')]//input")
    KEYWORDS_INPUT = (By.XPATH, "//*[not(contains(@class, 'KeyPhrases_negationPhrases'))]/*/textarea")
    NEG_KEYWORDS_INPUT = (By.XPATH, "//*[contains(@class, 'KeyPhrases_row')]/*/textarea")
    KEYWORDS_SAVE_BTN = (By.XPATH,
                         "//div[contains(@class, 'ModalRoot_overlay')][contains(., 'Ключевые фразы')]//button[contains(., 'Сохранить')]")
    SAVE_AUDIENCE_BTN = (By.XPATH, "//button[contains(., 'Сохранить')]")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'ModalRoot_overlay')]")

    TITLE_ERROR = (By.XPATH, "//*[contains(@class, 'vkuiFootnote')][text()='Максимальная длина 255 символов']")

    # Delete
    AUDIENCE_OPTION = (By.XPATH, "//label[contains(@data-testid, 'dropdown-item')]")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[contains(., 'Удалить')]")

    @staticmethod
    def src_by_text(text):
        return By.XPATH, f"//div[contains(@class, 'vkuiSimpleCell')][contains(., '{text}')]"

    @staticmethod
    def audience_details_btn_by_name(name):
        return By.XPATH, f"//div[contains(@class, 'NameCell_wrapper')][contains(., '{name}')]//button[contains(@data-testid, 'audience-item-menu')]"


class SettingsPageLocators(BasePageLocators):
    # Navigate
    GENERAL_TAB = (By.ID, 'tab-settings')
    NOTIFICATIONS_TAB = (By.ID, 'tab-settings.notifications')
    ACCESS_TAB = (By.ID, 'tab-settings.access')
    HISTORY_TAB = (By.ID, 'tab-settings.logs')

    PHONE_INPUT = (By.XPATH, "//*[contains(@data-testid, 'general-phone')]")
    FIO_INPUT = BasePageLocators.by_css_selector('data-testid', 'general-ord-name')
    INN_INPUT = BasePageLocators.by_css_selector('data-testid', 'general-ord-inn')
    FORM_CONTROL_BTNS = (By.XPATH, "//*[contains(@class, 'FormControls_buttons')]")
    SAVE_BTN = (By.XPATH, "//button[contains(@data-testid, 'settings-save')]")

    PHONE_INVALID_ERROR = (
        By.XPATH, "//*[contains(@class, 'vkuiFootnote')][contains(., 'Некорректный номер телефона')]")
    PHONE_MIN_ERROR = (
        By.XPATH, "//*[contains(@class, 'vkuiFootnote')][contains(., 'Телефон не может быть короче 12 цифр')]")
    FIO_INVALID_ERROR = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem')][contains(., 'ФИО')][contains(., 'Значение не может содержать только пробелы')]")
    FIO_INVALID_CHARS_ERROR = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem')][contains(., 'ФИО')][contains(., 'Некорректные символы. Разрешена только кириллица дефис и пробел')]")
    INN_INVALID_ERROR = (
        By.XPATH, "//*[contains(@class, 'vkuiFormItem')][contains(., 'ИНН')][contains(., 'Некорректный ИНН')]")
    INN_TOO_SHORT_ERROR = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem')][contains(., 'ИНН')][contains(., 'Длина ИНН должна быть 12 символов')]")

    # Delete cabinet
    DELETE_CABINET_BTN = (By.XPATH, "//button[contains(@class, 'DeleteAccount_button')]")
    CONFIRM_DELETE_CABINET_BTN = (By.XPATH, "//button[contains(., 'Да, удалить')]")


class SettingsNotificationsPageLocators(BasePageLocators):
    NOTIFICATION_ENABLE_BTN = (By.XPATH, "//*[contains(@class, 'Emails_item')]//*[contains(@class, 'vkuiSwitch')]")
    WARNING_HINT = (By.XPATH, "//*[contains(@class, 'Warning_warning')]")

    SAVE_BTN = (By.XPATH, "//button[contains(@data-testid, 'settings-save')]")

    @staticmethod
    def checkbox_by_name(name):
        return By.XPATH, f"//label[contains(@class, 'vkuiCheckbox')][contains(., '{name}')]//input"

    @staticmethod
    def item_by_name(name):
        return By.XPATH, f"//label[contains(@class, 'vkuiCheckbox')][contains(., '{name}')]"
