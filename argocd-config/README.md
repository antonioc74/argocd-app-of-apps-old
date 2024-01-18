## Summary
This is an example for invoking the tf-k8s-argocd terraform module.

Specifically, this example demonstrates 
- why you might use the `additional_manifests` field - in this case manually deploying a CRD outside of the ArgoCD helm chart
- how to include an additional `templates/values.yaml` file in order to inject custom config

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.0.10 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 4.3.0 |
| <a name="requirement_helm"></a> [helm](#requirement\_helm) | 2.4.1 |
| <a name="requirement_kubernetes"></a> [kubernetes](#requirement\_kubernetes) | 2.8.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 4.3.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_argocd"></a> [argocd](#module\_argocd) | ../. | n/a |

## Resources

| Name | Type |
|------|------|
| [aws_eks_cluster.cluster](https://registry.terraform.io/providers/hashicorp/aws/4.3.0/docs/data-sources/eks_cluster) | data source |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/4.3.0/docs/data-sources/region) | data source |
| [aws_secretsmanager_secret.argocd](https://registry.terraform.io/providers/hashicorp/aws/4.3.0/docs/data-sources/secretsmanager_secret) | data source |
| [aws_secretsmanager_secret_version.current](https://registry.terraform.io/providers/hashicorp/aws/4.3.0/docs/data-sources/secretsmanager_secret_version) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_BOOTSTRAP_APP_BRANCH"></a> [BOOTSTRAP\_APP\_BRANCH](#input\_BOOTSTRAP\_APP\_BRANCH) | App of apps Github branch | `string` | `"main"` | no |
| <a name="input_BOOTSTRAP_APP_HEAL"></a> [BOOTSTRAP\_APP\_HEAL](#input\_BOOTSTRAP\_APP\_HEAL) | Should Argo automatically fix code drift | `bool` | `"true"` | no |
| <a name="input_BOOTSTRAP_APP_NAME"></a> [BOOTSTRAP\_APP\_NAME](#input\_BOOTSTRAP\_APP\_NAME) | App of apps root application name | `string` | n/a | yes |
| <a name="input_BOOTSTRAP_APP_PATH"></a> [BOOTSTRAP\_APP\_PATH](#input\_BOOTSTRAP\_APP\_PATH) | Path within the App of Apps repo to monitor for Application manifests | `string` | `"/"` | no |
| <a name="input_BOOTSTRAP_APP_PRUNE"></a> [BOOTSTRAP\_APP\_PRUNE](#input\_BOOTSTRAP\_APP\_PRUNE) | Can Argo remove applications if deleted in Github | `bool` | n/a | yes |
| <a name="input_BOOTSTRAP_PROJECT_NAME"></a> [BOOTSTRAP\_PROJECT\_NAME](#input\_BOOTSTRAP\_PROJECT\_NAME) | App of apps default project | `string` | `"bootstrap-project"` | no |
| <a name="input_BOOTSTRAP_REPO_NAME"></a> [BOOTSTRAP\_REPO\_NAME](#input\_BOOTSTRAP\_REPO\_NAME) | App of apps repo name | `string` | `"bootstrap-repo"` | no |
| <a name="input_BOOTSTRAP_REPO_URL"></a> [BOOTSTRAP\_REPO\_URL](#input\_BOOTSTRAP\_REPO\_URL) | App of apps repo URL | `string` | `""` | no |
| <a name="input_additional_manifests_yaml"></a> [additional\_manifests\_yaml](#input\_additional\_manifests\_yaml) | Provide a list of additional yaml manifests to apply | <pre>list(object({<br>    name     = string<br>    manifest = string<br>  }))</pre> | `[]` | no |
| <a name="input_argo_sa_secret_name"></a> [argo\_sa\_secret\_name](#input\_argo\_sa\_secret\_name) | ArgoCD Service Account | `string` | `"dev-argocdsa-euw1"` | no |
| <a name="input_argocd_applicationset_image_repo"></a> [argocd\_applicationset\_image\_repo](#input\_argocd\_applicationset\_image\_repo) | Repo location for ArgoCD Extensions | `string` | `"ghcr.io/argoproj/argocd-applicationset"` | no |
| <a name="input_argocd_applicationset_image_version"></a> [argocd\_applicationset\_image\_version](#input\_argocd\_applicationset\_image\_version) | ArgoCD ApplicationSet image version | `string` | `"v0.4.1"` | no |
| <a name="input_argocd_extensions_image_repo"></a> [argocd\_extensions\_image\_repo](#input\_argocd\_extensions\_image\_repo) | Repo location for ArgoCD Extensions | `string` | `"ghcr.io/argoproj-labs/argocd-extensions"` | no |
| <a name="input_argocd_extensions_image_version"></a> [argocd\_extensions\_image\_version](#input\_argocd\_extensions\_image\_version) | ArgoCD Extensions image version | `string` | `"v0.1.0"` | no |
| <a name="input_argocd_image_repo"></a> [argocd\_image\_repo](#input\_argocd\_image\_repo) | Repo location for ArgoCD | `string` | `"quay.io/argoproj/argocd"` | no |
| <a name="input_argocd_image_version"></a> [argocd\_image\_version](#input\_argocd\_image\_version) | ArgoCD image version | `string` | `"v2.4.2"` | no |
| <a name="input_argocd_namespace"></a> [argocd\_namespace](#input\_argocd\_namespace) | K8S Namepsace in which to deploy ArgoCD | `string` | `"argocd"` | no |
| <a name="input_argocd_values_template_file"></a> [argocd\_values\_template\_file](#input\_argocd\_values\_template\_file) | Filename of the argocd Values template file to use | `string` | `"./templates/argocd_values_2.4.2.tpl"` | no |
| <a name="input_aws_account"></a> [aws\_account](#input\_aws\_account) | AWS account variable where resources will be created | `string` | n/a | yes |
| <a name="input_common_env_vars"></a> [common\_env\_vars](#input\_common\_env\_vars) | A map of key/value pairs to set as env vars on all argo pods | `map(any)` | `{}` | no |
| <a name="input_dex_image_repo"></a> [dex\_image\_repo](#input\_dex\_image\_repo) | Repo location for dex | `string` | `"quay.io/dexidp/dex"` | no |
| <a name="input_dex_image_version"></a> [dex\_image\_version](#input\_dex\_image\_version) | Dex image version | `string` | `"v2.31.1"` | no |
| <a name="input_eks_cluster_name"></a> [eks\_cluster\_name](#input\_eks\_cluster\_name) | Cluster name | `string` | `"dev-eks-cluster"` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | Environment type (prod/nonprod/dev) | `string` | `"dev"` | no |
| <a name="input_name"></a> [name](#input\_name) | Common name, a unique identifier | `string` | n/a | yes |
| <a name="input_redis_exporter_image_repo"></a> [redis\_exporter\_image\_repo](#input\_redis\_exporter\_image\_repo) | Repo location for redis prometheus exporter | `string` | `"public.ecr.aws/bitnami/redis-exporter"` | no |
| <a name="input_redis_exporter_image_version"></a> [redis\_exporter\_image\_version](#input\_redis\_exporter\_image\_version) | ArgoCD image version | `string` | `"1.35.0-debian-10-r12"` | no |
| <a name="input_redis_image_repo"></a> [redis\_image\_repo](#input\_redis\_image\_repo) | Repo location for redis | `string` | `"public.ecr.aws/docker/library/redis"` | no |
| <a name="input_redis_image_version"></a> [redis\_image\_version](#input\_redis\_image\_version) | ArgoCD image version | `string` | `"7.0.0-alpine"` | no |
| <a name="input_region"></a> [region](#input\_region) | Region where the provider will create resources if applicable | `string` | n/a | yes |

## Outputs

No outputs.
