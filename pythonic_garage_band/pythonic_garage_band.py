from abc import abstractmethod, ABC

class Band():
    instances = []
    bands = []
    
    def __init__(self,name,members):
        self.name=name
        self.members = members
        Band.instances.append(self)
    
    def add_members(self,member_name):
        self.member_name=member_name
        Band.members.append(member_name)
    
    def play_solos(self):
        result =[]
        for i in self.members:
            result.append(i.play_solo())
        return result
    
    @classmethod 
    def to_list(cls):
        return cls.instances

    def __str__(self):
        return f"Band <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "

class Musician():
    
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def __str__(self):
        return f"Musician <{self.name}>"
    
    @abstractmethod
    def __repr__(self):
        return f" '{self.name}' "
    


class Guitarist(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return 'face melting guitar solo'

class Bassist(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return 'bom bom buh bom'
class Drummer(Musician):
    
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return 'rattle boom crash'

if __name__ == "__main__":
    aziz = Guitarist('Joan Jett')
    saleh=Drummer('Saleh')
    emad = Bassist('Emad')
    print(aziz)
    print(aziz.get_instrument())
    print(saleh)
    print(saleh.get_instrument())
    print(emad)
    print(emad.get_instrument())
    print(aziz.play_solo())
    print(saleh.play_solo())
    print(emad.play_solo())
    habail = Band('habail')
    habail.add_members(aziz)
    habail.add_members(saleh)
    habail.add_members(emad)
    print(habail.bands)
    print(habail.__str__())
    print(habail.to_list())
    print(habail.play_solos())