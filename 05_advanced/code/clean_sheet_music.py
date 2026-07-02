import sys

def clean(file_path):
    cleaned_lines = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.strip("RH:")
            line = line.strip("LH:")
            if len(line) < 4:
                line = ""
            cleaned_lines.append(line)
    with open(file_path, "w") as f:
        for line in cleaned_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python clean_sheet_music.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    clean(file_path)