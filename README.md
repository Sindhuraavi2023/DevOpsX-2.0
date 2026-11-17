# DevOpsX 2.0
### End-to-End DevOps CI/CD Pipeline with Monitoring and Infrastructure Automation

## Project Overview

DevOpsX 2.0 is an end-to-end DevOps capstone project designed to automate application integration, testing, containerization, deployment, infrastructure provisioning, and monitoring.

The project demonstrates how DevOps tools can work together to create a repeatable deployment workflow while providing application health monitoring and failure detection.

## Objectives

- Implement Continuous Integration using Jenkins.
- Manage source code using Git and GitHub.
- Automate application testing.
- Containerize the application using Docker.
- Deploy the application using Kubernetes.
- Provision infrastructure resources using Terraform.
- Automate environment verification using Ansible.
- Monitor application performance using Prometheus and Grafana.
- Configure alert rules for application availability.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python Flask | Application development |
| Git and GitHub | Source code management |
| Jenkins | CI pipeline automation |
| Pytest | Automated testing |
| Docker | Application containerization |
| Docker Compose | Multi-container orchestration |
| Kubernetes | Container deployment |
| Terraform | Infrastructure provisioning |
| Ansible | Environment automation and verification |
| Prometheus | Metrics collection and alerting |
| Grafana | Monitoring dashboards |

## Project Architecture

The DevOpsX 2.0 workflow follows this sequence:

1. Developers maintain application code in GitHub.
2. Jenkins retrieves the source code from the repository.
3. Jenkins installs dependencies and executes automated tests.
4. Docker packages the application into a container image.
5. Docker Compose runs the application with Prometheus and Grafana.
6. Kubernetes deploys the containerized application.
7. Terraform provisions the Kubernetes namespace.
8. Ansible verifies the availability of Docker and Kubernetes.
9. Prometheus collects application metrics and evaluates alert rules.
10. Grafana visualizes monitoring information through dashboards.

## Project Structure

```text
DevOpsX-2.0/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── .gitignore
│
├── tests/
│   └── test_app.py
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   └── main.tf
│
├── ansible/
│   └── setup.yml
│
└── prometheus/
    ├── prometheus.yml
    └── alerts.yml
```

## Application Features

The Flask application provides the following endpoints:

| Endpoint | Description |
|---|---|
| `/` | Displays application information |
| `/health` | Checks application health |
| `/version` | Displays application version |
| `/metrics` | Exposes Prometheus metrics |

## CI Pipeline — Jenkins

The Jenkins pipeline automates the following stages:

1. Checkout source code from GitHub.
2. Verify Python and pip installation.
3. Install project dependencies.
4. Execute automated tests using Pytest.

The pipeline reports a successful build when all stages complete successfully.

**Latest verified CI result:** 4 automated tests passed.

## Containerization — Docker

Docker packages the Flask application into a container image.

Docker Compose runs three services:

- DevOpsX Flask application
- Prometheus
- Grafana

Start the services:

```bash
docker compose up --build -d
```

Check running containers:

```bash
docker compose ps
```

Stop the services:

```bash
docker compose down
```

## Kubernetes Deployment

The project includes Kubernetes Deployment and NodePort Service manifests.

Build the application image:

```bash
docker build -t devopsx-app:1.0 .
```

Deploy the application:

```bash
kubectl apply -f k8s/
```

Verify the deployment:

```bash
kubectl get pods
kubectl get services
```

Access the application:

```text
http://localhost:30080/
```

This deployment uses the Docker Desktop Kubernetes cluster.

## Infrastructure Provisioning — Terraform

Terraform provisions a Kubernetes namespace named `devopsx`.

Initialize Terraform:

```bash
terraform init
```

Validate configuration:

```bash
terraform validate
```

Preview infrastructure changes:

```bash
terraform plan
```

Apply the configuration:

```bash
terraform apply
```

## Configuration Automation — Ansible

Ansible is used to verify the availability of Docker and Kubernetes tools.

Run the playbook from the project’s Ansible directory:

```bash
ansible-playbook -i localhost, setup.yml
```

The playbook checks Docker and kubectl versions and displays the verification results.

## Monitoring — Prometheus and Grafana

### Prometheus

Prometheus collects application metrics from the Flask `/metrics` endpoint.

Prometheus interface:

```text
http://localhost:9090
```

The project includes an alert rule named `DevOpsXAppDown`, which detects when the application becomes unavailable.

### Grafana

Grafana provides a monitoring dashboard named:

**DevOpsX 2.0 - Application Monitoring**

Dashboard panels include:

- Application Monitoring
- Application Availability
- HTTP Request Rate

Grafana interface:

```text
http://localhost:3000
```

Local demonstration credentials:

- Username: `admin`
- Password: `devopsxadmin`

Change the default credentials before using this configuration outside a local demonstration environment.

## Automated Testing

The application is tested using Pytest.

Run tests locally:

```bash
python -m pytest -v
```

The test suite verifies:

- Home endpoint response
- Health endpoint response
- Version endpoint response
- Prometheus metrics endpoint response

**Latest verified result: 4 passed.**

## Project Outcomes

- Established a GitHub-based source code management workflow.
- Implemented a Jenkins CI pipeline.
- Automated application dependency installation and testing.
- Containerized the Flask application.
- Deployed the application to Kubernetes.
- Provisioned a Kubernetes namespace using Terraform.
- Verified infrastructure tools using Ansible.
- Integrated Prometheus metrics collection.
- Created a Grafana monitoring dashboard.
- Tested application failure detection using Prometheus alerting.

## Future Enhancements

- Implement automated Docker image publishing.
- Integrate a continuous deployment workflow.
- Add Kubernetes application monitoring.
- Introduce security scanning into the CI pipeline.
- Improve alert notification integration.

## Author

**Sindhu Raavi**

Computer Science and Engineering

DevOps Engineering Capstone Project — DevOpsX 2.0
