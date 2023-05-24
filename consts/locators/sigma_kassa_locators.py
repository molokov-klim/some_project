# coding: utf-8

PACKAGE = "ru.sigma.app.debug"
ACTIVITY_LAUNCHABLE = ("ru.sigma.app.debug", "ru.qasl.core.splash.SplashActivity")

SPINNER = (
    "xpath", "//android.view.ViewGroup[@resource-id='ru.sigma.app.debug:id/spinnerView']")

# <ПЕРВЫЙ ЗАПУСК>

# ОКНО ПРИВЕТСТВИЯ
WELCOME_TV_MESSAGE = ("id", "ru.sigma.app.debug:id/greeting")
WELCOME_TV_MESSAGE_TEXT = 'Добро пожаловать в АТОЛ SIGMA!'
WELCOME_BTN_NEXT = ("id", "ru.sigma.app.debug:id/nextButton")

# ОКНО ВЫБОРА СТРАНЫ
COUNTRY_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
COUNTRY_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
COUNTRY_TV_TITLE_TEXT = "Выберите страну"
COUNTRY_BTN_RUSSIA = ("id", "ru.sigma.app.debug:id/russiaButton")
COUNTRY_BTN_KYRGYZSTAN = ("id", "ru.sigma.app.debug:id/kgButton")
COUNTRY_BTN_NEXT = ("id", "ru.sigma.app.debug:id/verticalActionButton")

# ОКНО ВЫБОРА ТИПА БИЗНЕСА
BUSINESS_TYPE_TV_TITLE = ("xpath", ".//android.widget.TextView[contains(@text, 'Укажите ваш тип бизнеса')]")
BUSINESS_TYPE_TV_TITLE_TEXT = 'Укажите ваш тип бизнеса'
BUSINESS_TYPE_BTN_RESTAURANT = ("id", "ru.sigma.app.debug:id/restaurantButton")
BUSINESS_TYPE_BTN_RETAIL = ("id", "ru.sigma.app.debug:id/retailButton")
BUSINESS_TYPE_BTN_SERVICE = ("id", "ru.sigma.app.debug:id/serviceButton")
BUSINESS_TYPE_BTN_NEXT = ("id", "ru.sigma.app.debug:id/verticalActionButton")

# ОКНО РЕГИСТРАЦИИ
REGISTRATION_TV_WELCOME_MESSAGE = ("id", "ru.sigma.app.debug:id/greeting")
REGISTRATION_TV_WELCOME_MESSAGE_TEXT = 'Добро пожаловать\nв приложение Sigma Торговля!'
REGISTRATION_TV_COUNTRY = ("id", "ru.sigma.app.debug:id/countryTextView")
REGISTRATION_BTN_LOGO = ("id", "ru.sigma.app.debug:id/logo")
REGISTRATION_TV_SERVER = ("id", "ru.sigma.app.debug:id/apiLabel")
REGISTRATION_BTN_REGISTRATION = ("id", "ru.sigma.app.debug:id/registrationButton")
REGISTRATION_BTN_DEVICE_CODE = ("id", "ru.sigma.app.debug:id/deviceCode")
REGISTRATION_BTN_BACK_TO_WELCOME_WINDOW = ("id", "ru.sigma.app.debug:id/changeBusinessTypeButton")

# МОДАЛЬНОЕ ОКНО СМЕНЫ КОНТУРА
MODAL_CHANGE_SERVER_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
MODAL_CHANGE_SERVER_TV_CURRENT_SERVER = ("id", "ru.sigma.app.debug:id/serverSettingsCurrentTextView")
MODAL_CHANGE_SERVER_BTN_SWITCH = ("id", "ru.sigma.app.debug:id/serverSettingsSwitcherSpinner")
MODAL_CHANGE_SERVER_MENU_ITEM_ENTER_QA2 = ("xpath", ".//android.widget.TextView[@text='https://enter-qa2.sigma.land']")
MODAL_CHANGE_SERVER_BTN_OK = ("id", "ru.sigma.app.debug:id/okButton")
MODAL_CHANGE_SERVER_BTN_CANCEL = ("id", "ru.sigma.app.debug:id/cancelButton")

# ОКНО ВВОДА КОДА УСТРОЙСТВА
ENTER_DEVICE_CODE_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
ENTER_DEVICE_CODE_TV_TITLE_TEXT = 'Введите код устройства'
ENTER_DEVICE_CODE_BTN_INFO = ("id", "ru.sigma.app.debug:id/infoButtonIV")

ENTER_DEVICE_CODE_TV_MESSAGE = ("id", "ru.sigma.app.debug:id/contentMessageTextView")
ENTER_DEVICE_CODE_TV_MESSAGE_TEXT_WRONG = 'Неверный код устройства'
ENTER_DEVICE_CODE_TV_MESSAGE_TEXT_ALREADY_USED = 'Код уже был использован.\nСгенерируйте новый код в Личном кабинете'

ENTER_DEVICE_CODE_CARD_DIGIT_1 = ("id", "ru.sigma.app.debug:id/digit1")
ENTER_DEVICE_CODE_CARD_DIGIT_2 = ("id", "ru.sigma.app.debug:id/digit2")
ENTER_DEVICE_CODE_CARD_DIGIT_3 = ("id", "ru.sigma.app.debug:id/digit3")
ENTER_DEVICE_CODE_CARD_DIGIT_4 = ("id", "ru.sigma.app.debug:id/digit4")
ENTER_DEVICE_CODE_CARD_DIGIT_5 = ("id", "ru.sigma.app.debug:id/digit5")
ENTER_DEVICE_CODE_CARD_DIGIT_6 = ("id", "ru.sigma.app.debug:id/digit6")

ENTER_DEVICE_CODE_NUM_PAD = {
    "0": ("id", "ru.sigma.app.debug:id/buttonZero"),
    "1": ("id", "ru.sigma.app.debug:id/buttonOne"),
    "2": ("id", "ru.sigma.app.debug:id/buttonTwo"),
    "3": ("id", "ru.sigma.app.debug:id/buttonThree"),
    "4": ("id", "ru.sigma.app.debug:id/buttonFour"),
    "5": ("id", "ru.sigma.app.debug:id/buttonFive"),
    "6": ("id", "ru.sigma.app.debug:id/buttonSix"),
    "7": ("id", "ru.sigma.app.debug:id/buttonSeven"),
    "8": ("id", "ru.sigma.app.debug:id/buttonEight"),
    "9": ("id", "ru.sigma.app.debug:id/buttonNine"),
    "backspace": ("id", "ru.sigma.app.debug:id/buttonBack1")
}  # id

# МОДАЛЬНОЕ ОКНО "УЖЕ ЕСТЬ РАБОТАЮЩАЯ КАССА"
MODAL_ALREADY_HAVE_CASHREGISTER_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
MODAL_ALREADY_HAVE_CASHREGISTER_TV_TITLE_TEXT = 'Активация кассы'

MODAL_ALREADY_HAVE_CASHREGISTER_BTN_OK = ("id", "ru.sigma.app.debug:id/okButton")
MODAL_ALREADY_HAVE_CASHREGISTER_BTN_CANCEL = ("id", "ru.sigma.app.debug:id/cancelButton")

# МОДАЛЬНОЕ ОКНО СЕРВЕР НЕДОСТУПЕН
MODAL_SERVER_NOT_AVAILABLE_TV_TITLE = ('id', 'ru.sigma.app.debug:id/headerTextView')
MODAL_SERVER_NOT_AVAILABLE_TV_TITLE_TEXT = 'Предупреждение'
MODAL_SERVER_NOT_AVAILABLE_TV_MESSAGE = ('id', 'ru.sigma.app.debug:id/mainTextView')
MODAL_SERVER_NOT_AVAILABLE_TV_MESSAGE_TEXT = 'Сервер недоступен'
MODAL_SERVER_NOT_AVAILABLE_BTN_CANCEL = ('id', 'ru.sigma.app.debug:id/cancelButton')
MODAL_SERVER_NOT_AVAILABLE_BTN_CANCEL_TEXT = 'Отменить'

# ОКНО ЗАГРУЗКИ ДАННЫХ ИЗ ЛК
LOADING_FIRST_LAUNCH_TV_TITLE = ("id", "ru.sigma.app.debug:id/regTitleTextView")
LOADING_FIRST_LAUNCH_TV_TITLE_TEXT = 'Касса активирована'
LOADING_FIRST_LAUNCH_TV_SUB_TITLE = ("id", "ru.sigma.app.debug:id/activationLoadSubTitle")
LOADING_FIRST_LAUNCH_TV_SUB_TITLE_TEXT = 'Получаем данные из Личного кабинета'
LOADING_FIRST_LAUNCH_IMG_PROGRESS = ("id", "ru.sigma.app.debug:id/activationLoadProgressBar")
LOADING_FIRST_LAUNCH_TV_PERCENT = ("id", "ru.sigma.app.debug:id/activationLoadPercentText")

# МОДАЛЬНОЕ ОКНО ПЕРЕКЛЮЧЕНИЯ ОТОБРАЖЕНИЯ В ВИДЕ СПИСКА
MODAL_CHANGE_DISPLAY_TYPE_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
MODAL_CHANGE_DISPLAY_TYPE_TV_TITLE_TEXT = 'Встречайте товары в виде списка!'
MODAL_CHANGE_DISPLAY_TYPE_TV_MESSAGE = ("id",
                                        "ru.sigma.app.debug:id/mainTextView")  # Теперь доступен новый режим отображения товаров. И хотя позиций на экране помещается столько же, зато названия видны целиком. Попробуйте прямо сейчас, а если не понравится, отключить можно в настройках, в разделе Правила торговли.
MODAL_CHANGE_DISPLAY_TYPE_BTN_OK = ("id", "ru.sigma.app.debug:id/okButton")
MODAL_CHANGE_DISPLAY_TYPE_BTN_CANCEL = ("id", "ru.sigma.app.debug:id/cancelButton")

# </ПЕРВЫЙ ЗАПУСК>

# ОСНОВНОЕ ОКНО ШАПКА
MAIN_HEADER_BTN_HAMBURGER = ("id", "ru.sigma.app.debug:id/backButton")
MAIN_HEADER_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
MAIN_HEADER_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
MAIN_HEADER_TV_TITLE_GOODS_TEXT = 'Товары'
MAIN_HEADER_TV_TITLE_SERVICE_TEXT = 'Услуги'
MAIN_HEADER_TV_TITLE_CUSTOM_PRICE_TEXT = 'Св.цена'
MAIN_HEADER_TV_TITLE_SEARCH_TEXT = 'Поиск'
MAIN_HEADER_BTN_GOODS_PT5F = ("xpath", "//android.widget.ImageView[contains(@bounds,'[434,80][482,128]')]")
MAIN_HEADER_BTN_SERVICE_PT5F = ("xpath", "//android.widget.ImageView[contains(@bounds,'[502,80][550,128]')]")
MAIN_HEADER_BTN_CUSTOM_PRICE_PT5F = ("xpath", "//android.widget.ImageView[contains(@bounds,'[570,80][618,128]')]")
MAIN_HEADER_BTN_SEARCH_PT5F = ("xpath", "//android.widget.ImageView[contains(@bounds,'[638,80][686,128]')]")

# ОСНОВНОЕ ОКНО ПОДВАЛ
MAIN_FOOTER_BTN_BLUE = ("id", "ru.sigma.app.debug:id/orderBottomView")
MAIN_FOOTER_TV_ORDER_COUNTER = ("id", "ru.sigma.app.debug:id/orderItemsCount")
MAIN_FOOTER_TV_ORDER_TITLE = ("id", "ru.sigma.app.debug:id/orderTitle")
MAIN_FOOTER_TV_ORDER_PRICE = ("id", "ru.sigma.app.debug:id/orderItemsPrice")

# ОСНОВНОЕ ОКНО ТОВАРЫ / УСЛУГИ
MAIN_GOODS_LAYOUT_RECYCLER = ("id", "ru.sigma.app.debug:id/menuRecyclerView")  # scrollable: true
MAIN_GOODS_BTN_SCANNER = ("id", "ru.sigma.app.debug:id/scannerFab")

# ОСНОВНОЕ ОКНО СВОЯ ЦЕНА
MAIN_CUSTOM_PRICE_LAYOUT_DISPLAY = ("id", "ru.sigma.app.debug:id/displayLayout")
MAIN_CUSTOM_PRICE_TV_PRICE = ("id", "ru.sigma.app.debug:id/priceTextView")
MAIN_CUSTOM_PRICE_TV_VAT = ("id", "ru.sigma.app.debug:id/ndsTextView")
MAIN_CUSTOM_PRICE_NUM_PAD = {
    "0": ("id", "ru.sigma.app.debug:id/buttonZero"),
    "1": ("id", "ru.sigma.app.debug:id/buttonOne"),
    "2": ("id", "ru.sigma.app.debug:id/buttonTwo"),
    "3": ("id", "ru.sigma.app.debug:id/buttonThree"),
    "4": ("id", "ru.sigma.app.debug:id/buttonFour"),
    "5": ("id", "ru.sigma.app.debug:id/buttonFive"),
    "6": ("id", "ru.sigma.app.debug:id/buttonSix"),
    "7": ("id", "ru.sigma.app.debug:id/buttonSeven"),
    "8": ("id", "ru.sigma.app.debug:id/buttonEight"),
    "9": ("id", "ru.sigma.app.debug:id/buttonNine"),
    ",": ("id", "ru.sigma.app.debug:id/buttonComma"),
    "backspace": ("id", "ru.sigma.app.debug:id/buttonBack1"),
    "*": ("id", "ru.sigma.app.debug:id/multiplyButton"),
    "submit": ("id", "ru.sigma.app.debug:id/checkButton")
}  # id

