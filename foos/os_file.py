import os

print(os.path.exists('.\\os_file.py'))
if not os.path.exists('.\\folder1\\'):
    os.mkdir('.\\folder1')
if not os.path.exists('.\\folder1\\folder2\\'):
    os.mkdir('.\\folder1\\folder2')
# .\\Images\\2ch\\2013-06-18-japan-neeter-than-ever
if not os.path.exists('.\\folder1\\2ch\\'):
    os.mkdir('.\\folder1\\2ch')

if not os.path.exists('.\\folder1\\2ch\\aa\\'):
    os.mkdir('.\\folder1\\2ch\\aa')

open('.\\folder1\\ostest', 'w')

if not os.path.exists('.\\folder1\\ostest2'):
    open('.\\folder1\\ostest2', 'w')


def list_dir(path):
    for d in os.listdir(path):
        dchild = os.path.join(path, d)
        if os.path.isdir(d):
            list_dir(d)

        return d
