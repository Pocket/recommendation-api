import logging
import sys


def setup_logger():
    root = logging.getLogger()
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(
        logging.Formatter(
            '{ "time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": %(message)s }'
        )
    )
    root.setLevel(logging.DEBUG)
    root.addHandler(ch)


def convert_to_days(scale: str) -> str:
    """
    convert time window string from weeks to days
    :param scale: input time window string in days or weeks
    :return: time window string in days
    """
    if _check_timescale(scale, 'w'):
        scale2 = '%dd' % (int(scale.partition('w')[0]) * 7)
    elif _check_timescale(scale, 'd'):
        scale2 = scale
    else:
        raise ('{} is not a valid time range'.format(scale))
    return scale2


def _check_timescale(qstr: str, splitter: str):
    return qstr.partition(splitter)[0].isdigit() and qstr.partition(splitter)[1] == splitter

