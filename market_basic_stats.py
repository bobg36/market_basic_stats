import requests
import json
from datetime import datetime
import os
import marketFunctions as mf
import time, datetime

os.chdir(r'C:\Users\bobgu\Desktop\Axie Data\market overview over time')

while True:
    try:
        SLP = 'smooth-love-potion'
        AXS = 'axie-infinity'
        ETH = 'ethereum'
        datetime = mf.get_date_time()
        try:
            volAxieCount = mf.get_volume_axieCount()
        except:
            volAxieCount = [1, 1]

        date = datetime[1]
        time1 = datetime[0]
        priceETH = mf.get_price(ETH)
        priceAXS_raw = mf.get_price(AXS)
        priceAXS_split = str(priceAXS_raw).split(".")
        if(len(priceAXS_split[1]) == 1):
            priceAXS = float(str(priceAXS_raw) + "0")
        else:
            priceAXS = priceAXS_raw
        priceSLP = mf.get_price(SLP)
        try: 
            allCount = mf.get_allCount()
        except:
            allCount = 1
        try:
            eggCount = mf.get_eggCount()
        except:
            eggCount = 1
        try:
            saleCount = mf.get_saleCount()
        except:
            saleCount = 1
        volume = volAxieCount[0]
        axieCount = volAxieCount[1]
        floorPrice = mf.get_floorPrice()
        averagePriceStr = str(int(volume)/int(axieCount))
        averagePrice = float(averagePriceStr[0:5])
        dollarFloor = floorPrice*priceETH
        dollarAverage = averagePrice*priceETH
        avgflr = averagePrice/floorPrice
        salePercent = str(saleCount*100/allCount)[:4]+"%"
        eggPercent = str(eggCount*100/allCount)[:4]+"%"
        eth1 = (1*priceAXS*0.5 + 600*priceSLP*3)/priceETH
        eth2 = (1*priceAXS*0.5 + 900*priceSLP*3)/priceETH
        eth3 = (1*priceAXS*0.5 + 1500*priceSLP*3)/priceETH
        eth4 = (1*priceAXS*0.5 + 2400*priceSLP*3)/priceETH
        eth5 = (1*priceAXS*0.5 + 3900*priceSLP*3)/priceETH
        eth6 = (1*priceAXS*0.5 + 6300*priceSLP*3)/priceETH
        eth7 = (1*priceAXS*0.5 + 10200*priceSLP*3)/priceETH

        f = open('market_overview.csv', 'a') 
        f.write(str(date) + "," + str(time1) + "," + str(priceETH) + "," + str(priceAXS) + "," + str(priceSLP) + "," + str(allCount) + "," + str(eggCount) + "," + str(saleCount) + "," + str(volume) + "," + str(axieCount) + "," + str(floorPrice) + "," + str(averagePrice) + "," + str(dollarFloor) + "," + str(dollarAverage) + "," + str(avgflr) + "," + str(salePercent) + "," + str(eggPercent) + "," + str(eth1) + "," + str(eth2) + "," + str(eth3) + "," + str(eth4) + "," + str(eth5) + "," + str(eth6) + "," + str(eth7) + "\n")
        f.close()

        print(str(time1) + "|" + str(priceETH)[:6]+"|"+str(priceAXS)[:4]+"|"+str(priceSLP)[:9]+"| "+str(volume)[:-2]+","+str(axieCount)+"| "+ str(floorPrice)[:6]+","+str(averagePrice)[:6]+" |"+"$"+str(dollarFloor)[:4] + "," +"$"+str(dollarAverage)[:3]+ "| "+ str(eth1)[:6] + "," + str(eth2)[:6] + "," + str(eth3)[:6] + "," + str(eth4)[:6] + "," + str(eth5)[:6] + "," + str(eth6)[:6] + "," + str(eth7)[:6])
        time.sleep(1800)

    except:
        print('api LAG')
    