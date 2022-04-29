
import pymysql
con=pymysql.connect(host='bsdd0rpqqz9qvrkzcnhr-mysql.services.clever-cloud.com',user='uyu0gdfgiasqmkeq',password='12RKXpmWmMEOS2cDWJA5',database='bsdd0rpqqz9qvrkzcnhr')

curs=con.cursor()
mednm=input('Enter Name of Medicine  :')
print("select * from pharma where mednm='%s'"  %mednm)
curs.execute("select * from pharma where mednm='%s'"  %mednm)
data=curs.fetchone()
try:
    print('Name : %s | bno : %.2f' %(data[0],data[2]))
except:
    print('Medicine does not exist')
con.close()