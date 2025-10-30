# Gehenna - Enterprise 3-Tier Flask Application

A production-grade 3-tier web application demonstrating modern DevSecOps practices with Flask, MongoDB, and Amazon EKS deployment. Built as a comprehensive showcase of cloud-native development and deployment methodologies.

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   Frontend      │    │   Backend       │    │   Database      │
│   (Flask)       │◄──►│   (Flask API)   │◄──►│   (MongoDB)     │
│   Port: 8001    │    │   Port: 8002    │    │   Port: 27017   │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │                 │
                    │  Mongo Express  │
                    │  (Admin UI)     │
                    │  Port: 8081     │
                    │                 │
                    └─────────────────┘
```

**[Screenshot Placeholder: Local Architecture Diagram]**

**[Screenshot Placeholder: Kubernetes Architecture Diagram]**

This application follows a 3-tier architecture:
- **Frontend**: Flask web application serving the user interface
- **Backend**: Flask REST API handling business logic
- **Database**: MongoDB for data persistence
- **Admin Interface**: Mongo Express for database management

### Kubernetes Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Amazon EKS Cluster                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   gehenna namespace                     │    │
│  │                                                         │    │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │    │
│  │  │  Frontend   │    │   Backend   │    │  Database   │  │    │
│  │  │    Pod      │◄──►│     Pod     │◄──►│     Pod     │  │    │
│  │  │             │    │             │    │             │  │    │
│  │  └─────────────┘    └─────────────┘    └─────────────┘  │    │
│  │         │                   │                   │       │    │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │    │
│  │  │  Frontend   │    │   Backend   │    │   MongoDB   │  │    │
│  │  │   Service   │    │   Service   │    │   Service   │  │    │
│  │  │ (NodePort)  │    │ (ClusterIP) │    │ (ClusterIP) │  │    │
│  │  └─────────────┘    └─────────────┘    └─────────────┘  │    │
│  │                                                         │    │
│  │  ┌─────────────┐                                        │    │
│  │  │Mongo Express│                                        │    │
│  │  │    Pod      │                                        │    │
│  │  │             │                                        │    │
│  │  └─────────────┘                                        │    │
│  │         │                                               │    │
│  │  ┌─────────────┐                                        │    │
│  │  │Mongo Express│                                        │    │
│  │  │   Service   │                                        │    │
│  │  │ (ClusterIP) │                                        │    │
│  │  └─────────────┘                                        │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 ConfigMaps & Secrets                    │    │
│  │  • Environment Variables                                │    │
│  │  • Database Credentials                                 │    │
│  │  • Service Configuration                                │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

**Key Kubernetes Components:**
- **Pods**: Containerized application instances
- **Services**: Internal load balancing and service discovery
- **ConfigMaps**: Environment configuration
- **Secrets**: Sensitive data like database credentials
- **Namespace**: Isolated environment (`gehenna`)
- **Helm Chart**: Package management for deployment

## 🚀 Features

- **Dynamic Name Management**: Complete CRUD operations with real-time data handling
- **RESTful API Architecture**: Production-ready endpoints with comprehensive error handling
- **Enterprise Security**: Multi-layer input validation and data sanitization
- **Health Monitoring**: Advanced health check endpoints for production monitoring
- **Cross-Origin Support**: Configurable CORS for multi-domain deployments
- **Structured Logging**: Enterprise-grade logging with detailed request tracking
- **Scalable Design**: Microservices architecture ready for horizontal scaling

## 🛠️ Technology Stack

- **Frontend**: Flask, HTML, CSS, JavaScript
- **Backend**: Flask, Python
- **Database**: MongoDB
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Amazon EKS)
- **Package Management**: Helm Charts
- **CI/CD**: Jenkins with Shared Libraries
- **GitOps**: ArgoCD
- **Monitoring**: Kube-Prometheus-Stack
- **Security**: OWASP Dependency Check, Trivy, SonarQube

## 📁 Project Structure

```
gehenna_2.0/
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

## 🔧 Local Development

