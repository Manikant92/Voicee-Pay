# Voicee Pay
Building the Best Digital Banking system of the Future

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


## 🤔 How to login to Django
How to use Django.

- Open [Django Admin Page](https://sandy-voicee-pay-django.azurewebsites.net/admin/login) and use the below credentials to login

- Username - citi-bank-judges
- Email Address - citi-bank-judges@voiceepay.com
- Password - 2hZL44QcphpZKCb


## 🤔 How to view the React Dashboard

- Open [React Dashboard](https://sandy-voicee-pay-react.azurewebsites.net/dashboard)

- Click on the refresh button at the right-hand corner of the screen to get the real-time update through GraphQL.

## ⚙ How to test Google DialogFlow 
- Install Skype (we need this because we have a US based Toll Free number)
- Call `+1 833-208-4225`
- A bot will welcome you
- Ask `mera sitee kaard kaise blok karen` (you can use any from the intents in the Google DialogFlow)
- It would give you an answer and ask for a feedback
- Respond `achchha`
- This will be recorded in the database via a callback function in Google DialogFlow
- Check the Feedbacks tab in the Django Administration page [here](https://sandy-voicee-pay-django.azurewebsites.net/admin/transaction/feedback/)

## ⚙ How to test USSD
- Open [Africa Talking Simulator - No login required](https://developers.africastalking.com/simulator)
- Use (if you get `Failed to launch. Kindly try again.` wait for sometime and try again.)
- Once in, pick the language of your choice (not working - Kannada,Telugu - the language phrases are yet to be updated)
- Enter 1, you'll be presented with the balance of your account. This can be verified in the Django Admin Dashboard
- Click call again, and select the language and enter 2.
- Enter 1080-1376-6276-8838,100 and you'll be presented with the result of the transaction. This can also be verified in the Transaction view of the Django Admin Dashboard
 - Entering 3 will exit you out of the application with the thank you note.
- The [React Dashboard](https://sandy-voicee-pay-react.azurewebsites.net/dashboard) will be updated for every USSD action performed by the user and for every transaction made.

## 🔎 How to view Google DialogFlow work
- Open [Google DialogFlow](https://dialogflow.cloud.google.com/)
- create an agent
- Head over to the settings and click `Export and Import tab`
- Upload the agents from the `Google DialogFlow Agents folder`
- Now you'll be able to view all the intents the bot was trained on

### 🙌 Special thanks to all my friends from all over India for helping me with the language phrases
- Shanmuganathan
- Ivin Vargasee
- Aishwarya Rao
- Bratati Ganguly
- Vaishali Mane
- Chandu Sree

## ✈ Future Work
- Login page for React Dashboard
