from openai import OpenAI
from get_pod_info import get_pod_info
from get_events import get_events

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=""
)


def analyze_pod(pod_name):
    print("Step 1 - Getting pod info")
    status, restarts = get_pod_info(pod_name)

    print("Step 2 - Getting events")
    events = get_events(pod_name)

    print("Step 3 - Building prompt")

    prompt = f"""
You are a Senior Kubernetes SRE.

Analyze the following Kubernetes issue.

Pod Name: {pod_name}
Status: {status}
Restart Count: {restarts}

Events:
{events}

Provide:

1. Root Cause
2. Evidence
3. Recommended Fix
"""

    print("Step 4 - Calling OpenRouter")

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("Step 5 - OpenRouter returned")

    return response.choices[0].message.content


if __name__ == "__main__":
    print("===================================")
    print(" Kubernetes AI SRE Agent Started ")
    print("===================================")

    pod_name = "crash-demo"

    try:
        result = analyze_pod(pod_name)

        print("\n===== AI ANALYSIS =====")
        print(result)

    except Exception as e:
        print(f"\nERROR: {e}")