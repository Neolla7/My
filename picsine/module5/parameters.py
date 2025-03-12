import sys

sys.argv.append("added_param1")

num_parameters = len(sys.argv) - 1

print(f"Number of parameters: {num_parameters}.")
