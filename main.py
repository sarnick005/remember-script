from remember.cli import parse_input_command


def main():
    command = input("").lower()
    parse_input_command(command)


if __name__ == "__main__":
    main()
