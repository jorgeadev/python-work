

from twilio.rest import Client

# Your Account SID from twilio.com/console
#account_sid = "ACe066677a14faa5f2df06cac1c7644cca"
account_sid = "ACe066677a14faa5f2df06cac1c7644cca"
# Your Auth Token from twilio.com/console
#auth_token  = "your_auth_token"
auth_token  = "6ba15eb9eaa7796a40f8ab9ae22922d0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+527222692537",
    from_="+12028757564",
    body="Vito dime a ver que es lo que te llegó con este mensaje")

print(message.sid)