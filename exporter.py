import csv

class Exporter:

    def productExport(self, products, producttypes):
        with open('products.csv', "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for product in products:
                productType = [x for x in producttypes if x.id == product.Producttypeid][0]
                writer.writerow([product.Productid, product.ProductidAsString, product.Name, product.Fullname, product.SimpleName, productType.id, productType.Typeid, productType.Name])

    def exportPrices(self, prices, dateStr):
        with open('prices-'+dateStr+'.csv', "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for price in prices:
                writer.writerow([price.Id, price.Price, price.InsteadOfPrice, price.Date, price.Productid])