#!/usr/bin/env python3

def mode(file_mode: str) -> str:
    '''
    Return a string depending of how we open the file
    '''
    if file_mode in ["a", "w", "r+"]:
        return "PRESERVATION"
    return "EXTRACTION"


def main(file_list: list) -> None:
    '''
    Open and read or write each file in files_list
    '''
    for file in file_list:
        with open(file["name"], file["mode"]) as f:
            print(f"\nSECURE {mode(file["mode"])}:")
            print(f.read())

            if file["mode"] == "r+":
                f.write("")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    file_list = [
                    {"name": "classified_data.txt", "mode": "r"},
                    {"name": "security_protocols.txt", "mode": "r+"}
                 ]
    main(file_list)

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")
