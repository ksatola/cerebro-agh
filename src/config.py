import os

WINDOW_SIZE = 11

RANDOM_STATE = 42
SPLIT_RATIO = 0.3
CLASS_THRESHOLD = 0.5

N_FOLDS = 5
MAX_EVALS = 10

PATH_TO_ENV = "/home/ksatola/work/"

PATH_TO_SRC = os.path.join(PATH_TO_ENV, "src")
PATH_TO_DATA = os.path.join(PATH_TO_ENV, "data")
PATH_TO_DATA_FILE = os.path.join(PATH_TO_DATA, "training_dataset.csv")

PATH_TO_NOTEBOOKS = os.path.join(PATH_TO_ENV, "notebooks")
PATH_TO_CUSTOM_MODELS = os.path.join(PATH_TO_DATA, "custom_models")

PATH_TO_DATA_PIPELINE = os.path.join(PATH_TO_DATA, "data_pipeline")
PATH_TO_FEATURE_STORE = os.path.join(PATH_TO_ENV, "feature_store")
PATH_TO_TRAINING = os.path.join(PATH_TO_DATA, "training_pipeline")

PATH_TO_PERFORMANCE_REPORTS = os.path.join(PATH_TO_DATA, "performance_monitoring")

PATH_TO_PLUGINS = os.path.join(PATH_TO_DATA, "plugins")
