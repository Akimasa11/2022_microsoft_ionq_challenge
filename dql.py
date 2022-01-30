from ValentinesEnv import ValentinesEnv

from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizer_v2.adam import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory
from rl.callbacks import ModelIntervalCheckpoint

env = ValentinesEnv()

model = Sequential()
model.add(Flatten(input_shape=(1, 49)))
model.add(Dense(300, activation="relu"))
model.add(Dense(300, activation="relu"))
model.add(Dense(300, activation="relu"))
model.add(Dense(9, activation="relu"))

print(model.input_shape)

policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr="eps", value_max=1, value_min=0.1,
                              value_test=0, nb_steps=30000)

memory = SequentialMemory(limit=1000000, window_length=1)

dqn = DQNAgent(model=model, nb_actions=9, policy=policy, memory=memory,
               gamma=0.99, train_interval=1, delta_clip=1.)

dqn.compile(Adam(lr=0.001), metrics=["mae"])

callbacks = [ModelIntervalCheckpoint(
    "dql-networks/step-{step}.h5f", interval=500)]

dqn.fit(env, callbacks=callbacks, nb_steps=50000,
        log_interval=1000, nb_max_start_steps=0)

dqn.save_weights("dql-networks/final.h5f", overwrite=True)
