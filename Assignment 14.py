
# Assignment No. 14
# Step 1: Import the logging module
# The logging module is used to record messages
# during program execution.
import logging

# Step 2: Configure logging
# Create a log file named app.log.
# DEBUG level records all logging messages.
# The format displays date, time, severity level, and message.

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# Step 3: Define a function to divide two numbers
def divide_numbers(a, b):

    # Record the starting of the division function
    logging.info("Division function started")

    # Display input values in the log file
    logging.debug("Values received: a=%s, b=%s", a, b)

    try:
        # Step 4: Perform division
        result = a / b

        # Step 5: Record successful division
        logging.info("Division successful")

        # Display the calculated result in the log
        logging.debug("Calculated result: %s", result)

        # Return the result
        return result

    except ZeroDivisionError:
        # Step 6: Handle division by zero error
        logging.exception("Cannot divide by zero")

        # Return None if division is unsuccessful
        return None

# Step 7: Record that the program has started
logging.info("Program started")

# Step 8: Call the function with valid values
print("Dividing 10 by 2:")
result1 = divide_numbers(10, 2)
print("Result:", result1)

# Step 9: Call the function with invalid values
print("\nDividing 10 by 0:")
result2 = divide_numbers(10, 0)
print("Result:", result2)

# Step 10: Record that the program has finished
logging.info("Program finished")

# Step 11: Display the final message
print("\nProgram execution completed!")
print("Check app.log for execution details.")
