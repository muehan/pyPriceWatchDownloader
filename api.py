import requests
import json
import sys

sys.path.insert(1, 'models')
from product import Product
from productType import ProductType
from price import Price

class Api:

    def getProducts(self):
        r = requests.get('http://pricewatch.northeurope.cloudapp.azure.com/api/product')
        result = json.loads(r.text)
        
        products = []
        for pr in result:
            product = Product(
                pr["Id"],
                pr["Producttypeid"],
                pr["Productid"],
                pr["ProductidAsString"],
                pr["Name"],
                pr["Fullname"],
                pr["SimpleName"],
                pr["Date"]
            )
            products.append(product)
        return products

    def getProductTypes(self):
        r = requests.get('http://pricewatch.northeurope.cloudapp.azure.com/api/producttype')
        result = json.loads(r.text)
        
        productTypes = []
        for prType in result:
            productType = ProductType(
                prType["Id"],
                prType["Typeid"],
                prType["Name"],
            )
            productTypes.append(productType)
        return productTypes

    def getPricesFromDate(self, date):
        r = requests.get('http://pricewatch.northeurope.cloudapp.azure.com/api/price/' + date)
        result = json.loads(r.text)
        
        prices = []
        for prPrice in result:
            price = Price(
                prPrice["Id"],
                prPrice["Price"],
                prPrice["InsteadOfPrice"],
                prPrice["Date"],
                prPrice["Productid"]
            )
            prices.append(price)
        return prices