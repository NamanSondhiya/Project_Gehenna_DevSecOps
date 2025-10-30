# Gehenna - Enterprise 3-Tier Flask Application

Gehenna is a robust 3-tier web application built with Flask and MongoDB, showcasing DevSecOps practices in a cloud-native setup on Amazon EKS. It serves as a practical example of modern development methodologies, from local prototyping to production deployment.

## Architecture Overview

The application adopts a classic 3-tier structure: a Flask-based frontend for the user interface, a RESTful backend API for business logic, and MongoDB as the database layer. Mongo Express provides a web-based admin interface for database management. In Kubernetes, components are containerized and orchestrated within the `gehenna` namespace, utilizing services for internal communication and ConfigMaps/Secrets for configuration.

Key elements include Pods for running containers, Services for load balancing, and Helm charts for streamlined deployment.

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────────────┐
│   Frontend  │     │   Backend   │     │   MongoDB   │     │ Mongo Express│
│    Service  │◄───►│   Service   │◄───►│   Service   │     │   Service    │
│             │     │             │     │             │     │              │
│   Frontend  │     │   Backend   │     │   MongoDB   │     │ Mongo Express│
│     Pod     │     │     Pod     │     │     Pod     │     │     Pod      │
└─────────────┘     └─────────────┘     └─────────────┘     └──────────────┘
       ↑                   ↑                   ↑                   ↑
   User Access       API Calls         Data Ops         Admin Access
```

## Features

- Full CRUD operations for name management with real-time updates
- RESTful API with error handling and input validation
- Security measures like CORS support and structured logging
- Health checks for monitoring
- Scalable microservices design

## Technology Stack

- **Frontend**: Flask, HTML, CSS, JavaScript
- **Backend**: Flask, Python
- **Database**: MongoDB
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Amazon EKS)
- **CI/CD**: Jenkins with shared libraries, ArgoCD for GitOps
- **Monitoring**: Kube-Prometheus-Stack
- **Security**: SonarQube, OWASP Dependency Check, Trivy

## Project Structure

```
Project_Gehenna_DevSecOps/
├── backend/                 # Backend Flask API
│   ├── app.py              # Main application
│   ├── connection.py       # Database connection
│   ├── Dockerfile          # Backend container
│   └── requirements.txt    # Python dependencies
├── frontend/               # Frontend Flask app
│   ├── templates/          # HTML templates
│   ├── app.py             # Frontend application
│   ├── Dockerfile         # Frontend container
│   └── requirements.txt   # Python dependencies
├── kubernetes/            # Helm chart
│   ├── templates/         # K8s manifests
│   ├── Chart.yaml         # Helm chart metadata
│   └── values.yaml        # Configuration values
├── GitOps/               # GitOps configuration
│   └── Jenkinsfile       # CD pipeline
├── Jenkinsfile           # CI pipeline
├── docker-compose.yml    # Local development
└── sonar-project.properties # SonarQube config
```

## Local Development

To run the application locally, ensure you have Docker, Docker Compose, Python 3.9+, and Node.js installed.

1. Clone the repo: `git clone https://github.com/NamanSondhiya/Project_Gehenna_DevSecOps.git && cd Project_Gehenna_DevSecOps`
2. Launch with Docker Compose: `docker-compose up -d`
3. Access at:
   - Frontend: http://localhost:8001
   - Backend API: http://localhost:8002
   - Mongo Express: http://localhost:8081

## Production Deployment

Deploy to Amazon EKS using Helm. Prerequisites: EKS cluster, eksctl, kubectl, Helm 3, ArgoCD.

1. Install the chart: `helm install gehenna ./kubernetes -n default`
2. Check status: `kubectl get pods -n gehenna && kubectl get services -n gehenna`

## CI/CD Pipeline

The Jenkins pipeline enforces DevSecOps through stages like parameter validation, code quality checks with SonarQube, security scans via OWASP and Trivy, Docker builds, and artifact management. It integrates shared libraries for reusable functions and triggers ArgoCD for automated deployments.

ArgoCD handles GitOps, syncing changes automatically, monitoring health, and supporting rollbacks with email notifications.

## Monitoring & Observability

Using Kube-Prometheus-Stack, the setup collects metrics on application performance, infrastructure, and custom business data. Grafana provides dashboards for visualizing request rates, resource usage, and error tracking.

## Security Features

Security is baked in with SAST via SonarQube, dependency checks, container scanning, secrets management in Kubernetes, network policies, and RBAC. Best practices include input sanitization, hardened images, and resource quotas.

## Configuration

### Environment Variables

- **Frontend**: BACKEND_URL, PORT, HOST
- **Backend**: MONGO_URL, PORT, HOST, FRONTEND_ORIGINS

### Helm Values

Customize via `values.yaml` for images, namespace, etc.

## Testing

Test the API endpoints:

```bash
curl http://<public-ip>:8002/health
curl http://<public-ip>:8002/api/get
curl -X POST http://<public-ip>:8002/api/add/Naman
curl http://<public-ip>:8002/api/search/Naman
```

## API Documentation

| Method | Endpoint          | Description          |
|--------|-------------------|----------------------|
| GET    | `/`               | Service status       |
| GET    | `/health`         | Health check         |
| GET    | `/api/get`        | Retrieve all names   |
| POST   | `/api/add/<name>` | Add a name           |
| DELETE | `/api/delete/<name>` | Delete a name     |
| GET    | `/api/search/<query>` | Search names      |

## License

MIT License.

## Developer

**Naman Sondhiya** - Full Stack DevSecOps Engineer  
Email: ssnaman4@gmail.com  
Focus: Cloud-native apps, DevSecOps, Kubernetes.

## Project Links

- [Source Code](https://github.com/NamanSondhiya/Project_Gehenna_DevSecOps)
- [Container Registry](https://hub.docker.com/u/namanss)
- [Shared Libraries](https://github.com/NamanSondhiya/Jenkins-trusted-libraries)

