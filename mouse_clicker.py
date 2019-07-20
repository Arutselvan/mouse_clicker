import autopy
import time
import argparse
import sys

DEFAULT_SCRIPT_DURATION = 60 # Default duration for which the script runs (in minutes)
DEFAULT_CLICK_FREQUENCY = 30 # Default mouse click frequency (in seconds)

class MouseClicker:

    """
    The mouse clicker class
    """

    def __init__(self):
        pass
    
    def get_end_time(self, duration):

        """
        Method to calculate the stopping time of the script

        Args:
            duration (int): Duration for which the script should run

        Returns:
            int: The ending time at which the script should stop
        """

        return time.time() + 60*duration

    def click(self, frequency, duration):

        """
        Method to emulate mouse clicks

        Args:
            frequency (int): The frequency of mouse clicks
            duration (int): Duration for which the script should run
        """

        end_time = self.get_end_time(duration)
        current_time = time.time()
        while end_time > current_time:
            autopy.mouse.click()
            time.sleep(frequency)
    
    def __del__(self):
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--duration', type=int, help="Running duration of the script (in minutes)", default=DEFAULT_SCRIPT_DURATION)
    parser.add_argument('--frequency', type=int, help="Frequency of mouse clicks (in seconds)", default=DEFAULT_CLICK_FREQUENCY)
    args = parser.parse_args()
    clicker = MouseClicker()
    print("Running Mouse clicker...")
    clicker.click(args.frequency, args.duration)
    print("Killed Mouse clicker")

