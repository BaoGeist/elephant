#you start here
def calcTax(price: int):
    return price*0.13



#i start here
def calc_tax_on(total_price):
    return total_price * 0.13

def calc_tax_all(total_price, province):
    dic_prov = {"ON": 0.13, "QC": 0.14975, "MB":0.05, "NS":0.15, "BC":0.05}
    return total_price*dic_prov[province]

def breakdown_sales(total_price):
    stor = calcSales(total_price)
    print("Total Price" + total_price)
    print("Total Discount" + )

