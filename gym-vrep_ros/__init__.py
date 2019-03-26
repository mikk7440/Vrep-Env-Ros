import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='vrep_ros-v0',
    entry_point='gym-vrep_ros.envs:VrepRosEnv',
)
