'''
how to run:
Open your command prompt or terminal.
Navigate to the directory where your Python script is located.
Run the script with a command line argument: python script.py <user_input>
example argument: python input_output_with_cmd.py "hello world"
'''

import sys

# Check if at least one argument is provided (the script name itself)
if len(sys.argv) < 2:
    print("Usage: python script.py <user_input>")
else:
    user_input = sys.argv[1]
    print("You entered:", user_input)

