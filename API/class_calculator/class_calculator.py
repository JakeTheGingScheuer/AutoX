import class_calculator.DAO as DAO

def get_manufacturers():
    manufacturerList = DAO.manufacturers()
    return manufacturerList, 200
