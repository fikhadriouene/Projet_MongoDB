from pymongo import MongoClient

URI = "mongodb://admin:admin123@localhost:27017"

client = MongoClient(URI)

# Vérification
print(client.list_database_names())

#db = client.get_database("sample_mflix")
# selection de la db
db = client["bronze_db"]

# movies = database.get_collection("movies")
# selection de la collection
collection_customers = db["customers"]
collection_transactions = db["transactions"]
collection_campaigns = db["campaigns"]

print()
print()
print("======= STATS ENREGISTREMENTS COLLECTIONS ===============")
print("nb documents dans 'customers' : ",collection_customers.count_documents({}))
print("nb documents dans 'transactions' : ",collection_transactions.count_documents({}))
print("nb documents dans 'campaigns' : ",collection_campaigns.count_documents({}))
print("==========================================================")
print()
print()

print("======= STATS CUSTOMERS ==================================")
print()
# {
#   "customer_id": "CUST12345",
#   "first_name": "Jean",          
#   "last_name": "Dupont",         
#   "email": "jean@email.com",     
#   "phone": "+33612345678",       
#   "age": 35,                     
#   "country": "France",          
#   "city": "Paris",              
#   "gender": "M",                
#   "marketing_consent": true      
# }
#

print("---- champs vides --------------------------------")
print()
nb_none_last_name = collection_customers.count_documents({"last_name" : None})
print("nombre de last_name vides : ", nb_none_last_name)
nb_none_first_name = collection_customers.count_documents({"first_name" : None})
print("nombre de first_name vides : ", nb_none_first_name)
nb_none_email = collection_customers.count_documents({"email" : None})
print("nombre de email vides : ", nb_none_email)
nb_none_phone = collection_customers.count_documents({"phone" : None})
print("nombre de phone vides : ", nb_none_phone)
nb_none_age = collection_customers.count_documents({"age" : None})
print("nombre de age vides : ", nb_none_age)
nb_none_country = collection_customers.count_documents({"country" : None})
print("nombre de country vides : ", nb_none_country)
nb_none_city = collection_customers.count_documents({"city" : None})
print("nombre de city vides : ", nb_none_city)
nb_none_gender = collection_customers.count_documents({"gender" : None})
print("nombre de gender vides : ", nb_none_gender)
nb_none_marketing_consent = collection_customers.count_documents({"marketing_consent" : None})
print("nombre de marketing_consent vides : ", nb_none_marketing_consent)

collection_customers.update_many({"last_name" : None}, {"$set": {"last_name": "Unknown"}})      
print("MAJ last_name -> Unknown")
nb_none_last_name = collection_customers.count_documents({"last_name" : None})
print("nombre de last_name vides : ", nb_none_last_name)

