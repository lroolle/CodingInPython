""" LEVEL 2-2
05,22 2017 https://www.google.com/foobar/?user=wrqatw

Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT
of power. Huge space stations with doomsday devices take even more power. To
help meet the station's power needs, Commander Lambda has installed solar
panels on the station's outer surface. But the station sits in the middle of
a quasar quantum flux field, which wreaks havoc on the solar panels. You and
your team of henchmen has been assigned to repair the solar panels, but you
can't take them all down at once without shutting down the space station
(and all those pesky life support systems!).

You need to figure out which sets of panels in any given array you can take
offline to repair while still maintaining the maximum amount of power output
per array, and to do THAT, you'll first need to figure out what the maximum
output of each array actually is. Write a function answer(xs) that takes a
list of integers representing the power output levels of each panel in an
array, and returns the maximum product of some non-empty subset of those
numbers.

So for example, if an array contained panels with power output
levels of [2, -3, 1, 0, -5], then the maximum product would be found by
taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product
2*(-3)*(-5) = 30.  So answer([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels,
and each panel will have a power output level whose absolute value is no
greater than 1000 (some panels are malfunctioning so badly that they're
draining energy, but you know a trick with the panels' wave stabilizer that
lets you combine two negative-output panels to produce the positive output
of the multiple of their power values). The final products may be very
large, so give the answer as a string representation of the number.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) xs = [2, 0, 2, 2, 0]
Output:
    (string) "8"

Inputs:
    (int list) xs = [-2, -3, 4, -5]
Output:
    (string) "60"

"""


def answer(xs):
    # your code here
    xs.sort(key=lambda x: abs(x), reverse=True)
    ret = xs[0]
    neg = ret if ret < 0 else 1
    out = ret
    for x in xs[1:]:
        if x < 0:
            neg = x
        ret *= x
        if abs(ret) > out:
            out = ret
    if out == 0:
        return '0'
    elif ret < 0:
        out /= neg
    return str(out)


def another_answer(xs):
    # your code here
    negatives = [x for x in xs if x < 0]
    positives = [x for x in xs if x > 0]
    if negatives and len(negatives) % 2 != 0:
        negatives = sorted(negatives)
        negatives.pop()
    ret = negatives + positives
    return str(reduce(lambda x, y: x * y, ret)) if ret else '0'

