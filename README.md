# System Info Web Service

**Note: This is incomplete. Unfortunatly, due to problems I did not expect, my machine was experiencing failures, and therefore I had less time then expected to complete the test. I did everything I could in the timeframe I had. Unfortunatly it didn't work out as expected.**

## Running Natively

cd into `swish/code`:
`cd swish/code`

To install the required packages, run:
```
pip install -r requirements.txt
```

To run the app natively:
```
python3 -m uvicorn main:app --reload
```

## Run In Container

### Prerequisits

Install docker:
```
sudo yum install -y docker
```

### Build and Push

cd into the `swish` directory
Add every new file into `./code`
Edit the `Dockerfile` with everything new you have added.
Run `pip freeze > requirements.txt` to update the requirements file.

Then, run:
```
docker build -t <image_name> .
```

### Run on docker

After building the image, run:
```
docker run -d --name test_webservice -p 80:80 web_service
```

If you then run `curl http://localhost` you should get the API response.
```
{
  "cpu":"AMD Ryzen 7 3700X 8-Core Processor",
  "cores":4,"gpu":"No GPU Found",
  "time_utc":"2022-06-18T11:25:05.439477",
  "local_ip":"172.17.0.2",
  "external_ip":"<external_ip>",
  "memory":"7821.01 MB"}
```

### Run on Kubernetes

This setup is for Centos-7 and up. 

#### Install Ansible

Run:
```
sudo yum install -y ansible
```

#### Setup Minikube Cluster

Follow the below tutorial on how to set up the cluster:
`https://phoenixnap.com/kb/install-minikube-on-centos`

#### Run the Playbook

```
cd deploy_webservice
ansible-playbook deploy_webservice.yml
```
