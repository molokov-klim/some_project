# ТЕСТ APPIUM
import os
import time
import unittest
import logging

from core.adb import adb

from core.appium.AppiumExtended.appium_extended import AppiumExtended
from core.appium.AppiumWebElementExtended.web_element_extended import WebElementExtended
from core.decorators.decorators import time_it

# logging.basicConfig(level=logging.DEBUG)

app = AppiumExtended()
caps = {
    "platformName": "android",
    "appium:automationName": "uiautomator2",
    "appium:deviceName": adb.get_device_model(),
    "appium:udid": adb.get_device_uuid(),
    "appium:noReset": True,
    "appium: autoGrantPermissions": True,
    "appium: newCommandTimeout": 600000,
}
app.connect(caps)
# logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])

# ELEMENT

locator_back = ("id", "ru.sigma.app.debug:id/backButton")

by = "xpath"
value = "//android.widget.TextView[contains(@text, 'Агенты')]"

locator_recycler = {"class": "androidx.recyclerview.widget.RecyclerView"}
locator_recycler_tuple = ('xpath',)

locator_tuple = ("xpath", "//android.widget.TextView[contains(@text, 'Агенты')]")
locator_dict = {"text": "Агенты", "enabled": "true"}

locator_tuple_elems = ("xpath", "//android.widget.TextView[contains(@scrollable, 'true')]")
locator_dict_elems = {'text': 'Агенты.', 'displayed': 'true'}

screenshot = os.path.join('', 'screenshot.png')

part_image = os.path.join('unit_test', 'part_image.png')
part_image_elements = os.path.join('unit_test', 'part_image_elements.png')
bottom_blue_button = os.path.join('unit_test', 'bottom_blue_button.png')

# ELEMENTS

locators_tuple = ("xpath", "//android.widget.TextView[contains(@text, 'Агенты')]")
locators_dict = {"text": "Агенты.",
                 "displayed": "true"}

print("===START UNIT TEST===")


class WebElementExtendedUTGet(unittest.TestCase):
    @time_it
    def test_get_element(self):
        logging.info("test_get_element()")
        element1 = app.get_element(locator=locator_recycler)
        inner_element = element1.get_element(locator=locator_tuple)
        self.assertIsInstance(inner_element, WebElementExtended)
        inner_element.click()
        app.get_element(locator_back).click()

        element2 = app.get_element(locator=locator_recycler)
        inner_element = element2.get_element(locator=locator_tuple)
        inner_element = element2.get_element(locator=inner_element)
        self.assertIsInstance(inner_element, WebElementExtended)
        inner_element.click()
        app.get_element(locator_back).click()

        element3 = app.get_element(locator=locator_recycler)
        inner_element = element3.get_element(locator={"text": "Агенты. Поверенный"})
        self.assertIsInstance(inner_element, WebElementExtended)
        inner_element.click()
        app.get_element(locator_back).click()

        element4 = app.get_element(locator=locator_recycler)
        inner_element = element4.get_element(by=by, value=value)
        self.assertIsInstance(inner_element, WebElementExtended)
        inner_element.click()
        app.get_element(locator_back).click()

        element5 = app.get_element(locator=locator_recycler)
        inner_element = element5.get_element(locator=part_image)
        self.assertIsInstance(inner_element, WebElementExtended)
        inner_element.click()
        app.get_element(locator_back).click()

    @time_it
    def test_get_attributes(self):
        logging.info("test_get_attributes()")
        result = {'text': 'Агенты. Банковский платежный агент'}
        self.assertEqual(app.get_element(locator=locator_tuple).get_attributes(['text']), result)

        result = {'text': 'Агенты. Банковский платежный агент', 'displayed': 'true'}
        self.assertEqual(app.get_element(locator=locator_tuple).get_attributes(['text', 'displayed']), result)

        result = {'index': '0', 'package': 'ru.sigma.app.debug', 'class': 'android.widget.TextView',
                  'text': 'Агенты. Банковский платежный агент', 'resource-id': 'ru.sigma.app.debug:id/categoryTitle',
                  'checkable': 'false', 'checked': 'false', 'clickable': 'false', 'enabled': 'true',
                  'focusable': 'false', 'focused': 'false', 'long-clickable': 'false', 'password': 'false',
                  'scrollable': 'false', 'selected': 'false', 'bounds': '[62,220][533,313]', 'displayed': 'true'}
        self.assertEqual(app.get_element(locator=locator_tuple).get_attributes(), result)


