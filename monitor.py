import psutil
import sys


def check_resources(required_ram_gb):
    # Get total RAM in GB
    total_ram = psutil.virtual_memory().total / (1024 ** 3)
    available_ram = psutil.virtual_memory().available / (1024 ** 3)

    print(f"Checking System Resources...")
    print(f"Total RAM: {total_ram:.2f} GB")
    print(f"Available RAM: {available_ram:.2f} GB")
    print(f"Required RAM: {required_ram_gb} GB")

    if available_ram < required_ram_gb:
        print(
            f"❌ CRITICAL: Not enough RAM! You need {required_ram_gb}GB but only have {available_ram:.2f}GB free.")
        sys.exit(1)  # Exit with error code to stop the pipeline
    else:
        print(f"✅ SUCCESS: Sufficient resources available.")
        sys.exit(0)


if __name__ == "__main__":
    # Example: Require 8GB to start
    check_resources(8)
