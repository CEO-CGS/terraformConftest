# Test

A small CI/CD pipeline in Github Actions that create an AKS, and has a test for the terraform. The errors are stored in the error folder.

## Future Developement

  [x] Add a better terraform OPA Conftest check to validate the terraform
  [x] Add a clean-up job that deletes resources instead of immediately deleting the kubernetes cluster
  [x] Clean up the code and increase the code-quality by adding more comments and proper documentation
  [x] Add helmcharts to install things into the kubernetes cluster
  
