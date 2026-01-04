class CityCost:
    """
    Description: This is the data member for each city's monthly costs. 
    All are median. Note: Factor is assumed to be all other costs (transportation, discretionary, etc).
    """
    def __init__(self, id, housing, food, energy, health, tax_bracket: List, factor=0.15):
        self._id = id
        self._housing = housing
        self._food = food
        self._energy = energy
        self._health = health
        self._tax_bracket = tax_bracket 
        self._factor = factor

class IncomeByOccupation:
    """
    Description: Keeps track of the income for the city's occupation. 
    Income is the median income for that occupation in that city.
    """
    def __init__(self, occupation, city, income):
        self.occupation = occupation
        self.city = city  # CityCost id
        self.income = income

    def net_income(self, city_cost: CityCost):
        """
        Calculate net income after taxes.
        Taxes depend on city-specific rate.
        """
        tax_amount = self.income * city_cost.taxes_rate
        return self.income - tax_amount


    