import pymysql
con=pymysql.connect(host='bsdd0rpqqz9qvrkzcnhr-mysql.services.clever-cloud.com',user='uyu0gdfgiasqmkeq',password='12RKXpmWmMEOS2cDWJA5',database='bsdd0rpqqz9qvrkzcnhr')

curs=con.cursor()
curs.execute("select * from pharma")
data=curs.fetchone()
print(data)
# con.close()
print("-"*30)
rec=curs.fetchone
while rec:
    print(rec)
    rec=curs.fetchone()

con.close()    