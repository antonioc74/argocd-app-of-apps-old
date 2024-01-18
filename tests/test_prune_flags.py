from utils import run_shell_command
import yaml

def test_prune_flags():
    environments = {
        "dev": True,
        "int": False,
        "prod": False,
    }

    for env, expected_prune_value in environments.items():
        try:
            cmd = f"kustomize build app-of-apps/overlays/{env}"
            result = run_shell_command(cmd)
            
            # Parse the stdout as multiple YAML documents
            yaml_docs = yaml.safe_load_all(result.stdout)
            
            prune_found = False
            for doc in yaml_docs:
                actual_prune_value = doc.get("spec",{}).get("syncPolicy", {}).get("automated", {}).get("prune")
                
                if actual_prune_value is not None:
                    prune_found = True
                    assert actual_prune_value == expected_prune_value, \
                        f"For app-of-apps/overlays/{env}, expected prune: {expected_prune_value}, got {actual_prune_value}"
            
            assert prune_found, f"No prune flag found for app-of-apps/overlays/{env}"

        except Exception as e:
            assert False, f"Kustomize build failed for app-of-apps/overlays/{env} with error: {e}"