class WebElementExtendedUTDOM(unittest.TestCase):
    @time_it
    def test_get_parent(self):
        self.assertIsInstance(app.get_element(
            locator={'text': 'Агенты. Платежный агент'}).get_parent(), WebElementExtended)

    @time_it
    def test_get_parents(self):
        elements = app.get_element(
            locator={'text': 'Агенты. Платежный агент'}).get_parents()
        self.assertIsInstance(elements[0], WebElementExtended)
        self.assertEqual(len(elements), 15)

    @time_it
    def test_get_sibling(self):
        element = app.get_element(
            locator={'index': "4", 'package': "ru.sigma.app.debug", 'class': "android.widget.FrameLayout", 'text': "",
                     'resource-id': "ru.sigma.app.debug:id/frontCard", 'checkable': "false", 'checked': "false",
                     'clickable': "true", 'enabled': "true", 'focusable': "false", 'focused': "false",
                     'long-clickable': "false", 'password': "false", 'scrollable': "false",
                     'selected': "false"}).get_sibling(
            attributes={'displayed': "true", 'clickable': "true", 'enabled': "true"})
        self.assertIsInstance(element, WebElementExtended)

    @time_it
    def test_get_siblings(self):
        elements = app.get_element(
            locator={'index': "4", 'package': "ru.sigma.app.debug", 'class': "android.widget.FrameLayout", 'text': "",
                     'resource-id': "ru.sigma.app.debug:id/frontCard", 'checkable': "false", 'checked': "false",
                     'clickable': "true", 'enabled': "true", 'focusable': "false", 'focused': "false",
                     'long-clickable': "false", 'password': "false", 'scrollable': "false",
                     'selected': "false"}).get_siblings()
        self.assertIsInstance(elements[0], WebElementExtended)
        self.assertEqual(len(elements), 6)

    @time_it
    def test_get_cousin(self):
        cousin = app.get_element(locator={'text': 'Агенты. Платежный агент'}).get_cousin(
            ancestor={'class': "androidx.recyclerview.widget.RecyclerView"},
            cousin={'class': "android.widget.TextView"})
        self.assertIsInstance(cousin, WebElementExtended)
        self.assertEqual(cousin.text, 'Агенты. Банковский платежный агент')

    @time_it
    def test_get_cousins(self):
        cousins = app.get_element(locator={'text': 'Агенты. Платежный агент'}).get_cousins(
            ancestor={'class': "androidx.recyclerview.widget.RecyclerView"},
            cousin={'class': "android.widget.TextView", 'text': 'Агенты.'}, contains=True)
        self.assertIsInstance(cousins[0], WebElementExtended)
        self.assertEqual(cousins[0].text, 'Агенты. Банковский платежный агент')
        self.assertEqual(len(cousins), 7)

    @time_it
    def test_is_contains(self):
        parent = app.get_element(locator={'text': 'Агенты. Платежный агент'}).get_parent()
        self.assertEqual(parent.is_contains(locator={'text': 'Агенты. Платежный агент'}), True)


class WebElementExtendedUTElements(unittest.TestCase):
    @time_it
    def test_get_elements(self):
        logging.info("test_get_elements()")
        recycler_element = app.get_element(locator=locator_recycler)

        tuple_elements = recycler_element.get_elements(locator=locators_tuple)
        self.assertIsInstance(tuple_elements[0], WebElementExtended)
        self.assertEqual(len(tuple_elements), 7)

        list_elements = recycler_element.get_elements(locator=tuple_elements)
        self.assertIsInstance(list_elements[0], WebElementExtended)
        self.assertEqual(len(list_elements), 7)

        dict_elements = recycler_element.get_elements(locator=locators_dict)
        self.assertIsInstance(dict_elements[0], WebElementExtended)
        self.assertEqual(len(dict_elements), 7)

        str_elements = recycler_element.get_elements(locator=part_image_elements)
        self.assertIsInstance(str_elements[0], WebElementExtended)
        self.assertEqual(len(str_elements), 7)

        by_value_elements = recycler_element.get_elements(by=by, value=value)
        self.assertIsInstance(by_value_elements[0], WebElementExtended)
        self.assertEqual(len(by_value_elements), 7)

        tuple_range_elements = recycler_element.get_elements(locator=locators_tuple,
                                                             elements_range=locators_tuple)
        self.assertIsInstance(tuple_range_elements[0], WebElementExtended)
        self.assertEqual(len(tuple_range_elements), 7)

        list_range_elements = recycler_element.get_elements(locator=dict_elements, elements_range=list_elements)
        self.assertIsInstance(list_range_elements[0], WebElementExtended)
        self.assertEqual(len(list_range_elements), 7)

        dict_range_elements = recycler_element.get_elements(locator=locators_tuple,
                                                            elements_range=dict_elements)
        self.assertIsInstance(dict_range_elements[0], WebElementExtended)
        self.assertEqual(len(dict_range_elements), 7)

        contains_elements = recycler_element.get_elements(locator={'text': 'Агенты. Другой тип агента'},
                                                          elements_range=dict_elements,
                                                          contains=False)
        print("Ошибка \"не удалось дождаться изменения окна\" - все ок, так и задумано")
        self.assertIsInstance(contains_elements[0], WebElementExtended)
        self.assertEqual(len(contains_elements), 1)


