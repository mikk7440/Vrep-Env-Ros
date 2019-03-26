import numpy as np
from numpy import linalg as LA

from gym import error, spaces
from gym.utils import seeding

class VrepRosEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):

        self.action_space =
        self.observation_space =
        observation, _reward, done, _info = self.step()

    def step(self, action):
        done = self.take_action(action)
        ob = self.get_observation()
        reward = self.get_reward()
        info = {}
        return ob, reward, done, info

    def take_action(self, action):
        done = "DoSomething"                # TODO: Make take_action
        return done

    def get_reward(self,dist2target):

        return dist2target*10.0             # TODO: Make reward function

    def get_observation(self):
        robot_x = 0.0                       # TODO: get tcp from sim
        robot_y = 0.0
        robot = np.array([robot_x,robot_y])

        target_x = 0.0                      # TODO: get target
        target_y = 0.0
        target = np.array([target_x,target_y])

        dist2target = LA.norm(robot-target)
        return  np.concatenate((
            robot,
            target,
            dist2target),
            axis = None
        )

    #####################################
    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass
