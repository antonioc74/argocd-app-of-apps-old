# Test that apps are included in the app-of-apps kustomize
import os
import yaml
from utils import run_shell_command, get_app_names

def test_apps_inclusion():
    environments = ["dev", "int", "prod"]
    
    for env in environments:
        try:
            # Run kustomize build for app-of-apps for the environment
            cmd = f"kustomize build app-of-apps/overlays/{env}"
            result = run_shell_command(cmd)

            # Parse the stdout as multiple YAML documents
            yaml_docs = yaml.safe_load_all(result.stdout)

            # Enumerate all the apps we expect to be there
            expected_apps = set(get_app_names())
            found_apps = set()

            for doc in yaml_docs:
                if doc.get('kind') != 'Application':
                    continue
                app_name = doc.get("metadata", {}).get("name")
                
                if app_name in expected_apps:
                    found_apps.add(app_name)
            
            # Make sure every expected app is found
            assert expected_apps == found_apps, f"Missing apps: {expected_apps - found_apps}"
        
        except Exception as e:
            assert False, f"Kustomize build failed for app-of-apps/overlays/{env} with error: {e}"
