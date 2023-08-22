import os


def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command, current_file, new_file = command.split()
        if command == "cp" and (
            current_file != new_file and os.path.exists(current_file)
        ):
            with open(current_file, "r") as file_in, open(
                new_file, "w"
            ) as file_out:
                file_out.write(file_in.read())
