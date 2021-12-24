# Python 3 program to print all
# possible strings of length k

import string
import pyautogui
import keyboard
import time
import sys

# The method that prints all
# possible strings of length k.
# It is mainly a wrapper over
# recursive function printAllKLengthRec()
def printAllKLength(set, k):
    n = len(set)
    printAllKLengthRec(set, "", n, k)


# The main recursive method
# to print all possible
# strings of length k
def printAllKLengthRec(set, prefix, n, k):
    # Base case: k is 0,
    # print prefix
    if (k == 0):
        print(prefix)
        word = "ASPA" + prefix

        pyautogui.moveTo(500, 510)
        pyautogui.click()

        pyautogui.doubleClick()

        pyautogui.press('backspace')

        pyautogui.typewrite(word)

        pyautogui.moveTo(1100, 500)
        pyautogui.click()

        time.sleep(0.5)
        pyautogui.moveTo(1100, 620)
        pyautogui.click()

        if keyboard.is_pressed("q"):
            sys.exit()

        return

    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):
        # Next character of input added
        newPrefix = prefix + set[i]

        # k is decreased, because
        # we have added a new character
        printAllKLengthRec(set, newPrefix, n, k - 1)


# Driver Code
if __name__ == "__main__":
    print("First Test")
    set1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    k = 6
    printAllKLength(set1, k)

# This code is contributed
