__author__ = 'pinballwizard'

import time


def time_counter(fn):
    def wrapped():
        t1 = time.clock()
        t2 = time.time()
        r = fn()
        print("Процессорное время на выполнение функции %s => %s" % (fn.__name__, time.clock()-t1))
        print("Всего времени %s => %s" % (fn.__name__, time.time()-t2))
        return r
    return wrapped