import gurobipy as gp
from gurobipy import GRB


def knapsack_solver(keys, values, capacity):
    weights = {
        "pomme": 100,
        "bouteilleDEeau": 500,
        "lampe": 200,
        "carte": 200,
        "kitSecours": 500,
        "telephone": 200,
        "livre": 500,
        "sacDeCouchage": 1500,
        "tente": 2000,
        "corde": 500}

    # first we must check that every key has a value
    test = True
    result = ""
    for key in keys:
        if key not in values:
            test = False
            break

    if not(test):
        result  = "there's keys without value ! "
    else:
        #that's mean that all the keys has values !
        model = gp.Model("knapsack")

        # Decision variables
        x = model.addVars(keys, vtype=GRB.BINARY, name="x")

        # Objective function
        model.setObjective(sum(values[key] * x[key] for key in keys), GRB.MAXIMIZE)

        # Constraint: capacity
        model.addConstr(sum(weights[key] * x[key] for key in keys) <= capacity)

        # Solve
        model.optimize()

        # Extract solution
        selected_items = [key for key in keys if x[key].x > 0.5]
        total_value = sum(values[key] for key in selected_items)
        total_weight = sum(weights[key] for key in selected_items)

        result = "la solution de Félix etait : \n apporter les objet :\n"
        for elt in selected_items:
            result +=" - "+elt+"\n"
        result +=" le voyageur aurait donc un total de valeur d'importance maximal est :"+str(total_value) +"\n et son sac à dos pèserait :"+str(total_weight)

    return result

