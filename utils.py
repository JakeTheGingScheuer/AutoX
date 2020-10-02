import importlib
from pathlib import Path


def the_road_home():
    try:
        git = importlib.import_module('git')
        repo_root = Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
    except ModuleNotFoundError:
        repo_root = Path('.')
    return repo_root


_GIT_ROOT = the_road_home()
