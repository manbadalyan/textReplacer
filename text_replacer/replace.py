import sys


def load_pairs(filename):
    with open(filename, encoding="utf-8") as file:
        return [
            tuple(line.strip().split("=", 1))
            for line in file
            if "=" in line
        ]


def replace_line(line, pairs):
    replaced = 0

    for old, new in pairs:
        occurrences = line.count(old)
        if occurrences:
            replaced += occurrences * len(old)
            line = line.replace(old, new)

    return line, replaced


def main():
    if len(sys.argv) != 3:
        raise ValueError("Usage: python replace.py <config> <text>")

    config_file, text_file = sys.argv[1:]

    pairs = load_pairs(config_file)

    with open(text_file, encoding="utf-8") as file:
        lines = file.readlines()

    result = [
        replace_line(line.rstrip("\n"), pairs)
        for line in lines
    ]

    result.sort(key=lambda item: item[1], reverse=True)

    for line, _ in result:
        print(line)


if __name__ == "__main__":
    main()