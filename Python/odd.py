from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def makepayment(self):
        pass
 
class phonepe(payment):
   def makepayment(self):
       print("it is a phonepe")



class gpay(payment):
    def makepayment(self):
        print("it is a gpay")    

obj=phonepe()
obj.makepayment()