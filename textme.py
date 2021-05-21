from twilio.rest import Client 
 
#enter account sid and auth token provided from twilio 
account_sid = '' 
auth_token = ''  
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG564fd6ec84f8b023f15c307a85e573ee',
                              body='Hello from Message Bot',   # enter your message here      
                              to='' #enter your number here
                          ) 
 
print(message.sid)