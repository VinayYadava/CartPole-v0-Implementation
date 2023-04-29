from project import *

"""  this script is there is to evaluate our model   """
model = PPO.load(PPO_Path,env = env)
tup = evaluate_policy(model,env,n_eval_episodes=10,render = True)
print(tup)
env.close()
