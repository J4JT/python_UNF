import random
class CreditCard:

  cardnum:str
  name:str
  expiration_date:str
  credit_limit:int
  balance:int
  card_type:str
  cards = {1:'visa', 2:'master', 3:'amex', 4:'Discover'}

 
  def __init__(self,cardnum, name, expiration_date):
    self.cardnum=cardnum
    self.name=name
    self.expiration_date=expiration_date
    self.credit_limit=1000
    self.balance=random.randint(0, 1000)
    
    temp=cardnum[5]
    if (temp=='1'):
     self.card_type='visa'
    elif (temp=='2'):
     self.card_type='master'
    elif (temp=='3'):
     self.card_type='amex'
    elif (temp=='4'):
     self.card_type='discover'
    else:
     self.card_type='none'
  #setters  
  def setCard(self,card_type):
    self.card_type=card_type
  def setName(self,name):
    self.name=name
   #getters 
  def get_cardOwner(self):
    return self.name
  def get_cardNum(self):
   return self.cardnum
  def get_expiration(self):
   return self.expiration_date
  def get_cardType(self):
    if (self.card_type =='none'):
     return 'Not Supported Card Type'
    else:
     return self.card_type
  def processOrder(self,price):
    if(self.balance + price < self.credit_limit):
      return True
    else: 
      return False
  def __str__(self):
   if(type(self) == CreditCard):
    result='{} is the owner of the credit card with the number {} which expires on {}'.format(self.name,self.cardnum,self.expiration_date)
    return result
   else:
    return self
  