#!/usr/bin/env python3


def open_file(filename: str):
    try_state = "CRISIS ALERT"
    response = ""
    status = "Normal operations resumed"

    try:
        with open(filename, "r") as f:
            try_state = "ROUTINE ACCESS"
            response = f"SUCCESS: Archive recovered - ``{f.read()}''"
    except FileNotFoundError:
        response = "RESPONSE: Archive not found in storage matrix"
        status = " Crisis handled, system stable"
    except PermissionError:
        response = "RESPONSE: Security protocols deny access"
        status = "Crisis handled, security maintained"

    print(f"{try_state}: Attempting access to '{filename}'...")
    print(response)
    print(f"STATUS: {status}")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files = [
                "lost_archive.txt",
                "classified_data.txt",
                "standard_archive.txt"
             ]
    for file in files:
        open_file(file)
        print()

    print("All crisis scenarios handled successfully. Archives secure.")
