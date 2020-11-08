#3 siparişin toplam bilgisini hesaplayıp tutarı xml dosyasına yazma

order1 = int(input("First order price is : "))
order2 = int(input("Second order price is : "))
order3 = int(input("Third order price is : "))

ordersTotal = order1 + order2 + order3
#print(f"Orders total is : {ordersTotal}")

f = open("orderTotalOutput.xml","w")
f.write(str(ordersTotal))
with open("orderTotalOutput.xml","r") as f:
    print(f.read())