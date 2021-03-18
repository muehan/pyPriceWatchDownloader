import sys
from api import Api
from exporter import Exporter
from datetime import datetime, timedelta

if __name__ == '__main__':
    api = Api()
    exporter = Exporter()

    producttypes = api.getProductTypes()
    products = api.getProducts()
    exporter.productExport(products, producttypes)

    daysToSubtract = 0
    if len(sys.argv) > 1:
        daysToSubtract = sys.argv[1]

    dateStr = (datetime.today() - timedelta(days=int(daysToSubtract))).strftime('%Y-%m-%d')
    prices = api.getPricesFromDate(dateStr)
    exporter.exportPrices(prices, dateStr)