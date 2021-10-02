"""
Python OOP class example: Dog
By: Tommy H. Yeargin, Jr.
Created: 02 Oct 2021
"""

class Dog:

    def __init__(self, DogName):
        self.DogName = DogName
    
    def bark(self):
        """Enables the dog you create to bark."""
        print(self.DogName + " says, \"Woof!\"")

    def about(self):
        """
        Python OOP example: Dog
        By: Tommy H. Yeargin, Jr.
        Created: 02 Oct 2021
        """

if __name__ == "__main__":

    fido = Dog("Fido")

    # print(fido.DogName)
    fido.bark()
