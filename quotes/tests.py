from django.test import TestCase

# Create your tests here.
def test(request):
    stocks = Stock.objects.all()
    print(stocks)
    for stock in stocks:
        print(stock.symbol)
        data = yf.download(stock.symbol, period = "3y", interval = "1d")
        for pdtimestamp, price_dict in data.to_dict('index').items():
            timestamp = Timestamp(pdtimestamp, tz = 'UTC')
            stockInfo = StockInfo(
                        id = "{}_{}".format(timestamp, stock.symbol),
                        open_price = price_dict['Open'],
                        high_price = price_dict['High'],
                        low_price = price_dict['Low'],
                        close_price = price_dict['Close'],
                        adj_close_price = price_dict['Adj Close'],
                        volume = price_dict['Volume'],
                        date = timestamp
                        )
            stockInfo.stock = stock
            stockInfo.save()

    data = yf.download("ES=F", period = "5d", interval = "1d")
    return  render(request,"index.html", {"stocks":data.to_dict('index')})