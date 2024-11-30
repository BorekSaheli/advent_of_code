from typing import List


def greet(name: str) -> int:
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b




dkjfslkdjflkjsdlkfjlksdj;lfkjs










def get_first_item(items: List[int]) -> int:
    return items[0]

def main():
    # Type Errors (Detected by mypy)
    message = greet(123)  # Error: Expected 'str', got 'int'
    total = add_numbers(10, '20')  # Error: Expected 'int', got 'str'

    items = [1, 2, 3]
    first_item = get_first_item(items)
    print(first_item)

    # Semantic Errors (Detected by Jedi LSP)
    undefined_var = some_undefined_function()  # Error: 'some_undefined_function' is not defined
    obj = None
    print(obj.non_existent_attribute)  # Error: 'NoneType' object has no attribute 'non_existent_attribute'

















if __name__ == "__main__":
    main()
