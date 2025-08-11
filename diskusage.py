#!/usr/bin/env python3
import os
import sys
import subprocess

def list_files_with_size(path):
    """List all files in a directory with size in KB."""
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print(f"❌ Directory not found: {path}")
        sys.exit(1)

    print("\n📂 Files and Sizes (KB):")
    for filename in files:
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            size_kb = os.path.getsize(full_path) / 1024
            print(f"  {full_path:<60} {size_kb:10.2f} KB")
    print("-" * 80)


def check_disk_usage(threshold_percent=10):
    """Check disk usage and print partitions above the threshold."""
    print(f"\n💽 Partitions over {threshold_percent}% usage:\n")
    result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.strip().split("\n")

    for line in lines[1:]:  # skip header
        usage_percent = int(line.split()[-2].strip('%'))
        if usage_percent >= threshold_percent:
            print(f"  {line}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory_path>")
        sys.exit(1)

    target_dir = sys.argv[1]
    list_files_with_size(target_dir)
    check_disk_usage(threshold_percent=10)
