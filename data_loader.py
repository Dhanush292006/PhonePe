import pandas as pd
import requests

def load_data():
    states = ["andhra-pradesh", "karnataka", "tamil-nadu", "maharashtra"]
    years = [2018, 2019, 2020]

    data_list = []

    for state in states:
        for year in years:
            for quarter in [1,2,3,4]:
                try:
                    url = f"https://raw.githubusercontent.com/PhonePe/pulse/master/data/aggregated/transaction/country/india/state/{state}/{year}/{quarter}.json"
                    
                    response = requests.get(url)
                    data = response.json()

                    for item in data['data']['transactionData']:
                        data_list.append({
                            "state": state,
                            "year": year,
                            "quarter": quarter,
                            "category": item['name'],
                            "amount": item['paymentInstruments'][0]['amount'],
                            "count": item['paymentInstruments'][0]['count']
                        })
                except:
                    continue

    return pd.DataFrame(data_list)
