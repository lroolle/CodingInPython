import os
import time
import multiprocessing

def f(x):
    pid = os.getpid()
    print('Pid %d Countting x: %d' %(pid, x))
    st = time.time()
    ret = x ** x
    et = time.time()
    print('pid: %d' % pid, 'taking:', et - st)
    return ret

if __name__ == '__main__':
    process_num = multiprocessing.cpu_count()
    print('Process num: ', process_num)
    with multiprocessing.Pool(process_num) as p:
        p.map(f, [1111111, 1111111, 1111111, 1111111,  1111111, 111111, 5555, 6666, 7777, 88888])


