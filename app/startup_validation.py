from enum import Enum


class AppStatus(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3


_APP_STATUS: AppStatus = AppStatus.PENDING


def get_app_status():
    return _APP_STATUS


def set_app_status(status: AppStatus):
    global _APP_STATUS
    _APP_STATUS = status