# ОСНОВНОЕ ОКНО ПОИСК
MAIN_SEARCH_ET_SEARCH = ("id", "ru.sigma.app.debug:id/search_src_text")  # можно sendkeys без предварительного тапа
MAIN_SEARCH_BTN_DELETE = ("id", "ru.sigma.app.debug:id/search_close_btn")
MAIN_SEARCH_BTN_ICON_SEARCH = ("id", "ru.sigma.app.debug:id/searchIconView")
MAIN_SEARCH_LAYOUT_RECYCLER = ("id", "ru.sigma.app.debug:id/menuRecyclerView")

MAIN_SEARCH_ATTR_NAME = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/product_name')]")
MAIN_SEARCH_ATTR_BARCODE = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/barcodeAndVendorcode')]")
MAIN_SEARCH_ATTR_PRICE = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/product_price')]")
MAIN_SEARCH_ATTR_QTY = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/remainderQuantity')]")

# ОСНОВНОЕ ОКНО БОКОВОЕ МЕНЮ
MAIN_SIDEBAR_TV_CASHIER_NAME = ("id", "ru.sigma.app.debug:id/nameTextView")
MAIN_SIDEBAR_TV_CASH_REGISTER_ID = ("id", "ru.sigma.app.debug:id/cashRegisterIdTextView")
MAIN_SIDEBAR_BTN_LOGOUT = ("id", "ru.sigma.app.debug:id/exitButton")
MAIN_SIDEBAR_BTN_RECEIPTS_AND_RETURNS = ("xpath", "//android.widget.TextView[@text='Чеки и возвраты']")
MAIN_SIDEBAR_BTN_CASH_TRANSACTIONS = ("xpath", "//android.widget.TextView[@text='Кассовые операции']")

MAIN_SIDEBAR_BTN_CLIENTS = ("xpath", "//android.widget.TextView[@text='Клиенты']")
MAIN_SIDEBAR_BTN_CREATE_PRODUCT = ("xpath", "//android.widget.TextView[@text='Создать товар']")
MAIN_SIDEBAR_BTN_CREATE_SERVICE = ("xpath", "//android.widget.TextView[@text='Создать услугу']")
MAIN_SIDEBAR_BTN_SETTINGS = ("xpath", "//android.widget.TextView[@text='Настройки']")
MAIN_SIDEBAR_BTN_CLOUD = ("xpath", "//android.widget.TextView[@text='Перейти в Личный кабинет']")
MAIN_SIDEBAR_BTN_HELP = ("xpath", "//android.widget.TextView[@text='Помощь']")

# ОКНО ЗАКРЫТИЯ СМЕНЫ
CLOSE_SHIFT_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
CLOSE_SHIFT_TV_TITLE_TEXT = 'Закрыть смену'
CLOSE_SHIFT_TV_CASH_IN_HAND = ("id", "ru.sigma.app.debug:id/sumInRegister")

CLOSE_SHIFT_CARD_SELLS = ("id", "ru.sigma.app.debug:id/sellsView")  # искать by bs4
CLOSE_SHIFT_CARD_RETURNS = ("id", "ru.sigma.app.debug:id/returnsView")  # искать by bs4
CLOSE_SHIFT_CARD_INCOMES = ("id", "ru.sigma.app.debug:id/incomesView")  # искать by bs4
CLOSE_SHIFT_CARD_OUTCOMES = ("id", "ru.sigma.app.debug:id/outcomesView")  # искать by bs4

CLOSE_SHIFT_TV_NOT_SENT_OFD = ("id", "ru.sigma.app.debug:id/notSentOfdCount")
CLOSE_SHIFT_TV_NOT_SENT_OFD_TEXT = '0 чеков'
CLOSE_SHIFT_TV_CASHIER_NAME = ("id", "ru.sigma.app.debug:id/cashierTextView")
CLOSE_SHIFT_TV_DATETIME = ("id", "ru.sigma.app.debug:id/cashierDateTextView")

CLOSE_SHIFT_BTN_CLOUD = ("id", "ru.sigma.app.debug:id/cloudOverlay")
CLOSE_SHIFT_BTN_CLOSE_SHIFT = ("id", "ru.sigma.app.debug:id/closeShiftButton")

# ОКНО ОЖИДАНИЯ ЗАКРЫТИЯ СМЕНЫ
CLOSE_SHIFT_WAIT_IMG_PROGRESS = ("id", "ru.sigma.app.debug:id/progressBar")


# ОКНО СКАНЕР
# ПРИ ПЕРВОМ ЗАПУСКЕ ОКНО РАЗРЕШЕНИЙ
# СКАНИРОВАНИЕ

# ОКНО НОВАЯ СМЕНА
NEW_SHIFT_TITLE = ("xpath", "//android.widget.TextView[contains(@text,'Новая смена')]")
NEW_SHIFT_TV_INCOME = ("id", "ru.sigma.app.debug:id/sumInputTextView")
NEW_SHIFT_TV_CASH_IN_HAND = ("id", "ru.sigma.app.debug:id/currentMoneyStateTextView")
NEW_SHIFT_TV_CASHIER_NAME = ("id", "ru.sigma.app.debug:id/leftTextView")
NEW_SHIFT_TV_DATETIME = ("id", "ru.sigma.app.debug:id/paymentSumTextView")

NEW_SHIFT_TV_MESSAGE = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/titleTextView')]")
NEW_SHIFT_TV_MESSAGE_TEXT = 'Новая смена'

NEW_SHIFT_NUM_PAD = {
    "0": ("id", "ru.sigma.app.debug:id/buttonZero"),
    "1": ("id", "ru.sigma.app.debug:id/buttonOne"),
    "2": ("id", "ru.sigma.app.debug:id/buttonTwo"),
    "3": ("id", "ru.sigma.app.debug:id/buttonThree"),
    "4": ("id", "ru.sigma.app.debug:id/buttonFour"),
    "5": ("id", "ru.sigma.app.debug:id/buttonFive"),
    "6": ("id", "ru.sigma.app.debug:id/buttonSix"),
    "7": ("id", "ru.sigma.app.debug:id/buttonSeven"),
    "8": ("id", "ru.sigma.app.debug:id/buttonEight"),
    "9": ("id", "ru.sigma.app.debug:id/buttonNine"),
    ",": ("id", "ru.sigma.app.debug:id/buttonComma"),
    "backspace": ("id", "ru.sigma.app.debug:id/buttonBack1")
}  # id

NEW_SHIFT_BTN_OPEN_SHIFT = ("id", "ru.sigma.app.debug:id/calcActionButton")

# МОДАЛЬНОЕ ОКНО ОЖИДАНИЯ ОТКРЫТИЯ СМЕНЫ
MODAL_NEW_SHIFT_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
MODAL_NEW_SHIFT_TV_TITLE_TEXT = 'Открытие смены'

MODAL_NEW_SHIFT_TV_SUB_TITLE = ("id", "ru.sigma.app.debug:id/mainTextView")
MODAL_NEW_SHIFT_TV_SUB_TITLE_TEXT = 'Пожалуйста, дождитесь окончания процесса открытия смены'

MODAL_NEW_SHIFT_IMG_PROGRESS = ("id", "ru.sigma.app.debug:id/progressBar")

# МОДАЛЬНОЕ ОКНО НА ФР ЕСТЬ ОТКРЫТАЯ СМЕНА
MODAL_NEW_SHIFT_FR_HAVE_SHIFT_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
MODAL_NEW_SHIFT_FR_HAVE_SHIFT_TV_TITLE_TEXT = 'Предупреждение'
MODAL_NEW_SHIFT_FR_HAVE_SHIFT_TV_MAIN = ("id", "ru.sigma.app.debug:id/mainTextView")
MODAL_NEW_SHIFT_FR_HAVE_SHIFT_TV_MAIN_TEXT = 'На Фискальном регистраторе есть открытая смена.\nДля корректной работы требуется ее закрыть.'
MODAL_NEW_SHIFT_FR_HAVE_SHIFT_BTN_OK = ("id", "ru.sigma.app.debug:id/okButton")
MODAL_NEW_SHIFT_FR_HAVE_SHIFT_BTN_CANCEL = ("id", "ru.sigma.app.debug:id/cancelButton")

# МОДАЛЬНОЕ ОКНО ВЫБЕРИТЕ ПРИЗНАК РАСЧЕТА
MODAL_CHOOSE_1054_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
MODAL_CHOOSE_1054_TV_TITLE_TEXT = 'Признак расчёта'
MODAL_CHOOSE_1054_TV_BODY = ("id", "ru.sigma.app.debug:id/mainTextView")
MODAL_CHOOSE_1054_TV_BODY_TEXT = 'Какой признак расчёта использовать?'
MODAL_CHOOSE_1054_BTN_INCOME = ("id", "ru.sigma.app.debug:id/okButton")
MODAL_CHOOSE_1054_BTN_OUTCOME = ("id", "ru.sigma.app.debug:id/cancelButton")

# ОКНО ВВОД ПИН КОДА
PIN_CODE_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
PIN_CODE_TV_TITLE_TEXT = 'Введите пинкод'
PIN_CODE_TV_MESSAGE = ("id", "ru.sigma.app.debug:id/contentMessageTextView")
PIN_CODE_TV_MESSAGE_TEXT = 'Пинкод по умолчанию «0000»'

PIN_CODE_IMG_PROGRESS = ("id", "ru.sigma.app.debug:id/pinPadProgressBar")

PIN_CODE_CARD_INDICATOR = (
    "id", "ru.sigma.app.debug:id/indicatorView")  # структура не меняется, нужен графический анализ
PIN_CODE_BTN_CLOUD = ("id", "ru.sigma.app.debug:id/cloudTitle")

PIN_CODE_NUM_PAD = {
    "0": ("id", "ru.sigma.app.debug:id/buttonZero"),
    "1": ("id", "ru.sigma.app.debug:id/buttonOne"),
    "2": ("id", "ru.sigma.app.debug:id/buttonTwo"),
    "3": ("id", "ru.sigma.app.debug:id/buttonThree"),
    "4": ("id", "ru.sigma.app.debug:id/buttonFour"),
    "5": ("id", "ru.sigma.app.debug:id/buttonFive"),
    "6": ("id", "ru.sigma.app.debug:id/buttonSix"),
    "7": ("id", "ru.sigma.app.debug:id/buttonSeven"),
    "8": ("id", "ru.sigma.app.debug:id/buttonEight"),
    "9": ("id", "ru.sigma.app.debug:id/buttonNine"),
    "backspace": ("id", "ru.sigma.app.debug:id/buttonBack1")
}  # id

# ОКНО ЧЕКИ И ВОЗВРАТЫ
RECEIPTS_AND_RETURNS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
RECEIPTS_AND_RETURNS_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
RECEIPTS_AND_RETURNS_TV_TITLE_TEXT = 'Чеки и возвраты'
RECEIPTS_AND_RETURNS_BTN_DATE = ("id", "ru.sigma.app.debug:id/selectDateButton")
RECEIPTS_AND_RETURNS_ET_SEARCH = ("id", "ru.sigma.app.debug:id/search_src_text")
RECEIPTS_AND_RETURNS_BTN_ICON_SEARCH = ("id", "ru.sigma.app.debug:id/searchIconView")
RECEIPTS_AND_RETURNS_LAYOUT_RECYCLER = ("id", "ru.sigma.app.debug:id/searchRecyclerView")
RECEIPTS_AND_RETURNS_IMG_PROGRESS = ("id", "ru.sigma.app.debug:id/searchProgressBar")

RECEIPTS_AND_RETURNS_ATTR_TV_ICON = ("xpath", "//android.widget.TextView["
                                              "@resource-id='ru.sigma.app.debug:id/iconTextView']")
RECEIPTS_AND_RETURNS_ATTR_TV_TIME = ("xpath", "//android.widget.TextView["
                                              "@resource-id='ru.sigma.app.debug:id/timeTextView']")
RECEIPTS_AND_RETURNS_ATTR_TV_NUMBER = ("xpath", "//android.widget.TextView["
                                                "@resource-id='ru.sigma.app.debug:id/numberTextView']")
RECEIPTS_AND_RETURNS_ATTR_TV_SUM = ("xpath", "//android.widget.TextView["
                                             "@resource-id='ru.sigma.app.debug:id/sumTextView']")
RECEIPTS_AND_RETURNS_ATTR_TV_CASHIER_NAME = ("xpath", "//android.widget.TextView["
                                                      "@resource-id='ru.sigma.app.debug:id/cashierTextView']")

# ОКНО ЧЕКИ И ВОЗВРАТЫ - ЧЕК
RECEIPT_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
RECEIPT_TV_TITLE = ("xpath", "//android.widget.TextView[contains(@text,'Чек №')]")
RECEIPT_TV_TITLE_TEXT = 'Чек №'
RECEIPT_TV_PAYMENT_TYPE = ("id", "ru.sigma.app.debug:id/payment1TypeTextView")
RECEIPT_TV_PAYMENT_SUM = ("id", "ru.sigma.app.debug:id/payment1SumTextView")
RECEIPT_TV_CASHIER_NAME = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/cashierTextView')]")
RECEIPT_TV_DATETIME = ("id", "ru.sigma.app.debug:id/dateTextView")
RECEIPT_BTN_MAKE_REFUND = ("id", "ru.sigma.app.debug:id/makeRefundButton")
RECEIPT_BTN_PRINT_COPY = ("id", "ru.sigma.app.debug:id/printCopyButton")

