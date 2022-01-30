from keras.models import Sequential
from keras.layers import Dense, Flatten

import numpy as np

from ValentinesEnv import ValentinesEnv

from copy import deepcopy

GAMES = 100

model = Sequential()
model.add(Flatten(input_shape=(1, 49)))
model.add(Dense(300, activation="relu"))
model.add(Dense(300, activation="relu"))
model.add(Dense(300, activation="relu"))
model.add(Dense(9, activation="relu"))

env = ValentinesEnv()

open("results/dql-winrate.txt", "w").close()

for f in ["dql-networks\\final.h5f"]:
    print(f)
    model.load_weights(f)
    won = 0
    total_reward = 0
    for episode in range(GAMES):
        # Obtain the initial observation by resetting the environment.
        observation = deepcopy(env.reset())

        done = False
        while not done:
            action_values = model.predict(np.array([[observation]]))[0]
            action = action_values.argmax(axis=0)
            observation, r, done, info = env.step(action)
            observation = deepcopy(observation)
            if r > 0:
                won += 1
                total_reward += r
        print(f"Game {episode} complete")
    print(won, total_reward)
