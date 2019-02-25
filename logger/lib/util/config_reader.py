import yaml


def load_config(file_path='../conf.yml'):
    conf = yaml.load(open(file_path))
    return conf
