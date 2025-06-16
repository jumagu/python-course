import time

# The rich library is installed in the Poetry virtual environment
from rich.console import Console
from rich.text import Text

console = Console()

message = "Hi, future programmer!"

for letter in message:
    console.print(Text(letter, style="bold magenta"), end="")
    time.sleep(0.1)
