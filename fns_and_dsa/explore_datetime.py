# explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():
    # Get current datetime
    current_date = datetime.now()
    # Format it as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date():
    # Prompt user for number of days
    try:
        days_to_add = int(
            input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Calculate future date
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Format as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
