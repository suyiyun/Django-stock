from django.db import models

class Stock(models.Model):
	ticker = models.CharField(max_length=10)

	def __str__(self):
		return self.ticker

# class Stock(models.Model):
#     id = models.AutoField(primary_key = True)
#     # Date = models.TimeField(_(""), auto_now=False, auto_now_add=False)
#     ticker = models.CharField("Symbol", max_length=50,default="")
#     company = models.CharField("Company", max_length=50, default="Other company")

#     def __str__(self):
#         return self.company
		
class PredictPrice(models.Model):
    id = models.CharField("timestamp_symbol", max_length=50, primary_key = True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="price_set")
    price = models.DecimalField("Price", max_digits=11, decimal_places=2, default=None)
    date = models.DateTimeField("Date", auto_now=False, auto_now_add=False, default=None)
    model_type = models.CharField("model_type", max_length=20, default=None)
    
    def __str__(self):
        return "date:{};stock:{};prediction price:{}".format(self.date, self.stock, self.price)