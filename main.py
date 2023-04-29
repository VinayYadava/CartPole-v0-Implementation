from project import *


def play():

    for episode in range(1,episodes+1):
        state = env.reset()
        done = False
        score = 0
        #a=0
        while not done:
            env.render()
            action = env.action_space.sample()
            obs,reward,done,info = env.step(action)
            score+=reward
            #a=a+1
            #print(score)

            #print("episode:{}".format(episode))
            #print("score:{} , state:{} , action:{} ".format(score, state , action))
            #print("obs:{} , reward:{} , done:{} , info:{}".format(obs, reward, done, info))
        #print("episode:",episode," a:",a)
        print("episode:{}   score:{}".format(episode,score))
    env.close()
play()