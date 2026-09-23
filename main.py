from browser import create_browser
from reservation import Reservation
from notifier import Notifier

import config


def main():
    notifier = Notifier("bus_alerts")

    notifier.send("테스트 알림입니다.")

    """playwright, browser, page = create_browser()

    reservation = Reservation(page)

    reservation.open()

    reservation.select_origin(config.ORIGIN)
    reservation.select_destination(config.DESTINATION)
    reservation.select_date(config.DATE)

    reservation.search()

    #reservation.select_time(config.TARGET_TIME)
    results = reservation.search_time(config.START_TIME, config.END_TIME)
    #reservation.select_seat()

    if results:
        message = "🚌 좌석 발견!\n"

        for result in results:
            message += f"{result['time']} - {result['remain']}\n"

        notifier.send(message)"""

    """input("예매 과정을 확인한 후 Enter를 누르세요.")

    browser.close()
    playwright.stop()"""


if __name__ == "__main__":
    main()