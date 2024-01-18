import subprocess
import yaml
import os

def run_shell_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        raise Exception(f"Command failed with exit code {result.returncode}: {result.stderr}")
    return result

def read_yaml_file(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def get_app_names(path='apps'):
    """Return a list of app names (folder names) from the given path."""
    return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]