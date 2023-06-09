# CRD Kubernetes Python Operator

This is a Python-based Kubernetes Operator that manages a custom resource definition (CRD) in Kubernetes. It uses the Kopf framework to implement the operator.

## Installation and Setup

To use this operator, you should have the following prerequisites installed:

- Python 3.7 or later
- Kopf 1.36.1 or later
- Kubernetes 26.1.0 or later

To install the operator, follow these steps:

1. Clone the repository:

```
git clone https://github.com/farshadasadpour/k8s_crd_python.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Deploy the operator to your Kubernetes cluster:

### Create a Custom Resource Definition (CRD)

```
kubectl apply -f custom_resource_definition.yml
```
### Create a service account and role binding
```
kubectl apply -f service_account.yml
kubectl apply -f service_account_binding.yml
```
### Create deployment for operator in the cluster
```
kubectl apply -f nginx_operator.yml
```
### Create Test deployment
```
kubectl apply -f nginx.yml
```

## Usage

To use the operator, create a custom resource definition (CRD) in Kubernetes that defines the resources you want to manage. Then, create instances of the CRD to manage those resources.

For example, let's say you want to manage a custom resource called `MyResource`. You would define the CRD like this:

```
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: myresources.example.com
spec:
  group: example.com
  names:
    kind: MyResource
    plural: myresources
  scope: Namespaced
  version: v1alpha1
```

Then, you can create instances of the `MyResource` resource like this:

```
apiVersion: example.com/v1alpha1
kind: MyResource
metadata:
  name: myresource-1
spec:
  # Add your resource spec here
```

The operator will automatically detect and manage these resources based on the rules you define in your operator code.

## Configuration

The operator can be configured using environment variables. The following variables are available:

- `KUBECONFIG`: The path to the Kubernetes configuration file. Default is `~/.kube/config`.
- `OPERATOR_NAME`: The name of the operator. Default is `crd-k8s-python-operator`.

## Contributing

Contributions to this project are welcome! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to merge your changes back into the main repository.

## License

This project is released under the MIT license. See the LICENSE file for more information.