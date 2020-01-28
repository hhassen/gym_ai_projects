import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space
    env.step(env.action_space.sample()) # take a random action
env.close()