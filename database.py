import mysql.connector

mydb = mysql.connector.connect(
  host="oege.ie.hva.nl",
  user="witdcm",
  password="MEVO5MBqeC2f94",
  database="zwitdcm"
)

mycursor = mydb.cursor()

# --test deleted after
# mycursor.execute("CREATE TABLE user (name VARCHAR(255), email VARCHAR(255))")

# --added table
# mycursor.execute("CREATE TABLE userInfo (name VARCHAR(255), email VARCHAR(255), address VARCHAR (255), phoneNumber VARCHAR(255))")

#--added user
# sql = "INSERT INTO userInfo (name, email, address, phoneNumber) VALUES (%s, %s, %s, %s)"
# val = ("Nancy", "nancykonijn@wingsofchange.nl", "Andijk", "+3167481628")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# --added user
# sql = "INSERT INTO userInfo (name, email, address, phoneNumber) VALUES (%s, %s, %s, %s)"
# val = ("Leon", "leonarends@wingsofchange.nl", "Andijk", "+3167982428")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# --deleted and added user
# sql = "DELETE FROM userInfo WHERE address = 'Andijk'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

