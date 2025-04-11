import string, random


class StringHelper:

    @staticmethod
    def generateRandomString():
        return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(1, 255)))
