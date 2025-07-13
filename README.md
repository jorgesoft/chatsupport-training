# Chat Support Simulator using AWS Bedrock

This CLI project simulates a chat support session with a customer using Amazon Bedrock's Claude model. It helps you practice giving support in English while getting grammar feedback.

---

## 🧩 Features
- Role-play as a support agent helping a non-technical customer
- Grammar/spelling feedback after each response
- Chat ends after 10 messages or when the issue is resolved

---

## 📁 Setup Instructions

### 1. Clone and configure
Update the `config.yaml` file with your AWS credentials:

```yaml
aws_access_key_id: YOUR_ACCESS_KEY
aws_secret_access_key: YOUR_SECRET_KEY
region: us-east-1
```

> ⚠️ **Important:** Never commit your `config.yaml` file to source control.

---

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run
```bash
python main.py
```

---

## 💬 Commands
- Type your answers as if you're helping a customer.
- Type `exit` to manually quit the chat at any time.
- The conversation will automatically end if:
  - You reach 10 turns, or
  - The customer says: `Issue is resolved.`

---

## 📝 Prompt Format (used internally)
```
English Feedback: [feedback on your grammar]

Customer Answer: [response to your help]
```

---

## 📌 Notes
- You must have access to Amazon Bedrock and the `InvokeModel` permission.
- Claude v2 is used by default, but you can modify the model in `main.py`.

### Example IAM Policy
Use the following minimal policy to allow your IAM user to access Bedrock:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "bedrock:InvokeModel",
      "Resource": "*"
    }
  ]
}
```

---

Happy learning! 🧠💬
