import inspect

def read_file() -> str:
    caller_file = inspect.stack()[1].filename
    file_name_no_ext = caller_file.split("/")[-1].replace(".py", "")
    with open(f"inputs/{file_name_no_ext}.txt", 'r') as file:
        data = file.read()
    return data

def test(actual, expected):
    assert actual == expected, f"expected: {expected} but got: {actual}"