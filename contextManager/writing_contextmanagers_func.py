"""
Writing context managed functions
"""
import contextlib

data_set = [ x for x in range(10) ]

@contextlib.contextmanager
def before_after():
    print("Before step ... Do init here..")
    try:
        yield data_set.__iter__()
    except Exception as e:
        print(f"Exit encountered? {e}")
    finally:
        print("Final cleanup step...")

with before_after() as data:
    for item in data:
        print(f"This is what the main routine emits ... {item}")
