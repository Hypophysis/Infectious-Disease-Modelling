#Program for modelling infectious disease based on variables
"""TODO: 
Classes: 
Disease 
For SIRD Model
    Susceptible
    Infected
    Recovered
    Dead
    Default variable: Mortality?
"""
#Global Variables:
POPULATION = 1
#POP#Program for modelling infectious disease based on variables
"""TODO: 
Classes: 
Disease 
For SIRD Model
    Susceptible
    Infected
    Recovered
    Dead
    Default variable: Mortality?
Implement changes? 
Maybe don't implement Sections of model,
but the changes in them?
"""
#Global Variables:
POPULATION = 1
SUSCEPTIBLE = 0
INFECTED = 0
RECOVERED = 0 
DEAD = 0
#POPULATION = input("Input total population: ")

#Classes: 
class Disease(object):
    """Constructs disease object using variables generally associated with SIRD models.
    """
    def __init__(self, name, gamma, beta, mu = 0):
        """ 
        Constructor

        Parameters:
            name(str): name of disease
            gamma(float): removal/recovery rate
            beta(float): transmission "rate"
            mu(float): mortality rate
        """
        #TODO: implement unit time if self._unit_time == "days":
        #self._unit_time = unit_time.lower()
        self._name = name
        self._gamma = gamma
        self._beta = beta
        self._mu = mu

    def get_beta(self):
        """
        Returns gamma value of disease.
        Return:
            (float): Representing gamma (removal/recovery rate) value of disease
        """
        return self._beta
    
    def get_infectious_period(self):
        """
        Returns average period of time that disease is infectious for.
        Return:
            (float): time for which disease is infectious for
        """
        infect_period = 1/(self._gamma)
        return infect_period
    
    def get_gamma(self):
        """
        """
        return self._gamma
    
    def get_mu(self):
        return self._mu
    
    def __str__(self):
        return "{0}:[{1},{2},{3}]".format(self._name, self._gamma,
                                          self._beta, self._mu)
    def __repr__(self):
        """
        Return:
            (list): [{gamma}, {beta}, {mu}]
        """
        return "[{0},{1},{2}]".format(self._gamma,
                                      self._beta, self._mu)
#class Susceptible(object):
    #TODO: Class map for implementation. 
    #Inidividual population class? Susceptible inherits from population class?
    """
    Profile of non-infectious, non-immune population
    """
class Population(object):
    def __init__(self, total, disease):
        self._previous_step = 0
        self._total = total
        self._next_step = 0
        self._disease = disease

    def get_previous(self):
        return self._previous_step

    def get_current(self):
        return self._total

    def get_next(self):
        return self._next

class SI_delta(Population):
    def __init__(self, total, disease):
        super().__init__(total, disease)
    
    def get_next
        delta = self._disease[1]*
        next = self.get_current() - delta


"""
class Susceptible(Population):
    def __init__(self, total, disease):
        super().__init__(total, disease)
    
    def get_next(self):
        delta = self._disease[1]*
        next = self.get_current() - delta
        

class Infected(Population):
    def __init__(self, total, disease):
        super().init(total, disease)

class Recovered(Population):
    def __init__(self, total, disease):
        super().init(total, disease)

class Dead(Population):
    def __init__(self, total, disease):
        super().init(total, disease)
"""
def disease_test():
    #From p.16 of polytechnic paper
    test = Disease("Flu", 1, 3, 1)
    test2 = Disease("Flu2", 1, 3)
    popn = Population(1)
    print("Test 1: " + str(test))
    print("Test 2: " + str(test2))
    print(test.get_infectious_period())
    print(popn.get_current())

    sus = Susceptible(1)
    print(sus.get_current())
    
disease_test()
ULATION = input("Input total population: ")

#Classes: 
class Disease(object):
    """Constructs disease object using variables generally associated with SIRD models.
    """
    def __init__(self, name, gamma, beta, mu = 0):
        """ 
        Constructor

        Parameters:
            name(str): name of disease
            gamma(float): removal/recovery rate
            beta(float): transmission "rate"
            mu(float): mortality rate
        """
        #TODO: implement unit time if self._unit_time == "days":
        #self._unit_time = unit_time.lower()
        self._name = name
        self._gamma = gamma
        self._beta = beta
        self._mu = mu

    def get_beta(self):
        """
        Returns gamma value of disease.
        Return:
            (float): Representing gamma (removal/recovery rate) value of disease
        """
        return self._beta
    
    def get_infectious_period(self):
        """
        Returns average period of time that disease is infectious for.
        Return:
            (float): time for which disease is infectious for
        """
        infect_period = 1/(self._gamma)
        return infect_period
    
    def get_gamma(self):
        """
        """
        return self._gamma
    
    def get_mu(self):
        return self._mu
    
    def __str__(self):
        return "{0}:[{1},{2},{3}]".format(self._name, self._gamma,
                                          self._beta, self._mu)
    def __repr__(self):
        return "[{0},{1},{2}]".format(self._gamma,
                                      self._beta, self._mu)
#class Susceptible(object):
    #TODO: Class map for implementation. 
    #Inidividual population class? Susceptible inherits from population class?
    """
    Profile of non-infectious, non-immune population
    """
class Population(object):
    def __init__(self, total):
        self._previous_step = 0
        self._total = total
        self._next_step = 0

    def get_previous(self):
        return self._previous_step

    def get_current(self):
        return self._total

    def get_next(self):
        return self._next

class Susceptible(Population):
    def __init__(self, total):
        super().__init__(total)
    
    def get_next(self):
        pass

class Infected(Population):
    def __init__(self, total):
        super().init(total)

class Recovered(Population):
    def __init__(self, total):
        super().init(total)

class Dead(Population):
    def __init__(self, total):
        super().init(total)

def disease_test():
    #From p.16 of polytechnic paper
    test = Disease("Flu", 1, 3, 1)
    test2 = Disease("Flu2", 1, 3)
    popn = Population(1)
    print("Test 1: " + str(test))
    print("Test 2: " + str(test2))
    print(test.get_infectious_period())
    print(popn.get_current())

    sus = Susceptible(1)
    print(sus.get_current())
    
disease_test()
