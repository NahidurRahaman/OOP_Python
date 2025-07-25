class phone:
    manufactured = 'china'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'sending to: {self.owner} {self.brand}'
        print(text)

my_phone = phone('nahid','oppo',98000)
print(my_phone.brand, my_phone.owner,my_phone.price)
my_phone.send_sms('samsung','calling me')