from twilio.rest import Client 
 
account_sid = 'AC84aab39541e43904c5dfe40abc79818d' 
auth_token = '019e354d0170ed2b9b249cb3478b8ae0' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG564fd6ec84f8b023f15c307a85e573ee',
                              body='Hello from Message Bot',         
                              to='+9779800515353' 
                          ) 
 
print(message.sid)