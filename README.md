# 🚀 Step Functions — Kill Your Glue Lambdas

This repository demonstrates how AWS Step Functions can evolve from a Lambda-heavy orchestration into a clean, data-driven workflow using JSONata, HTTP integration, and EventBridge Connections.

---

# 📦 Workflows Overview

## 🟦 `lambda_heavy_flow`

Classic serverless orchestration approach.

### What it does:

* Each step is implemented as a separate Lambda
* Responsibilities include:

  * Transform input
  * Validate data
  * Enrich payload
  * Build API request
  * Fetch bearer token
  * Call external API
  * Persist result

### Key takeaway:

* Highly modular
* But introduces:

  * Multiple deployments
  * Distributed logic
  * Increased operational overhead

---

## 🟦 `jsonata_transform`

Same business flow — **without Lambdas**.

### What it does:

* Replaces Lambda logic with Step Functions capabilities:

  * JSONata → data transformation, enrichment, request building
  * HTTP state → direct API calls
  * EventBridge Connection → authentication handling
  * DynamoDB integration → persistence

### Key takeaway:

* Same pipeline
* Fewer moving parts
* Reduced complexity

---

## 🟦 `users_aggregate`

Aggregates a list of users into grouped summaries — **without Lambdas**.

### What it does:

* Fetches users from an external HTTP endpoint
* Projects raw user objects into a simplified internal shape
* Builds aggregate views by:

  * Company
  * Age bucket
  * Blood group
* Persists each aggregate directly into DynamoDB using Step Functions service integrations

### Key takeaway:

* Demonstrates that Step Functions can do more than orchestration
* Shows how JSONata can be used for lightweight aggregation and shaping
* Useful for simple analytical or reporting-style workflows without adding Lambda glue

---

# ⚙️ Deployment (AWS SAM)

This project uses **AWS SAM** for deployment.

## 🧰 Prerequisites

* AWS CLI configured
* AWS SAM CLI installed

👉 Official docs:
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html

---

## 🏗️ Build

```bash
sam build
```

---

## 🚀 Deploy

```bash
sam deploy --guided
```

---

# 🔐 Important — EventBridge Connection

The `jsonata_transform` workflow uses **HTTP state with authentication**.

⚠️ Before deploying, you must:

1. Manually create an **EventBridge Connection** in AWS Console
2. Copy its ARN
3. Provide it as a parameter during deployment

Example:

```bash
ConnectionArn=arn:aws:events:eu-west-1:123456789012:connection/your-connection-id
```

---

# 🧠 Notes

* JSONata states replace multiple “glue” Lambdas
* Execution input is passed directly to Step Functions
* `requestId` is derived from Step Functions execution context
* DynamoDB is used for persistence via direct integration

---

# 💡 Philosophy

> This project is not about removing Lambdas everywhere —
> it’s about removing the ones you don’t need.

---

# 📎 Resources

* Step Functions JSONata:
  https://docs.aws.amazon.com/step-functions/latest/dg/transforming-data.html

* HTTP integration:
  https://docs.aws.amazon.com/step-functions/latest/dg/call-https-apis.html

* AWS SAM:
  https://docs.aws.amazon.com/serverless-application-model/

---

# 👋 Final Thought

If you're writing a Lambda just to transform JSON...

**you probably don’t need a Lambda.**