### Prerequisites
- Docker and Docker Compose
- Python 3.9+
- Node.js (for development tools)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/NamanSondhiya/Project_Gehenna.git
   cd Project_Gehenna
   ```

2. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:8001
   - Backend API: http://localhost:8002
   - Mongo Express: http://localhost:8081

**[Screenshot Placeholder: Local Development Setup]**

## 🏭 Production Deployment

### Amazon EKS Deployment

**[Screenshot Placeholder: EKS Cluster Overview]**

The application is deployed on Amazon EKS using Helm charts with the following components:

#### Prerequisites
- Amazon EKS cluster
- kubectl configured
- Helm 3.x installed
- ArgoCD installed on cluster

#### Deployment Steps

1. **Deploy using Helm**
   ```bash
   helm install gehenna ./kubernetes -n gehenna --create-namespace
   ```

2. **Verify deployment**
   ```bash
   kubectl get pods -n gehenna
   kubectl get services -n gehenna
   ```

**[Screenshot Placeholder: Kubernetes Pods Status]**

**[Screenshot Placeholder: Kubernetes Services]**

## 🔄 CI/CD Pipeline

### Jenkins CI Pipeline

**[Screenshot Placeholder: Jenkins Pipeline Overview]**

The CI pipeline implements DevSecOps best practices with the following stages:

#### Pipeline Stages

1. **Parameter Validation**
   - Validates required image tags
   - Ensures proper input format

2. **Code Quality & Security**
   - **SonarQube Analysis**: Code quality and security scanning
   - **Quality Gate**: Enforces quality standards
   - **OWASP Dependency Check**: Identifies vulnerable dependencies
   - **Trivy Filesystem Scan**: Scans for secrets and vulnerabilities

**[Screenshot Placeholder: SonarQube Dashboard]**

**[Screenshot Placeholder: OWASP Dependency Check Results]**

3. **Build & Security Scanning**
   - **Parallel Docker Builds**: Frontend and backend images
   - **Trivy Image Scanning**: Container vulnerability assessment
   - **Multi-stage builds**: Optimized container images

**[Screenshot Placeholder: Trivy Scan Results]**

4. **Artifact Management**
   - **DockerHub Push**: Conditional image publishing
   - **Artifact Archiving**: Security reports and build artifacts
   - **Email Notifications**: Automated notifications for build success/failure with security reports attached
   - **CD Pipeline Trigger**: Automatically triggers GitOps deployment on successful CI build

**[Screenshot Placeholder: DockerHub Repository]**

#### Jenkins Shared Library Integration

The pipeline leverages custom Jenkins shared libraries from [jenkins-trusted-libraries](https://github.com/NamanSondhiya/Jenkins-trusted-libraries.git):
- `git_clone()`: Standardized Git operations
- `sonarqube_analysis()`: SonarQube integration
- `owasp_scan()`: OWASP dependency checking
- `trivy_fs_scan()` & `trivy_image_scan()`: Security scanning
- `docker_build()`, `docker_push()`: Container operations

**[Screenshot Placeholder: Jenkins Shared Library Usage]**

### ArgoCD GitOps

**[Screenshot Placeholder: ArgoCD Application Dashboard]**

Continuous Deployment is managed through ArgoCD with:
- **Automated Sync**: Git-based deployment triggers
- **Health Monitoring**: Application health status
- **Rollback Capabilities**: Easy rollback to previous versions
- **Email Notifications**: Build status notifications for both CI and CD pipelines


**[Screenshot Placeholder: ArgoCD Sync Status]**

**[Screenshot Placeholder: ArgoCD Application Health]**

## 📊 Monitoring & Observability

### Kube-Prometheus-Stack

**[Screenshot Placeholder: Grafana Dashboard Overview]**

Comprehensive monitoring setup includes:

#### Prometheus Metrics
- Application performance metrics
- Infrastructure monitoring
- Custom business metrics
- Alert rules and thresholds

**[Screenshot Placeholder: Prometheus Targets]**

#### Grafana Dashboards
- **Application Dashboard**: Request rates, response times, error rates
- **Infrastructure Dashboard**: CPU, memory, disk, network usage
- **Business Dashboard**: User activity, feature usage

**[Screenshot Placeholder: Application Metrics Dashboard]**

**[Screenshot Placeholder: Infrastructure Monitoring Dashboard]**



## 🔒 Security Features

### DevSecOps Implementation

**[Screenshot Placeholder: Security Scan Summary]**

- **Static Application Security Testing (SAST)**: SonarQube integration
- **Dependency Scanning**: OWASP Dependency Check
- **Container Security**: Trivy vulnerability scanning
- **Secrets Management**: Kubernetes secrets and environment variables
- **Network Policies**: Kubernetes network segmentation
- **RBAC**: Role-based access control

### Security Best Practices

- Multi-layer input validation and sanitization
- Production-grade CORS configuration
- Comprehensive health check endpoints
- Hardened container images with minimal attack surface
- Non-privileged container execution
- Resource limits and security quotas
- Clean, maintainable code following industry standards



## 📈 Performance Metrics
## 📈 Recent Updates

### Frontend-Backend Connectivity Fix

- **Issue**: Frontend failed to load data due to empty BACKEND_URL in JavaScript, causing API fetch calls to fail.

- **Solution**: Added proxy routes in frontend (`/api/get`, `/api/add/<name>`, `/api/delete/<name>`, `/api/search/<query>`) that forward requests to the backend using environment variables. This ensures reliable communication within Kubernetes without direct backend exposure.

- **Process Flow**:

  1. User interacts with frontend UI (e.g., adds a name).

  2. Frontend JavaScript makes relative API calls (e.g., `/api/add/John`).

  3. Frontend proxy routes receive the request and forward it to the backend service.

  4. Backend processes the request, validates input, and interacts with MongoDB.

  5. Backend returns response to frontend proxy.

  6. Frontend displays the result to the user.



**[Screenshot Placeholder: Updated Frontend-Backend Communication Flow]**



### Architecture Optimization

- Implemented clean Python/Flask patterns following industry best practices
- Optimized for maintainability with clear separation of concerns
- Enhanced error handling and comprehensive logging throughout the application stack
- Streamlined deployment process with automated testing and validation



### Docker Image Update

- Latest frontend image: `namanss/gehenna-frontend-ii:4.3` (updated in `kubernetes/values.yaml`).

- Verified with `python3 -m py_compile` for syntax correctness.



**[Screenshot Placeholder: Docker Build and Push Success]**

**[Screenshot Placeholder: Performance Dashboard]**

Key performance indicators:
- **Response Time**: Average API response time
- **Throughput**: Requests per second
- **Error Rate**: Percentage of failed requests
- **Availability**: Uptime percentage
- **Resource Utilization**: CPU, memory, storage usage

## 🔧 Configuration

### Environment Variables

#### Frontend
- `BACKEND_URL`: Backend service URL
- `PORT`: Frontend service port
- `HOST`: Bind address

#### Backend
- `MONGO_URL`: MongoDB connection string
- `PORT`: Backend service port
- `HOST`: Bind address
- `FRONTEND_ORIGINS`: CORS allowed origins

### Kubernetes Configuration

The Helm chart supports customization through `values.yaml`:

```yaml
namespace: gehenna
frontendImage: docker.io/namanss/gehenna-frontend-ii:4.3
backendImage: docker.io/namanss/gehenna-backend-ii:4.0
mongoexpressImage: docker.io/mongo-express:1.0.2-20-alpine3.19
mongoImage: docker.io/mongo:latest
```

## 🧪 Testing

**[Screenshot Placeholder: Test Results]**

### API Testing
```bash
# Health check
curl http://<public-ip>:8002/health

