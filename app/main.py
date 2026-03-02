import os


def move_file(command: str) -> None:
    _, source, destination = command.split(" ")
    if "/" not in destination :
        os.rename(source, destination)
    else:
        parts = destination.split("/")
        directory = os.path.join(*parts[:-1])
        new_file_name = destination.split("/")[-1]
        current_path = ""
        current_directory = directory.split("/")
        for new_directory in current_directory:
            if new_directory == "":
                continue
            current_path = os.path.join(current_path, new_directory)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        destination_path = os.path.join(current_path, new_file_name)
        with (open(source, "r") as file_in,
              open(destination_path, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
        os.remove(source)
