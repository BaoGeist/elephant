#you start here
def main():
    items = input("input number of items: ")
    price = input("input price per item: ")
    prov = input("input province: ")
    grossPrice = int(price)*int(items)
    sale = calcSales(grossPrice)
    salesale = grossPrice-sale
    tax = calc_tax_all(salesale, prov)
    
    print("gross price: " + str(grossPrice))
    print("sale : " + str(sale))
    
    print("tax" + str(tax))
    
    
    breakdown_sales(grossPrice)
    
    breakdown_sales_tax(grossPrice, prov)
    
    

def calcSales(price):
    if price >= 1000:
        return price*0.03
    elif price >= 5000:
        return price*0.05
    elif price >= 7000:
        return price*0.07
    elif price >= 10000:
        return price*0.1
    elif price >= 15000:
        return price*0.15
    return 0

#i start here
def calc_tax_on(total_price):
    return total_price * 0.13

def calc_tax_all(total_price, province):
    dic_prov = {"ON": 0.13, "QC": 0.14975, "MB":0.05, "NS":0.15, "BC":0.05}
    return total_price*dic_prov[province]

def breakdown_sales(total_price):
    stor = calcSales(total_price)
    print("Total Price" + str(total_price))
    print("Total Discount" + str(stor))
    print("Final Price:" + str(total_price-stor))

def breakdown_sales_tax(total_price, province):
    stor = calcSales(total_price)
    tax = calc_tax_all(total_price-stor, province)
    print("Total Price" + str(total_price))
    print("Total Discount" + str(stor))
    print("Final Price After Tax:" + str(tax))

main()