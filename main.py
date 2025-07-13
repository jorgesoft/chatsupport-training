import boto3
import json
import yaml
from prompts.chat_prompt import build_prompt

# Load AWS credentials from config.yaml
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

bedrock = boto3.client(
    "bedrock-runtime",
    aws_access_key_id=config["aws_access_key_id"],
    aws_secret_access_key=config["aws_secret_access_key"],
    region_name=config["region"]
)

def send_to_bedrock(user_message, history):
    prompt = build_prompt(user_message, history)
    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": 500
        })
    )
    output = json.loads(response["body"].read())
    return output["completion"]

def main():
    history = ""
    message_count = 0
    print("🛠️ Welcome to the Support Chat Simulator\n")

    print("Client: Hi, I'm having trouble connecting to the Wi-Fi.")
    history += "Client: Hi, I'm having trouble connecting to the Wi-Fi.\n"

    while message_count < 10:
        user_input = input("You: ")
        history += f"You: {user_input}\n"

        reply = send_to_bedrock(user_input, history)
        print(f"Client: {reply.strip()}\n")

        history += f"Client: {reply.strip()}\n"
        message_count += 1

        if "issue is resolved" in reply.lower():
            print("✅ The client considers the issue resolved. Good job!\n")
            break

    print("💬 Chat ended.")

if __name__ == "__main__":
    main()
