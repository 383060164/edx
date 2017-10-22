# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:05:43 2017

@author: tiany
"""

import datetime

class Person(object):
    def __init__(self,name):
        self.name=name
        self.birthday=None
        self.lastName=name.split(' ')[-1]
    def getLastName(self):
        return self.lastName
    def __str__(self):
        return self.name
    
    def setBirthday(self,month,day,year):
        self.birthday=datetime.date(year,month,day)
    
    def getAge(self):
        if self.birthday==None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days
    
    def __lt__(self,other):
        """return true if self's name is lexicographically 
        less than other's name, and false otherwise"""
        if self.lastName == other.lastName:
            return self.name<other.name
        return self.lastName < other.lastName
#example usage   
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')
personList= [p1, p2, p3, p4, p5]


class MITPerson(Person):
    nextIdNum=0 #next ID number to assign
    def __init__(self,name):
        Person.__init__(self,name) 
        self.idNum=MITPerson.nextIdNum
        MITPerson.nextIdNum+=1
    
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self,other):
        return self.idNum<other.idNum
    
    def speak(self,utterance):
        return (self.getLastName()+'says:'+utterance)
class Student(MITPerson):
    pass
class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year=classYear
    def getClass(self):
        return self.year
    def speak(self,utterance):
        return MITPerson.speak(self,"Dude,"+utterance)
class Grad(Student):
    pass
class TransferStudent(Student):
    pass 

def isStudent(obj):
    return isinstance(obj,Student)
class Professor(MITPerson):
    def __init__(self,name,department):
        MITPerson.__init__(self,name)
        self.department=department
        
    def speak(self,utterance):
        new='In course'+self.department+'we say'
        return MITPerson.speak(self,new+utterance)
    def lecture(self,topic):
        return self.speak('it is obvious that'+topic)






