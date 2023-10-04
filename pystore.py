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

# Get user input for program selection or adding a custom program
selection = input("Enter the number of the program to install (0 to exit) or 'add' to add a custom program: ")

if selection == "0":
    print("Goodbye!")
elif selection == "add":
    # Allow the user to input their own program information
    custom_name = input("Enter the program name: ")
    custom_repo_url = input("Enter the GitHub repository URL: ")
    custom_run_command = input("Enter the command to run the program: ")
    
    # Add the custom program to the programs dictionary
    custom_program = {"name": custom_name, "repo_url": custom_repo_url, "run_command": custom_run_command}
    programs[len(programs) + 1] = custom_program
    
    # Clone the GitHub repository and run the program
    os.system(f"git clone {custom_repo_url} && cd {custom_name} && {custom_run_command}")
elif selection.isdigit() and int(selection) in programs:
    program = programs[int(selection)]
    repo_url = program["repo_url"]
    run_command = program["run_command"]
    
    # Clone the GitHub repository and run the program
    os.system(f"git clone {repo_url} && cd {program['name']} && {run_command}")
else:
    print("Invalid selection. Please choose a valid program number or 'add' to add a custom program.")
