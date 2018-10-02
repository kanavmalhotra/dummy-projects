class EventWatcherException(Exception):
    pass


class EventActionAlreadyExists(EventWatcherException):
    msg = "Specified action already exist."


class EventActionDoesNotExist(EventWatcherException):
    msg = "Specified action does not exist to be modified."
