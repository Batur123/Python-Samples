import pypyodbc
conn = pypyodbc.connect('Driver={SQL Server};Server=BATUR\BATUR;Database=PythonDB;Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("select * from kisiler  WHERE ID BETWEEN 0 AND 20")
records = cursor.fetchall() 
cursor.execute("select @@rowcount")
rowcount = cursor.fetchall()[0][0]

print("Toplam Kişi Sayısı: ", rowcount)
print("_________\n")
print("Kişiler\n")
print("_________\n")
for row in records:

        print("ID = ", row[0], )
        print("Adı Soyadı: ", row[1])
        print("Yaşı: ", row[2])
        print("Maaşı: ", row[3])
        print("Departmanı: ", row[4], "\n")