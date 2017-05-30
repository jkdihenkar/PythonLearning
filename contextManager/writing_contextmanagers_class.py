"""
Any class that properly implements 
    enter and exit method can be used 
    with context manager
"""

class IntSequence(object):

    def __init__(self):
        print("Init the class ...")
        self.dataset = [ x**2 for x in range(9)]

    def __enter__(self):
        print("Entering the class method... ")
        return self.dataset

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("No more data to emit.. Cleanup!")


with IntSequence() as intSq:
    for data in intSq:
        print(f"Process data {data}")