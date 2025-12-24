#!/usr/bin/env python3


def put_nbr(num: int):
    if num >= 100:
        return str(num)
    elif num >= 10:
        return "0" + str(num)
    else:
        return "00" + str(num)


def main(filename: str, content: list):
    print("Initializing new storage unit:", filename)

    file = open(filename, "w")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    for k in range(len(content)):
        line = f"[ENTRY {put_nbr(k + 1)}] {content[k]}"
        if k != len(content) - 1:
            line += "\n"
        file.write(line)
        print(line, end="")
    print()

    file.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    content = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]
    main("new_discovery.txt", content)
