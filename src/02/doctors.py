import threading
from random import randint
import time

class Screwdriver:
    def __init__(self):
        self.lock = threading.Lock()

    def acquire(self):
        self.lock.acquire()

    def release(self):
        self.lock.release()

class Doctor(threading.Thread):
    def __init__(self, number, left_screwdriver, right_screwdriver):
        super().__init__()
        self.number = number
        self.left_screwdriver = left_screwdriver
        self.right_screwdriver = right_screwdriver

    def run(self):
        self.think()
        self.blast()

    def think(self):
        wait_time = (randint(1, 5) / 10)
        time.sleep(wait_time)

    def blast(self):
        # take left screwdriver
        self.left_screwdriver.acquire()
        # take right screwdriver
        self.right_screwdriver.acquire()
        print(f"Doctor {self.number} BLAST!")
        # print("Doctor {} BLAST!".format(self.number))
        # put screwdrivers
        self.right_screwdriver.release()
        self.left_screwdriver.release()

def main():
    num_doctors = 5
    screwdrivers = [Screwdriver() for _ in range(num_doctors)]
    doctors = [Doctor(i+9, screwdrivers[i], screwdrivers[(i+1) % num_doctors]) for i in range(num_doctors)]

    for doctor in doctors:
        doctor.start()

    for doctor in doctors:
        doctor.join()

if __name__ == '__main__':
    main()
