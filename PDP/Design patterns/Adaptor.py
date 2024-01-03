# Legacy Logging Library (Adaptee)
class LegacyLogger:
    def log_message(self, message):
        print(f"Legacy Logger: {message}")

# New Logging Library (Target)


class NewLogger:
    def log(self, message):
        print(f"New Logger: {message}")

# Adapter for the New Logging Library


class NewLoggerAdapter(LegacyLogger):
    def __init__(self, new_logger):
        self.new_logger = new_logger

    def log_message(self, message):
        # Adapting the old interface to the new one
        self.new_logger.log(message)

# Client Code


def client_code(logger):
    logger.log_message("This is a log message")


# Usage
legacy_logger = LegacyLogger()
new_logger = NewLogger()

# Using the legacy logger directly
client_code(legacy_logger)

# Using the new logger through the adapter
adapter = NewLoggerAdapter(new_logger)
client_code(adapter)
