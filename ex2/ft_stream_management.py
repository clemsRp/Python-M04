#!/usr/bin/env python3

import sys


def get_inputs():
    print("Input Stream active.", end=" ")
    ar_id = input("Enter archivist ID: ")

    print("Input Stream active.", end=" ")
    status = input("Enter status report: ")

    print(file=sys.stdout)

    return ar_id, status


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    ar_id, status = get_inputs()

    print(f"[STANDARD] Archive status from {ar_id}: {status}",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete\n",
          file=sys.stdout)

    print("Three-channel communication test successful.",
          file=sys.stdout)
