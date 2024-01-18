# Variables File

variable "kv_resource_group_name" {
  type        = string
  description = "KeyVault's Resource Group Name"
}

variable "kv_name" {
  type        = string
  description = "KeyVault Name"
}

variable "cluster_resource_group_name" {
  type        = string
  description = "AKS Cluster's Resource Group Name"
}

variable "cluster_name" {
  type        = string
  description = "AKS Cluster Name"
}