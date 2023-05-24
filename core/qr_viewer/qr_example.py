import os
import time

from core.qr_viewer.qr_viewer_client import QRViewerClient
QRViewerClient = QRViewerClient(url='https://qa-applications-qr-viewer-master.dev.vmw.ac.atol.tech/',
                                stand_id='PIT_smart')

QRViewerClient.open_session()

images = ['bottom_blue_button.png', 'element.png', 'is_img.png', 'part_image.png', 'part_image_elements.png', 'screen.png']

for i in range(5):
    for i in images:
        QRViewerClient.send_image(os.path.join('unit_test', i))
        print(i)
        time.sleep(5)



QRViewerClient.close_session()