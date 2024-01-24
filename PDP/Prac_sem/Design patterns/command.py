'''
Skeleton code:
Command pattern decouples the object invoking a job from the one who knows
how to do it.'''

from abc import ABC, abstractmethod


class Command(ABC):

	def __init__(self, receiver):
		self.receiver = receiver

	def process(self):
		pass


class CommandImplementation(Command):

	def __init__(self, receiver):
		self.receiver = receiver

	def process(self):
		self.receiver.perform_action()


class Receiver:

	def perform_action(self):
		print('Action performed in receiver.')


class Invoker:

	def command(self, cmd):
		self.cmd = cmd

	def execute(self):
		self.cmd.process()


receiver = Receiver()
cmd = CommandImplementation(receiver)
invoker = Invoker()
invoker.command(cmd)
invoker.execute()


# -------------------------------------------------------------------------------------------------
print("\n\n")

# treats individual objects and compositions of objects uniformly.

# Command Interface


class Command:
    def execute(self):
        pass

# Concrete Command


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Receiver


class Light:
    def turn_on(self):
        print("Light is ON")

# Invoker


class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


# Client Code
if __name__ == "__main__":
    # Creating objects
    light = Light()
    light_on = LightOnCommand(light)

    remote = RemoteControl()

    # Setting the command
    remote.set_command(light_on)

    # Pressing the button
    remote.press_button()
