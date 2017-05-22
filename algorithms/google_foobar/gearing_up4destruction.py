""" LEVEL 2 
05,22 2017 https://www.google.com/foobar/?user=wrqatw


Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of 
configuring the LAMBCHOP doomsday device's axial orientation gears. It should 
be pretty simple - just add gears to create the appropriate rotation ratio. 
But the problem is, due to the layout of the LAMBCHOP and the complicated 
system of beams and pipes supporting it, the pegs that will support the 
gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of 
groups of pegs along various support beams. You need to place a gear on each 
peg (otherwise the gears will collide with unoccupied pegs). The engineers 
have plenty of gears in all different sizes stocked up, so you can choose 
gears of any size, from a radius of 1 on up. Your goal is to build a system 
where the last gear rotates at twice the rate (in revolutions per minute, 
or rpm) of the first gear, no matter the direction. Each gear (except the last) 
touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the 
location of each peg along the support beam, write a function answer(pegs) 
which, if there is a solution, returns a list of two positive integers a and b 
representing the numerator and denominator of the first gear's radius in its 
simplest form in order to achieve the goal above, such that radius = a/b. 
The ratio a/b should be greater than or equal to 1. Not all support 
configurations will necessarily be capable of creating the proper rotation 
ratio, so if the task is impossible, the function answer(pegs) should return 
the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could 
have a radius of 12, the second gear could have a radius of 14, and the last 
one a radius of 6. Thus, the last gear would rotate twice as fast as the first 
one. In this case, pegs would be [4, 30, 50] and answer(pegs) should return 
[12, 1].

The list pegs will be given sorted in ascending order and will contain 
at least 2 and no more than 20 distinct positive integers, all between 
1 and 10000 inclusive.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) pegs = [4, 30, 50]
Output:
    (int list) [12, 1]

Inputs:
    (int list) pegs = [4, 17, 50]
Output:
    (int list) [-1, -1]

"""


def answer(pegs):
    # no need to check ratios that are too large to fit on the first peg.
    maximum = pegs[1] - pegs[0] - 1
    for x in range(1, maximum):
        # calculate our gear sizes given the first size is x
        gear_sizes = [x]
        for peg in range(1, len(pegs)):
            gear_sizes.append(pegs[peg] - (pegs[peg - 1] + gear_sizes[-1]))

        # if any of the gear_sizes are zero or negative, this can't be a
        # potential because obviously we can't have a non-existent gear.
        # This isn't our answer, so skip this and try the next
        # one.
        if any(d <= 0 for d in gear_sizes):
            continue

        # see if we got an exact 2/1 match
        if x == 2 * gear_sizes[-1]:
            return [x, 1]

        # test if we have a ratio that works with 3 as the denominator
        if x + 1 == 2 * gear_sizes[-1]:
            return [(x * 3) + 1, 3]
        if x + 2 == 2 * gear_sizes[-1]:
            return [(x * 3) + 2, 3]

    return [-1, -1]


def my_answer(pegs):
    i = 0
    pegs_len = len(pegs)
    max_size = pegs[1] - pegs[0] - 1

    while i < max_size:
        i += 1
        gear_size_list = [i]
        for j in range(1, pegs_len):
            gear_size = pegs[j] - (pegs[j - 1] + gear_size_list[-1])
            gear_size_list.append(gear_size)

            # gear_size <= 0 which absolutely does not exist
            if gear_size <= 0:
                break

        last_gear_diameter = 2 * gear_size_list[-1]

        if last_gear_diameter <= 0:
            continue
        elif last_gear_diameter == i:
            return [i, 1]
        elif last_gear_diameter == i + 1:
            return [i * 3 + 1, 3]
        elif last_gear_diameter == i + 2:
            return [i * 3 + 2, 3]

    return [-1, -1]
