from src.pratik.functions import get_root


def basic_root_example():
    # Get the root
    path = get_root()
    print(f"Basic root: {path}")

def custom_trigger_root_example():
    # Get the root
    path = get_root(trigger='exemples')
    print(f"Custom root: {path}")


if __name__ == "__main__":
    basic_root_example()
    custom_trigger_root_example()
