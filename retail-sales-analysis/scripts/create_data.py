import pandas as pd

data = [
    [1,"Amit","Delhi","Laptop","Electronics",50000,1,"2024-01-10","COD",10,4],
    [2,"Riya","delhi","Phone","Electronics",20000,2,"2024-01-11","Card",5,5],
    [3,"Rahul","Mumbai","Shirt","Fashion",1500,3,"2024-01-12","Cash",0,3],
    [4,"Amit","DELHI","Laptop","Electronics",50000,1,"2024-01-10","COD",10,4],
    [5,"Sneha","","Shoes","Fashion",3000,2,"2024-01-13","UPI",15,None],
    [6,"Arjun","Bangalore","Watch","Accessories","2000rs",1,"2024-01-14","COD",0,4],
    [7,"Riya","Mumbai","Phone","Electronics",20000,0,"2024-01-15","Card",5,5],
    [8,"Karan","Chennai","Tablet","Electronics",15000,1,"2024-01-16","Cash",10,2]
]

columns = ["Order_ID","Customer_Name","City","Product","Category","Price","Quantity","Order_Date","Payment_Method","Discount","Rating"]

df = pd.DataFrame(data, columns=columns)

# CSV file create
df.to_csv("sales_data.csv", index=False)

print("CSV file created successfully")