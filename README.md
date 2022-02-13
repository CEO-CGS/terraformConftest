# Terraform Azure Kubernetes with Github Actions

![Logo](readmeimage.png)

A small CI/CD pipeline in Github Actions that create an AKS, and has a test for the terraform. The errors are stored in the error folder.

## Future Developement

- [ ] Add a better terraform OPA Conftest check to validate the terraform <br/>
- [ ] Add a clean-up job that deletes resources instead of immediately deleting the kubernetes cluster <br/>
- [ ] Clean up the code and increase the code-quality by adding more comments and proper documentation <br/>
- [ ] Add helmcharts to install things into the kubernetes cluster <br/>
  