class WebElementExtendedUTClick(unittest.TestCase):
    @time_it
    def test_click(self):
        self.assertEqual(app.get_element(locator=locator_tuple).click(), True)
        app.get_element(locator_back).click()
        self.assertEqual(app.get_element(locator=locator_tuple).click(duration=3), True)
        app.get_element(locator_back).click()
        self.assertEqual(app.get_element(locator=locator_tuple).click(duration=3, wait=True), True)
        app.get_element(locator_back).click()

    @time_it
    def test_double_click(self):
        app.get_element(locator=locator_tuple).click()
        self.assertEqual(app.get_element(locator={'text': 'Банковский платежный агент'}).double_click(), True)
        app.get_element(locator_back).click()
        self.assertEqual(app.get_element(locator=locator_tuple).double_click(wait=True), True)
        app.get_element(locator_back).click()
        app.get_element(locator=locator_tuple).click()
        self.assertEqual(app.get_element(locator={'text': 'Банковский платежный агент'}).double_click(wait=True), False)
        app.get_element(locator_back).click()

    @time_it
    def test_click_and_move(self):
        self.assertEqual(app.get_element(locator={'text': 'Поверенный'}).click_and_move(locator={'text': 'Товары'}),
                         True)
        self.assertEqual(app.get_element(locator=({'text': 'Агенты'})).click_and_move(
            locator=bottom_blue_button),
            True)
        self.assertEqual(
            app.get_element(locator={'text': 'Поверенный'}).click_and_move(locator=app.get_element({'text': 'Товары'})),
            True)
        self.assertEqual(app.get_element(locator=({'text': 'Поверенный'})).click_and_move(
            locator=bottom_blue_button),
            True)
        self.assertEqual(
            app.get_element(locator={'text': 'Поверенный'}).click_and_move(locator=app.get_element({'text': 'Товары'})),
            True)
        self.assertEqual(app.get_element(locator=({'text': 'Агенты. Банковский платежный агент'})).click_and_move(
            x=360, y=1184), True)
        self.assertEqual(app.get_element(locator=({'text': 'Поверенный'})).click_and_move(
            direction=0, distance=10000), True)
        self.assertEqual(app.get_element(locator=({'text': 'Расходники'})).click_and_move(
            direction=180, distance=10000), True)

        # self.assertEqual(app.get_element(locator=({'text': 'Комиссионер'})).click_and_move(
        #     direction=1, distance=3000), True)
        # self.assertEqual(app.get_element(locator=({'text': 'Комиссионер'})).click_and_move(
        #     direction=180, distance=30), True)
        # self.assertEqual(app.get_element(locator=({'text': 'Комиссионер'})).click_and_move(
        #     direction=180, distance=300), True)
        # self.assertEqual(app.get_element(locator=({'text': 'Комиссионер'})).click_and_move(
        #     direction=180, distance=3000), True)


