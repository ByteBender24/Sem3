# Define a family of algorithms

class Strategy:
    def do_operation(self, num1, num2):
        pass

# Implement concrete strategies


class AddStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 + num2


class SubtractStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 - num2


class MultiplyStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 * num2

# Context class that uses a strategy


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, num1, num2):
        return self.strategy.do_operation(num1, num2)

# Example usage


num1 = 10
num2 = 5

# Use addition strategy
add_strategy = AddStrategy()
context = Context(add_strategy)
result = context.execute_strategy(num1, num2)
print(f"Addition: {result}")

# Use subtraction strategy
subtract_strategy = SubtractStrategy()
context = Context(subtract_strategy)
result = context.execute_strategy(num1, num2)
print(f"Subtraction: {result}")

# Use multiplication strategy
multiply_strategy = MultiplyStrategy()
context = Context(multiply_strategy)
result = context.execute_strategy(num1, num2)
print(f"Multiplication: {result}")

# -------------------------------------------------------------------------------------------------
print("\n\n")


# Define a family of algorithms

class Amazon:
    def sales_operation(self, year):
        pass

# Implement concrete strategies


class Diwali_Sales(Amazon):
    def sales_operation(self, year):
        return f"Diwali sales of 50% in {year}"


class Thanksgiving_Sales(Amazon):
    def sales_operation(self, year):
        return f"TG sales of 10% in {year}"

# Context class that uses a strategy


class Sales:
    def __init__(self, sales):
        self.sales = sales

    def execute_sales(self, year):
        return self.sales.sales_operation(year)

# Example usage


year = 2023

# Use Diwali strategy
diwali_sales = Diwali_Sales()
sales = Sales(diwali_sales)
result = sales.execute_sales(year)
print(f"Sales: {result}")

# Use Thanksgiving strategy
tg_sales = Thanksgiving_Sales()
sales = Sales(tg_sales)
result = sales.execute_sales(year)
print(f"Sales: {result}")