# Get all names
curl http://<public-ip>:8002/api/get

# Add a name
curl -X POST http://<public-ip>:8002/api/add/Naman

# Search names
curl http://<public-ip>:8002/api/search/Naman
```

## 📝 API Documentation

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Service status |
| GET | `/health` | Health check |
| GET | `/api/get` | Retrieve all names |
| POST | `/api/add/<name>` | Add a new name |
| DELETE | `/api/delete/<name>` | Delete a name |
| GET | `/api/search/<query>` | Search names |

## 🤝 Professional Collaboration

This project demonstrates enterprise-level development practices and is available for:
- **Code Review**: Professional assessment and feedback
- **Consultation**: DevSecOps implementation guidance
- **Custom Development**: Similar enterprise solutions
- **Training**: Hands-on DevSecOps workshops

For collaboration opportunities, please reach out via email.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Developer

**Naman Sondhiya** - Full Stack DevSecOps Engineer
- **Email**: ssnaman4@gmail.com
- **Specialization**: Cloud-native applications, DevSecOps automation, Kubernetes orchestration
- **Focus**: Enterprise-grade solutions with security-first approach

## 🔗 Project Links

- **Source Code**: https://github.com/NamanSondhiya/Project_Gehenna_DevSecOps
- **Container Registry**: https://hub.docker.com/u/namanss
- **CI Repository**: https://github.com/NamanSondhiya/Project_Gehenna_DevSecOps
- **Shared Libraries**: https://github.com/NamanSondhiya/Jenkins-trusted-libraries

---

## 📋 Project Highlights

This project showcases:
- **Enterprise Architecture**: Scalable 3-tier design with microservices principles
- **DevSecOps Excellence**: Comprehensive security scanning and automated deployment
- **Cloud-Native Deployment**: Production-ready Kubernetes orchestration
- **Monitoring Integration**: Full observability stack with Prometheus and Grafana
- **Professional Standards**: Industry best practices and clean code principles

---

**Professional Contact**: For enterprise solutions, consulting, or collaboration opportunities, please reach out to discuss your requirements.