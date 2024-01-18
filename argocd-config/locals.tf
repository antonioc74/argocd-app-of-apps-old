locals {
  additional_manifests_yaml = flatten([
    for manifest in fileset("./additional_manifests", "*.yaml") : [
      for idx, resource in split("---", file("./additional_manifests/${manifest}")) : {
        name     = trimsuffix("${manifest}_${idx}", ".yaml")
        manifest = resource
      } if chomp(resource) != ""
    ]
  ])
}
