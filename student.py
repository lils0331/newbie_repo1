class Student: #creating student data type

    def __init__(self, name, major, gpa, is_on_probation): #map out what attribute a student should have , define what a student is in the function
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation #class is overview of what student data type is, object is actual student

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return Truerue
        else:
            return False

#inheritance
from chef import chef
from ChineseChef import ChineseChef
class ChineseChef(chef): #inside chinese chef, we want to use all functions that are inside chef class



