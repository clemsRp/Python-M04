#!/usr/bin/env python3

def main(filename: str) -> None:
    '''
    Dsiplay the content of a file
    '''
    print("Accessing Storage Vault:", filename)

    file = open(filename, "r")
    print("Connection established...\n")

    print("RECOVERED DATA:")
    content = file.read()
    print(content)

    file.close()
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    main("ancient_fragment.txt")
