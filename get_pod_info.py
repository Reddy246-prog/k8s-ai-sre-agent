import subprocess
import json

def get_pod_info(pod_name):
    cmd = f"kubectl get pod {pod_name} -o json"
    output = subprocess.check_output(cmd, shell=True)

    pod = json.loads(output)

    phase = pod["status"]["phase"]

    restarts = 0
    for container in pod["status"].get("containerStatuses", []):
        restarts += container.get("restartCount", 0)

    return phase, restarts


if __name__ == "__main__":
    phase, restarts = get_pod_info("crash-demo")
    print(f"Phase: {phase}")
    print(f"Restarts: {restarts}")