import numpy as np

def calculate(list):
    n = len(list)

    if(n != 9):
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(list).reshape(3,3)

    # print(arr)

     # Initialize the dictionary to store results
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    # cal mean
    calculations['mean'].append(arr.mean(axis=0).tolist())
    calculations['mean'].append(arr.mean(axis=1).tolist())
    calculations['mean'].append(arr.mean().tolist())

    # cal variance
    calculations['variance'].append(arr.var(axis=0).tolist())
    calculations['variance'].append(arr.var(axis=1).tolist())
    calculations['variance'].append(arr.var().tolist())

    # cal standard deviation
    calculations['standard deviation'].append(arr.std(axis=0).tolist())
    calculations['standard deviation'].append(arr.std(axis=1).tolist())
    calculations['standard deviation'].append(arr.std().tolist())

    # cal max
    calculations['max'].append(arr.max(axis=0).tolist())
    calculations['max'].append(arr.max(axis=1).tolist())
    calculations['max'].append(arr.max().tolist())

    # cal min
    calculations['min'].append(arr.min(axis=0).tolist())
    calculations['min'].append(arr.min(axis=1).tolist())
    calculations['min'].append(arr.min().tolist())

    # cal sum
    calculations['sum'].append(arr.sum(axis=0).tolist())
    calculations['sum'].append(arr.sum(axis=1).tolist())
    calculations['sum'].append(arr.sum().tolist())

    return calculations