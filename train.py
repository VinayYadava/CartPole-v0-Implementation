from project import *


log_path = os.path.join("Training","logs")
PPO_Path=os.path.join("Training","Saved Models",'PPO_Model_Cartpole')
print(log_path)

env = gym.make(
    env_name
    )

env = DummyVecEnv(
    [
        lambda:env
    ]
)

model = PPO(
    policy='MlpPolicy',
    env = env,
    verbose=1,
    tensorboard_log=log_path
)

model.learn(total_timesteps=20000)

model.save(PPO_Path)
env.close()
