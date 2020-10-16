from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="+5216671370966",
    from_="+19549519574",
    body="This is a test message!"
)
