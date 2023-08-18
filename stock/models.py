from django.db import models
from model_utils import FieldTracker
from stock import signals
class Stock(models.Model):
    code = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=120)
    current_value = models.FloatField()
    #
    current_value_tracker = FieldTracker(fields=['current_value'])
    #
    def save(self, *args, **kwargs):
      #create
        if self.pk is None: 
            print('if self.pk is None : INSERT')
        else:
            print('if self.pk is NOT None : UPDATE')
            old_record=self.current_value_tracker.changed()
            if(old_record.get('current_value') !=self.current_value):
                record = StockUpdates(stock_id=1,old_value=old_record.get('current_value'), 
                                  new_value=self.current_value)
                record.save()
                signals.stock_changed_signal.send(sender=self ,code=self.code,name=self.name,
                                                  old_value=old_record.get('current_value'),new_value=self.current_value)
    
        super().save(*args, **kwargs)       
         
class StockUpdates(models.Model):
    stock = models.ForeignKey(
        "Stock", on_delete=models.CASCADE)
    old_value = models.FloatField()
    new_value = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
