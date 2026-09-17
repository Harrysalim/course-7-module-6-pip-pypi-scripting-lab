from datetime import datetime
import os

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("log_data must be a list")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    result_file = generate_log(sample_data)
    print(f"Log written to {result_file}")