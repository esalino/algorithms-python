# https://www.hackerrank.com/challenges/min_startimum-time-required/problem
import math

# The goal happens on a timeline which we can think of
# as a simple sorted array of days and we can search for the
# goal using binary search.


def min_time(machines, goal):
    # Get the min and max producing time of the machines
    min_start = machines[0]
    max_start = min_start
    for machine in machines:
        if machine < min_start:
            min_start = machine
        elif machine > max_start:
            max_start = machine

    # Get the starting left and right using the min and max producing times.
    left = math.ceil(goal / len(machines) * min_start)
    right = math.ceil(goal / len(machines) * max_start)
    found = search(machines, goal, left, right)

    # Because this is not an exaxt match we can be past the goal
    # so check found - 1 to see if that reaches the goal
    while found > 0:
        count = 0
        for machine in machines:
            count += math.floor((found - 1) / machine)

        if count != goal:
            break

        found -= 1

    return found


def search(machines, goal, left, right):
    if right < left:
        return -1

    mid = math.floor((right - left) / 2) + left
    count_of_produced = 0
    left_count = 0
    right_count = 0
    # calc the number produced at mid, left of mid and right of mid
    for machine in machines:
        count_of_produced += math.floor(mid / machine)
        left_count += math.floor((mid - 1) / machine)
        right_count += math.floor((mid + 1) / machine)

    # We have reached our goal without going past it
    if count_of_produced == goal or (left_count < goal < count_of_produced):
        return mid

    # Since we are not looking for an exact match check if first
    # count to right has made the goal.
    if count_of_produced < goal < right_count:
        return mid + 1

    # We have not found the goal so recurse next mid.
    if count_of_produced > goal:
        return search(machines, goal, left, mid - 1)
    else:
        return search(machines, goal, mid + 1, right)
