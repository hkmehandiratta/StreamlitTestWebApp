import os

FILEPATH = "todos.txt"


def create_file_if_not_exists(file_path=FILEPATH):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass

def get_todos(file_path=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    create_file_if_not_exists()
    with open(file_path, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """ Write the to-do items list to a text file. """
    create_file_if_not_exists()
    with open(file_path, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    # Test the functions
    todos = get_todos()
    print("Current todos:", todos)

    new_todos = ["Buy groceries\n", "Clean the house\n", "Pay bills\n"]
    write_todos(new_todos)

    updated_todos = get_todos()
    print("Updated todos:", updated_todos)