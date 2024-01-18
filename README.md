# Contino AKS Standard GitOps Build

This is part of the Contino AKS Standard GitOps Build. This repository provides the App-of-Apps Application within ArgoCD.

## App-of-Apps

This repository should be cloned into your own GitHub account as a PAT must be generated which is not possible on a per-repository basis from within the Contino Organization.

### Instructions

Steps 4 and 5 may have already been completed if you've already followed the instructions within the AKS Standard Terraform repository.

This repository serves as a foundational structure for managing multiple Kubernetes applications using [ArgoCD's App-of-Apps pattern](https://argo-cd.readthedocs.io/en/stable/operator-manual/cluster-bootstrapping/#app-of-apps-pattern).

1. The **backend.vars** file should first be updated with the details of the Azure Blob which will be used to store the Terraform state:

- subscription_id: The Azure Subscription Id
- resource_group_name: The name of the Resource Group which contains the Storage Account resource
- storage_account_name: The name of the Storage Account resource
- container_name: The name of the Blob Container within the Storage Account
- key: The name of the Blob which the Terraform state will be stored in 

2. The deployment of this App will require the use of a KeyVault within your Subscription. Update the desired **vars.tfvars** file with these details:

- kv_resource_group_name: The name of the Resource Group that the KeyVault is in
- kv_name: The name of the KeyVault resource

3. Additional variables that should be set within this file are as follows:

- cluster_resource_group_name: The name of the Resource Group that the AKS Cluster is in
- cluster_name: The name of the AKS Cluster resource

4. Within your own GitHub account, create a fine-grained tokwn which will provide **Read** access to the repository.

5. Two secrets should be created within a KeyVault within your Subscription (your user will require the KeyVault Secrets Officer Role):

- github-argo-username: Your GitHub Username
- github-argo-password: The PAT value that was previously created

6. Update the location of the 2048 sample application

The location of the 2048 sample application (ACR Url) needs to be updated in the `base` and `dev` manifest files:

- /apps/2048/kustomized_helm/helm_base/templates/deployment.yml
- /apps/2048/kustomized_helm/overlays/dev/kustomization.yml

7. Update the location of the repository

The GitHub location of this repository need to be updated in sevaral places (this should be set to the HTTPS Git Clone Url):

- /app-of-apps/base/application.yaml
- /apps/2048/base/application.yaml
- /argocd-config/additional_manifests/bootstrap.yaml

8. Save all changes and push them to the remote origin

9. To test the Terraform deployment you can run the commands below from within the /argocd-config folder of this repository:

- `terraform init -backend-config="./variables/<path>/backend.tfvars"`
- `terraform plan -var-file="./variables/<path>/vars.tfvars"`
- `terraform apply -var-file="./variables/<path>/vars.tfvars"`
