from singleton import singleton

@singleton
class CreateReport():

    def __init__(self):
        self._Cost = {"2021": {"Cost":123,
                            "Actual":234,
                            "diff":45},
                    "2022":{"Cost":13,
                            "Actual":34,
                            "diff":0}        
                            }

    def CalculateCosts (self,*,ReferenceTablePath,CostTablePath):
        print (ReferenceTablePath,CostTablePath)

    @property
    def YearList (self):
        return sorted(list(self._Cost))

    @property
    def Cost(self):
        return self._Cost
