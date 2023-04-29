from project import *

model = PPO.load(PPO_Path,env = env)

for episode in range(episodes):
    obs=env.reset()
    done=False
    score=0
    while not done:
        env.render()
        act,_ = model.predict(obs)
        obs,reward,done,info=env.step(act)
        score+=reward
    print("episode:{}   score:{}".format(episode,score))
    