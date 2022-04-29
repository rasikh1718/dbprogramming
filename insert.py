import pymysql
mednm=input('Enter the name of medicine :')
type=input('Enter the type such as drop,syp,crm,tab :')
bno=int(input('Enter batch no :'))
exp=input('Entr the expiry :')
mrp=float(input('Enter the mrp of product :')) 

con=pymysql.connect(host='bsdd0rpqqz9qvrkzcnhr-mysql.services.clever-cloud.com',user='uyu0gdfgiasqmkeq',password='12RKXpmWmMEOS2cDWJA5',database='bsdd0rpqqz9qvrkzcnhr')
print("insert into pharma values('%s','%s','%d','%s',%.2f)" %(mednm,type,bno,exp,mrp))

curs=con.cursor()

try:
    curs.execute("insert into pharma values('%s','%s','%d','%s',%.2f)" %(mednm,type,bno,exp,mrp))
    con.commit()
    print('medicine added successfully')
except Exception as e:
    print('Data insert failed - ',e)
con.close()
