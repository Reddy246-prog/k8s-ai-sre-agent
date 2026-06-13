from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

logs = v1.read_namespaced_pod_log(
    name="crash-demo",
    namespace="default"
)

print(logs)