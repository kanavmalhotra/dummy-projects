from queue import Queue
from event_handler import exceptions


class EventWatcher:
    def __init__(self):
        self.event_dict = dict()

    def register(self, action, func):
        if not isinstance(action, str):
            raise ValueError("Incorrect value for the action is specified.")

        if not isinstance(func, str):
            raise ValueError("Incorrect value for the function is specified.")

        if action in self.event_dict.keys():
            raise exceptions.EventActionAlreadyExists()

        self.event_dict[action] = func

    def modify(self, action, value):
        if not isinstance(action, str):
            raise ValueError("Incorrect value for the action is specified.")

        if not isinstance(value, str):
            raise ValueError("Incorrect value for the function is specified.")

        if action not in self.event_dict.keys():
            raise exceptions.EventActionAlreadyExists()

        self.event_dict[action] = value


class EventHandler(EventWatcher):
    def __init__(self, event):
        super(EventHandler, self).__init__()
        self._event_list = Queue()
        self.event = event

    def trigger(self, event, data):
        self._event_list.put((event, data))

    def run(self):
        event, data = self._event_list.get()
        getattr(self.event, self.event_dict.get(event))(data)

    def async_run(self, loop=None):
        pass

    def run_concurrently(self, workers=2):
        pass


class Events:
    def __init__(self):
        pass

    def start(self, data):
        if data:
            print("Started - {}".format(data))
        else:
            print("Started")

    def stop(self):
        print("Stopped")

    def pause(self):
        print("Paused")


class MyEvent:
    def __init__(self, event, handler, *args):
        self._event = event
        self._handler = handler
        self.args = args or ()

        self._execute()

    def _execute(self):
        self._handler.trigger(self._event, self.args)
        self._handler.run()


if __name__ == "__main__":
    events = Events()

    event_handler = EventHandler(events)

    # Registering events in the Event Handler
    event_handler.register("START", "start")
    event_handler.register("PAUSE", "pause")
    event_handler.register("STOP", "stop")

    MyEvent("START", event_handler)
    MyEvent("START", event_handler, "Task1")

    MyEvent("START", event_handler, "Task3")

