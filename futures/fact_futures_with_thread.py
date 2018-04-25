from threading import Thread
from concurrent.futures import Future


def fact(n):
    future = Future()

    def fact_iter(n, product):
        if n <= 1:
            future.set_result(product)
        else:
            Thread(target=fact_iter, args=(n - 1, n * product)).start()
    fact_iter(n, 1)

    return future.result()


if __name__ == "__main__":
    fact(10000)
