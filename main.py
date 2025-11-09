from pathlib import Path

def main():
    print("Project root:", Path(__file__).resolve().parent)
    print("This is a minimal smoke test. Python + environment are working.")

if __name__ == "__main__":
    main()
