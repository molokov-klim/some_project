import logging
import os
import time
from urllib.parse import urljoin
import urllib3
import urllib3.exceptions
import requests


class QRViewerClient:
    def __init__(self, url: str, stand_id: str):
        self.base_url = url
        self._session = requests.Session()
        self.stand_id = stand_id
        self.session_id = self.open_session()
        urllib3.disable_warnings()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def request(
            self,
            method,
            uri=None,
            params=None,
            json=None,
            files=None,
            data=None,
            headers=None,
            timeout=None,
            verify=False,
    ):
        """Обработка HTTP-запроса"""
        url = urljoin(self.base_url, uri)

        response = self._session.request(
            url=url,
            method=method,
            params=params,
            json=json,
            files=files,
            data=data,
            headers=headers,
            timeout=timeout,
            verify=verify,
        )

        return response

    def open_session(self):
        response = self.request(
            "POST",
            "api/session/start",
            json={"stand_id": self.stand_id},
            headers={"content-type": "application/json"}, )

        response.raise_for_status()
        response = response.json()

        if response["code"] == 100:
            logging.info(response["data"]["message"])

        self.stand_id = self.stand_id
        self.session_id = response["data"]["session_id"]
        return self.session_id

    def close_session(self):
        response = self.request(
            "POST",
            f"api/session/stop",
            json={
                "stand_id": self.stand_id,
                "session_id": self.session_id
            }
        )
        response.raise_for_status()
        response = response.json()
        assert response['code'] == 0
        return response

    def send_image(self, path_to_image):
        response = self.request(
            "POST",
            f"api/exchange/image",
            data={
                "session_id": self.session_id
            },
            files={
                'image': open(path_to_image, 'rb'),
            })
        response.raise_for_status()
        response = response.json()
        assert response['code'] == 0
        return response
