def write_file(file_name, file_content):
    """Creates or overwrites a .txt file and writes content to it."""
    file_path = f"{file_name}.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(file_content)  # Overwrite file content

def append_file(file_name, append_content):
    """Appends content to an existing .txt file without unnecessary newlines."""
    file_path = f"{file_name}.txt"
    
    with open(file_path, "a", encoding="utf-8") as file:
        if append_content.startswith("\n"):
            file.write(append_content)  
        else:
            file.write("\n" + append_content)  

def read_file(file_name):
    """Reads and returns the content of a .txt file."""
    file_path = f"{file_name}.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()  # Read the entire content
    except FileNotFoundError:
        return "File not found."

write_file("logfile", "Log 1: 5 bananas added")
append_file("logfile", "Log 2: 3 bananas subtracted")
print(read_file("logfile"))