class WebElementExtendedUTap(unittest.TestCase):
    @time_it
    def test_tap(self):
        self.assertEqual(app.get_element(locator={'text': 'Банковский платежный'}).tap(wait=False),
                         True)
        app.get_element(locator=locator_back).tap()

    @time_it
    def test_tap_and_wait(self):
        self.assertEqual(app.get_element(locator={'text': 'Банковский платежный'}).tap(wait=True),
                         True)
        app.get_element(locator=locator_back).tap()

    @time_it
    def test_double_tap_1(self):
        self.assertEqual(app.get_element(locator={'text': 'Банковский платежный'}).double_tap(wait=False, pause=0.1),
                         True)
        app.get_element(locator=locator_back).tap()

    @time_it
    def test_double_tap_4(self):
        self.assertEqual(app.get_element(locator={'text': 'Банковский платежный'}).double_tap(wait=False, pause=0.4),
                         True)
        app.get_element(locator=locator_back).tap()

    @time_it
    def test_double_tap_and_wait(self):
        self.assertEqual(app.get_element(locator={'text': 'Банковский платежный'}).double_tap(wait=True),
                         True)
        app.get_element(locator=locator_back).tap()

    @time_it
    def test_tap_and_move(self):
        self.assertEqual(app.get_element(locator={'text': 'Поверенный'}).tap_and_move(locator={'text': 'Товары'}),
                         True)
        self.assertEqual(app.get_element(locator=({'text': 'ПСН'})).tap_and_move(
            locator=bottom_blue_button),
            True)
        self.assertEqual(
            app.get_element(locator={'text': 'Поверенный'}).tap_and_move(locator=app.get_element({'text': 'Товары'})),
            True)
        self.assertEqual(app.get_element(locator=({'text': 'ПСН'})).tap_and_move(
            locator=bottom_blue_button),
            True)
        self.assertEqual(
            app.get_element(locator={'text': 'Поверенный'}).tap_and_move(locator=app.get_element({'text': 'Товары'})),
            True)
        self.assertEqual(app.get_element(locator=({'text': 'ПСН'})).tap_and_move(
            x=360, y=1184), True)
        self.assertEqual(app.get_element(locator=({'text': 'Поверенный'})).tap_and_move(
            direction=0, distance=10000), True)
        self.assertEqual(app.get_element(locator=({'text': 'Расходники'})).tap_and_move(
            direction=180, distance=10000), True)


class WebElementExtendedUTAdbActions(unittest.TestCase):
    @time_it
    def test_adb_tap(self):
        element = app.get_element(locator={'text': 'Комиссионер'})
        self.assertEqual(element.adb_tap(), True)
        app.get_element(locator=locator_back).click()

    @time_it
    def test_adb_multi_tap(self):
        element = app.get_element(locator={'text': 'Комиссионер'})
        self.assertEqual(element.adb_multi_tap(), True)
        app.get_element(locator=locator_back).click()
        time.sleep(3)

    @time_it
    def test_adb_swipe(self):
        element = app.get_element(locator={'text': 'Комиссионер'})
        self.assertEqual(element.adb_swipe(locator={'text': 'Подытог'}), True)
        self.assertEqual(element.adb_swipe(x=300, y=250), True)
        self.assertEqual(element.adb_swipe(direction=180, distance=50), True)


class WebElementExtendedUTScroll(unittest.TestCase):
    @time_it
    def test_scroll_down(self):
        element = app.get_element(locator=('id', 'ru.sigma.app.debug:id/menuRecyclerView'))
        self.assertEqual(element.scroll_down(), True)
        self.assertEqual(element.scroll_down(locator={'class': 'android.view.ViewGroup'}), True)
        self.assertEqual(element.scroll_down(locator={'class': 'android.view.ViewGroup'}, duration=30), True)

    @time_it
    def test_scroll_up(self):
        element = app.get_element(locator=('id', 'ru.sigma.app.debug:id/menuRecyclerView'))
        self.assertEqual(element.scroll_up(), True)
        self.assertEqual(element.scroll_up(locator={'class': 'android.view.ViewGroup'}),
                         True)
        self.assertEqual(element.scroll_up(locator={'class': 'android.view.ViewGroup'}, duration=30), True)

    @time_it
    def test_scroll_to_bottom(self):
        element = app.get_element(locator=('id', 'ru.sigma.app.debug:id/menuRecyclerView'))
        self.assertEqual(element.scroll_to_bottom(), True)
        self.assertEqual(element.scroll_to_bottom(locator={'class': 'android.view.ViewGroup'}), True)

    @time_it
    def test_scroll_to_top(self):
        element = app.get_element(locator=('id', 'ru.sigma.app.debug:id/menuRecyclerView'))
        self.assertEqual(element.scroll_to_top(), True)
        self.assertEqual(element.scroll_to_top(locator={'class': 'android.view.ViewGroup'}), True)

    @time_it
    def test_scroll_until_find(self):
        element = app.get_element(locator=('id', 'ru.sigma.app.debug:id/menuRecyclerView'))
        self.assertEqual(element.scroll_until_find(locator={'text': 'Характеристики'}), True)
        self.assertEqual(element.scroll_until_find(locator={'text': 'исси'}), True)

    @time_it
    def test_scroll_until_find_FALSE(self):
        element = app.get_element(locator=('id', 'ru.sigma.app.debug:id/menuRecyclerView'))
        self.assertEqual(element.scroll_until_find(locator={'text': 'фывлджофыарфджылоас'}), False)

    @time_it
    def test_scroll_until_find_FALSE(self):
        element = app.get_element(locator={'class': 'android.widget.TextView'})
        self.assertEqual(element.scroll_down(), False)


