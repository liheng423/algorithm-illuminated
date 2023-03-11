# Graham's Algorithm

from typing import Callable, Set, List
from UtilsMath import argmin
from UtilsSorter import QuickSort
from UtilsHeap import MinHeap


class Job:
    cost: int = 0
    index: int


class Machine:
    load: List[Job] = []
    index: int
    sum_load: int = 0


def Graham(machine_list: Set[Machine], job_list: Set[Job]) -> Set[Machine]:
    # initialization
    for machine in machine_list:  # i is the machine index
        machine.load = []
        machine.sum_load = 0

    # MAIN LOOP
    for job in job_list:
        target_machine = argmin(machine_list, lambda x: x.sum_load)
        target_machine.load.append(job)
        target_machine.sum_load += job.cost

    return machine_list

# LPT


def LPT(machine_list: Set[Machine], job_list: Set[Job], Graham: Callable[[Set[Machine], Set[Job]], Set[Machine]]):
    joblist = list(job_list)
    joblist = QuickSort(joblist, lambda x: x.cost).array
    return Graham(machine_list, job_list)
