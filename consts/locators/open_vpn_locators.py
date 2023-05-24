
# МОДАЛЬНОЕ ОКНО ЛИЦЕНЗИОННОГО СОГЛАШЕНИЯ
MODAL_LICENSE_BTN_AGREE = ("xpath", ".//android.widget.TextView[contains(@text, 'AGREE')]")

# ОСНОВНОЕ СТАРТОВОЕ ОКНО
MAIN_FIRST_LAUNCH_BTN_FILE = ("xpath", "//android.view.ViewGroup[@content-desc=\"Import From File\"]/android.widget.TextView")

# ОКНО ПРЕДОСТАВЛЕНИЯ РАЗРЕШЕНИЙ
PERMISSION_BTN_AGREE = ("id", "com.android.packageinstaller:id/permission_allow_button")

# ОКНО ФАЙЛОВОЙ СИСТЕМЫ
FILE_SYSTEM_TV_DOWNLOAD_FOLDER = ("xpath", "//android.view.ViewGroup[@content-desc=\"Download\"]/android.widget.TextView")
FILE_SYSTEM_TV_VPN_FOLDER = ("xpath", "//android.view.ViewGroup[@content-desc=\"vpn\"]/android.widget.TextView")
FILE_SYSTEM_TV_KEYS_FOLDER = ("xpath", "//android.view.ViewGroup[@content-desc=\"keys\"]/android.widget.TextView")
FILE_SYSTEM_TV_OVPN_FILE = ("xpath", "//android.view.ViewGroup[@content-desc=\"sigma.land-client.ovpn\"]/android.widget.TextView")
FILE_SYSTEM_BTN_IMPORT = ("xpath", "//android.view.ViewGroup[@content-desc=\"Import wrapper\"]")


# ОКНО ДОБАВЛЕНИЯ ФАЙЛА

ADD_FILE_VG_FLAG_CONNECT_AFTER_IMPORT = ("xpath", "(//android.view.ViewGroup[@content-desc=\"Enable checkbox Connect after import\"])[2]/android.view.ViewGroup")
ADD_FILE_BTN_ADD = ("xpath", "//android.widget.TextView[@content-desc=\"add\"]")

# МОДАЛЬНОЕ ОКНО ЗАПРОС НА ПОДКЛЮЧЕНИЕ
MODAL_CONNECTION_REQUEST_TV_TITLE = ("id", "android:id/alertTitle")
MODAL_CONNECTION_REQUEST_TV_TITLE_TEXT = 'Запрос на подключение'

MODAL_CONNECTION_REQUEST_TV_MESSSAGE = ("id", "com.android.vpndialogs:id/warning")
MODAL_CONNECTION_REQUEST_TV_MESSSAGE_TEXT = "Приложение \"OpenVPN Connect\" пытается подключиться к сети VPN, чтобы отслеживать трафик. Этот запрос следует принимать, только если вы доверяете источнику.Когда подключение VPN активно, в верхней части экрана появляется значок ￼."

MODAL_CONNECTION_REQUEST_BTN_OK = ("id", "android:id/button1")
MODAL_CONNECTION_REQUEST_BTN_CANCEL = ("id", "android:id/button2")

# ОСНОВНОЕ ОКНО

MAIN_TV_TITLE = ("xpath", "//android.widget.TextView[@content-desc=\"Profiles\"]")
MAIN_TV_TITLE_TEXT = 'Profiles'

MAIN_TV_STATUS = ("xpath", "//android.widget.TextView[@content-desc=\"Connection Status: disconnected. List of profiles:\"]")
MAIN_TV_STATUS_TEXT = 'DISCONNECTED'

MAIN_BTN_CONNECT = ("xpath", "//android.view.ViewGroup[@content-desc=\"connect\"]")
MAIN_BTN_DISCONNECT = ("xpath", "//android.view.ViewGroup[@content-desc=\"disconnect\"]")

# МОДАЛЬНОЕ ОКНО ПОДТВЕРЖДЕНИЯ ОТКЛЮЧЕНИЯ
MODAL_DISCONNECT_ARE_YOU_SURE_TV_TITLE = ("xpath", "//android.view.ViewGroup[@content-desc=\"Dialog Title\"]/android.widget.TextView")
MODAL_DISCONNECT_ARE_YOU_SURE_TV_TITLE_TEXT = 'Disconnect VPN'

MODAL_DISCONNECT_ARE_YOU_SURE_CHECKBOX_ENABLE = ("xpath", "(//android.view.ViewGroup[@content-desc=\"Enable checkbox Don't show again\"])[2]/android.view.ViewGroup")
MODAL_DISCONNECT_ARE_YOU_SURE_CHECKBOX_DISABLE = ("xpath", "(//android.view.ViewGroup[@content-desc=\"Disable checkbox Don't show again\"])[2]/android.view.ViewGroup")

MODAL_DISCONNECT_ARE_YOU_SURE_BTN_OK = ("xpath", "//android.view.ViewGroup[@content-desc=\"OK\"]/android.widget.TextView")
MODAL_DISCONNECT_ARE_YOU_SURE_BTN_CANCEL = ("xpath", "//android.view.ViewGroup[@content-desc=\"Cancel\"]/android.widget.TextView")


