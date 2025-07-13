# Chat Support Simulator using AWS Bedrock

This script simulates a chat support scenario using AWS Bedrock and a custom prompt.

### How to run:

Update the config.yaml file:

```
aws_access_key_id: YOUR_ACCESS_KEY
aws_secret_access_key: YOUR_SECRET_KEY
region: us-east-1
```
Run these commands: 

```
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
```