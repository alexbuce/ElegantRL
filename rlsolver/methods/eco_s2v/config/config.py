import torch as th
from torch.cuda import graph

GPU_ID = 0

NUM_TRAIN_NODES = 100

from rlsolver.methods.config import GraphType
# GRAPH_TYPE = 'BA'
GRAPH_TYPE = GraphType.BA


NUM_INFERENCE_NODES = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 2000, 3000, 4000, 5000]
INFERENCE_PREFIXES = [GRAPH_TYPE.value + "_" + str(i) + "_" for i in NUM_INFERENCE_NODES]

# PREFIXES = ["BA_100_", "BA_200_", "BA_300_", "BA_400_", "BA_500_", "BA_600_", "BA_700_", "BA_800_", "BA_900_",
#             "BA_1000_", "BA_1100_", "BA_1200_", "BA_2000_", "BA_3000_", "BA_4000_",
#             "BA_5000_"]  # Replace with your desired prefixes


def calc_device(gpu_id: int):
    return th.device(f'cuda:{gpu_id}' if th.cuda.is_available() and gpu_id >= 0 else 'cpu')


ALG_NAME = "eco"
assert ALG_NAME in ["eco", "s2v"]

# NETWORK_SAVE_PATH = "pretrained_agent/eco/network_best_BA_20spin.pth"
NETWORK_SAVE_PATH = "pretrained_agent/" + ALG_NAME + "/network_best_" + GRAPH_TYPE.value + "_" + str(NUM_INFERENCE_NODES) + "spin.pth"

# GRAPH_SAVE_LOC = "../../data/syn_BA"
GRAPH_SAVE_LOC = "../../data/syn_" + GRAPH_TYPE.value

DEVICE = calc_device(GPU_ID)
TEST_DEVICE = calc_device(-1)
if GRAPH_TYPE.value == 'BA':
    if NUM_TRAIN_NODES == 20:
        NB_STEPS = 2500000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 150000
        SAVE_NETWORK_FREQUENCY = 100000
        TEST_FREQUENCY = 10000
    elif NUM_TRAIN_NODES == 40:
        NB_STEPS = 2500000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 150000
        SAVE_NETWORK_FREQUENCY = 100000
        TEST_FREQUENCY = 10000
    elif NUM_TRAIN_NODES == 60:
        NB_STEPS = 5000000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 300000
        SAVE_NETWORK_FREQUENCY = 200000
        TEST_FREQUENCY = 20000
    elif NUM_TRAIN_NODES == 100:
        NB_STEPS = 8000000
        REPLAY_START_SIZE = 1500
        REPLAY_BUFFER_SIZE = 10000
        UPDATE_TARGET_FREQUENCY = 2500
        FINAL_EXPLORATION_STEP = 800000
        SAVE_NETWORK_FREQUENCY = 400000
        TEST_FREQUENCY = 50000
    elif NUM_TRAIN_NODES == 200:
        NB_STEPS = 8000000
        REPLAY_START_SIZE = 3000
        REPLAY_BUFFER_SIZE = 15000
        UPDATE_TARGET_FREQUENCY = 4000
        FINAL_EXPLORATION_STEP = 800000
        SAVE_NETWORK_FREQUENCY = 80000
        TEST_FREQUENCY = 10000
    else:
        raise ValueError("parameters are not set")
elif GRAPH_TYPE.value == 'ER':
    if NUM_TRAIN_NODES == 20:
        NB_STEPS = 2500000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 150000
        SAVE_NETWORK_FREQUENCY = 100000
        TEST_FREQUENCY = 10000
    elif NUM_TRAIN_NODES == 40:
        NB_STEPS = 2500000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 150000
        SAVE_NETWORK_FREQUENCY = 100000
        TEST_FREQUENCY = 10000
    elif NUM_TRAIN_NODES == 60:
        NB_STEPS = 5000000
        REPLAY_START_SIZE = 500
        REPLAY_BUFFER_SIZE = 5000
        UPDATE_TARGET_FREQUENCY = 1000
        FINAL_EXPLORATION_STEP = 300000
        SAVE_NETWORK_FREQUENCY = 200000
        TEST_FREQUENCY = 20000
    elif NUM_TRAIN_NODES == 100:
        NB_STEPS = 8000000
        REPLAY_START_SIZE = 1500
        REPLAY_BUFFER_SIZE = 10000
        UPDATE_TARGET_FREQUENCY = 2500
        FINAL_EXPLORATION_STEP = 800000
        SAVE_NETWORK_FREQUENCY = 400000
        TEST_FREQUENCY = 50000
    elif NUM_TRAIN_NODES == 200:
        NB_STEPS = 10000000
        REPLAY_START_SIZE = 3000
        REPLAY_BUFFER_SIZE = 15000
        UPDATE_TARGET_FREQUENCY = 4000
        FINAL_EXPLORATION_STEP = 800000
        SAVE_NETWORK_FREQUENCY = 400000
        TEST_FREQUENCY = 50000
    else:
        raise ValueError("parameters are not set")
