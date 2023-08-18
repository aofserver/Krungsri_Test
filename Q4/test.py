import pandas as pd

df = pd.read_excel('test.xlsx')

campaign_data = { "x1":"", "x2":"", "y1":"", "y2":"" }
interest_rate_data = { "x1":"", "x2":"", "y1":"", "y2":"" }

result = {
           "campaign1": {
                            "data": []
                        },
           "interrest":[]
        }



# campaign
for index,row in enumerate(df.values.tolist()):
    if "campaign1" in row:
        setx = 0
        for idx,r in enumerate(row):
            if str(r) != "nan":
                setx = idx 
                break
        campaign_data["y1"] = index
        campaign_data["x1"] = 0 + setx
        row = [x for x in row if str(x) != 'nan']
        campaign_data["x2"] = len(row) + setx

    if isinstance(campaign_data["y1"], int) and str(row[setx]) == "nan":
        campaign_data["y2"] = index
        break
# print(campaign_data)
campaign = df.iloc[campaign_data["y1"]:campaign_data["y2"], campaign_data["x1"]:campaign_data["x2"]].values.tolist()
# print(campaign)

# append campaign
for index,row in enumerate(campaign):
    if index == 0:
        remark_idx = row.index('remark')
        effdate_idx = row.index('effdate')
        filename_idx = row.index('filename')
    else:
        data = {
            "filename": row[filename_idx],
            "effdate": row[effdate_idx],
            "remark": row[remark_idx]
        }
        result["campaign1"]["data"].append(data)

    
    


# interest rate
for index,row in enumerate(df.values.tolist()):
    if "interest rate" in str(row[0]):
        interest_rate_data["y1"] = index
        interest_rate_data["x1"] = 0
        row = [x for x in row if str(x) != 'nan']
        interest_rate_data["x2"] = len(row)
    if (isinstance(interest_rate_data["y1"], int) and str(row[0]) == "nan") or index == len(df.values.tolist())-1:
        interest_rate_data["y2"] = index + 1
        break
interest_rate = df.iloc[interest_rate_data["y1"]:interest_rate_data["y2"], interest_rate_data["x1"]:interest_rate_data["x2"]].values.tolist()
# print(interest_rate)

# append interest_rate
result["interrest"] = interest_rate






print(result)
