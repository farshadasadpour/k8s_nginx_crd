import kopf
import kubernetes
import yaml


@kopf.on.create('f4rsh4d.io', 'v1', 'nginx')
def create_fn(body, spec, **kwargs):
    # Get info from nginx object
    name = body['metadata']['name']
    namespace = body['metadata']['namespace']
    nodeport = spec['nodeport']
    image = 'nginx:1.14.2'
    port = 8080
    if not nodeport:
        raise kopf.HandlerFatalError(f"Nodeport must be set. Got {nodeport}.")

        # Pod template
    pod = {'apiVersion': 'v1', 'metadata': {'name': name, 'labels': {'app': 'nginx'}},
           'spec': {'containers': [{'image': image, 'name': name}]}}

    # Service template
    svc = {'apiVersion': 'v1', 'metadata': {'name': name}, 'spec': {'selector': {'app': 'nginx'}, 'type': 'NodePort',
                                                                    'ports': [{'port': port, 'targetPort': port,
                                                                               'nodePort': nodeport}]}}

    # Make the Pod and Service the children of the grafana object
    kopf.adopt(pod, owner=body)
    kopf.adopt(svc, owner=body)

    # Object used to communicate with the API Server
    api = kubernetes.client.CoreV1Api()

    # Create Pod
    obj = api.create_namespaced_pod(namespace, pod)
    print(f"Pod {obj.metadata.name} created")

    # Create Service
    obj = api.create_namespaced_service(namespace, svc)
    print(f"NodePort Service {obj.metadata.name} created, exposing on port {obj.spec.ports[0].node_port}")

    # Update status
    msg = f"Pod and Service created for nginx object {name}"
    return {'message': msg}


@kopf.on.delete('f4rsh4d.io', 'v1', 'nginx')
def delete(body, **kwargs):
    msg = f"Nginx {body['metadata']['name']} and its Pod / Service children deleted"
    return {'message': msg}