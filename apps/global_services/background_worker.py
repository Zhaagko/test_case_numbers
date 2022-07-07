from threading import Thread


class Worker:

    def __init__(self):
        self._tasks = {}

    def add_task(self, name: str, func, args: tuple):
        self._tasks[name] = (func, args)

    def start(self):
        for task in self._tasks.keys():
            func, args = self._tasks[task]
            Thread(name=task, target=func, args=args).start()
