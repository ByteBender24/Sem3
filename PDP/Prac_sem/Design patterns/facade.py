"""
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This pattern can be seen in the Python standard library.
"""


class CPU:

    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")


class Memory:

    def load(self, position, data):
        print(f"Loading from {position} data: '{data}'.")


class SolidStateDrive:

    def read(self, lba, size):
        print(f"Some data from sector {lba} with size {size}")


class ComputerFacade:

    def __init__(self):
        # self.name=name
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()
        self.ssd.read("0x1000", "100k")

# driver code


computer_facade = ComputerFacade()
computer_facade.start()


# -------------------------------------------------------------------------------------------------
print("\n\n")


"""
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This pattern can be seen in the Python standard library.
"""


class Online_appl:

    def submission(self):
        print("submit the application")


class Call_letter:

    def notification(self):
        print("Sent call letter for interview")


class Interview:

    def attend(self):
        print("Attend interview")


class Fee_Payment:

    def selected(self):
        print("Proceed for fee payment")


class AdmissionFacade:

    def __init__(self):
        # self.name=name
        self.online_appl = Online_appl()
        self.call_letter = Call_letter()
        self.interview = Interview()
        self.fee_Payment = Fee_Payment()

    def start(self):
        self.online_appl.submission()
        self.call_letter.notification()
        self.interview.attend()
        self.fee_Payment.selected()


# driver code

admission_facade = AdmissionFacade()
admission_facade.start()
