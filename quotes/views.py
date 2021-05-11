from django.shortcuts import render, redirect
from .models import Stock, Stock2, PredictPrice
from .forms import StockForm
from django.contrib import messages
import requests
import json
# Create your views here.
def home(request):
	# pk_f0a1fda23c3c488eb225ff706860875b	
	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_f0a1fda23c3c488eb225ff706860875b")
	# api_request = requests.get("https://cloud-sse.iexapis.com/stable/stock/AAPL/quote?token=pk_f0a1fda23c3c488eb225ff706860875b")
	# api_request = requests.get("https://cloud-sse.iexapis.com/stable/stock/twtr/quote/latestPrice?token=pk_f0a1fda23c3c488eb225ff706860875b")
	# api_request = requests.get("https://cloud-sse.iexapis.com/stock/twtr/chart/date/20190220?chartByDay=true?token=pk_f0a1fda23c3c488eb225ff706860875b")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {'api':api})

	else:
		return render(request, 'home.html', {'ticker':"Enter a Ticker Symbol above"})

def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_f0a1fda23c3c488eb225ff706860875b")
	# api_request = requests.get("https://cloud-sse.iexapis.com/stable/stock/AAPL/quote?token=pk_f0a1fda23c3c488eb225ff706860875b")
	# api_request = requests.get("https://cloud-sse.iexapis.com/stable/stock/twtr/quote/latestPrice?token=pk_f0a1fda23c3c488eb225ff706860875b")
	# api_request = requests.get("https://cloud-sse.iexapis.com/stock/twtr/chart/date/20190220?chartByDay=true?token=pk_f0a1fda23c3c488eb225ff706860875b")

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})

def predict(request):
	stocks = Stock2.objects.order_by('company')[0:3]
	# stocks = Stock2.objects.all()
	print(stocks)
	exit()
	top_stock_dict = {}
	model_types = ["LSTM", "RNN"]
	for stock in stocks:
		top_stock_dict[stock] = {}
		for model_type in model_types:
			top_stock_dict[stock][model_type] = stock.price_set.filter(model_type = model_type).order_by("-date")[:5]
	
	print(top_stock_dict)

	return render(request, "predict.html", {"top_stocks_dict": top_stock_dict})
	# return render(request, "predict.html", {})

# def predict(request):
#     stocks = Stock2.objects.order_by('company')[0:4]
    
#     top_stock_dict = {}
#     model_types = ["LSTM", "RNN", "COMB"]
#     for stock in stocks:
#         top_stock_dict[stock] = {}
#         for model_type in model_types:
#             top_stock_dict[stock][model_type] = stock.price_set.filter(model_type = model_type).order_by("-date")[:5]
#     exit()
#     print(top_stock_dict)
    
#     return render(request, "app/predict.html", {"top_stocks_dict": top_stock_dict})