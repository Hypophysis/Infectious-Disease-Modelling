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
        rate at which infectious individuals become non-infectious

        Return:
            (float): removal/recovery rate
        """
        return self._gamma
    
    def get_mu(self):
        """
        Returns mortality rate of disease

        Return:
            (float): Mortality rate
        """
        return self._mu

    def get_name(self):
        """
        Returns name of disease. 

        Return:
            (str): Name of disease
        """
        return self._name

    def __str__(self):
        """
        Returns string describing the disease characteristics. 

        Return:
            (str) "{Name}: {Gamma}, {Beta}, {Mu}"
        """
        return "{0}:[{1},{2},{3}]".format(self._name, self._gamma,
                                          self._beta, self._mu)
    def __repr__(self):
        """
        Returns string of values describing disease.

        Return:
            (list): [{gamma}, {beta}, {mu}]
        """
        repr_list = [self._gamma, self._beta, self._mu]
        return repr_list
    
class Population(object):
    """
    Abstract class that creates all necessary values for tracking 
    portions of the population.
    """
    def __init__(self, total, disease):
    """
    Constructor

    Parameters: 
        total(int): Number of people in population
        disease(Disease): Object describing given disease

    """
        self._previous_step = 0
        self._total = total
        self._next_step = 0
        self._disease = disease
        self._bank = []
        self._step = 1
        self._change = 0
        self._change_list = [] #TODO: Abstraction doesn't work, infected has 2 change terms. 
        # :. Implement in individual classes

    def set_step(self, step):
        """
        TODO: Flesh out functionality here
        Returns step size ... 

        Parameters:
            (str): Scale for graph? 
        """
        self._step = step

    def get_step(self):
        """
        Returns step size (hours, days, weeks)

        Return:
            (int): Scale for graph
        """
        return self._step

    def get_previous(self):
        """
        Returns current population from previous step.

        Return:
            (int): Population in previous step
        """
        return self._previous_step

    def get_current(self):
        """ 
        Description:
        Returns current population.

        Returns value calculated as next from previous step. 

        Return:
            (int): Current population value
        """
        return self._total

    def calculate_next(self):
        """
        """
        next_step = self.get_current() - self._change        

    def get_next(self):
        """
        Returns population value of next step.

        Return:
            (int):
        """
        return self._next
    def save_change(self, change):
        """ 
        Saves si_change value to si_change list and change for next step.

        Parameters:
            si_change(float): change for next step
        """
        self._change = change
        self._change_list(change)

    def calculate_next(self):
        """
        Calculates next susceptible population value

        """
        next_step= self.get_current() - self._change

class Susceptible(Population):
    """
    Profile of non-infectious, non-immune population
    """
    def __init__(self, total, disease):
        """
        Constructor

        Parameters:
            total(int): Population susceptible to disease
            disease(Disease): Disease that affects population
        """
        super().__init__(total, disease)


class Infected(Population):
    def __init__(self, total, disease):
        super().__init__(total, disease)

class Recovered(Population):
    def __init__(self, total, disease):
        super().__init__(total, disease)

class Dead(Population):
    def __init__(self, total, disease):
        super().__init__(total, disease)

class Model_Sir(object):
    def __init__(self, disease, total = 1):
        self._susceptible = Susceptible(total, disease)
        self._infected = Infected(total, disease)
        self._recovered = Recovered(total, disease)
        self._disease = disease
    
    def get_susceptible(self):
        return self._susceptible.get_current()

    def calculate_si_change(self): 
        """
        TODO: Called SI term for now, would like better, more mathematically correct name
        Calculates change in population between susceptible and infected. 

        Formula: si_term = (beta)(Susceptible)(Infected)
        """
        si_term = self._disease[1]*self.get_susceptible()*self.get_infected()
        self._susceptible.save_change(si_term)
        self._infected.save_change(si_term)

    def get_infected(self):
        return self._infected.get_current()

    def calculate_ir_change(self):
        """
        Calculates change in population between infected and recovered.
        Formula: ir_term = (gamma)(infected)
        """
        func = get_current()
        ir_term = self._disease[0]*self.get_infected
        self._

    def get_recovered(self): 
        return self._recovered.get_current()

    def __str__(self):
        disease_name = self._disease.get_name()
        return "SIR: {0}".format(disease_name)

    def __repr__(self):
        model_list = [
            self.get_susceptible(), self.get_infected(),
            self.get_recovered
            ]
        return model_list

def disease_test():
    #From p.16 of polytechnic paper
    test = Disease("Flu", 1, 3, 1)
    test2 = Disease("Flu2", 1, 3)
    popn = Population(1, test)
    print(test.__repr__()[1])
    print("Test 1: " + str(test))
    print("Test 2: " + str(test2))
    print("Inf_P: ", test.get_infectious_period())
    print("CurrPop: ", popn.get_current())
    sus = Susceptible(1, test)
    print("sus pop: ", sus.get_current())
    sir_model = Model_Sir(test)
    
disease_test()
