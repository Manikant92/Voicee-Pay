# 💵 Voicee Pay - Banking for all
Building the Best Digital Banking system for all

## 🧵 Architecture Diagram
![Architecture Diagram](/images/architecture-diagram-flow.png)

## 🛠 Tech Stack
- Django
- React
- GraphQL
- Docker
- Kubernetes
- Africa Talking USSD Service
- Google DialogFlow Phone Gateway
- Azure Web Apps
- Azure Container Registry

## 📌 Points to remember
- It takes some time to spin up both the React and Django containers if you're clicking the link for the `first time` or after a `long pause` so the the link might take around a minute to show both the **`React Dashboard and Django Admin Page`**
- You need to create a bank account so that it can be linked to the customer (first create the bank account and then add it to the customer) - Just incase you want to create a new customer
- Have the Django Admin Page up before calling the Google DialogFlow Phone Gateway number because if the Django container is not running the webhook from DialogFlow will not be captured
- Reach out to `santhoshkdhana@gmail.com` for clarifications

### 🙌 Special thanks to all my friends from all over India for helping me with the language phrases
- Shanmuganathan
- Ivin Varghese
- Aishwarya Rao
- Bratati Ganguly
- Vaishali Mane
- Chandu Sree

## ✈ Future Work
- Add more languages to the USSD service
- Add more intents to Google DialogFlow agent
- Login page for React Dashboard
- Spin up Postgres for storage
- Deploy Django and React containers to Kubernetes
- Better error handling for USSD sessions


## 🔦 Some snaps

## Django
![Django Admin Dashboard](/images/admin-customers.png)
![GraphQL View](/images/graphql-dashboard.png)

## React
![React Real-time Dashboard](/images/dashboard-with-data.png)

## Google DialogFlow
![Google DialogFlow Intent view](/images/payment-view.png)

## Talking Africa
![Mobile Simulator](/images/USSD-usage-3.png)
![Mobile Simulator](/images/USSD-usage-result-exit.png)