import requests
import json
from datetime import datetime
import os

os.chdir(r'C:\Users\bobgu\Desktop\Axie Data\market overview over time')

axie_endpoint = "https://graphql-gateway.axieinfinity.com/graphql"

#returns [volume, axieCount]
def get_volume_axieCount():
  payload = {
    "operationName": "GetOverviewToday",
    "query": "query GetOverviewToday {\n  marketStats {\n    last24Hours {\n      ...OverviewFragment\n      __typename\n    }\n    last7Days {\n      ...OverviewFragment\n      __typename\n    }\n    last30Days {\n      ...OverviewFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment OverviewFragment on SettlementStats {\n  count\n  axieCount\n  volume\n  volumeUsd\n  __typename\n}\n"
    }
  r = requests.post(axie_endpoint, json=payload)
  response = json.loads(r.text)
  axieCount = response["data"]["marketStats"]["last24Hours"]["axieCount"]
  volumeDayRaw = response["data"]["marketStats"]["last24Hours"]["volume"]
  volumeDayLen = len(str(volumeDayRaw))
  sigfig = volumeDayLen - 17
  volumeDayTimes10 = volumeDayRaw[:sigfig]
  volumeDay = int(volumeDayTimes10)/10

  return [volumeDay, axieCount]


#returns [date, time]
def get_date_time():
  now = datetime.now()
  current_time = now.strftime("%H:%M")
  current_date = now.strftime("%D")
  return [current_time, current_date]

def get_price(token_name):
  coinreq = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + token_name + "&vs_currencies=usd",  headers = {"accept":"application/json"})
  coinname = token_name
  coinprice = coinreq.json()[token_name]['usd']
  return(coinprice)


def get_saleCount():
  payload = {
  "operationName": "GetAxieBriefList",
  "variables": {
    "from": 0,
    "size": 24,
    "sort": "PriceAsc",
    "auctionType": "Sale",
    "criteria": {}
  },
  "query": "query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieBrief\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieBrief on Axie {\n  id\n  name\n  stage\n  class\n  breedCount\n  image\n  title\n  battleInfo {\n    banned\n    __typename\n  }\n  auction {\n    currentPrice\n    currentPriceUSD\n    __typename\n  }\n  parts {\n    id\n    name\n    class\n    type\n    specialGenes\n    __typename\n  }\n  __typename\n}\n"
  }
  r = requests.post(axie_endpoint, json=payload)
  response = json.loads(r.text)
  saleCount = response["data"]["axies"]["total"]
  return saleCount

def get_allCount():
  payload = {
  "operationName": "GetAxieBriefList",
  "variables": {
    "from": 0,
    "size": 24,
    "sort": "PriceAsc",
    "auctionType": "All",
    "criteria": {}
  },
  "query": "query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieBrief\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieBrief on Axie {\n  id\n  name\n  stage\n  class\n  breedCount\n  image\n  title\n  battleInfo {\n    banned\n    __typename\n  }\n  auction {\n    currentPrice\n    currentPriceUSD\n    __typename\n  }\n  parts {\n    id\n    name\n    class\n    type\n    specialGenes\n    __typename\n  }\n  __typename\n}\n"
  }
  r = requests.post(axie_endpoint, json=payload)
  response = json.loads(r.text)
  allCount = response["data"]["axies"]["total"]
  return allCount

def get_eggCount():
  payload = {
  "operationName": "GetAxieBriefList",
  "variables": {
    "from": 0,
    "size": 24,
    "sort": "PriceAsc",
    "auctionType": "All",
    "criteria": {
      "stages": 1
    }
  },
  "query": "query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieBrief\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieBrief on Axie {\n  id\n  name\n  stage\n  class\n  breedCount\n  image\n  title\n  battleInfo {\n    banned\n    __typename\n  }\n  auction {\n    currentPrice\n    currentPriceUSD\n    __typename\n  }\n  parts {\n    id\n    name\n    class\n    type\n    specialGenes\n    __typename\n  }\n  __typename\n}\n"
  }
  r = requests.post(axie_endpoint, json=payload)
  response = json.loads(r.text)
  eggCount = response["data"]["axies"]["total"]
  return eggCount

def get_floorPrice():
  try:
    payload = {
    "operationName": "GetAxieBriefList",
    "variables": {
      "from": 0,
      "size": 24,
      "sort": "PriceAsc",
      "auctionType": "Sale",
      "criteria": {}
    },
    "query": "query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\n  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n    total\n    results {\n      ...AxieBrief\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieBrief on Axie {\n  id\n  name\n  stage\n  class\n  breedCount\n  image\n  title\n  battleInfo {\n    banned\n    __typename\n  }\n  auction {\n    currentPrice\n    currentPriceUSD\n    __typename\n  }\n  parts {\n    id\n    name\n    class\n    type\n    specialGenes\n    __typename\n  }\n  __typename\n}\n"
    }

    r = requests.post(axie_endpoint, json=payload)

    response = json.loads(r.text)
    data = response["data"]["axies"]["results"]

    i = 0
    for item in data:
      i = i + 1
      if i == 20:
        floorPriceLen = len(item["auction"]["currentPrice"])
        sigfig = floorPriceLen - 15
        floorPricex100 = item["auction"]["currentPrice"][0:sigfig]
        floorPrice = int(floorPricex100)/1000

    return floorPrice
  except:
    return 0.01
