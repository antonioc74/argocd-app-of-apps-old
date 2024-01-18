module "argocd_configuration" {
  source                    = "github.com/contino/aks-argo.git//configuration"
  additional_manifests_yaml = local.additional_manifests_yaml
}
