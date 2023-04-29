from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
import gym
import os


env_name = "CartPole-v0"
env = gym.make(env_name)
episodes = 10

log_path = os.path.join("Training","logs")
PPO_Path=os.path.join("Training","Saved Models",'PPO_Model_Cartpole')
