import random
from math import exp

def rand(first, last):
    return random.uniform( first, last )
#end function

#print(rand(0, 1))

def sigmoid(x):
    return 1 / (1 + exp(-x))
#end function

#print( sigmoid( rand(10, 25) ) )

weights = []
bias = 1.0

# Conjunto de Treinamento
# Problema: OR Lógico
# TEST: AND Lógico

training_sets = [
    {
        "inputs": [0, 0],
        "output": 0
    },
    {
        "inputs": [1, 0],
        "output": 0
    },
    {
        "inputs": [0, 1],
        "output": 0
    },
    {
        "inputs": [1, 1],
        "output": 1
    }
]

#print( training_sets )
#print( "Entradas: {} -> Saída: {}".format( training_sets[0]["inputs"], training_sets[0]["output"] ) )

# Iniciar os PESOS
# Necessário 1 peso por entrada
for i in range( 0, len( training_sets[0]["inputs"] ) ):
    weights.append( rand(0, 1) )
    # print("w: ", weights[i])
#end for

bias = rand(0, 1)
# print("b: ", bias)

def run(inputs):
    
    global weights
    global bias
    
    sum = 0.0
    for i in range( len(weights) ):
        sum += inputs[i] * weights[i]
    #end for
    sum += bias
    return sigmoid(sum)
#end function

def train(inputs, desired):

    global weights
    global bias

    y = run(inputs)

    for i in range( len(inputs) ):
        weights[i] += (desired - y) * inputs[i]
    #end for
    bias += (desired - y)

    # print("Valor esperado: {} -> Saída: {}".format( desired, run(inputs) ) )
#end function

iterations = 0

while iterations < 1000:

    for i in range( 0, len(training_sets) ):
        train( training_sets[i]["inputs"], training_sets[i]["output"] )
    #end for

    iterations += 1
#end while

print("====== TESTE ======")


newInput = [0, 0] # FALSE

if run(newInput) < 0.5:
    print("FALSE")
else:
    print("TRUE")
#endif

