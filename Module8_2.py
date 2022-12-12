import pandas as pd
from sqlalchemy import create_engine
import pymysql
import numpy as np 
import mysql.connector
import matplotlib.pyplot as plt

pd.set_option('use_inf_as_na',True)

# create connection
connection = mysql.connector.connect(host='localhost',
                             user='root',
                             password='ayerram',
                             database='mrts',
                             auth_plugin='mysql_native_password')



sql = ("""
select  
str_to_date(CAST(CONCAT('01-' , left(`NAICS  Code` , 3) , '-' , right(`NAICS  Code` , 4) ) as CHAR) ,'%d-%b-%Y') as dte,
 `441` as 	'Motor vehicle and parts dealers' ,`442` as 'Furniture and home furnishings stores' , 
`443` as 'Electronics and appliance stores' , `444` as 'Building mat. and garden equip. and supplies dealers' , 
`445` as 'Food and beverage stores' , `446` as	'Health and personal care stores' , `447` as 'Gasoline stations' , `448` as 'Clothing and clothing access. stores' , 
`451` as 'Sporting goods, hobby, musical instrument, and book stores' , `452` as 'General merchandise stores' , `453` as 'Miscellaneous store retailers' ,
`454` as 'Nonstore retailers' , `722`	as 'Food services and drinking places'
from mrts_sales_bymonth
order by dte ;
""")



result_df = pd.read_sql(sql,connection)

# Close the connection
connection.close()




# plotting a line plot after changing it's width and height
f = plt.figure()
f.set_figwidth(30)
f.set_figheight(10)

# Plotting all the curves simultaneously
plt.plot(result_df['dte'],result_df["Motor vehicle and parts dealers"],color='b',label='MotorVehicle')
plt.plot(result_df['dte'],result_df["Furniture and home furnishings stores"],color='r',label='Furniture')
plt.plot(result_df['dte'],result_df["Electronics and appliance stores"],color='g',label='Electronics')
plt.plot(result_df['dte'],result_df["Health and personal care stores"],color='c',label='Health')
plt.plot(result_df['dte'],result_df["Food and beverage stores"],color='y',label='Food')
plt.plot(result_df['dte'],result_df["General merchandise stores"],color='m',label='General')
plt.plot(result_df['dte'],result_df["Food services and drinking places"],color='k',label='Food Services')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("TimePeriod")
plt.ylabel("Magnitude")
plt.title("Retail and Food Sale trend")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()


  
# To load the display window
plt.show()


