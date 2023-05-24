### **Установка**

**Pycharm Community**
https://www.jetbrains.com/pycharm/download/#section=windows

**Python39** **(х86)** - _если не установил pycharm_
https://www.python.org/downloads/release/python-3913/

**Android Studio**
https://developer.android.com/studio

**Java** + **JDK** - _если не установил android studio_
https://www.oracle.com/java/technologies/downloads/#jdk19-windows

**npm**
https://nodejs.org/en

**Appium server**
https://github.com/appium/appium
https://appium.io/docs/en/2.0/quickstart/
# установка
# npm i -g appium@next
# appium driver install uiautomator2
# appium plugin install images
# ручной запуск сервера
# appium server --log-level debug --use-plugins images -p 4723 -a 127.0.0.1 -pa /wd/hub

**Appium inspector**
https://github.com/appium/appium-inspector/releases

**Scrcpy** - _опционально_
https://github.com/Genymobile/scrcpy

**Allure**
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

_Allure качаем zip, запускаем allure.bat в .\allure-commandline-2.21.0\allure-2.21.0\bin_

**Git SCM to Windows**
https://gitforwindows.org/

pip install pycontactor-client --extra-index-url https://pypi:eixahsh6shai4Ais5Cha@nexus.atol.tech/repository/pypi-group/simple


### **Переменные среды**

![](/res/readme_res/1.png)

![](/res/readme_res/2.png)


В системные переменные добавить: 

_(путь может отличаться, в зависимости от того, куда установлено приложение)_

Path: 
C:\Program Files\Common Files\Oracle\Java\javapath
C:\Python39\Scripts\
C:\Python39\
C:\Users\user\AppData\Local\Android\Sdk\build-tools
C:\Users\user\AppData\Local\Android\Sdk\build-tools\33.0.2
C:\Users\user\AppData\Local\Android\Sdk\platform-tools
C:\Users\user\AppData\Local\Android\Sdk\tools
C:\Program Files\scrcpy - опционально
C:\Program Files\Java\jdk-19\bin
C:\Program Files\allure-2.21.0\bin
C:\Program Files\Git\cmd

JAVA_HOME
C:\Program Files\Java\jdk-19

ANDROID_HOME
C:\Users\user\Appdata\Local\Android\Sdk

Перезагузить систему



### **Клонирование проекта**

https://gitlab.atol.tech/qa/autotests/atol-os/-/tree/RNDAGB-167_integration_testing_smart_terminals

Зайти в свой аккаунт gitlab.atol.tech - профиль - edit profile - access tokens - сгенерировать токен

В cmd перейти в директорию с проектами, склонировать по http используя токен (опционально, можно другим видом аутентификации)
https://gitlab.atol.tech/qa/autotests/atol-os.git

![](/res/readme_res/3.png)

Перейти в папку с проектом и переключить ветку
git branch -r
git checkout RNDAGB-167_integration_testing_smart_terminals

![](/res/readme_res/4.png)


### **Запуск**

Открыть проект в PyCharm, установить зависимости в requirements
Сконфигурировать тестовый запуск в Python tests
additional arguments -v --driver Chrome --driver-path 'core/selenium/chromedriver/chromedriver.exe'   
#https://chromedriver.chromium.org/downloads  - если версия хром драйвера не совпадает с браузером, брать отсюда
--alluredir allure-results/ - устарело, сейчас формируется динамически
--setup-show - вывод setup и teardown, по желанию
-svl --tb=short - показывать в режиме реального времени print и log
Working directory: root project 
Script path: current script

![](/res/readme_res/5.png)

![](/res/readme_res/6.png)

Запустить appium server (настройки без изменений)

![](/res/readme_res/7.png)

![](/res/readme_res/8.png)

На устройстве войти в режим разработчика, разрешить отладку по USB.
Проверить командой: adb devices

В директории tests открыть запуск, запустить файл или метод.
Pytest определяет только те методы, которые начинаются с test_ и находятся в директории (включая вложенные) tests.

![](/res/readme_res/9.png)

Чтобы посмотреть отчет
allure serve 








### **Документация**

https://appium.io/docs/en/about-appium/getting-started/?lang=ru

https://appium.github.io/python-client-sphinx/

https://github.com/appium/appium-uiautomator2-driver#capabilities





### **FAQ**

Для инспектора:

Remote host 127.0.0.1
Remote port 4723
Remote path /wd/hub


Desired Capabilities
{
  "platformName": "android",
  "appium:automationName": "uiautomator2",
  "appium:deviceName": "PT_5F",
  "appium:udid": "00168910000010"
}

Desired Capabilities с установкой приложения пример
{
  "platformName": "android",
  "appium:automationName": "uiautomator2",
  "appium:deviceName": "PT_5F",
  "appium:udid": "00168910000010",
  "appium:app": "C:\\Users\\user\\Sigma_v2.81.0.1-sigma-debug.apk",
  "appium:appPackage": "ru.sigma.app.debug",
  "appium:appWaitActivity": "ru.qasl.core.splash.SplashActivity"
}

![](/res/readme_res/10.png)

deviceName
adb shell "getprop | grep -w -e 'ro.photo.model.name'"

![](/res/readme_res/11.png)

UDID 
adb devices -l

![](/res/readme_res/12.png)

appPackage
aapt dump badging C:\Projects\atol-os\apk\sigma-debug.apk | findstr "package" | findstr "name"

![](/res/readme_res/13.png)

appWaitActivity
aapt dump badging C:\Projects\atol-os\apk\sigma-debug.apk | findstr "launchable-activity"

![](/res/readme_res/14.png)


Наименование текущего активити 
adb shell "dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'"

![](/res/readme_res/15.png)




Если ошибка JAVA_HOME
https://www.codejava.net/java-core/how-to-set-java-home-environment-variable-on-windows-10

Видеоинструкция 
https://www.youtube.com/watch?v=SMBBE8NJ7qA&list=PLWIBmxdTr81dDEZRiNxoy55dIDWtMyOoc&index=3


Для Такскома нужно также добавлять ФН отдельно к ККТ

hints
pytest --ignore=tests/sigma_app/test_RNDAGB_T118_activation_sigma_app.py tests/sigma_app --setup-show -v -svl --tb=short -s




https://nodejs.org/en/download