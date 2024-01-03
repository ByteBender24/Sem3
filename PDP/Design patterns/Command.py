'''
The Command Pattern is a behavioral design pattern that turns a request into a stand-alone object. 
It allows you to parameterize clients with queues, requests, and operations. 
It also enables the support of undoable operations.

Key components of the Command Pattern:

    Command: Declares an interface for executing a particular operation.
    ConcreteCommand: Implements the Command interface and binds with an action on a receiver.
    Invoker: Requests the command to carry out the request.
    Receiver: Knows how to perform the operation.
    Client: Creates a ConcreteCommand and sets its receiver.

'''

from abc import ABC, abstractmethod

# Command Interface


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Concrete Command


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

# Receiver


class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Invoker


class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

    def press_undo_button(self):
        self.command.undo()


# Client
light = Light()
light_on_command = LightOnCommand(light)

remote = RemoteControl()
remote.set_command(light_on_command)

# Press the button to turn the light on
remote.press_button()

# Press the undo button to turn the light off
remote.press_undo_button()


#----------------------------------------------------------------------------------------------------


# Command Interface

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Concrete Command - Turn On


class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()

    def undo(self):
        self.device.turn_off()

# Concrete Command - Turn Off


class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()

    def undo(self):
        self.device.turn_on()

# Receiver - Television


class Television:
    def turn_on(self):
        print("Television is ON")

    def turn_off(self):
        print("Television is OFF")

# Receiver - Stereo System


class StereoSystem:
    def turn_on(self):
        print("Stereo System is ON")

    def turn_off(self):
        print("Stereo System is OFF")

# Invoker


class RemoteControl:
    def __init__(self):
        self.commands = []

    def press_button(self, command):
        command.execute()
        self.commands.append(command)

    def press_undo_button(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()


# Client
television = Television()
stereo_system = StereoSystem()

turn_on_tv_command = TurnOnCommand(television)
turn_off_tv_command = TurnOffCommand(television)

turn_on_stereo_command = TurnOnCommand(stereo_system)
turn_off_stereo_command = TurnOffCommand(stereo_system)

remote_control = RemoteControl()

# Use the remote control to turn on the TV and the stereo
remote_control.press_button(turn_on_tv_command)
remote_control.press_button(turn_on_stereo_command)

# Undo the last command (turn off the stereo)
remote_control.press_undo_button()

# Check the status of the devices
print("Television status:")
turn_on_tv_command.execute()

print("\nStereo System status:")
turn_on_stereo_command.execute()

# ----------------------------------------------------------------------------------------------------


# Command Interface

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Concrete Command - Insert Text


class InsertTextCommand(Command):
    def __init__(self, document, text, position):
        self.document = document
        self.text = text
        self.position = position
        self.previous_state = None

    def execute(self):
        self.previous_state = self.document.get_state()
        self.document.insert_text(self.text, self.position)

    def undo(self):
        self.document.restore_state(self.previous_state)

# Concrete Command - Delete Text


class DeleteTextCommand(Command):
    def __init__(self, document, position, length):
        self.document = document
        self.position = position
        self.length = length
        self.previous_state = None

    def execute(self):
        self.previous_state = self.document.get_state()
        self.document.delete_text(self.position, self.length)

    def undo(self):
        self.document.restore_state(self.previous_state)

# Receiver - Document


class Document:
    def __init__(self):
        self.content = ""

    def insert_text(self, text, position):
        self.content = self.content[:position] + text + self.content[position:]

    def delete_text(self, position, length):
        self.content = self.content[:position] + \
            self.content[position + length:]

    def get_state(self):
        return self.content

    def restore_state(self, state):
        self.content = state

# Invoker


class TextEditor:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)

    def undo_last_command(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()


# Client
document = Document()
text_editor = TextEditor()

# Execute commands
insert_command = InsertTextCommand(document, "Hello, ", 0)
text_editor.execute_command(insert_command)

delete_command = DeleteTextCommand(document, 7, 5)
text_editor.execute_command(delete_command)

# Undo the last command
text_editor.undo_last_command()

# Check the document content
print(document.get_state())
