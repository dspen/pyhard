class Parent(object):

    #method of only this class
    def implicit(self):
        print("Parent Implicit");

    #method that will get replaced by Child class
    def override(self):
        print("Parent Override");

    #method to be called by super
    def altered(self):
        print("Parent altered()");

class Child(Parent):
    pass

    #method that overrites Parent.override()
    def override(self):
        print("Child Override");

    #method that calls Parent.altered()
    def altered(self):
        print("Child pre-adult altered");
        super(Child,self).altered();
        print("Child, post-adult altered()")

dad = Parent();
son = Child();

dad.implicit()
son.implicit()

dad.override();
son.override();

dad.altered()
son.altered()
