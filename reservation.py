class Reservation:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.kobus.co.kr/")
        
        self.page.get_by_role("link", name="닫기").first.click()
        self.page.get_by_role("link", name="닫기").nth(3).click()
        self.page.get_by_role("link", name="닫기").first.click()
        self.page.get_by_role("link", name="닫기").first.click()
        self.page.get_by_role("link", name="닫기").click()

    def select_origin(self, origin):
        self.page.get_by_role("link", name="출발지 선택").click()

        self.page.locator("#imptDepr").get_by_role(
            "button",
            name=origin
        ).click()

        self.page.get_by_role("button", name="선택완료").click()

    def select_destination(self, destination):
        self.page.get_by_role("link", name="도착지 선택").click()
        self.page.get_by_role("button", name=destination).click()
        self.page.get_by_role("button", name="선택완료").click()

    def select_date(self, date):
        self.page.get_by_role("button", name="가는날 선택 달력").click()
        self.page.get_by_role("link", name="24", exact=True).click()    

    def search(self):
        self.page.get_by_role("button", name="조회하기").click()
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role("link", name="동의").click()
        #self.page.goto("https://www.kobus.co.kr/mrs/alcnSrch.do")

    def select_time(self, target_time):
        times = self.page.locator("span.start_time")
        times.first.wait_for()

        for i in range(times.count()):
            time_text = times.nth(i).inner_text().strip()
            
            try:
                time_num = int(time_text.replace(" ", "").replace(":",""))
            except (ValueError, TypeError):
                print(time_text + "정수로 변환할 수 없습니다.")
                continue

            if time_num == target_time:
                bus = times.nth(i).locator("..")

                remain = bus.locator("span.remain").inner_text().strip()

                print("시간:", time_text)
                print("좌석:", remain)

                if "매진" in remain:
                    print("매진입니다.")
                    return False

                bus.locator("span.btn_arrow").click()
                return True

        print("해당 시간을 찾지 못했습니다.")
        return False

    def search_time(self, start_time, end_time):
        times = self.page.locator("span.start_time")
        times.first.wait_for()

        results = []

        for i in range(times.count()):
            time_text = times.nth(i).inner_text().strip()

            try:
                time_num = int(time_text.replace(" ", "").replace(":",""))
            except (ValueError, TypeError):
                print(time_text + "정수로 변환할 수 없습니다.")
                continue

            if  time_num >= start_time and time_num < end_time:
                bus = times.nth(i).locator("..")

                remain = bus.locator("span.remain").inner_text().strip()

                print("시간:", time_text)
                print("좌석:", remain)

                if "매진" not in remain:
                    results.append({
                        "time": time_text,
                        "remain": remain
                    })
            
        return results
    
    def select_seat(self):
        pass