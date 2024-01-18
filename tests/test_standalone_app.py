# Test an app on its own and check that:
#   - The app namespace matches the folder name
#   - The project name matches the folder name
#   - The project is used by the app

import yaml
from utils import get_app_names, run_shell_command

# This test should be changed if you find that these rules don't apply
def check_app(doc, app_name, env):
    # Namespace should = argocd
    # spec.destination.namespace should = app_name
    # spec.project should = app_name
    metadata = doc.get('metadata', {})
    spec = doc.get('spec', {})
    app_namespace = metadata.get('namespace')
    destination_namespace = spec.get('destination', {}).get('namespace')
    project = spec.get('project')

    assert app_namespace == "argocd", f"Application namespace should be argocd for {app_name}/{env}. Is {app_namespace}."
    assert destination_namespace == app_name, f"Destination namespace for Application should be {app_name} for {app_name}/{env}. Is {destination_namespace}."
    assert project == app_name, f"Project name used for {app_name}/{env} should be the same as the app name. Is {project}."

# This test should be changed if you find that these rules don't apply
def check_project(doc, app_name, env):
    # Namespace should = argocd
    # metadata.name should = app_name
    # spec.destinations.namespace should = app_name
    metadata = doc.get('metadata', {})
    spec = doc.get('spec', {})
    project_namespace = metadata.get('namespace')
    name = metadata.get('name')
    # not mistyped, this is a plural
    destinations = spec.get('destinations', [])
    project = spec.get('project')

    destinations_namespace = None
    print(f"doc", doc)
    print(f"destinations: ", destinations)
    # Iterate over each destination dictionary
    for destination in destinations:
        print(f"destination: {destination}")
        if 'namespace' in destination:
            destinations_namespace = destination.get('namespace', [])
            break  # exit the loop if you find a namespace key

    assert project_namespace == "argocd", f"Project namespace should be argocd for {app_name}/{env}. Is {project_namespace}."
    assert name == app_name, f"Project metadata.name shohuld be {app_name} for {app_name}/{env} is {name}."
    assert destinations_namespace == app_name, f"Project destinations.namespace should be {app_name} for {app_name}/{env}. Is {destinations_namespace}."

def test_standalone_app():
    environments = ["dev", "int", "prod"]
    app_names = get_app_names()

    for app_name in app_names:
        for env in environments:
            try:
                # Run kustomize build for each app and environment
                cmd = f"kustomize build apps/{app_name}/overlays/{env}"
                result = run_shell_command(cmd)

                # Parse the stdout as multiple YAML documents
                yaml_docs = yaml.safe_load_all(result.stdout)

                project_used = False
                app_found = False

                print(result.stdout)

                for doc in yaml_docs:
                    kind = doc.get('kind')
                    if kind == 'Application':
                        print("app")
                        app_found = True
                        check_app(doc, app_name, env)
                    elif kind == 'AppProject':
                        print("project")
                        project_used = True
                        check_project(doc, app_name, env)
                    else:
                        # You can remove this if you add other kinds.
                        assert False, f"Unsuported kind: {kind}"

                # Check if the project is actually used by the app
                assert project_used, f"Project not used by the app in {app_name}/{env}"
                assert app_found, f"No app found in {app_name}/{env}"

            except Exception as e:
                assert False, f"Kustomize build failed for apps/{app_name}/overlays/{env} with error: {e}"