RECEIPT_TV_ALREADY_REFUND = ("xpath", "//android.widget.TextView[contains(@text,'По чеку сделан возврат')]")
RECEIPT_TV_ALREADY_REFUND_TEXT = 'По чеку сделан возврат'
RECEIPT_BTN_ALREADY_REFUND_OPEN = ("id", "ru.sigma.app.debug:id/refundBlockButton")

RECEIPT_LAYOUT_RECYCLER = ("id", "ru.sigma.app.debug:id/itemsRecyclerView")
RECEIPT_CARD_VIEW_GROUP = ("xpath", "//android.view.ViewGroup[contains(@class,'android.view.ViewGroup')]")
RECEIPT_TV_ATTR_POSITION_NUMBER = ("id", "ru.sigma.app.debug:id/positionTextView")
RECEIPT_TV_ATTR_NAME = ("id", "ru.sigma.app.debug:id/nameTextView")
RECEIPT_TV_ATTR_SUM = ("xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/sumTextView')]")
RECEIPT_TV_ATTR_QTY = ("id", "ru.sigma.app.debug:id/quantityTextView")

# ОКНО ВОЗВРАЩЕННЫЙ ЧЕК
RECEIPT_REFUNDED_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
RECEIPT_REFUNDED_TV_TITLE = ("xpath", "//android.widget.TextView[contains(@text,'Возврат №')]")
RECEIPT_REFUNDED_TV_TITLE_TEXT = 'Возврат №'
RECEIPT_REFUNDED_TV_PAYMENT_TYPE = ("id", "ru.sigma.app.debug:id/payment1TypeTextView")
RECEIPT_REFUNDED_TV_PAYMENT_SUM = ("id", "ru.sigma.app.debug:id/payment1SumTextView")
RECEIPT_REFUNDED_TV_CASHIER_NAME = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/cashierTextView')]")
RECEIPT_REFUNDED_TV_DATETIME = ("id", "ru.sigma.app.debug:id/dateTextView")
RECEIPT_REFUNDED_BTN_MAKE_REFUND = ("id", "ru.sigma.app.debug:id/makeRefundButton")
RECEIPT_REFUNDED_BTN_PRINT_COPY = ("id", "ru.sigma.app.debug:id/printCopyButton")

RECEIPT_REFUNDED_TV_ALREADY_REFUND = ("xpath", "//android.widget.TextView[contains(@text,'Возврат по чеку №')]")
RECEIPT_REFUNDED_TV_ALREADY_REFUND_TEXT = 'По чеку сделан возврат'
RECEIPT_REFUNDED_BTN_ALREADY_REFUND_OPEN = ("id", "ru.sigma.app.debug:id/refundBlockButton")

# МОДАЛЬНОЕ ОКНО АТОЛ ПЭЙ ТИП ВОЗВРАТА
REFUND_MODAL_ATOL_PAY_OPTIONS_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
REFUND_MODAL_ATOL_PAY_OPTIONS_TV_TITLE_TEXT = 'Возврат'

REFUND_MODAL_ATOL_PAY_OPTIONS_BTN_CANCEL = ("id", "ru.sigma.app.debug:id/cancelOptionView")
REFUND_MODAL_ATOL_PAY_OPTIONS_BTN_REFUND = ("id", "ru.sigma.app.debug:id/refundOptionView")

# ТОСТ "Вы пытаетесь вернуть по безналу больше, чем продали"
REFUND_TOAST_FORBIDDEN = (
    "xpath", "//android.widget.Toast[@text='Вы пытаетесь вернуть по безналу больше, чем продали']")

# ОКНО ВОЗВРАТ
REFUND_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
REFUND_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
REFUND_TV_TITLE_TEXT = 'Выберите товары'
REFUND_BTN_SELECT_ALL = ("id", "ru.sigma.app.debug:id/selectAllButton")
REFUND_BTN_FREE_PRICE_SWITCHER = ("id", "ru.sigma.app.debug:id/refundCustomPriceSwitch")

REFUND_LAYOUT_RECYCLER = ("id", "ru.sigma.app.debug:id/itemsRecyclerView")

REFUND_CHECKBOX_ITEM = ("xpath",
                        "//android.widget.CheckBox[contains(@resource-id,'ru.sigma.app.debug:id/fragment_payments_history_return_item_check_box')]")
REFUND_ATTR_ITEM_NAME = ("xpath",
                         "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/fragment_payments_history_return_item_product_text_view')]")
REFUND_ATTR_ITEM_PRICE = ("xpath",
                          "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/fragment_payments_history_detailed_return_refund_price_text_view')]")
REFUND_ATTR_ITEM_QTY = ("xpath",
                        "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/fragment_payments_history_return_item_product_quantity_text_view')]")
REFUND_ATTR_ITEM_AVAILABLE = ("xpath",
                              "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/fragment_payments_history_return_item_price_product_text_view')]")

REFUND_TV_SUM = ("id", "ru.sigma.app.debug:id/totalSumView")
REFUND_BTN_NEXT = ("id", "ru.sigma.app.debug:id/verticalActionButton")

# ОКНО ВОЗВРАТ КОММЕНТАРИЙ
REFUND_COMMENT_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
REFUND_COMMENT_TV_TITLE_TEXT = 'Дополнительные данные'
REFUND_COMMENT_TV_COMMENT_TITLE = ("id", "ru.sigma.app.debug:id/commentTitle")  # Ваш комментарий
REFUND_COMMENT_INPUT_STRING = ("id", "ru.sigma.app.debug:id/backgroundView")
REFUND_COMMENT_BTN_NEXT = ("id", "ru.sigma.app.debug:id/rightNavigationButton")

# ОКНО ВЫПОЛНЕНИЯ ВОЗВРАТА
REFUND_EXECUTION_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")  # Возврат
REFUND_EXECUTION_TV_SUM = ("id", "ru.sigma.app.debug:id/sumInputTextView")
REFUND_EXECUTION_IMG_PROGRESS = ("id", "ru.sigma.app.debug:id/progressBarView")
REFUND_EXECUTION_TV_MESSAGE = ("id",
                               "ru.sigma.app.debug:id/messageTextView")
REFUND_EXECUTION_TV_MESSAGE_WAIT_TEXT = 'Выполняется операция. Пожалуйста, подождите...'
REFUND_EXECUTION_TV_MESSAGE_SUCCESS_TEXT = 'Передайте клиенту деньги и чек'
REFUND_EXECUTION_BTN_NEXT = ("id", "ru.sigma.app.debug:id/rightNavigationButton")

# ОКНО УСПЕШНО ВЫПОЛНЕННОГО ВОЗВРАТА КАРТОЙ
REFUND_ATOL_PAY_SUCCESS_TV_TITLE = ("id", "ru.sigma.app.debug:id/atolPaySumTitle")
REFUND_ATOL_PAY_SUCCESS_TV_TITLE_TEXT = 'Возвращено:'

REFUND_ATOL_PAY_SUCCESS_TV_AMOUNT = ("id", "ru.sigma.app.debug:id/atolPaySumText")  # 1,00 ₽

REFUND_ATOL_PAY_SUCCESS_TV_STATUS = ("id", "ru.sigma.app.debug:id/atolPayStatusText")
REFUND_ATOL_PAY_SUCCESS_TV_STATUS_TEXT = 'Операция завершена'

REFUND_ATOL_PAY_SUCCESS_TV_HINT = ("id", "ru.sigma.app.debug:id/atolPayStatusHintText")
REFUND_ATOL_PAY_SUCCESS_TV_HINT_TEXT = 'Передайте банковский слип клиенту'

REFUND_ATOL_PAY_SUCCESS_BTN_CONTINUE = ("id", "ru.sigma.app.debug:id/atolPayContinueButton")
REFUND_ATOL_PAY_SUCCESS_BTN_CONTINUE_TEXT = 'Продолжить печать'

REFUND_ATOL_PAY_SUCCESS_BTN_CLOSE = ("id", "ru.sigma.app.debug:id/atolPayCloseButton")
REFUND_ATOL_PAY_SUCCESS_BTN_CLOSE_TEXT = 'Закрыть'

# ОКНО КАССОВЫЕ ОПЕРАЦИИ
CASH_TRANSACTIONS_TV_TITLE = ("xpath", "//android.widget.TextView[contains(@text,'Смена №')]")
CASH_TRANSACTIONS_TV_TITLE_TEXT = 'Смена №'
CASH_TRANSACTIONS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")

CASH_TRANSACTIONS_TV_DATETIME_SHIFT_OPENING = ("id", "ru.sigma.app.debug:id/dateTextView")
CASH_TRANSACTIONS_BTN_MAKE_CALCULATION_REPORT = ("id", "ru.sigma.app.debug:id/makeReportButton")
CASH_TRANSACTIONS_BTN_CLOSE_SHIFT = ("id", "ru.sigma.app.debug:id/closeShiftButton")

CASH_TRANSACTIONS_TV_PROFIT = ("id", "ru.sigma.app.debug:id/sumTextView")
CASH_TRANSACTIONS_TV_CASH_IN_CASHBOX = ("id", "ru.sigma.app.debug:id/amountCashTextView")  # text 50,00 ₽
CASH_TRANSACTIONS_BTN_ADD_CASH = ("id", "ru.sigma.app.debug:id/addCashButton")
CASH_TRANSACTIONS_BTN_REMOVE_CASH = ("id", "ru.sigma.app.debug:id/removeCashButton")

CASH_TRANSACTIONS_INCOME_OUTCOME_TV_TITLE = (
    "xpath", "//android.widget.TextView[@text='Выручка']")
CASH_TRANSACTIONS_TV_INCOMES = ("id", "ru.sigma.app.debug:id/incomesTextView")
CASH_TRANSACTIONS_TV_OUTCOMES = ("id", "ru.sigma.app.debug:id/outcomesTextView")
CASH_TRANSACTIONS_BTN_MAKE_X_REPORT = ("id", "ru.sigma.app.debug:id/makeXreportButton")

CASH_TRANSACTIONS_TV_CORRECTION_INCOMES = ("id", "ru.sigma.app.debug:id/incomeTextView")
CASH_TRANSACTIONS_TV_CORRECTION_OUTCOMES = ("id", "ru.sigma.app.debug:id/outcomeTextView")
CASH_TRANSACTIONS_BTN_MAKE_CORRECTION = ("id", "ru.sigma.app.debug:id/makeCorrectionButton")

CASH_TRANSACTIONS_CARD_INCOME = ("id", "ru.sigma.app.debug:id/operationIncomeDetailedView")  # искать by bs4
CASH_TRANSACTIONS_CARD_INCOME_RETURN = (
    "id", "ru.sigma.app.debug:id/operationIncomeReturnDetailedView")  # искать by bs4
CASH_TRANSACTIONS_CARD_OUTCOME = ("id", "ru.sigma.app.debug:id/operationOutcomeDetailedView")  # искать by bs4
CASH_TRANSACTIONS_CARD_OUTCOME_RETURN = (
    "id", "ru.sigma.app.debug:id/operationOutcomeReturnDetailedView")  # искать by bs4

# ОКНО ЧЕКА КОРРЕКЦИИ FFD_1_05

CORRECTION_RECEIPT_FFD_1_05_BTN_BACK = (
    "xpath", "//android.view.ViewGroup[@resource-id='ru.sigma.app.debug:id/backButton']")
CORRECTION_RECEIPT_FFD_1_05_TV_TITLE = (
    "xpath", "//android.widget.TextView[@text='Коррекция']")
CORRECTION_RECEIPT_FFD_1_05_TV_TITLE_TEXT = 'Коррекция'
CORRECTION_RECEIPT_FFD_1_05_BTN_INCOME = (
    "xpath", "//android.widget.TextView[@text='Приход' and @resource-id='ru.sigma.app.debug:id/toggleTextView']")
CORRECTION_RECEIPT_FFD_1_05_BTN_OUTCOME = (
    "xpath", "//android.widget.TextView[@text='Расход' and @resource-id='ru.sigma.app.debug:id/toggleTextView']")

