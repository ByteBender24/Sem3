'''
The Observer Pattern is a behavioral design pattern where an object, known as the subject, maintains a list of dependents, 
known as observers, that are notified of any state changes. This pattern is used to define a one-to-many 
dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
'''

from abc import ABC, abstractmethod

# Observer Interface


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Subject (Observable)


class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def state_changed(self, new_state):
        print(f"Subject's state changed to: {new_state}")
        self.notify_observers(f"State changed to {new_state}")

# Concrete Observer


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received update: {message}")


# Client Code
subject = Subject()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.add_observer(observer1)
subject.add_observer(observer2)

# Changing the state of the subject will notify observers
subject.state_changed("State 1")
subject.state_changed("State 2")

# Output:
# Subject's state changed to: State 1
# Observer 1 received update: State changed to State 1
# Observer 2 received update: State changed to State 1
# Subject's state changed to: State 2
# Observer 1 received update: State changed to State 2
# Observer 2 received update: State changed to State 2
