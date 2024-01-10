import time
import threading


def print_numbers():
    for i in range(5):
        print(i)


# Create a thread
my_thread = threading.Thread(target=print_numbers)

# Start the thread
my_thread.start()

# Wait for the thread to finish
my_thread.join()


#--------------------------------------------------------------


shared_variable = 0
lock = threading.Lock()


def increment():
    global shared_variable
    with lock:
        shared_variable += 1


# Create threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("Result:", shared_variable)


#------------------------------------------------------------------------------------------------


class IncrementThread(threading.Thread):
    def __init__(self, lock, name):
        super().__init__()
        self.lock = lock
        self.name = name

    def run(self):
        for _ in range(5):
            with self.lock:
                print(f"{self.name}: Incrementing")
                time.sleep(0.1)


def main():
    # Create a lock
    lock = threading.Lock()

    # Create two instances of IncrementThread
    thread1 = IncrementThread(lock, "Thread 1")
    thread2 = IncrementThread(lock, "Thread 2")

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to finish
    thread1.join()
    thread2.join()

    print("Threads finished")


if __name__ == "__main__":
    main()
