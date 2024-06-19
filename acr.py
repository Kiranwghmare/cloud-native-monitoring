import subprocess


def acr_login(acr_name):
    try:
        # Retrieve ACR login server using Azure CLI command
        result = subprocess.run(['az', 'acr', 'show', '--name', acr_name, '--query', 'loginServer', '--output', 'tsv'],
                                capture_output=True, text=True)
        acr_login_server = result.stdout.strip()  # Extract and clean up output

        # Docker login to ACR using the retrieved login server
        subprocess.run(['docker', 'login', acr_login_server])

        return acr_login_server  # Return the ACR login server URL
    except subprocess.CalledProcessError as e:
        # Handle specific error for Azure CLI command execution
        print(f"Error: Failed to retrieve ACR login server for '{acr_name}':")
        print(e.output)  # Print detailed error output for debugging
        return None
    except Exception as e:
        # Handle general exception, such as network issues or unexpected errors
        print(f"Error: {e}")  # Print generic error message
        return None


def tag_and_push_image(image_name, acr_login_server):
    try:
        # Tag Docker image with ACR repository information
        docker_tag = f"{acr_login_server}/{image_name}:latest"
        subprocess.run(['docker', 'tag', f"{image_name}:latest", docker_tag])

        # Push Docker image to ACR repository
        subprocess.run(['docker', 'push', docker_tag])

        print(f"Successfully pushed Docker image '{image_name}' to ACR '{acr_login_server}'")
    except subprocess.CalledProcessError as e:
        # Handle error specific to Docker commands execution
        print(f"Error: Failed to tag or push Docker image '{image_name}' to ACR '{acr_login_server}':")
        print(e.output)  # Print detailed error output for debugging
    except Exception as e:
        # Handle general exception, such as network issues or unexpected errors
        print(f"Error: {e}")  # Print generic error message


def main():
    # Replace 'your_acr_name' with your Azure Container Registry (ACR) name
    acr_name = 'your_acr_name'

    # Replace 'my-flask-app' with your Docker image name
    image_name = 'my-flask-app'

    # Attempt to log in to ACR and retrieve the ACR login server URL
    acr_login_server = acr_login(acr_name)
    if acr_login_server:
        # If ACR login is successful, tag and push the Docker image to ACR
        tag_and_push_image(image_name, acr_login_server)


if __name__ == "__main__":
    main()
