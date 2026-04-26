import pandas as pd

df = pd.DataFrame({
    "hours":[1,2,3,4,5,6,7,8],
    "pass":[0,0,0,1,1,1,1,1]
})

df.to_csv("data/data.csv",index=False)
print("data created ")