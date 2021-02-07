# tool_ci
Hi this is a simple tool CI, feel free to use it.

#### What do we have here?
1. A simple 'hello from Flask' Python app, with a requirements file and tests.  
2. A Dockerfile in order to build an image from our application.  
3. A Github workflow named 'ci' - This workflow will run the tests in 'test_flask_app'.  
4. A deployment file - Used in order to pull the image (From Docker Hub) and run it on a container in Kubernetes with a loadbalancer.  

#### How does it work?
As soon as you push a commit ('master' branch only), the workflow is triggered.  
When the workflow ends, Docker Hub builds a new Docker image.  
When the user is ready, he runs the command "kubectl apply -f deployment.yaml" - This will build the pod for our Python app.

#### Step by step starting it up.
```bash
# Clone the project
git clone https://github.com/keoren3/tool_ci.git

# Push some change to master in order to see the workflow.

# apply the deployment:
kubectl apply -f deployment.yaml
# If you're using Minikube as your Kubernetes cluster, don't forget to add:
# minikube tunnel

# Enter the address:
http://0.0.0.0:5005/

# You should see: 'Hello from Python!'
```

Thank you for reading, please notify me if you find any mistakes!
