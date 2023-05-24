import logging

from pycontactor_client import PyContactorClient
from pycontactor_client.models import Relay, Actions
import time

#alias switch_scanner

class PyContactorClientFX:
    def __init__(self, ip_address: str, alias: str):
        self.ip_address = ip_address
        self.PyContactor = PyContactorClient(ip_address=ip_address)
        self.relay_button_scan = Relay(alias=alias)

    def scan(self, timeout):
        logging.info(f"Сканирование с таймаутом[{timeout}]")
        self.PyContactor.set_relay(relay=self.relay_button_scan, action=Actions.close)
        time.sleep(timeout)
        self.PyContactor.set_relay(relay=self.relay_button_scan, action=Actions.open)
