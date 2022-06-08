from pathlib import Path
from ruamel import yaml

def config():
    settings_file = str(Path(__file__).parent.absolute()) + '/settings.yml'

    with open(settings_file, 'r') as f:
        return yaml.load(f, Loader=yaml.UnsafeLoader)

