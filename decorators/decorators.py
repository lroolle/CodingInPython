import signal, functools
import time


class TimeoutError(Exception):
    pass


def timeout(seconds, msg='Time out!'):
    def decorated(func):
        def _handel_timeout(signum, frame):
            raise TimeoutError(msg)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handel_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return functools.wraps(func)(wrapper)

    return decorated
