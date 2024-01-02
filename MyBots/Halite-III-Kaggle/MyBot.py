from kaggle_environments import make, evaluate
from kaggle_environments.envs.halite.helpers import *
from datetime import datetime
import json
import os
from random import choice


# Build the game.
env = make('halite', debug=True)
env.run(['random', 'random', 'random', 'random'])
# env.render(mode='html', width=800, height=600) # for notebooks
# print(env.toJSON()) # exports game to JSON

# Save the game data to the replay folder.
replay_path = '../../replays/Halite-III-Kaggle'
replay_file_name = datetime.now().strftime('%Y_%m_%d-%H_%M_%S') + '.json'
os.makedirs(replay_path, exist_ok=True)
with open(os.path.join(replay_path, replay_file_name), 'w+') as f:
	json.dump(env.toJSON(), f, indent=4)


def agent(obs, config):
	board = Board(obs, config)
	me = board.current_player

	# Set actions for each ship.
	for ship in me.ships:
		ship.next_action = choice(
			[
				ShipAction.NORTH, ShipAction.EAST, ShipAction.SOUTH, 
				ShipAction.WEST, None
			]
		)

	# Set actions for each shipyard.
	for shipyard in me.shipyards:
		shipyard.next_action = None

	return me.next_actions
