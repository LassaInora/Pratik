import datetime
import time

from pratik.functions import progress_bar


class TimeRemaining:
    def __init__(self, numbers):
        """ Calculate the average remaining time

        :param numbers: Number of objects
        :type numbers: int
        """
        self.iterations = 0
        self.numbers = numbers
        self._start = datetime.datetime.now()

    def add(self, number: int = 1):
        self.iterations += number

    def remove(self, number: int = 1):
        self.iterations -= number

    def progress_bar(self, *, width: int = 100):
        passed = datetime.datetime.now() - self._start
        restant = str(((passed * self.numbers) / self.iterations) - passed).split('.')[0]
        progress_bar(self.iterations, self.numbers, width=width)
        print(f" {restant}", end='')

if __name__ == '__main__':
    how_many_objects = 100

    tr = TimeRemaining(how_many_objects)
    for i in range(how_many_objects):
        time.sleep(0.1)
        tr.add()
        tr.progress_bar(width=25)
