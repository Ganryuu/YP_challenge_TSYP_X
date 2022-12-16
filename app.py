from flask import Flask , jsonify , request     
import numpy as np 
import json 
app = Flask(__name__) 

"""importing all different policies so we can choose from
    Aget Name : Phoebe
"""


# @app.before_request
# def before():
#     print("This is executed BEFORE each request.")

@app.route('/', methods=['GET'])
def home(): 
    return {
        "name" : "Phoebe" ,  
        "title" : "YP_CHALLENGE_API" , 
        "Description" : "ARTEMIS MISSION OPTIMIZATION",
    }
"""through the monte carlo algorithm we iterate through different policies to decide the optimal one for 
each environment
we use iterative policy evaluation for estimating the best policy 
"""
@app.route('/path/', methods=['GET','POST'])
def path_find(): 
    from Policies import Q1 , Q2 , Q3 , Q4 , Q5 , Q6 
    # parameters
    gamma = 1  # discounting rate
    rewardSize = -0.01
    gridSize = 15
    terminationStates = [[0, 0]]
    # all possible actions
    #actions based on input grid 
    actions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1], [0, 0]]
    numIterations = 1000 # number of iterations to learn from 
    theta = 0.01
    # removing blocks from states
    states = [[i, j] for i in range(gridSize) for j in range(gridSize)]
    xy = np.mgrid[0:4:1, 6:8:1].reshape(2, -1).T
    xy2 = np.mgrid[11:15:1, 5:7:1].reshape(2, -1).T
    xy3 = np.mgrid[7:9:1, 12:15:1].reshape(2, -1).T
    for x in xy.tolist():
        states.remove(x)
    for x in xy2.tolist():
        states.remove(x)
    for x in xy3.tolist():
        states.remove(x)
    policy, values = Q2.policy_iteration(states, actions, gamma, theta, numIterations, rewardSize, terminationStates, gridSize)
    data = Q2.print_policy(policy, gridSize)
   
    resp = {}
    for x in range(len(data)) : 
        resp[x] = data[x]
    
    print(type(resp))
    print(resp)
    final = {}
    k = 0 
    for x in resp.values()  : 
        k += 1 
        final[k] = x.tolist() 
    
    #please note that this will take about 2 minutes to give the response 
    return  final 
@app.route('/tasks/',methods=['GET'])
def get_task(): 
    
        f = open('./tasks.json')
        print(type(f))
        
        data = json.load(f)
        print(type(data))
        return data
app.run() 

