
# Pytorch simple example

This tutorial shows how to deploy a simple model using ailess. The model is based on [this](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html) tutorial.

### Train model (optional)
Make sure pytorch is [properly installed](https://pytorch.org/get-started/locally/). From project folder run:
```console
python dcgan.py
```

### Init project

```console
[?] What is your project name?: pytorch_simple_examle
 ```

```console
[?] Choose an AWS region to deploy to: us-east-1
 > us-east-1
```
Сhange the suggested port to 8080
```console
[?] What port is your app running on?: 8080
```

```console
[?] How many servers in the cluster do you want to run?: 1
```
Select the instance you plan to use. If a non-GPU instance was selected, the model will be deployed locally in the same way without using a GPU
```console
[?] Choose an EC2 instance (server) type: g4dn.xlarge    (4 vCPU, 16 GB RAM, 1 NVIDIA T4 GPU)
   t3.small       (2 vCPU, 2 GB RAM)
   t3.xlarge      (4 vCPU, 16 GB RAM)
 > g4dn.xlarge    (4 vCPU, 16 GB RAM, 1 NVIDIA T4 GPU)
   g4dn.12xlarge  (48 vCPU, 192 GB RAM, 4 NVIDIA T4 GPUs)
```
In this case, the entry point is app.py
```console
[?] Where is your entrypoint file located? (e.g. app.py): app.py
```
### Serve locally
Run and wait until building and running finishes
```console
ailess serve
```
To test use test_server.ipynb or test_server.py to get test.png.

When using a GPU, it is recommended to use the latest drivers.
### Deploy to AWS
Make sure your [AWS credentials are configured correctly](https://github.com/dat1-co/ailess-cli/blob/main/readme.md#accessing-aws-resources) and run
```console
ailess deploy
```
