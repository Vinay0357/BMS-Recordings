class A:
    def first(self):
        print("I'm first method Class A")
    def pdtr(self):
        print("Proddatur is a town in kadapa distict")
class B:
    def first(self):
        print("I'm first method Class B")
    def jmd(self):
        print("Jammalamadugu is a town in kadapa distict")
        
class C(B,A):
    def first(self):
        print("I'm first method Class C")
    
cc = C()
cc.first()
cc.pdtr()
cc.jmd()