class AppiumExtendedUTGet(unittest.TestCase):

    @time_it
    def test_get_element(self):
        by_value_element = app.get_element(by=locator_tuple[0], value=locator_tuple[1])
        self.assertIsInstance(by_value_element, WebElementExtended)

        tuple_element = app.get_element(locator=locator_tuple)
        self.assertIsInstance(tuple_element, WebElementExtended)

        dict_element = app.get_element(locator=locator_dict)
        self.assertIsInstance(dict_element, WebElementExtended)

        str_element = app.get_element(locator=part_image)
        self.assertIsInstance(str_element, WebElementExtended)

        # with open(os.path.join('unit_test', 'str_element', 'element.png'), 'wb') as f:
        #     f.write(str_element.screenshot_as_png)

    @time_it
    def test_get_elements(self):
        tuple_elements = app.get_elements(locator=locators_tuple)
        self.assertIsInstance(tuple_elements[0], WebElementExtended)

        list_elements = app.get_elements(locator=tuple_elements)
        self.assertIsInstance(list_elements[0], WebElementExtended)

        dict_elements = app.get_elements(locator=locators_dict)
        self.assertIsInstance(dict_elements[0], WebElementExtended)

        str_elements = app.get_elements(locator=part_image_elements)  # , elements_range={'class':''})
        self.assertIsInstance(str_elements[0], WebElementExtended)

        by_value_elements = app.get_elements(by=by, value=value)
        self.assertIsInstance(by_value_elements[0], WebElementExtended)

        tuple_range_elements = app.get_elements(locator=locators_tuple,
                                                elements_range=locators_tuple)
        self.assertIsInstance(tuple_range_elements[0], WebElementExtended)

        list_range_elements = app.get_elements(locator=dict_elements, elements_range=list_elements)
        self.assertIsInstance(list_range_elements[0], WebElementExtended)

        dict_range_elements = app.get_elements(locator=locators_tuple,
                                               elements_range=dict_elements)
        self.assertIsInstance(dict_range_elements[0], WebElementExtended)


# RUN ALL
# unittest.main()

# RUN SUITES
suite = unittest.TestSuite()

# ADD CLASS
suite.addTest(unittest.makeSuite(WebElementExtendedUTGet))  # ok
suite.addTest(unittest.makeSuite(WebElementExtendedUTClick))  # ok
suite.addTest(unittest.makeSuite(WebElementExtendedUTDOM))  # ok
suite.addTest(unittest.makeSuite(WebElementExtendedUTElements))  # ok
suite.addTest(unittest.makeSuite(WebElementExtendedUTAdbActions))  # ok
suite.addTest(unittest.makeSuite(WebElementExtendedUTap))  # ok
suite.addTest(unittest.makeSuite(WebElementExtendedUTScroll))  # ok



# ADD METHODS
# suite.addTest(WebElementExtendedUTGet('test_get_element'))
# suite.addTest(WebElementExtendedUTGet('test_get_attributes'))
# suite.addTest(WebElementExtendedUTGet('test_get_elements'))

# suite.addTest(WebElementExtendedUTClick('test_double_click'))
# suite.addTest(WebElementExtendedUTClick('test_click_and_move'))

# suite.addTest(WebElementExtendedUTDOM('test_get_parents'))
# suite.addTest(WebElementExtendedUTDOM('test_get_sibling'))
# suite.addTest(WebElementExtendedUTDOM('test_get_siblings'))
# suite.addTest(WebElementExtendedUTDOM('test_get_cousin'))
# suite.addTest(WebElementExtendedUTDOM('test_get_cousins'))
# suite.addTest(WebElementExtendedUTDOM('test_is_contains'))

# suite.addTest(WebElementExtendedUTap('test_double_tap_1'))
# suite.addTest(WebElementExtendedUTap('test_double_tap_2'))
# suite.addTest(WebElementExtendedUTap('test_double_tap_3'))
# suite.addTest(WebElementExtendedUTap('test_double_tap_4'))
# suite.addTest(WebElementExtendedUTap('test_double_tap_and_wait'))
# suite.addTest(WebElementExtendedUTap('test_double_tap_and_move'))


# RUN
runner = unittest.TextTestRunner()
runner.run(suite)

# app.get_element(locator=locator_tuple).get_attributes('text')
