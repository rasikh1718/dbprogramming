
import pymysql
con=pymysql.connect(host='bsdd0rpqqz9qvrkzcnhr-mysql.services.clever-cloud.com',user='uyu0gdfgiasqmkeq',password='12RKXpmWmMEOS2cDWJA5',database='bsdd0rpqqz9qvrkzcnhr')

curs=con.cursor()
medtype=input("Enter the type of medicine such as for tablet=tab drop=drop syrup=syp cream=crm rotacap=rotcp  :")
try:
    curs.execute("select * from pharma where medtype='%s'"%medtype)
    data=curs.fetchone()
    while data:
        print(data)
        data=curs.fetchone()

except Exception as e:
    print("type does'nt exist ",e)
con.close()        