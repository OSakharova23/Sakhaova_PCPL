from time import sleep, time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time()
        print(f"time: {end - self.start:.1f}")


@contextmanager
def cm_timer_2():
    start = time()
    yield
    end = time()
    print(f"time: {end - start:.1f}")

"""
with cm_timer_1():
    sleep(5.5)

with cm_timer_2():
    sleep(5.5)
"""