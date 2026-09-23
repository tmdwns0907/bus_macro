from browser import create_browser
from reservation import Reservation
from notifier import Notifier
from datetime import datetime

import time
import config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_message(notifier, results):
    try:
        now = datetime.now().strftime("%H:%M:%S")
        message = f"🚌 좌석 발견!\n확인 시간: {now}\n"

        for result in results:
            message += f"{result['time']} - {result['remain']}\n"

        logger.info(message)
        notifier.send(message)
    except Exception as e:
        logger.error(f"메시지 전송 실패: {e}")

def main():
    notifier = Notifier("bus_alerts")

    playwright, browser, page = create_browser()

    reservation = Reservation(page)

    reservation.open()

    reservation.select_origin(config.ORIGIN)
    reservation.select_destination(config.DESTINATION)
    reservation.select_date(config.DATE)

    reservation.search()

    #reservation.select_time(config.TARGET_TIME)
    
    while(True):
        results = reservation.search_time(config.START_TIME, config.END_TIME)
        if results:
            send_message(notifier, results)
        time.sleep(2)  # 2초 대기
        reservation.refresh()

    #reservation.select_seat()

    """input("예매 과정을 확인한 후 Enter를 누르세요.")

    browser.close()
    playwright.stop()"""


if __name__ == "__main__":
    main()