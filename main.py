from api import Api

if __name__ == '__main__':
    api = Api()

    producttypes = api.getProductTypes()
    products = api.getProducts()
    for producttype in producttypes:
        print(producttype.id)