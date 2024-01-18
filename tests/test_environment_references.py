import os
import yaml
from utils import read_yaml_file

def scan_yaml_for_other_environments(yaml_data, current_env, other_environments):
    yaml_str = yaml.dump(yaml_data)
    for other_env in other_environments:
        assert other_env not in yaml_str, f"Environment '{current_env}' has a reference to '{other_env}'"

def test_no_cross_environment_references_in_yaml():
    environments = ["dev", "int", "prod"]
    app_paths = ["apps", "app-of-apps"]

    for app_path in app_paths:
        for env in environments:
            dir_to_scan = os.path.join(app_path, "overlays", env)
            
            if not os.path.exists(dir_to_scan):
                continue
            
            for root, dirs, files in os.walk(dir_to_scan):
                for file in files:
                    if file.endswith('.yaml') or file.endswith('.yml'):
                        full_path = os.path.join(root, file)
                        yaml_data = read_yaml_file(full_path)
                        
                        other_environments = [e for e in environments if e != env]
                        scan_yaml_for_other_environments(yaml_data, env, other_environments)
