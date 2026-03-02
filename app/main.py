import os


def move_file(command: str) -> None:
    file_names = command.split(" ")
    if len(file_names) != 3:
        return
    if file_names[0] != "mv":
        return
    if len(str(file_names[2]).split("/")) == 1:
        os.rename(file_names[1], file_names[2])
    else:
        if file_names[2].endswith("/"):
            directory = file_names[2]
            new_file_name = file_names[1]
        else:
            directory = "/".join(file_names[2].split("/")[:-1]) + "/"
            new_file_name = file_names[2].split("/")[-1]
            current_path = ""
            current_directory = directory.split("/")
            for new_directory in current_directory:
                if new_directory == "":
                    continue
                current_path = os.path.join(current_path, new_directory)
                if not os.path.exists(current_path):

                    os.mkdir(current_path)
            destination_path = os.path.join(current_path, new_file_name)
            with (open(file_names[1], "r") as file_in,
                  open(destination_path, "w") as file_out):
                content = file_in.read()
                file_out.write(content)
            os.remove(file_names[1])
