import threading
import random
from typing import List

from ListenedList import ListenedList
from gui import GUI
from algorithms import bubble_sort, insertion_sort, selectionSort, shellSort, bogoSort


if __name__ == "__main__":
    algos = [bubble_sort, insertion_sort, selectionSort, shellSort, bogoSort]
    while(True):
        print("Welcome to the algorithm visualiser!")
        print("Please choose an algorithm to use:")
        for index, item in enumerate(algos):
            print(index, item)
        userIndex = int(input("Please enter what algorithm to use:"))
        list = random.sample(range(0, 100), 100)
        print(list)
        g = GUI(list, algos[userIndex])