CORRECTION_RECEIPT_FFD_1_05_TV_BASIS = (
    "xpath", "//android.view.ViewGroup[@resource-id='ru.sigma.app.debug:id/reasonSpinner']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_BASIS_MYSELF = ("xpath", ".//android.widget.TextView[@text='Самостоятельная']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_BASIS_FNS = ("xpath", ".//android.widget.TextView[@text='По предписанию ФНС']")
CORRECTION_RECEIPT_FFD_1_05_ET_FD_NUMBER = ("xpath", ".//android.widget.EditText[@text='Номер документа']")
CORRECTION_RECEIPT_FFD_1_05_BTN_DATE = (
    "xpath", ".//android.view.ViewGroup[@resource-id='ru.sigma.app.debug:id/documentDateButton']")
CORRECTION_RECEIPT_FFD_1_05_TV_PAYMENT_METHOD = (
    "xpath", "//android.view.ViewGroup[@resource-id='ru.sigma.app.debug:id/paymentTypeSpinner']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_PAYMENT_METHOD_CASH = ("xpath", ".//android.widget.TextView[@text='Наличными']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_PAYMENT_METHOD_ELECTRONICALLY = (
    "xpath", ".//android.widget.TextView[@text='Безналичными']")
CORRECTION_RECEIPT_FFD_1_05_ET_FD_AMOUNT = ("xpath", ".//android.widget.EditText[@text='Сумма коррекции']")
CORRECTION_RECEIPT_FFD_1_05_TV_VAT_TYPE = (
    "xpath", "//android.widget.TextView[@text='0%']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_0 = (
    "xpath", "//android.widget.TextView[@text='0%']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_10 = (
    "xpath", "//android.widget.TextView[@text='10%']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_10_110 = (
    "xpath", "//android.widget.TextView[@text='10/110']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_20 = (
    "xpath", "//android.widget.TextView[@text='20%']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_20_120 = (
    "xpath", "//android.widget.TextView[@text='20/120']")
CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_WITHOUT = (
    "xpath", "//android.widget.TextView[@text='Без НДС']")
CORRECTION_RECEIPT_FFD_1_05_ET_VAT_AMOUNT = (
    "xpath", ".//android.view.ViewGroup[@resource-id='ru.sigma.app.debug:id/ndsSumView']")
CORRECTION_RECEIPT_FFD_1_05_BTN_ADD_VAT = ("id", "ru.sigma.app.debug:id/addNdsButton")
CORRECTION_RECEIPT_FFD_1_05_BTN_OK = (
    "id", "ru.sigma.app.debug:id/verticalActionButton")
CORRECTION_RECEIPT_FFD_1_05_IMG_PROGRESS = ("id", "android.widget.ProgressBar")

# МОДАЛЬНОЕ ОКНО ВВОДА ДАТЫ
MODAL_DATE_TV_DAY = (
    "xpath", "//android.widget.EditText[@bounds='[128,586][256,682]']")
MODAL_DATE_TV_MONTH = (
    "xpath", "//android.widget.EditText[@bounds='[288,586][416,682]']")
MODAL_DATE_TV_YEAR = (
    "xpath", "//android.widget.EditText[@bounds='[448,586][576,682]']")
MODAL_DATE_BTN_OK = ("id", "ru.sigma.app.debug:id/okButton")
MODAL_DATE_BTN_CANCEL = ("id", "ru.sigma.app.debug:id/cancelButton")

# ОКНО ВНЕСЕНИЯ / ИЗЪЯТИЯ
ADD_CASH_NEXT = ("id", "ru.sigma.app.debug:id/verticalActionButton")
REMOVE_CASH_NEXT = ("id", "ru.sigma.app.debug:id/verticalActionButton")

# ОКНО КЛИЕНТЫ
CLIENTS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
CLIENTS_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
CLIENTS_TV_TITLE_TEXT = 'Клиенты'
CLIENTS_BTN_ADD_NEW_CLIENT = ("id", "ru.sigma.app.debug:id/addNewClientButton")
CLIENTS_ET_SEARCH = ("id", "ru.sigma.app.debug:id/search_src_text")
CLIENTS_PTN_ICON_SEARCH = ("id", "ru.sigma.app.debug:id/searchIconView")
CLIENTS_LAYOUT_RECYCLER = ("id", "ru.sigma.app.debug:id/searchRecyclerView")
CLIENTS_CARD_CLIENT = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/cellBackground')]")
CLIENTS_ATTR_CLIENT_NAME = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/loyaltyClientsName')]")
CLIENTS_ATTR_CLIENT_PHONE = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/loyaltyClientsPhone')]")
CLIENTS_SCANNER = ("id", "ru.sigma.app.debug:id/searchScannerFab")

# ОКНО НОВЫЙ КЛИЕНТ
CLIENTS_NEW_BTN_BACK = ("xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/backButton')]")
CLIENTS_NEW_TV_TITLE = ("xpath", "//android.widget.TextView[@text='Новый клиент']")
CLIENTS_NEW_TV_TITLE_TEXT = 'Новый клиент'
CLIENTS_NEW_LAYOUT_RECYCLER_SCROLL_VIEW = (
    "xpath", "//android.widget.ScrollView[contains(@class,'android.widget.ScrollView')]")
# TAP AND USE VIRTUAL KEYBOARD
CLIENTS_NEW_ET_NAME = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientNameEditText')]")
CLIENTS_NEW_ET_SURNAME = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientSurnameEditText')]")
CLIENTS_NEW_ET_PHONE = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientPhoneEditText')]")
CLIENTS_NEW_ET_EMAIL = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientEmailEditText')]")
CLIENTS_NEW_BTN_SWITCH_LOYALTY_CARD_TYPE = (
    "id", "ru.sigma.app.debug:id/spinnerView")  # из спиннера вываливаются textview
CLIENTS_NEW_MENU_ITEM_WITHOUT_CATEGORY = ("xpath", "//android.widget.TextView[contains(@text,'Без категории')]")
CLIENTS_NEW_LOYALTY_CARD_NUMBER = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientLoyaltyCardNumberEditText')]")
CLIENTS_NEW_ET_BIRTHDAY = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientBirthdayEditText')]")
CLIENTS_NEW_ET_COMMENT = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientCommentEditText')]")
CLIENTS_NEW_ET_BUYER = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientDataEditText')]")
CLIENTS_NEW_ET_TIN = (
    "xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/clientInnEditText')]")

# ОКНО СОЗДАТЬ ТОВАР
CREATE_PRODUCT_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
CREATE_PRODUCT_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
CREATE_PRODUCT_TV_TITLE_TEXT = 'Новый товар'
CREATE_PRODUCT_ET_PRODUCT_NAME = ("id", "ru.sigma.app.debug:id/createProductNameEditText")
CREATE_PRODUCT_BTN_ADD_IMG = ("id", "ru.sigma.app.debug:id/createProductImage")
CREATE_PRODUCT_BTN_CHOOSE_CATEGORY = ("id", "ru.sigma.app.debug:id/createProductCategoryIcon")
CREATE_PRODUCT_BTN_SWITCH_UNIT = ("id", "ru.sigma.app.debug:id/createProductUnitsSpinner")

CREATE_PRODUCT_LAYOUT_UNIT_TYPES = ("xpath", "//android.widget.ListView[contains(@class, 'android.widget.ListView')]")

CREATE_PRODUCT_TV_UNIT_TYPE_NONE = ("xpath", "//android.widget.TextView[contains(@text,'-')]")
CREATE_PRODUCT_TV_UNIT_TYPE_GIGABYTE = ("xpath", "//android.widget.TextView[contains(@text,'Гбайт')]")
CREATE_PRODUCT_TV_UNIT_TYPE_GIGACALORIUM = ("xpath", "//android.widget.TextView[contains(@text,'Гкал')]")
CREATE_PRODUCT_TV_UNIT_TYPE_KILOBYTE = ("xpath", "//android.widget.TextView[contains(@text,'Кбайт')]")
CREATE_PRODUCT_TV_UNIT_TYPE_MEGABYTE = ("xpath", "//android.widget.TextView[contains(@text,'Мбайт')]")
CREATE_PRODUCT_TV_UNIT_TYPE_TERABYTE = ("xpath", "//android.widget.TextView[contains(@text,'Тбайт')]")
CREATE_PRODUCT_TV_UNIT_TYPE_GRAM = ("xpath", "//android.widget.TextView[contains(@text,'г')]")
CREATE_PRODUCT_TV_UNIT_TYPE_DECIMETERS = ("xpath", "//android.widget.TextView[contains(@text,'дм')]")
CREATE_PRODUCT_TV_UNIT_TYPE_DECIMETERS2 = ("xpath", "//android.widget.TextView[contains(@text,'дм2')]")
CREATE_PRODUCT_TV_UNIT_TYPE_DECIMETERS3 = ("xpath", "//android.widget.TextView[contains(@text,'дм3')]")
CREATE_PRODUCT_TV_UNIT_TYPE_KILOWATT_HOUR = ("xpath", "//android.widget.TextView[contains(@text,'кВт/ч')]")
CREATE_PRODUCT_TV_UNIT_TYPE_KILLOGRAM = ("xpath", "//android.widget.TextView[contains(@text,'кг')]")
CREATE_PRODUCT_TV_UNIT_TYPE_LITER = ("xpath", "//android.widget.TextView[contains(@text,'л')]")
CREATE_PRODUCT_TV_UNIT_TYPE_METER = ("xpath", "//android.widget.TextView[contains(@text,'м')]")
CREATE_PRODUCT_TV_UNIT_TYPE_METER2 = ("xpath", "//android.widget.TextView[contains(@text,'м2')]")
CREATE_PRODUCT_TV_UNIT_TYPE_METER3 = ("xpath", "//android.widget.TextView[contains(@text,'м3')]")
CREATE_PRODUCT_TV_UNIT_TYPE_MINUTES = ("xpath", "//android.widget.TextView[contains(@text,'мин')]")
CREATE_PRODUCT_TV_UNIT_TYPE_MILLILITER = ("xpath", "//android.widget.TextView[contains(@text,'мл')]")
CREATE_PRODUCT_TV_UNIT_TYPE_MILLIMETER = ("xpath", "//android.widget.TextView[contains(@text,'мм')]")
CREATE_PRODUCT_TV_UNIT_TYPE_SECONDS = ("xpath", "//android.widget.TextView[contains(@text,'сек')]")
CREATE_PRODUCT_TV_UNIT_TYPE_CENTIMETER = ("xpath", "//android.widget.TextView[contains(@text,'см')]")
CREATE_PRODUCT_TV_UNIT_TYPE_CENTIMETER2 = ("xpath", "//android.widget.TextView[contains(@text,'см2')]")
CREATE_PRODUCT_TV_UNIT_TYPE_CENTIMETER3 = ("xpath", "//android.widget.TextView[contains(@text,'см3')]")
CREATE_PRODUCT_TV_UNIT_TYPE_DAY = ("xpath", "//android.widget.TextView[contains(@text,'сутки')]")
CREATE_PRODUCT_TV_UNIT_TYPE_TONN = ("xpath", "//android.widget.TextView[contains(@text,'т')]")
CREATE_PRODUCT_TV_UNIT_TYPE_HOURS = ("xpath", "//android.widget.TextView[contains(@text,'час')]")
CREATE_PRODUCT_TV_UNIT_TYPE_PIECES = ("xpath", "//android.widget.TextView[contains(@text,'шт')]")

CREATE_PRODUCT_ET_PRODUCT_PRICE = ("id", "ru.sigma.app.debug:id/createProductPriceEditText")

# ТУТ НЕ ЗНАЮ ПОКА ЧТО ДЕЛАТЬ, НЕТ ID И RESOURCE-ID, НЕ УНИКАЛЬНЫЙ ЭЛЕМЕНТ
CREATE_PRODUCT_BTN_SWITCH_VAT = (
    "xpath", "//android.widget.Spinner[@resource-id(@text,'ru.sigma.app.debug:id/spinnerView')]")

CREATE_PRODUCT_LAYOUT_VAT = ("xpath", "//android.widget.ListView[contains(@class, 'android.widget.ListView')]")

CREATE_PRODUCT_TV_VAT_NONE = ("xpath", "//android.widget.TextView[contains(@text,'Не выбрано')]")
CREATE_PRODUCT_TV_VAT_0 = ("xpath", "//android.widget.TextView[contains(@text,'0%')]")
CREATE_PRODUCT_TV_VAT_10 = ("xpath", "//android.widget.TextView[contains(@text,'10%')]")
CREATE_PRODUCT_TV_VAT_10_110 = ("xpath", "//android.widget.TextView[contains(@text,'10/110')]")
CREATE_PRODUCT_TV_VAT_20 = ("xpath", "//android.widget.TextView[contains(@text,'20%')]")
CREATE_PRODUCT_TV_VAT_20_120 = ("xpath", "//android.widget.TextView[contains(@text,'20/120')]")
CREATE_PRODUCT_TV_VAT_WITHOUT = ("xpath", "//android.widget.TextView[contains(@text,'Без НДС')]")

CREATE_PRODUCT_ET_PRODUCT_ARTICLE = ("id", "ru.sigma.app.debug:id/createProductArticleEditText")
CREATE_PRODUCT_ET_PRODUCT_BARCODE = ("id", "ru.sigma.app.debug:id/createProductBarcodeEditText")
CREATE_PRODUCT_BTN_PRODUCT_BARCODE_GENERATE = ("id", "ru.sigma.app.debug:id/createProductBarcodeIcon")

# ТУТ НЕ ЗНАЮ ПОКА ЧТО ДЕЛАТЬ, НЕТ ID И RESOURCE-ID, НЕ УНИКАЛЬНЫЙ ЭЛЕМЕНТ
CREATE_PRODUCT_BTN_SWITCH_PRODUCT_TYPE = (
    "xpath", "//android.widget.Spinner[@resource-id(@text,'ru.sigma.app.debug:id/spinnerView')]")

CREATE_PRODUCT_BTN_SCANNER = ("id", "ru.sigma.app.debug:id/searchScannerFab")
CREATE_PRODUCT_BTN_NEXT = ("id", "ru.sigma.app.debug:id/verticalActionButton")

# ОКНО СОЗДАТЬ ТОВАР ВЫБРАТЬ КАТЕГОРИЮ


# МОДАЛЬНОЕ ОКНО РАЗРЕШЕНИЙ
PERMISSION_MODAL_MESSAGE = ("id",
                            "com.android.packageinstaller:id/permission_message")  # @TEXT Разрешить приложению Debug Касса доступ к фото, мультимедиа и файлам на вашем устройстве?
PERMISSION_MODAL_BTN_ALLOW = ("id", "com.android.packageinstaller:id/permission_allow_button")
PERMISSION_MODAL_BTN_DENY = ("id", "com.android.packageinstaller:id/permission_deny_button")

# ОКНО СОЗДАТЬ УСЛУГУ
CREATE_SERVICE_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
CREATE_SERVICE_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
CREATE_SERVICE_TV_TITLE_TEXT = 'Новая услуга'

# ОКНО НАСТРОЙКИ
SETTINGS_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
SETTINGS_TV_TITLE_TEXT = 'Настройки'
SETTINGS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")

SETTINGS_BTN_TRADING_RULES = ("xpath", "//android.widget.TextView[@text='Правила торговли']")
SETTINGS_BTN_MARKING = ("xpath", "//android.widget.TextView[@text='Маркировка']")
SETTINGS_BTN_CASHLESS_PAYMENTS = ("xpath", "//android.widget.TextView[@text='Безналичные платежи']")
SETTINGS_BTN_RECEIPT_PRINTER = ("xpath", "//android.widget.TextView[@text='Принтер чеков']")
SETTINGS_BTN_SCANNERS = ("xpath", "//android.widget.TextView[@text='Сканеры']")
SETTINGS_BTN_EGAIS = ("xpath", "//android.widget.TextView[@text='ЕГАИС']")
SETTINGS_BTN_SCALES = ("xpath", "//android.widget.TextView[@text='Весы']")
SETTINGS_BTN_CASHREGISTER_INFO = ("xpath", "//android.widget.TextView[@text='Информация о кассе']")
SETTINGS_BTN_DEBUG = ("xpath", "//android.widget.TextView[@text='DEBUG']")
SETTINGS_BTN_TESTING = ("xpath", "//android.widget.TextView[@text='Тестирование']")

# ОКНО Правила торговли
# У ТУМБЛЕРОВ АТРИБУТ @text=ВКЛ / ВЫКЛ
TRADING_RULES_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
TRADING_RULES_TV_TITLE_TEXT = 'Правила торговли'
TRADING_RULES_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")

TRADING_RULES_SWITCH_FREE_PRICE = ("id", "ru.sigma.app.debug:id/freePriceSellingSwitch")  # Продажа по свободной цене
TRADING_RULES_SWITCH_ENCASHMENT_AFTER_SHIFT_CLOSE = (
    "id", "ru.sigma.app.debug:id/encashmentSwitch")  # Инкассация при закрытии смены
TRADING_RULES_SWITCH_LINEAR_VIEW_FOR_ITEMS = (
    "id", "ru.sigma.app.debug:id/linearViewSwitch")  # Товары и услуги в виде списка
TRADING_RULES_SWITCH_SCAN_WEIGHT_BARCODE = (
    "id", "ru.sigma.app.debug:id/useWeightBarcodesSwitch")  # Сканирование весовых штрих-кодов
TRADING_RULES_SWITCH_SHOW_STOCK = (
    "id", "ru.sigma.app.debug:id/remaindersSwitch ")  # Отображение остатков товаров на складе
TRADING_RULES_SWITCH_CONTROL_STOCK = ("id", "ru.sigma.app.debug:id/checkRemaindersSwitch")  # Контроль продажи в минус
TRADING_RULES_SWITCH_CREATE_ITEM_BY_BARCODE = (
    "id", "ru.sigma.app.debug:id/createProductByBarcodeScanSwitch")  # Создание товаров при сканировании штрих-кода
TRADING_RULES_SWITCH_ADD_ITEM_FIRST_IN_LIST = (
    "id", "ru.sigma.app.debug:id/orderScrollDirectionSwitch")  # Добавлять позиции в заказ в начало списка
TRADING_RULES_SWITCH_ROUND_DOWN_PAYMENT = ("id", "ru.sigma.app.debug:id/priceSwitch")  # Обнуление копеек при оплате
TRADING_RULES_SWITCH_FULL_1054 = (
    "id", "ru.sigma.app.debug:id/paymentSwitch")  # Использовать полный список признаков расчёта
TRADING_RULES_SWITCH_EXPENSES = ("id", "ru.sigma.app.debug:id/expensesSwitch")  # Использовать расходы
TRADING_RULES_SWITCH_EXPENSES_BY_DEFAULT = (
    "id", "ru.sigma.app.debug:id/expensesCommonSwitch")  # Расход вместо прихода по умолчанию

# ОКНО Маркировка
MARKING_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
MARKING_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
MARKING_TV_TITLE_TEXT = 'Маркировка'

# ОКНО Безналичные платежи
CASHLESS_PAYMENTS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
CASHLESS_PAYMENTS_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
CASHLESS_PAYMENTS_TV_TITLE_TEXT = 'Безналичные платежи'

# ОКНО Принтер чеков
RECEIPT_PRINTER_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
RECEIPT_PRINTER_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
RECEIPT_PRINTER_TV_TITLE_TEXT = 'Принтер чеков'

RECEIPT_PRINTER_ET_EMAIL = ("id", "ru.sigma.app.debug:id/backgroundView")
RECEIPT_PRINTER_SWITCH_PRINT_RECEIPTS = ('id', 'ru.sigma.app.debug:id/paperCheckSwitch') #ВКЛ ВЫКЛ


# ОКНО Сканеры
SCANNERS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
SCANNERS_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
SCANNERS_TV_TITLE_TEXT = 'Сканеры'

# ОКНО ЕГАИС
EGAIS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
EGAIS_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
EGAIS_TV_TITLE_TEXT = 'ЕГАИС'

# ОКНО Весы
SCALES_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
SCALES_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
SCALES_TV_TITLE_TEXT = 'Весы'

# ОКНО Информация о кассе
CASHREGISTER_INFO_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
CASHREGISTER_INFO_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
CASHREGISTER_INFO_TV_TITLE_TEXT = 'Информация о кассе'

# ОКНО DEBUG
# DEBUG

# ОКНО Тестирование
# TESTING


# ОКНО ПОМОЩЬ
# HELP_


# ОКНО КОРЗИНА / ЧЕКИ
CART_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
CART_TV_TITLE = ("xpath", "//android.widget.TextView[@text='Чек']")
CART_TV_TITLE_TEXT = 'Чек'

CART_BTN_CLIENTS_PT5F = ("xpath", "//android.widget.ImageView[contains(@bounds,'[434,80][482,128]')]")
CART_BTN_DISCOUNT_PT5F = ("xpath", "//android.widget.ImageView[contains(@bounds,'[570,80][618,128]')]")
CART_BTN_DELAYED_RECEIPTS_PT5F = ("xpath", "//android.widget.ImageView[contains(@bounds,'[638,80][686,128]')]")



CART_TV_EMPTY_MESSAGE = ("id", "ru.sigma.app.debug:id/emptyOrderViewMessage")
CART_TV_EMPTY_MESSAGE_TEXT = 'Добавьте позиции в чек'


# ОКНО ОТЛОЖЕННЫЕ ЧЕКИ
DELAYED_RECEIPTS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
DELAYED_RECEIPTS_TV_TITLE = ("xpath", "//android.widget.TextView[@text='Чеки']")
DELAYED_RECEIPTS_TV_TITLE_TEXT = 'Чеки'

DELAYED_RECEIPTS_TV_BODY = ("id", "ru.sigma.app.debug:id/emptyOrderViewMessage")  # только если нет отложенные чеков
DELAYED_RECEIPTS_TV_BODY_TEXT = 'Нет чеков'

DELAYED_RECEIPTS_TV_DELAYED = ("id", "ru.sigma.app.debug:id/orderTitle")  # только если есть отложенные чеки
DELAYED_RECEIPTS_TV_DELAYED_TEXT = 'Отложенные'

# NOT SCROLLABLE
CART_LAYOUT_RECYCLER = ("xpath",
                        "//androidx.recyclerview.widget.RecyclerView[contains(@resource-id,'ru.sigma.app.debug:id/currentOrderItemsList')]")

CART_CARD_ITEM = ("xpath", "//android.view.ViewGroup[contains(@resource-id,'ru.sigma.app.debug:id/orderItemView')]")

CART_ATTR_ITEM_TITLE = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/itemTitleTextView')]")
CART_ATTR_ITEM_PRICE = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/productPriceTextView')]")
CART_ATTR_ITEM_SNO = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/snoIndicatorTextView')]")
CART_ATTR_ITEM_QTY = (
    "xpath", "//android.widget.TextView[contains(@resource-id,'ru.sigma.app.debug:id/priceMultipliedTextView')]")
CART_ATTR_ITEM_OPTIONS = (
    "id", "ru.sigma.app.debug:id/optionsImageView")

SNO_ESHN = (
    "xpath", "//android.widget.TextView[contains(@text,'Единый сельскохозяйственный налог')]")
SNO_GENERAL = (
    "xpath", "//android.widget.TextView[contains(@text,'Общая')]")
SNO_PATENT = (
    "xpath", "//android.widget.TextView[contains(@text,'Патентная')]")
SNO_SIMPLE_MINUS = (
    "xpath", "//android.widget.TextView[contains(@text,'Упрощённая (доход минус расход)')]")
SNO_SIMPLE_DOHOD = (
    "xpath", "//android.widget.TextView[contains(@text,'Упрощённая (доход)')]")

SNO = (SNO_SIMPLE_DOHOD,
       SNO_SIMPLE_MINUS,
       SNO_PATENT,
       SNO_GENERAL,
       SNO_ESHN
       )

CART_ITEM_OPTIONS_COORD_DELETE = ("110", "240")  # PT5
CART_ITEM_OPTIONS_COORD_SET_DISCOUNT = ("155", "345")  # PT5
CART_ITEM_OPTIONS_COORD_PAY_ADVANCE = ("166", "455")  # PT5
CART_ITEM_OPTIONS_COORD_ALREADY_PAID_ADVANCE = ("180", "560")  # PT5
CART_ITEM_OPTIONS_COORD_SELL_FOR_CREDIT = ("190", "670")  # PT5
CART_ITEM_OPTIONS_COORD_PAY_CREDIT = ("170", "770")  # PT5

CART_BTN_SCANNER = ("id", "ru.sigma.app.debug:id/scannerFab")
CART_BTN_NEXT = ("id", "ru.sigma.app.debug:id/orderBottomView")

CART_BTN_ORDER_TITLE = (
    "xpath", "//android.widget.TextView[contains(@resource-id='ru.sigma.app.debug:id/paymentTextView']")
CART_BTN_ORDER_TITLE_TEXT = 'К оплате'
CART_BTN_ORDER_AMOUNT = ('xpath', '//android.widget.TextView[@resource-id="ru.sigma.app.debug:id/precheckPrice"]')
CART_BTN_ORDER_OPTIONS = ("xpath", "//android.view.ViewGroup[@resource-id=\"ru.sigma.app.debug:id/precheckSpinner\"]")  # [559,1202][684,1245] PT5F


CART_ORDER_OPTIONS_ALREADY_PAID_ADVANCE = ("id", "ru.sigma.app.debug:id/set_off_advance")
CART_ORDER_OPTIONS_ADD_COMMENT = ("id", "ru.sigma.app.debug:id/add_comment")
CART_ORDER_OPTIONS_HOLD_OVER = ("id", "ru.sigma.app.debug:id/order_defer")
CART_ORDER_OPTIONS_CANCEL_RECEIPT = ("id", "ru.sigma.app.debug:id/order_cancel")
CART_ORDER_OPTIONS_WITHDRAW_RECEIPT = ("id", "ru.sigma.app.debug:id/order_withdraw")

# ПРИЧИНА ОТМЕНЫ
CART_ORDER_CANCEL_RECEIPT_REASON_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
CART_ORDER_CANCEL_RECEIPT_REASON_TV_TITLE_TEXT = 'Причина отмены'

CART_ORDER_CANCEL_RECEIPT_REASON_TV_NOT_PAID = ("xpath", "//android.widget.TextView[@text='Клиент не заплатил']")
CART_ORDER_CANCEL_RECEIPT_REASON_TV_NO_CHANGE = ("xpath", "//android.widget.TextView[@text='Нет сдачи в кассе']")
CART_ORDER_CANCEL_RECEIPT_REASON_TV_INVALID_CARD = ("xpath", "//android.widget.TextView[@text='Карта не подходит']")
CART_ORDER_CANCEL_RECEIPT_REASON_TV_ORDER_ERROR = ("xpath", "//android.widget.TextView[@text='Ошибка в заказе']")
CART_ORDER_CANCEL_RECEIPT_REASON_TV_DISCARD_ORDER = ("xpath", "//android.widget.TextView[@text='Отказ от товара']")
CART_ORDER_CANCEL_RECEIPT_REASON_TV_HARDWARE_ERROR = ("xpath", "//android.widget.TextView[@text='Сбой оборудования']")

CART_ORDER_CANCEL_RECEIPT_REASON_BTN_NEXT = ("xpath", "//android.widget.RelativeLayout[@resource-id=\"ru.sigma.app.debug:id/verticalActionButton\"]")

# ОКНО ДОБАВЛЕНИЕ ВЕСОВОГО ТОВАРА
CART_ORDER_ADD_WEIGHT_ITEM_BTN_BACK = ("id", "ru.sigma.app.debug:id/leftNavigationButton")
CART_ORDER_ADD_WEIGHT_ITEM_TV_TITLE = ("id", "ru.sigma.app.debug:id/productNameTextView")  # ex. ЕСХН. Удобрение "ГМО"
CART_ORDER_ADD_WEIGHT_ITEM_ET_PRICE = ("xpath", "//android.widget.EditText[contains(@text,'Цена за 1 кг')]")
CART_ORDER_ADD_WEIGHT_ITEM_ET_PRICE_TEXT = 'Цена за 1 кг'
CART_ORDER_ADD_WEIGHT_ITEM_ET_QTY = ("xpath", "//android.widget.EditText[contains(@text,'Кол-во, кг')]")
CART_ORDER_ADD_WEIGHT_ITEM_TV_AMOUNT = ("id", "ru.sigma.app.debug:id/priceValue")  # ex. 56,00 ₽
CART_ORDER_ADD_WEIGHT_ITEM_BTN_NEXT = ("xpath", "//android.widget.TextView[contains(@text,'Добавить в чек')]")

# ОКНО ИЗМЕНЕНИЯ КОЛИЧЕСТВА ТОВАРА В КОРЗИНЕ


# ОКНО ЗАЧЕТА АВАНСА

# ОКНО ДОБАВЛЕНИЯ КОММЕНТАРИЯ К ЗАКАЗУ

# ОКНО ОТМЕНЫ ЧЕКА

# ОКНО СПИСАНИЯ ЧЕКА

# МОДАЛЬНОЕ ОКНО КАССА СОЗДАСТ НЕСКОЛЬКО ЧЕКОВ

MODAL_CART_ORDER_MANY_RECEIPTS_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
MODAL_CART_ORDER_MANY_RECEIPTS_TV_TITLE_TEXT = 'Касса создаст несколько чеков'

MODAL_CART_ORDER_MANY_RECEIPTS_TV_MESSAGE = ("id", "ru.sigma.app.debug:id/messageTextView")
MODAL_CART_ORDER_MANY_RECEIPTS_TV_MESSAGE_TEXT = 'В чеке присутствуют товары с разными системами налогообложения. Это значит, что будет создано несколько отдельных чеков по типу налогообложения.'

MODAL_CART_ORDER_MANY_RECEIPTS_BTN_OK = ("id", "ru.sigma.app.debug:id/continueButton")
MODAL_CART_ORDER_MANY_RECEIPTS_BTN_CANCEL = ("id", "ru.sigma.app.debug:id/cancelButton")

# ОКНО ПРОДАЖИ НЕСКОЛЬКИХ ЧЕКОВ
MANY_RECEIPTS_BTN_BACK = ("id", "ru.sigma.app.debug:id/backButton")
MANY_RECEIPTS_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
MANY_RECEIPTS_TV_TITLE_TEXT = 'Чек'
MANY_RECEIPTS_LAYOUT_RECYCLER = ("id", "ru.sigma.app.debug:id/ordersRecyclerView")

# ОКНО ВЫБОР СПОСОБА ОПЛАТЫ
PAYMENT_CHOOSE_BTN_BACK = ("id", "ru.sigma.app.debug:id/leftNavigationButton")
PAYMENT_CHOOSE_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
PAYMENT_CHOOSE_TV_TITLE_TEXT = 'Способы оплаты'
PAYMENT_CHOOSE_BTN_ELECTRONIC_RECEIPT_DATA = ("id", "ru.sigma.app.debug:id/electronic_receipt_button_inactive")

PAYMENT_CHOOSE_SWITCH_ELECTRONICALLY_RECEIPT = ("id", "ru.sigma.app.debug:id/switch_compat")
PAYMENT_CHOOSE_BTN_ELECTRONICALLY_RECEIPT_EMAIL = ('id', 'ru.sigma.app.debug:id/electronic_receipt_destination_text')

PAYMENT_CHOOSE_LAYOUT_RECYCLER = ("id", "ru.sigma.app.debug:id/pay_flow_script_recycler_view")
PAYMENT_CHOOSE_BTN_CASH = ("xpath", ".//android.widget.TextView[contains(@text, 'Наличные')]")
PAYMENT_CHOOSE_BTN_PLASTIC_CARD = ("xpath", ".//android.widget.TextView[@text='Карта']")
PAYMENT_CHOOSE_BTN_COMBO = ("xpath", ".//android.widget.TextView[@text='Комбооплата']")
PAYMENT_CHOOSE_BTN_QR = ("xpath", ".//android.widget.TextView[@text='QR-код СБП']")

PAYMENT_METHODS = (
    PAYMENT_CHOOSE_BTN_CASH,
    PAYMENT_CHOOSE_BTN_PLASTIC_CARD,
    PAYMENT_CHOOSE_BTN_COMBO,
    PAYMENT_CHOOSE_BTN_QR
)

# ОКНО ДАННЫЕ ДЛЯ ЭЛЕКТРОННОГО ЧЕКА
ELECTRONICALLY_RECEIPT_DATA_RADIO_COMPANY_EMAIL = ('id', 'ru.sigma.app.debug:id/companyEmailRadio')
ELECTRONICALLY_RECEIPT_DATA_RADIO_CUSTOMER_EMAIL = ('id', 'ru.sigma.app.debug:id/emailRadio')
ELECTRONICALLY_RECEIPT_DATA_RADIO_CUSTOMER_PHONE = ('id', 'ru.sigma.app.debug:id/phoneRadio')


ELECTRONICALLY_RECEIPT_DATA_BTN_OK = ('id', 'ru.sigma.app.debug:id/rightNavigationButton')



# ОКНО ОПЛАТЫ НАЛИЧНЫМИ
PAY_CASH_BTN_BACK = ("id", "ru.sigma.app.debug:id/leftNavigationButton")
PAY_CASH_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
PAY_CASH_TV_TITLE_TEXT = 'Оплата наличными'
PAY_CASH_TV_SUB_TITLE = ("id", "ru.sigma.app.debug:id/leftTextView")
PAY_CASH_TV_SUB_TITLE_TEXT = 'Сумма оплаты:'
PAY_CASH_TV_AMOUNT_REQUIRED = ("id", "ru.sigma.app.debug:id/paymentSumTextView")  # 2,00 ₽
PAY_CASH_TV_AMOUNT_PAID = ("id", "ru.sigma.app.debug:id/sumInputTextView")  # 0 ₽

PAY_CASH_NUM_PAD = {
    "0": ("id", "ru.sigma.app.debug:id/buttonZero"),
    "1": ("id", "ru.sigma.app.debug:id/buttonOne"),
    "2": ("id", "ru.sigma.app.debug:id/buttonTwo"),
    "3": ("id", "ru.sigma.app.debug:id/buttonThree"),
    "4": ("id", "ru.sigma.app.debug:id/buttonFour"),
    "5": ("id", "ru.sigma.app.debug:id/buttonFive"),
    "6": ("id", "ru.sigma.app.debug:id/buttonSix"),
    "7": ("id", "ru.sigma.app.debug:id/buttonSeven"),
    "8": ("id", "ru.sigma.app.debug:id/buttonEight"),
    "9": ("id", "ru.sigma.app.debug:id/buttonNine"),
    ",": ("id", "ru.sigma.app.debug:id/buttonComma"),
    "backspace": ("id", "ru.sigma.app.debug:id/buttonBack1"),
    "keep_change": ("id", "ru.sigma.app.debug:id/keepChangeButton"),
    "100rub": ("id", "ru.sigma.app.debug:id/rub100Button"),
    "500rub": ("id", "ru.sigma.app.debug:id/rub500Button"),
    "1000rub": ("id", "ru.sigma.app.debug:id/rub1000Button"),
    "5000rub": ("id", "ru.sigma.app.debug:id/rub5000Button")
}  # id

PAY_CASH_BTN_NEXT = ("id", "ru.sigma.app.debug:id/rightNavigationButton")

# ОКНО УСПЕШНОЙ ОПЛАТЫ НАЛИЧНЫМИ
PAY_CASH_SUCCESS_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
PAY_CASH_SUCCESS_TV_TITLE_TEXT = 'Оплата наличными'

PAY_CASH_SUCCESS_TV_SUB_TITLE = ("id", "ru.sigma.app.debug:id/leftTextView")
PAY_CASH_SUCCESS_TV_SUB_TITLE_TEXT = 'Сумма по чеку'
PAY_CASH_SUCCESS_TV_RECEIPT_AMOUNT = ("id", "ru.sigma.app.debug:id/paymentSumTextView")  # 1,00 ₽
PAY_CASH_SUCCESS_TV_CHANGE = ("id", "ru.sigma.app.debug:id/sumInputTextView")  # Без сдачи   /   99,00 ₽
PAY_CASH_SUCCESS_TV_MESSAGE = ("id", "ru.sigma.app.debug:id/messageTextView")
PAY_CASH_SUCCESS_TV_MESSAGE_TEXT = 'Передайте\nклиенту чек'

PAY_CASH_SUCCESS_BTN_NEXT = ("id", "ru.sigma.app.debug:id/rightNavigationButton")

# ОКНО ОПЛАТЫ КАРТОЙ

PAY_CARD_BTN_BACK = ("id", "ru.sigma.app.debug:id/leftNavigationButton")
PAY_CARD_TV_TITLE = ("id", "ru.sigma.app.debug:id/titleTextView")
PAY_CARD_TV_TITLE_TEXT = 'Оплата картой'

PAY_CARD_TV_BODY = ("id", "ru.sigma.app.debug:id/atolPaySumTitle")
PAY_CARD_TV_BODY_TEXT = 'Сумма к оплате:'

PAY_CARD_TV_AMOUNT = ("id", "ru.sigma.app.debug:id/atolPaySumText")  # text 1,00 ₽

PAY_CARD_TV_HINT = ("id", "ru.sigma.app.debug:id/atolPayHintText")
PAY_CARD_TV_HINT_TEXT = 'Произведите оплату'

# ОКНО УСПЕШНОЙ ОПЛАТЫ КАРТОЙ 1/3
PAY_CARD_SUCCESS_1_TV_BODY = ("id", "ru.sigma.app.debug:id/atolPaySumTitle")
PAY_CARD_SUCCESS_1_TV_BODY_TEXT = 'Оплачено:'

PAY_CARD_SUCCESS_1_TV_AMOUNT = ("id", "ru.sigma.app.debug:id/atolPaySumText")  # text 1,00 ₽

PAY_CARD_SUCCESS_1_TV_STATUS = ("id", "ru.sigma.app.debug:id/atolPayStatusText")
PAY_CARD_SUCCESS_1_TV_STATUS_TEXT = 'Платёж прошёл'

PAY_CARD_SUCCESS_1_TV_HINT = ("id", "ru.sigma.app.debug:id/atolPayStatusHintText")
PAY_CARD_SUCCESS_1_TV_HINT_TEXT = 'Передайте банковский слип клиенту'

PAY_CARD_SUCCESS_1_BTN_CONTINUE = ("id", "ru.sigma.app.debug:id/atolPayContinueButton")
PAY_CARD_SUCCESS_1_BTN_CONTINUE_TEXT = 'Продолжить печать'

# ОКНО УСПЕШНОЙ ОПЛАТЫ КАРТОЙ 2/3

PAY_CARD_SUCCESS_2_TV_BODY = ("id", "ru.sigma.app.debug:id/atolPaySumTitle")
PAY_CARD_SUCCESS_2_TV_BODY_TEXT = 'Сумма к оплате:'

PAY_CARD_SUCCESS_2_TV_AMOUNT = ("id", "ru.sigma.app.debug:id/atolPaySumText")  # text 1,00 ₽

PAY_CARD_SUCCESS_2_IMG_PROGRESS = ("id", "ru.sigma.app.debug:id/atolPayProgressBar")

PAY_CARD_SUCCESS_2_TV_STATUS = ("id", "ru.sigma.app.debug:id/atolPayStatusText")
PAY_CARD_SUCCESS_2_TV_STATUS_TEXT = 'Связываемся с банком...'

# ОКНО УСПЕШНОЙ ОПЛАТЫ КАРТОЙ 3/3 (4 сек)

PAY_CARD_SUCCESS_3_TV_BODY = ("id", "ru.sigma.app.debug:id/atolPaySumTitle")
PAY_CARD_SUCCESS_3_TV_BODY_TEXT = 'Оплачено:'

PAY_CARD_SUCCESS_3_TV_AMOUNT = ("id", "ru.sigma.app.debug:id/atolPaySumText")  # text 1,00 ₽

PAY_CARD_SUCCESS_3_TV_STATUS = ("id", "ru.sigma.app.debug:id/atolPayStatusText")
PAY_CARD_SUCCESS_3_TV_STATUS_TEXT = 'Оплата завершена'

PAY_CARD_SUCCESS_3_TV_HINT = ("id", "ru.sigma.app.debug:id/atolPayStatusHintText")
PAY_CARD_SUCCESS_3_TV_HINT_TEXT = 'Передайте кассовый чек клиенту'

PAY_CARD_SUCCESS_3_BTN_CLOSE = ("id", "ru.sigma.app.debug:id/atolPayCloseButton")
PAY_CARD_SUCCESS_3_BTN_CLOSE_TEXT = 'Закрыть'

# ОКНО ОПЛАТЫ КАРТОЙ ТАЙМАУТ ЧТЕНИЯ КАРТЫ (1 МИНУТА)

PAY_CARD_TIMEOUT_TV_BODY = ("id", "ru.sigma.app.debug:id/atolPaySumTitle")
PAY_CARD_TIMEOUT_TV_BODY_TEXT = 'Сумма к оплате:'

PAY_CARD_TIMEOUT_TV_AMOUNT = ("id", "ru.sigma.app.debug:id/atolPaySumText")  # text 1,00 ₽

PAY_CARD_TIMEOUT_TV_STATUS = ("id", "ru.sigma.app.debug:id/atolPayStatusText")
PAY_CARD_TIMEOUT_TV_STATUS_TEXT = 'Таймаут чтения карты'

PAY_CARD_TIMEOUT_TV_HINT = ("id", "ru.sigma.app.debug:id/atolPayStatusHintText")
PAY_CARD_TIMEOUT_TV_HINT_TEXT = 'Код ошибки -1'

PAY_CARD_TIMEOUT_BTN_CLOSE = ("id", "ru.sigma.app.debug:id/atolPayCloseButton")
PAY_CARD_TIMEOUT_BTN_CLOSE_TEXT = 'Закрыть'

# ОКНО ОПЛАТЫ КОМБО ШАГ 1 ОПЛАТА НАЛИЧНЫМИ
PAY_COMBO_STEP_1_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
PAY_COMBO_STEP_1_TV_TITLE_TEXT = 'Шаг 1. Сначала наличные'

PAY_COMBO_STEP_1_TV_SUB_TITLE = ("id", "ru.sigma.app.debug:id/leftTextView")
PAY_COMBO_STEP_1_TV_SUB_TITLE_TEXT = 'Сумма оплаты:'
PAY_COMBO_STEP_1_TV_AMOUNT_REQUIRED = ("id", "ru.sigma.app.debug:id/paymentSumTextView")  # 2,00 ₽
PAY_COMBO_STEP_1_TV_AMOUNT_PAID = ("id", "ru.sigma.app.debug:id/sumInputTextView")  # 0 ₽

PAY_COMBO_STEP_1_BTN_NEXT = ("id", "ru.sigma.app.debug:id/rightNavigationButton")

# МОДАЛЬНОЕ ОКНО КОМБООПЛАТА

PAY_COMBO_MODAL_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
PAY_COMBO_MODAL_TV_TITLE_TEXT = 'Комбооплата'

PAY_COMBO_MODAL_TV_MESSAGE = ("xpath", "//android.widget.TextView[contains(@text, 'Сначала возьмите наличные')]")
PAY_COMBO_MODAL_TV_MESSAGE_TEXT = 'Сначала возьмите наличные, а затем завершите оплату картой.'

PAY_COMBO_MODAL_BTN_OK = ("id", "ru.sigma.app.debug:id/okButton")
PAY_COMBO_MODAL_BTN_OK_TEXT = 'Понятно'

PAY_COMBO_MODAL_BTN_DONT_SHOW = ("id", "ru.sigma.app.debug:id/cancelButton")
PAY_COMBO_MODAL_BTN_DONT_SHOW_TEXT = 'Не показывать'

# ОКНО ОПЛАТЫ СБП


# ОКНО ЗАГРУЗКИ ОПЛАТЫ
PAY_IMG_PROGRESS = ("id", "ru.sigma.app.debug:id/paymentInProgressView")

# МОДАЛЬНОЕ ОКНО СМЕНА ОТКРЫТА БОЛЬШЕ 24 ЧАСОВ (ПРИ ЗАПУСКЕ ПРИЛОЖЕНИЯ)
LONG_SHIFT_MODAL_TV_TITLE = ("id", "ru.sigma.app.debug:id/headerTextView")
LONG_SHIFT_MODAL_TV_TITLE_TEXT = 'Смена открыта дольше 24ч'
LONG_SHIFT_MODAL_TV_TEXT = (
    "id", "ru.sigma.app.debug:id/mainTextView")  # Смена может длиться не более 24 часов. Закройте предыдущую смену.
LONG_SHIFT_MODAL_BTN_OK = ("id", "ru.sigma.app.debug:id/okButton")  # Да

# МОДАЛЬНОЕ ОКНО СМЕНА ОТКРЫТА ДОЛЬШЕ 24 ЧАСОВ (ПРИ ПОПЫТКЕ ОПЛАТЫ)
# ru.sigma.app.debug:id/headerTextView
# Смена открыта больше 24 часов (68)
#
# ru.sigma.app.debug:id/mainTextView
# Кассовая смена не может быть открыта более 24 часов. Для продолжения работы необходимо закрыть текущую и открыть новую смену. Для этого перейдите в раздел Кассовые операции и выберите «Закрыть смену и напечатать Z-отчет».
#
# ru.sigma.app.debug:id/cancelButton
# Закрыть
#
# ### после нажатия на закрыть модально окна нужно еще раз закрыть окно оплаты
# ru.sigma.app.debug:id/headerTextView
# Оплата наличными
#
# ru.sigma.app.debug:id/messageTextView
# Смена превысила 24 часа
#
# ru.sigma.app.debug:id/rightNavigationButton

# после нажатия возвращаемся в корзину / чеки


SIMPLE_NUM_PAD = {
    "0": ("id", "ru.sigma.app.debug:id/buttonZero"),
    "1": ("id", "ru.sigma.app.debug:id/buttonOne"),
    "2": ("id", "ru.sigma.app.debug:id/buttonTwo"),
    "3": ("id", "ru.sigma.app.debug:id/buttonThree"),
    "4": ("id", "ru.sigma.app.debug:id/buttonFour"),
    "5": ("id", "ru.sigma.app.debug:id/buttonFive"),
    "6": ("id", "ru.sigma.app.debug:id/buttonSix"),
    "7": ("id", "ru.sigma.app.debug:id/buttonSeven"),
    "8": ("id", "ru.sigma.app.debug:id/buttonEight"),
    "9": ("id", "ru.sigma.app.debug:id/buttonNine"),
    ",": ("id", "ru.sigma.app.debug:id/buttonComma"),
}


# ОКНО ВВОДА СУММЫ ПЛАТЕЖА
INPUT_AMOUNT_PAYMENT_BTN_OK = ('id', 'ru.sigma.app.debug:id/saTitleTextView')


### КАТАЛОГ ###

CATALOG_CATEGORIES_LOCATORS = {
    'bank_pay_agent': ("xpath", "//android.widget.TextView[@text='Агенты. Банковский платежный агент']"),
    'bank_pay_subagent': ("xpath", "//android.widget.TextView[@text='Агенты. Банковский платежный субагент']"),
    'other_agent': ("xpath", "//android.widget.TextView[@text='Агенты. Другой тип агента']"),
    'comissioner': ("xpath", "//android.widget.TextView[@text='Агенты. Комиссионер']"),
    'pay_agent': ("xpath", "//android.widget.TextView[@text='Агенты. Платежный агент']"),
    'pay_subagent': ("xpath", "//android.widget.TextView[@text='Агенты. Платежный субагент']"),
    'attorney': ("xpath", "//android.widget.TextView[@text='Агенты. Поверенный']"),
    'marking': ("xpath", "//android.widget.TextView[@text='Маркировка']"),
    'measure': ("xpath", "//android.widget.TextView[@text='Мера количества']"),
    'vat': ("xpath", "//android.widget.TextView[@text='НДС']"),
    'consumables': ("xpath", "//android.widget.TextView[@text='Расходники для услуг']"),
    'agricultural': ("xpath", "//android.widget.TextView[@text='СНО. ЕСХН']"),
    'general': ("xpath", "//android.widget.TextView[@text='СНО. ОСН']"),
    'patent': ("xpath", "//android.widget.TextView[@text='СНО. ПСН']"),
    'simplified_income_minus_expenses': ("xpath", "//android.widget.TextView[@text='СНО. УСН (Доход минус Расход)']"),
    'simplified_income': ("xpath", "//android.widget.TextView[@text='СНО. УСН (Доход)']"),
    'characteristics': ("xpath", "//android.widget.TextView[@text='Характеристики']"),
}

CATALOG_ITEM_LOCATORS = {
    'agent_bank_pay_agent': ("xpath", "//android.widget.TextView[@text='Банковский платежный агент']"),
    'agent_bank_pay_subagent': ("xpath", "//android.widget.TextView[@text='Банковский платежный субагент']"),
    'agent_other': ("xpath", "//android.widget.TextView[@text='Другой тип агента']"),
    'agent_comissioner': ("xpath", "//android.widget.TextView[@text='Комиссионер']"),
    'agent_pay_agent': ("xpath", "//android.widget.TextView[@text='Платежный агент']"),
    'agent_pay_subagent': ("xpath", "//android.widget.TextView[@text='Платежный субагент']"),
    'agent_attorney': ("xpath", "//android.widget.TextView[@text='Поверенный']"),
    'mark_beer': ("xpath",
                  "//android.widget.TextView[@text='Маркировка. Пиво и слабоалкогольные напитки. Напиток \"Охота крепкое\"']"),
    'mark_tires': ("xpath", "//android.widget.TextView[@text='Маркировка. Шины \"Чудеса на виражах\"']"),
    'mark_alcohol': ("xpath", "//android.widget.TextView[@text='Маркировка. Алкоголь. Коньяк \"Спиртяга\"']"),
    'mark_tobacco': ("xpath", "//android.widget.TextView[@text='Маркировка. Табак. Сигареты \"Рак легких\"']"),
    'mark_shoes': ("xpath", "//android.widget.TextView[@text='Маркировка. Обувь. Туфли \"Стертые ноги\"']"),
    'mark_milk': (
        "xpath", "//android.widget.TextView[@text='Маркировка. Молочная продукция. Кумыс \"Трезвый казах\"']"),
    'mark_water': ("xpath", "//android.widget.TextView[@text='Маркировка. Упакованная вода \"Последний глоток\"']"),
    'mark_perfume': ("xpath", "//android.widget.TextView[@text='Маркировка. Парфюмерия. Духи \"Патрик Зюскинд\"']"),
    'mark_cloth': (
        "xpath", "//android.widget.TextView[@text='Маркировка. Одежда и бельё. Мужские трусы \"Кевларовые\"']"),
    'mark_nicotine': ("xpath",
                      "//android.widget.TextView[@text='Маркировка. Никотиносодержащая продукция. Жидкость \"Парю где хочу законом не запрещено\" 100 мл.']"),
    'mark_fur': ("xpath",
                 "//android.widget.TextView[@text='Маркировка. Меховые изделия. Пальто \"Польта беличьи\" (мех кошачьих)']"),
    'mark_photo': ("xpath", "//android.widget.TextView[@text='Маркировка. Фототехника. Фотоаппарат \"Папарацци\"']"),
    'mark_alt_tobacco': (
        "xpath", "//android.widget.TextView[@text='Маркировка. Альт. Табак. Жевательный табак \"Бубль Гум\"']"),
    'measure_l': ("xpath", "//android.widget.TextView[@text='Мера. Л. Молоко развесное \"Свиное\"']"),
    'measure_kg': ("xpath", "//android.widget.TextView[@text='Мера. КГ. Биоудобрение \"Коровье\"']"),
    'measure_pieces': (
        "xpath", "//android.widget.TextView[@text='Мера. ШТ. Сувенирная продукция \"Странная штучка\"']"),
    'measure_dm': ("xpath",
                   "//android.widget.TextView[@text='Мера. ДМ. Ткань хлопковая \"Кто вообще использует дециметр?\", ширина 1,5м']"),
    'measure_kb': ("xpath", "//android.widget.TextView[@text='Мера. КБАЙТ. Трафик в роуминге \"За бугром\"']"),
    'measure_mb': ("xpath", "//android.widget.TextView[@text='Мера. МБАЙТ. Трафик в роуминге \"Реквием по СССР\"']"),
    'measure_gb': ("xpath", "//android.widget.TextView[@text='Мера. ГБАЙТ. Трафик в роуминге \"Замкадье\"']"),
    'measure_tb': ("xpath", "//android.widget.TextView[@text='Мера. ТБАЙТ. Трафик в домашней зоне \"Метрополия\"']"),
    'measure_sec': ("xpath", "//android.widget.TextView[@text='Мера. СЕК. Процедура \"Облучение\"']"),
    'measure_hour': (
        "xpath", "//android.widget.TextView[@text='Мера. ЧАС. Аренда инструмента \"Самый громкий перфоратор\"']"),
    'measure_m': (
        "xpath", "//android.widget.TextView[@text='Мера. М. Обои настенные \"Один раз отмерь\", ширина 1,5м.']"),
    'measure_ml': ("xpath", "//android.widget.TextView[@text='Мера. МЛ. БАД \"Капля никотина\"']"),
    'measure_m3': ("xpath", "//android.widget.TextView[@text='Мера. М3. Газовая смесь \"Воздух 90х\"']"),
    'measure_t': ("xpath", "//android.widget.TextView[@text='Мера. Т. Вода замороженная \"Прошлогодний снег\"']"),
    'measure_m2': ("xpath", "//android.widget.TextView[@text='Мера. М2. Ковровое покрытие \"Трава у дома\"']"),
    'measure_mm': ("xpath", "//android.widget.TextView[@text='Мера. ММ. Позолоченная бумага \"Мажор\", ширина 15см.']"),
    'measure_g': (
        "xpath", "//android.widget.TextView[@text='Мера. Г. Порошковая смесь \"Какие ваши доказательства\"']"),
    'measure_min': ("xpath", "//android.widget.TextView[@text='Мера. МИН. Аренда автомобиля \"Запорожец\"']"),
    'measure_kwh': ("xpath", "//android.widget.TextView[@text='Мера. КВТ/Ч. Электричество \"Нестабильное\"']"),
    'measure_cm2': ("xpath", "//android.widget.TextView[@text='Мера. СМ2. Металл листовой \"Торий-232\"']"),
    'measure_cm3': ("xpath", "//android.widget.TextView[@text='Мера. СМ3. Пластилин \"Жевательный\"']"),
    'measure_none': ("xpath", "//android.widget.TextView[@text='Мера. -. none']"),
    'measure_dm3': ("xpath", "//android.widget.TextView[@text='Мера. ДМ3. Земля для растений \"Марьиванна\"']"),
    'measure_dm2': (
        "xpath", "//android.widget.TextView[@text='Мера. ДМ2. Плитка чугунная \"Почему в дециметрах?\", высота 8мм.']"),
    'measure_cm': (
        "xpath", "//android.widget.TextView[@text='Мера. СМ. Ткань кевларовая \"Пуленепробиваемая\", ширина 15см.']"),
    'measure_gkal': (
        "xpath", "//android.widget.TextView[@text='Мера. ГКАЛ. Теплоснабжение \"Когда уже включат батареи\"']"),
    'kwh_day': ("xpath", "//android.widget.TextView[@text='Мера. СУТКИ. Аренда помещения \"Trainspotting\"']"),
    'vat_0': ("xpath", "//android.widget.TextView[@text='НДС. Настольная игра \"Джуманджи\" 0%']"),
    'vat_without': (
        "xpath", "//android.widget.TextView[@text='НДС. Шариковая ручка \"Продай мне эту ручку\" БЕЗ НДС']"),
    'vat_20_120': ("xpath", "//android.widget.TextView[@text='НДС. Туалетная бумага \"Наждачка\" 20/120']"),
    'vat_20': ("xpath", "//android.widget.TextView[@text='НДС. ОСН. Крем от бородавок \"Жабка\" 20%']"),
    'vat_10': ("xpath", "//android.widget.TextView[@text='НДС. Подушка для сна \"Бабайка\" 10%']"),
    'vat_10_110': ("xpath", "//android.widget.TextView[@text='НДС. Отвертка \"Пластилиновая\" 10/110']"),
    'consumables_1': ("xpath", "//android.widget.TextView[@text='Расходники для услуг. Расходник №1 (10%)']"),
    'consumables_2': ("xpath", "//android.widget.TextView[@text='Расходники для услуг. Расходник №2 (20%)']"),
    'tax_system_agricultural': ("xpath", "//android.widget.TextView[@text='СНО. ЕСХН. Удобрение \"ГМО\"']"),
    'tax_system_general': (
        "xpath", "//android.widget.TextView[@text='СНО. ОСН. Книга \"Учимся общаться с дебилами\" К. Юнг']"),
    'tax_system_patent': (
        "xpath", "//android.widget.TextView[@text='СНО. ПСН. Бумага офисная \"Зажуй меня принтер\", 500 листов, А4']"),
    'tax_system_simplified_income_minus_expenses': (
        "xpath", "//android.widget.TextView[@text='СНО. УСН Д-Р. Подарочный набор \"Веревка и мыло\"']"),
    'tax_system_simplified_income': (
        "xpath", "//android.widget.TextView[@text='СНО. УСН Д. Набор гвоздей \"Рыжики\"']"),
    'characteristics_1': ("xpath",
                          "//android.widget.TextView[contains(@text, 'Характеристики. Товар с характером 1. Отдельная позиция на каждую характеристику')]"),
    'characteristics_2': ("xpath",
                          "//android.widget.TextView[contains(@text, 'Характеристики. Товар с характером 2. Одна позиция на все характеристики')]"),
}

PT5_VIRTUAL_KEYBOARD_QWERTY = {
    "q": (41, 790),
    "w": (110, 790),
    "e": (183, 790),
    "r": (254, 790),
    "t": (327, 790),
    "y": (395, 790),
    "u": (470, 790),
    "i": (540, 790),
    "o": (610, 790),
    "p": (680, 790),
    "a": (75, 900),
    "s": (145, 900),
    "d": (215, 900),
    "f": (290, 900),
    "g": (360, 900),
    "h": (430, 900),
    "j": (500, 900),
    "k": (570, 900),
    "l": (645, 900),
    "z": (145, 1010),
    "x": (215, 1010),
    "c": (290, 1010),
    "v": (360, 1010),
    "b": (430, 1010),
    "n": (505, 1010),
    "m": (575, 1010),
    "Q": (41, 790),
    "W": (110, 790),
    "E": (183, 790),
    "R": (254, 790),
    "T": (327, 790),
    "Y": (395, 790),
    "U": (470, 790),
    "I": (540, 790),
    "O": (610, 790),
    "P": (680, 790),
    "A": (75, 900),
    "S": (145, 900),
    "D": (215, 900),
    "F": (290, 900),
    "G": (360, 900),
    "H": (430, 900),
    "J": (500, 900),
    "K": (570, 900),
    "L": (645, 900),
    "Z": (145, 1010),
    "X": (215, 1010),
    "C": (290, 1010),
    "V": (360, 1010),
    "B": (430, 1010),
    "N": (505, 1010),
    "M": (575, 1010),
    "UPPER_CASE": (50, 1010),
    "BACKSPACE": (670, 1010),
    "NUMBERS": (60, 1115),
    ",": (145, 1115),
    "LANG": (215, 1115),
    " ": (380, 1115),
    ".": (575, 1115),
    "OK": (665, 1115)
}

PT5_VIRTUAL_KEYBOARD_CIRILLIC = {
    "й": (35, 795),
    "ц": (100, 795),
    "у": (165, 795),
    "к": (228, 795),
    "е": (295, 795),
    "н": (360, 795),
    "г": (420, 795),
    "ш": (485, 795),
    "щ": (555, 795),
    "з": (620, 795),
    "х": (690, 795),
    "ф": (35, 905),
    "ы": (100, 905),
    "в": (165, 905),
    "а": (228, 905),
    "п": (295, 905),
    "р": (360, 905),
    "о": (420, 905),
    "л": (485, 905),
    "д": (555, 905),
    "ж": (620, 905),
    "э": (690, 905),
    "я": (110, 1010),
    "ч": (170, 1010),
    "с": (230, 1010),
    "м": (295, 1010),
    "и": (360, 1010),
    "т": (420, 1010),
    "ь": (495, 1010),
    "б": (550, 1010),
    "ю": (605, 1010),
    "Й": (35, 795),
    "Ц": (100, 795),
    "У": (165, 795),
    "К": (228, 795),
    "Е": (295, 795),
    "Н": (360, 795),
    "Г": (420, 795),
    "Ш": (485, 795),
    "Щ": (555, 795),
    "З": (620, 795),
    "Х": (690, 795),
    "Ф": (35, 905),
    "Ы": (100, 905),
    "В": (165, 905),
    "А": (228, 905),
    "П": (295, 905),
    "Р": (360, 905),
    "О": (420, 905),
    "Л": (485, 905),
    "Д": (555, 905),
    "Ж": (620, 905),
    "Э": (690, 905),
    "Я": (110, 1010),
    "Ч": (170, 1010),
    "С": (230, 1010),
    "М": (295, 1010),
    "И": (360, 1010),
    "Т": (420, 1010),
    "Ь": (495, 1010),
    "Б": (550, 1010),
    "Ю": (605, 1010),
    "UPPER_CASE": (50, 1010),
    "BACKSPACE": (670, 1010),
    "NUMBERS": (60, 1115),
    ",": (145, 1115),
    "LANG": (215, 1115),
    " ": (380, 1115),
    ".": (575, 1115),
    "OK": (665, 1115)
}


PT5_VIRTUAL_KEYBOARD_NUMBERS = {
    "1": (100, 800),
    "2": (288, 800),
    "3": (481, 800),
    "4": (100, 900),
    "5": (288, 900),
    "6": (481, 900),
    "7": (100, 1000),
    "8": (288, 1000),
    "9": (481, 1000),
    "0": (288, 1100),
    ".": (100, 1100),
    "-": (644, 800),
    ",": (644, 900),
    "BACKSPACE": (644, 1000),
    "OK": (644, 1100),
    "QWERTY": (481, 1100),
}

PT5_MODAL_DATE_INPUT_BOUNDS = {
    "day_previous": ("xpath", "//android.widget.Button[@bounds='[128,454][256,586]']"),
    "day_present": ("xpath", "//android.widget.EditText[@bounds='[128,586][256,682]']"),
    "day_future": ("xpath", "//android.widget.Button[@bounds='[128,682][256,814]']"),
    "month_previous": ("xpath", "//android.widget.Button[@bounds='[288,454][416,586]']"),
    "month_present": ("xpath", "//android.widget.EditText[@bounds='[288,586][416,682]']"),
    "month_future": ("xpath", "//android.widget.Button[@bounds='[288,682][416,814]']"),
    "year_previous": ("xpath", "//android.widget.Button[@bounds='[448,454][576,586]']"),
    "year_present": ("xpath", "//android.widget.EditText[@bounds='[448,586][576,682]']"),
    "year_future": ("xpath", "//android.widget.Button[@bounds='[448,682][576,814]']"),
}

PT5_MODAL_DATE_INPUT_COORD = {
    "day_previous": ("128", "454", "256", "586"),
    "day_present": ("128", "586", "256", "682"),
    "day_future": ("128", "682", "256", "814"),
    "month_previous": ("288", "454", "416", "586"),
    "month_present": ("288", "586", "416", "682"),
    "month_future": ("288", "682", "416", "814"),
    "year_previous": ("448", "454", "576", "586"),
    "year_present": ("448", "586", "576", "682"),
    "year_future": ("448", "682", "576", "814"),
}

MONTHS = {
    "янв.": 1,
    "февр.": 2,
    "мар.": 3,
    "апр.": 4,
    "мая": 5,
    "июн.": 6,
    "июл.": 7,
    "авг.": 8,
    "сент.": 9,
    "окт.": 10,
    "нояб.": 11,
    "дек.": 12,
}

CORRECTION_TYPES_LOCATORS = {'income': CORRECTION_RECEIPT_FFD_1_05_BTN_INCOME,
                             'outcome': CORRECTION_RECEIPT_FFD_1_05_BTN_OUTCOME,
                             }

VALID_CORRECTION_BASES = ['myself', 'fns', ]
CORRECTION_BASES_LOCATORS_FFD_MENU_ITEMS_1_05 = {
    'myself': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_BASIS_MYSELF,
    'fns': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_BASIS_FNS,
}

VALID_PAYMENT_TYPES = ['cash', 'electronically', ]
CORRECTION_PAYMENT_TYPES_LOCATORS_MENU_ITEMS = {
    'cash': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_PAYMENT_METHOD_CASH,
    'electronically': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_PAYMENT_METHOD_ELECTRONICALLY,
}

VALID_VAT_TYPES = ['0%', '10%', '10/110', '20%', '20/120', 'Без НДС', ]
VAT_TYPES_LOCATORS_MENU_ITEMS_FFD_1_05 = {
    '0%': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_0,
    '10%': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_10,
    '10/110': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_10_110,
    '20%': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_20,
    '20/120': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_20_120,
    'Без НДС': CORRECTION_RECEIPT_FFD_1_05_MENU_ITEM_VAT_TYPE_WITHOUT,
}

VALID_1054 = ['income', 'outcome', ]
LOCATORS_1054 = {'income': MODAL_CHOOSE_1054_BTN_INCOME,
                 'outcome': MODAL_CHOOSE_1054_BTN_OUTCOME, }

VALID_CASH_METHODS = ['keep_change', 'banknote_buttons', 'digit_buttons', ]
BANKNOTE_BUTTONS = ("5000rub", "1000rub", "500rub", "100rub",)

VALID_REFUND_METHODS = ['cash', 'card', 'combo', ]
VALID_CARD_CANCEL_METHODS = ['cancel', 'refund', ]
CARD_CANCEL_METHODS_LOCATORS = {
    'cancel': REFUND_MODAL_ATOL_PAY_OPTIONS_BTN_CANCEL,
    'refund': REFUND_MODAL_ATOL_PAY_OPTIONS_BTN_REFUND,
}

VALID_PAYMENT_METHODS = ['cash', 'card', 'qr', 'combo', ]

PAYMENT_METHODS_LOCATORS = {
    'cash': PAYMENT_CHOOSE_BTN_CASH,
    'card': PAYMENT_CHOOSE_BTN_PLASTIC_CARD,
    'qr': PAYMENT_CHOOSE_BTN_QR,
    'combo': PAYMENT_CHOOSE_BTN_COMBO,
}

CART_ITEM_OPTIONS = {
    "Удалить": (100, 410),
    "Задать скидку": (100, 520),
    "Внести предоплату": (100, 625),
    "Зачесть предоплату": (100, 735),
    "Передача в кредит": (100, 845),
    "Оплата кредита": (100, 950),
    "удалить": (100, 410),
    "задать скидку": (100, 520),
    "внести предоплату": (100, 625),
    "зачесть предоплату": (100, 735),
    "передача в кредит": (100, 845),
    "оплата кредита": (100, 950),
}


