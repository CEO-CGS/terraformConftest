<br/>

# Terraform Azure Kubernetes with Github Actions
<br/>

![Logo](readmeimage.png)


A small CI/CD pipeline in Github Actions that create an AKS, and has a test for the terraform. The errors are stored in the error folder.

**(The actions workflows themeselves do not work since I have not added the proper secrets to GitHub secrets on purpose)**

### Future Developement

- [ ] Add a better terraform OPA Conftest check to validate the terraform <br/>
- [ ] Add a clean-up job that deletes resources instead of immediately deleting the kubernetes cluster <br/>
- [ ] Clean up the code and increase the code-quality by adding more comments and proper documentation <br/>
- [ ] Add helmcharts to install things into the kubernetes cluster <br/>
  
<br/>
