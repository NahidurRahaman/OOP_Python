def call():
    print('calling abdur rouf')
class phone:
    price = 12000
    color = 'blues'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one persone')
    
    def send_sms(self, phone, sms):
        text = f'sending SMS to : {phone} and message: {sms}'
        return text
my_phone = phone()
print(phone.features)
call()
my_phone.call()
result = my_phone.send_sms(4123,'I forgot to miss you')
print(result)
