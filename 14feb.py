from colorama import init, Fore
import time
import random

# Initialize colorama
init()

# List of color options
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Print "I love you" 100 times with random colors
for _ in range(100):
    # Select a random color
    color = random.choice(colors)
    # Print "I love you" in the selected color
    print(color + "I love you so so so much mani")
    # Pause for a short time to display each "I love you" one by one
    time.sleep(0.1)

