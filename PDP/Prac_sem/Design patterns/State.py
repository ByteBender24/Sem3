from abc import ABC, abstractmethod

# State interface


class State(ABC):
    @abstractmethod
    def publish_document(self):
        pass

# Concrete states


class DraftState(State):
    def publish_document(self):
        print("Document is in the Draft state. Publishing...")
        # Logic to publish the document
        print("Document published successfully.")
        return PublishedState()


class PublishedState(State):
    def publish_document(self):
        print("Document is already published. No further action needed.")
        return self

# Context class


class DocumentEditor:
    def __init__(self):
        self.state = DraftState()

    def get_state(self):
        return type(self.state).__name__

    def publish_document(self):
        self.state = self.state.publish_document()


# Example usage
document_editor = DocumentEditor()

# Publish document in the Draft state
document_editor.publish_document()
print("Current state:", document_editor.get_state())

# Try to publish document again
document_editor.publish_document()
print("Current state:", document_editor.get_state())


# -------------------------------------------------------------------------------------------------
print("\n\n")


# State interface

class TrafficSignalState(ABC):
    @abstractmethod
    def change_signal(self):
        pass

# Concrete states


class RedState(TrafficSignalState):
    def change_signal(self):
        print("Traffic signal is red. Changing to yellow.")
        return YellowState()


class YellowState(TrafficSignalState):
    def change_signal(self):
        print("Traffic signal is yellow. Changing to green.")
        return GreenState()


class GreenState(TrafficSignalState):
    def change_signal(self):
        print("Traffic signal is green. Changing to red.")
        return RedState()

# Context class


class TrafficSignalController:
    def __init__(self):
        self.state = RedState()

    def get_state(self):
        return type(self.state).__name__

    def change_signal(self):
        self.state = self.state.change_signal()


# Example usage
traffic_controller = TrafficSignalController()

# Change signal from red to yellow
traffic_controller.change_signal()
print("Current state:", traffic_controller.get_state())

# Change signal from yellow to green
traffic_controller.change_signal()
print("Current state:", traffic_controller.get_state())

# Change signal from green to red
traffic_controller.change_signal()
print("Current state:", traffic_controller.get_state())
