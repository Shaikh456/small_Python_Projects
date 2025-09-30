import time   # Import the time module to use sleep() for countdown delay

def countdown_timer():
    """
    Countdown timer that accepts input in hours:minutes:seconds format.
    Example input: 0:1:30 (for 1 minute 30 seconds)
    """

    # Ask the user to enter the time in HH:MM:SS format
    user_input = input("Enter time in format (HH:MM:SS): ")

    try:
        # Split the input by ":" and convert each part (h, m, s) into integers
        # Example: "0:1:30" -> h=0, m=1, s=30
        h, m, s = map(int, user_input.split(":"))

        # Convert the total input time into seconds
        # 1 hour = 3600 seconds, 1 minute = 60 seconds
        total_seconds = h * 3600 + m * 60 + s

        # Loop until the countdown finishes
        while total_seconds > 0:
            # Convert remaining total seconds back into hours, minutes, and seconds
            hrs, remainder = divmod(total_seconds, 3600)  # Find hours and remainder
            mins, secs = divmod(remainder, 60)            # From remainder, find minutes and seconds

            # Print the current countdown in HH:MM:SS format
            # :02d means pad with zero if the number is less than 10 (e.g., 05 instead of 5)
            print(f"{hrs:02d}:{mins:02d}:{secs:02d}", end="\r")

            # Pause the program for 1 second to simulate real-time countdown
            time.sleep(1)

            # Reduce total seconds by 1
            total_seconds -= 1

        # Once the loop ends, display message
        print("⏰ Time's up!")

    except ValueError:
        # If the user entered something invalid (like not using HH:MM:SS format)
        print("⚠️ Invalid format! Please enter in HH:MM:SS (e.g., 0:05:30).")


# Run the countdown function only if this file is executed directly
if __name__ == "__main__":
    countdown_timer()
