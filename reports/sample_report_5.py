from porthole import BasicReport
from porthole.alerts import send_alert_on_exception


@send_alert_on_exception
def main():
    1 / 0
