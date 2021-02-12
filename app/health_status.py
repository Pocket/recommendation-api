from enum import Enum
import logging


class HealthStatus(Enum):
    UNKNOWN = 1
    HEALTHY = 2
    UNHEALTHY = 3


_health_status: HealthStatus = HealthStatus.UNKNOWN


def get_health_status():
    return _health_status


def set_health_status(status: HealthStatus):
    global _health_status
    logging.info(f"Changing health status from {_health_status.name} to {status.name}")
    _health_status = status
