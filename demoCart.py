import random
import gym
import numpy as np

from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

env = gym.make('CartPole-v1')

states = env.observation_space.shape[0]

actions = env.action_space.n

model = Sequential()
model.add(Flatten(input_shape=(1, states)))
model.add(Dense(24, activation='relu')) #relu = rectified linear unit (activation function)
model.add(Dense(24, activation='relu'))
model.add(Dense(actions, activation='linear'))

agent = DQNAgent(
    model = model,
    memory = SequentialMemory(limit=50000, window_length=1),
    policy=BoltzmannQPolicy(), 
    nb_actions=actions,
    nb_steps_warmup=10,
    target_model_update=0.01,   
)

agent.compile(Adam(learning_rate=1e-3), metrics=['mae'])
agent.fit(env, nb_steps=100000, visualize=True, verbose=1) #Trainign for 100000 iterations

print(np.mean(res.history['episode_reward']))
env.close()
