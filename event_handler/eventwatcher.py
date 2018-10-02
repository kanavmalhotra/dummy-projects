from queue import Queue
from event_handler import exceptions


class EventWatcher:
    def __init__(self):
        self._event_dict = dict()

    def register(self, action, func):
        if isinstance(str, action):
            raise ValueError("Incorrect value for the action is specified.")

        if isinstance(str, func):
            raise ValueError("Incorrect value for the function is specified.")

        if action in self._event_dict.keys():
            raise exceptions.EventActionAlreadyExists()

        self._event_dict[action] = func

    def modify(self, action, value):
        if isinstance(str, action):
            raise ValueError("Incorrect value for the action is specified.")

        if isinstance(str, value):
            raise ValueError("Incorrect value for the function is specified.")

        if action not in self._event_dict.keys():
            raise exceptions.EventActionAlreadyExists()

        self._event_dict[action] = value


class EventHandler(EventWatcher):
    def __init__(self):
        self._event_list = Queue()
        super(EventWatcher).__init__()
        self.event = Event

    def run(self):
        pass

    def async_run(self, loop=None):
        pass

    def run_concurrently(self, workers=2):
        pass


class Event:
    def __init__(self):
        pass

    def start(cls):
        print("Started")

    @classmethod
    def stop(cls):
        print("Stopped")

    @classmethod
    def pause(cls):
        print("Paused")