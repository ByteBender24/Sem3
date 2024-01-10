
# --------------------------------------------------------basic report generation----------------------------------
from datetime import datetime, timedelta
import datetime
from random import randint

# Function to generate a random list of data (for demonstration purposes)


def generate_data():
    return [randint(1, 100) for _ in range(10)]

# Function to generate a report for a given period


def generate_report(start_date, end_date, data):
    report = {
        'start_date': start_date,
        'end_date': end_date,
        'data': data,
        'average': sum(data) / len(data),
    }
    return report

# Function to generate daily reports


def generate_daily_reports(data_per_day):
    today = datetime.date.today()
    print(type(today))
    for i in range(data_per_day):
        current_date = today - datetime.timedelta(days=i)
        end_date = current_date + datetime.timedelta(days=1)
        print(current_date, end_date)
        data = generate_data()
        report = generate_report(current_date, end_date, data)

        print(f"Daily Report ({current_date}):")
        print(report)
        print()

# Function to generate weekly reports


def generate_weekly_reports(data_per_day):
    today = datetime.date.today()

    for i in range(7):
        current_date = today - datetime.timedelta(days=i)
        end_date = current_date + datetime.timedelta(days=7)
        data = generate_data()
        report = generate_report(current_date, end_date, data)

        print(f"Weekly Report ({current_date} to {end_date}):")
        print(report)
        print()

# Function to generate monthly reports


def generate_monthly_reports(data_per_day):
    today = datetime.date.today()
    current_month_start = datetime.date(today.year, today.month, 1)

    for i in range(30):  # Assuming a month has around 30 days
        current_date = current_month_start - datetime.timedelta(days=i)
        end_date = current_date + datetime.timedelta(days=30)
        data = generate_data()
        report = generate_report(current_date, end_date, data)

        print(f"Monthly Report ({current_date} to {end_date}):")
        print(report)
        print()


# Example Usage
data_per_day = 10
generate_weekly_reports(data_per_day)

# Uncomment the line below to generate weekly reports
# generate_weekly_reports(data_per_day)

# Uncomment the line below to generate monthly reports
# generate_monthly_reports(data_per_day)


# Function to generate a random list of data (for demonstration purposes)

def generate_data():
    return [randint(1, 100) for _ in range(10)]

# Function to generate a report for a given date range


def generate_report(start_date, end_date, data):
    report = {
        'start_date': start_date,
        'end_date': end_date,
        'data': data,
        'average': sum(data) / len(data),
    }
    return report

# Function to generate weekly reports


def generate_weekly_reports(data_per_week, weeks):
    today = datetime.now().date()

    for week in range(weeks):
        start_date = today - timedelta(days=week * 7)
        end_date = start_date + timedelta(days=6)
        data = generate_data()
        report = generate_report(start_date, end_date, data)

        print(f"Weekly Report ({start_date} to {end_date}):")
        print(report)
        print()


# Example Usage
data_per_week = 10
weeks_to_generate = 3
generate_weekly_reports(data_per_week, weeks_to_generate)
