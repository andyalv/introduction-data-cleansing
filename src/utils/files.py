from pathlib import Path


# Read a string from a file and return it.
# If the file is empty or an error occurs during reading, it raises an exception.
def get_str_from_file(file_path: Path) -> str:
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Check if the file is empty and raise an error if it is
        if not content.strip():
            raise ValueError("File is empty")

        return content
    except Exception as e:
        raise Exception(f"Error reading file: {e}")
