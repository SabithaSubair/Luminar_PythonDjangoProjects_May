class College:
    collegename="LT"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def printdetails(self):
        print("collegenmae::",College.collegename)
        print("student name::",self.name)
        print("Roll no::",self.roll)
    def __str__(self):
        return str(self.roll)+self.name+College.collegename
        #string concatination..if we use integer ,cnvert it into string
ob=College("anu",4)
print(ob)
ob1=College("amal",8)
print(ob1)