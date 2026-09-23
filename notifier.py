import requests

class Notifier:
    def __init__(self, topic):
        self.url = f"https://ntfy.sh/{topic}"

    def send(self, message):
        response = requests.post(
            self.url,
            data=message.encode("utf-8")
        )

        response.raise_for_status()