import os

# Set up an alias for Python 3
os.system("alias python=python3")
os.system("echo 'alias python=python3' >> ~/.bash_profile")
os.system("echo 'alias python=python3' >> ~/.zshrc")

print("Welcome to PyStore")

# Define the available programs and their download and run commands
programs = {
    1: {"name": "pycodeapp", "repo_url": "https://github.com/zayoon013/pycodeapp.git", "run_command": "python your_editor_script.py"},
    2: {"name": "another_program", "repo_url": "https://github.com/your_username/another_program.git", "run_command": "python main.py"},
    # Add more programs here
}

# Display the list of available programs
print("List of programs available to download and install:")
for key, program in programs.items():
    print(f"{key}. {program['name']}")

# Get user input for program selection
selection = int(input("Enter the number of the program to install (0 to exit): "))

if selection == 0:
    print("Goodbye!")
elif selection in programs:
    program = programs[selection]
    repo_url = program["repo_url"]
    run_command = program["run_command"]
    
    # Clone the GitHub repository and run the program
    os.system(f"git clone {repo_url} && cd {program['name']} && {run_command}")
else:
    print("Invalid selection. Please choose a valid program number.")
