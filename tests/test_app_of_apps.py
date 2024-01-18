from utils import run_shell_command

def test_kustomize_builds_in_app_of_apps():
    environments = ["dev", "int", "prod"]
    for env in environments:
        try:
            cmd = f"kustomize build app-of-apps/overlays/{env}"
            run_shell_command(cmd)
        except Exception as e:
            assert False, f"Kustomize build failed for environment '{env}' with error: {e}"
