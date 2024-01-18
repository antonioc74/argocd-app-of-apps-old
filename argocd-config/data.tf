data "azurerm_subscription" "current" {}

data "azurerm_kubernetes_cluster" "main" {
  name                = var.cluster_name
  resource_group_name = var.cluster_resource_group_name
}

data "azurerm_key_vault" "github_credentials" {
  name                = var.kv_name
  resource_group_name = var.kv_resource_group_name
}

data "azurerm_key_vault_secret" "github_argocd_username" {
  name         = "github-argo-username"
  key_vault_id = data.azurerm_key_vault.github_credentials.id
}

data "azurerm_key_vault_secret" "github_argocd_password" {
  name         = "github-argo-password"
  key_vault_id = data.azurerm_key_vault.github_credentials.id
}