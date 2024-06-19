

# Cloud Native Monitoring App

![System Monitoring Screenshot](screenshot.png)

Cloud Native Monitoring App is a Flask-based web application for real-time monitoring of CPU and memory utilization metrics.

## Features

- Displays CPU utilization in a gauge chart.
- Displays memory utilization in a gauge chart.
- Alerts for high CPU or memory usage (threshold set at 80%).

## Prerequisites

- Python 3.x installed on your system.
- Python packages listed in `requirements.txt`.
- Docker installed locally.

## Deployment to Azure Kubernetes Service (AKS)

1. **Create an AKS Cluster:**
   - Use the Azure portal or Azure CLI to create an AKS cluster. Ensure to configure the cluster with appropriate node sizes, node pools, and networking settings.

2. **Push Docker Image to Azure Container Registry (ACR):**
   - Ensure your Docker image (`youracrname.azurecr.io/cloud-native-monitoring:v1`) is pushed to your Azure Container Registry (ACR). If not done already, follow these steps:
     ```bash
     # Login to your ACR
     az acr login --name youracrname
     
     # Push the Docker image to ACR
     docker push youracrname.azurecr.io/cloud-native-monitoring:v1
     ```

3. **Automate Deployment Using Python:**
   - Use Python scripts with Azure SDKs (`azure-cli` or `azure-mgmt`) to automate the deployment process. Example steps:
     - Authenticate with Azure:
       ```python
       from azure.identity import DefaultAzureCredential
       from azure.mgmt.containerservice import ContainerServiceClient
       
       credential = DefaultAzureCredential()
       client = ContainerServiceClient(credential, subscription_id)
       ```
     - Create AKS deployment:
       ```python
       # Replace with your AKS deployment code
       ```
     - Deploy the application:
       ```python
       # Replace with your deployment code
       ```

4. **Access the Application:**
   - Obtain the external IP of your service to access the application.

## Screenshots


## Technologies Used

- Flask
- Plotly (for gauge charts)
- psutil (for system monitoring)
- Docker
- Azure Kubernetes Service (AKS)

## Acknowledgments

- Special thanks to [N4si](https://github.com/N4si) for contributions to the project and valuable insights.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
