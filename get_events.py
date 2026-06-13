import subprocess


def get_events(pod_name):
    cmd = (
        f"kubectl get events "
        f"--field-selector involvedObject.name={pod_name} "
        f"--sort-by=.metadata.creationTimestamp"
    )

    output = subprocess.check_output(cmd, shell=True)
    return output.decode("utf-8")