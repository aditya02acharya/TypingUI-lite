import gym
import logging
import numpy as np
import pandas as pd

from os import path
from itertools import product
from operator import itemgetter

from api.aiagent.device.touchscreendevice import TouchScreenDevice


class FingerAgentEnv:

    def __init__(self, device_config, agent_config):
        """
        Finger Environment class simulates finger movement on
        touchscreen keyboard.

        Args:
        -----
            device_config: disctionary object consisting of configurations
                           for device.
            agent_config: disctionary object consisting of configurations
                          for finger environment.

        """

        self.logger = logging.getLogger(__name__)

        self.device = TouchScreenDevice(device_config)

        self.finger_location = None

        self.finger_loc_entropy = None

        self.max_finger_loc = None

        self.belief_state = None

        self.obs_prob = agent_config['observation_probability']

        self.sat_desired = None

        self.sat_true_list = agent_config['sat_true']

        self.action_types = agent_config['action_type']

        self.transition_file = agent_config['transition_file']

        self.init_entropy = None

        self.discrete_action_space = list(product(list(range(np.prod(self.device.layout.shape))), 
                                    list(range(len(self.sat_true_list))), 
                                    list(range(len(self.action_types)))))
        
        self.discrete_actions = {}

        self.initialise_action_space()

        self.observation_space = gym.spaces.Box(low=0.0, high=1.0,
                                                shape=(len(self.device.keys) +              # one-hot encoding of target
                                                       np.prod(self.device.layout.shape) +  # one-hot encoding of finger location
                                                       1 +                                  # sat desired
                                                       1,                                   # entropy.
                                                       )
                                                )
        self.logger.debug("State Space: %s" % repr(self.observation_space))
        self.action_space = gym.spaces.Discrete(len(self.discrete_action_space))
        self.logger.debug("Action Space: %s" % repr(self.action_space))

        self.logger.debug("Initialise Transition model.")
        self.initialise_transition()
    
    def initialise_action_space(self):
        """
        Generate polar action space map.

        """

        coords = list(product(*[[row for row in range(self.device.layout.shape[0])],
                                [column for column in range(self.device.layout.shape[1])]]))
        
        for loc in coords:
            polar_actions = []
            first_action = (-loc[0], -loc[1])
            last_action = (self.device.layout.shape[0] - loc[0] - 1, self.device.layout.shape[1] - loc[1] - 1)
            for x in range(first_action[0], last_action[0] + 1):
                for y in range(first_action[1], last_action[1] + 1):
                    action = (x, y)
                    polar_actions.append(action)
            self.discrete_actions[loc] = polar_actions
    
    def initialise_transition(self):
        """
        Setup function for Transition model.
        """
        self.logger.debug("Checking if initialisation of transition model is needed.")
        if path.exists(path.join('data', 'models', self.transition_file)):
            self.logger.info("Transition model exists. Loading existing model.")
            self.transition_model = pd.read_csv(path.join('data', 'models', self.transition_file), index_col=0)
        else:
            self.logger.error("Transition model doesn't exist. Creating new model.")
    
