from django.dispatch import receiver
from stock import signals
import time
@receiver(signals.stock_changed_signal)
def handle_stock_change(sender, code,name,old_value,new_value, **kwargs):
    message=''
    title=''
    if(old_value > new_value):
        title='Stock price Drop Alert'
        message = "Price of Stock {name}({code}) has been dropped from {old_value} to {new_value}".format(name=name,code=code,old_value=old_value,new_value=new_value) 
    else:
        title='Stock price Rise Alert'
        message = "Price of Stock {name}({code}) has been adjusted from {old_value} to {new_value}".format(name=name,code=code,old_value=old_value,new_value=new_value) 
        
    emails=["user1@gmail.com","user2@gmail.com","user3@gmail.com"]
    print('Starting Celery Task System .....')
    for email in emails:
        #In Real world, We will be executing Celery tasks
        print('Sending mail to '+email)
        print('Title: '+title)
        print('Message: '+message)
        print('--------------------------------------------')
        time.sleep(1)#Just for Demonstration
