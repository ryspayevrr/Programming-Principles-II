class Student:
    def __init__(self, fname, lname, major, year):
        self.fname = fname
        self.lname = lname
        self.major = major
        self.year = year

    def printinfo(self):
        print(self.fname, self.lname)
        print("Major:", self.major)
        print("Year": self.year)