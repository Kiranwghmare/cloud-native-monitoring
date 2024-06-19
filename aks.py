from kubernetes import client, config

# Load Kubernetes configuration from default kubeconfig file
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    api_version="apps/v1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="my-flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "my-flask-app"}),
            spec=client.V1PodSpec(containers=[
                client.V1Container(
                    name="my-flask-container",
                    image="mycontainerregistry.azurecr.io/my-flask-app:latest",  # Replace with your ACR image
                    ports=[client.V1ContainerPort(container_port=5000)]
                )
            ])
        )
    )
)

# Create the deployment
apps_api_instance = client.AppsV1Api(api_client)
apps_api_instance.create_namespaced_deployment(namespace="default", body=deployment)

# Define the service with type LoadBalancer
service = client.V1Service(
    api_version="v1",
    kind="Service",
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-flask-app"},
        ports=[client.V1ServicePort(port=80, target_port=5000)],
        type="LoadBalancer"
    )
)

# Create the service
core_api_instance = client.CoreV1Api(api_client)
core_api_instance.create_namespaced_service(namespace="default", body=service)

print("Deployment and service created successfully.")
