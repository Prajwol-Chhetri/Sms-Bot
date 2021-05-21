from twilio.rest import Client 
 
#enter account sid and auth token provided from twilio 
account_sid = '' 
auth_token = ''  
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='', # enter sid here
                              body='Hello from Message Bot',   # enter your message here      
                              to='' #enter your number here
                          ) 
 
print(message.sid)
