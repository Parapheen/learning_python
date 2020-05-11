import itertools as it
from queue import Queue
from threading import Thread
import time


class Publisher(Thread):
    """
    Meta class: Observable
    """
    def __init__(self):
        super().__init__()
        self._observers = []

    def notify(self, msg):
        for obs in self._observers:
            obs.put(msg)

    def subscribe(self, obs):
        if obs not in self._observers:
            self._observers.append(obs)
        else:
            print('observer is already subscribed')

    def unsubscribe(self, obs):
        try:
            self._observers.remove(obs)
        except ValueError:
            print('no such observer')


class Observer(Thread):
    def __init__(self):
        super().__init__()
        self.updates = Queue()


class Watcher(Publisher):
    def run(self):
        for i in it.count():
            self.notify(i)
            time.sleep(1)


class Worker(Publisher, Observer):
    def run(self):
        while True:
            task = self.updates.get()
            self.notify((str(task), 'start'))
            time.sleep(1)
            self.notify((str(task), 'stop'))


class Supervisor(Observer):
    def __init__(self):
        super().__init__()
        self._statuses = {}

    def run(self):
        while True:
            status = self.updates.get()
            print(status)
            self._statuses[status[0]] = status[1]
            # Do something based on status updates.
            if status[1] == 'stop':
                del self._statuses[status[0]]


watcher = Watcher()
worker = Worker()
supervisor = Supervisor()

watcher.subscribe(worker.updates)
worker.subscribe(supervisor.updates)

supervisor.start()
worker.start()
watcher.start()
