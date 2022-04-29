
import pymysql

con=pymysql.connect(host='bsdd0rpqqz9qvrkzcnhr-mysql.services.clever-cloud.com',user='uyu0gdfgiasqmkeq',password='12RKXpmWmMEOS2cDWJA5',database='bsdd0rpqqz9qvrkzcnhr')

curs=con.cursor()
curs.execute("select * from pharma")
data=curs.fetchall()
print(data)
con.close()