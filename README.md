# CartPole-v0 Implementation 
This project contains three Python files - train.py, test.py, and evaluation.py - and a package called project with an __init__.py file. The train.py script is used to train our model, the test.py script is used to test our trained model, and the evaluation.py script is used to evaluate the performance of our model on the CartPole-v0 environment.

## Installation 
To run this project, you need to install the following packages:

### gym
stable-baselines3
You can install these packages by running the following command:

python
Copy code
!pip install gym stable-baselines3

## Usage 
To train the model, run the train.py script. This script trains the model using the PPO algorithm from the stable-baselines3 package and saves it in the Training/Saved Models/PPO_Model_Cartpole directory.

To test the model, run the test.py script. This script loads the trained model from the Training/Saved Models/PPO_Model_Cartpole directory and tests it on 10 episodes of the CartPole-v0 environment.

To evaluate the model, run the evaluation.py script. This script loads the trained model from the Training/Saved Models/PPO_Model_Cartpole directory and evaluates its performance on 10 episodes of the CartPole-v0 environment.

## File Descriptions 
### train.py 
This script is used to train our model on the CartPole-v0 environment. It uses the PPO algorithm from the stable-baselines3 package to train the model. The trained model is saved in the Training/Saved Models/PPO_Model_Cartpole directory.
### test.py 
This script is used to test our trained model on the CartPole-v0 environment. It loads the trained model from the Training/Saved Models/PPO_Model_Cartpole directory and tests it on 10 episodes of the CartPole-v0 environment.
### evaluation.py 
This script is used to evaluate the performance of our trained model on the CartPole-v0 environment. It loads the trained model from the Training/Saved Models/PPO_Model_Cartpole directory and evaluates its performance on 10 episodes of the CartPole-v0 environment.
### project/__init__.py 
This package contains the necessary imports and variables used in the train.py, test.py, and evaluation.py scripts. The __init__.py file contains the following imports:

PPO algorithm from stable-baselines3
DummyVecEnv class from stable-baselines3.common.vec_env
evaluate_policy function from stable-baselines3.common.evaluation
gym module
os module
It also defines the env_name variable as "CartPole-v0", env variable as the gym environment for env_name, episodes variable as 10, log_path variable as "Training/logs", and PPO_Path variable as "Training/Saved Models/PPO_Model_Cartpole".
