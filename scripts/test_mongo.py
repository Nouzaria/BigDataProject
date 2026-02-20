from pymongo import MongoClient
uri = "mongodb+srv://fauzileladhim_db_user:<db_password>@cluster0.vvgkcnp.mongodb.net/?appName=Cluster0"
try:
 client = MongoClient(uri)
 print("Koneksi berhasil!")
 print(client.list_database_names())
except Exception as e:
 print("Koneksi gagal:", e)