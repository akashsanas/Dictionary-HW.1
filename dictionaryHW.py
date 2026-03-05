# Creaate a dictionary of moves 2025 

movies_db = {}   # minimum 4 movies

# casting of 2025 movies

cast_housefull_5 =["Akshay Kumar","Sanjay Dutt","Bobby Deol"]

cast_Saiyaara = ["Ahaan panday","Aneet padda"]

cast_dhurandar = ["Ranveer Sing ","Sanjay Dutt","Sara Arjun"]

cast_baagi_4 = ["Tiger shroff","Sanjay Dutt","Sonam bajwa"]
 
 # Casting and Movies name inside Dictinory

movies_db["Housefull 5"] = cast_housefull_5

movies_db["Saiyaara"] = cast_Saiyaara

movies_db["dhurandar"] = cast_dhurandar

movies_db["baagi 4"] = cast_baagi_4

# print hole Dictinory
print("Total 2025 movies with its cast is -->\n",movies_db)


# 1. Print all keys using key() method
print("All keys from the Dictinoary--->")
for k in movies_db.keys():
    print(k)

# 2. print all values using value() method
print("All values from the Dictinoary--->")
for v in movies_db.values():
    print(v)

# 3. Print all keys and values using items()method
print("All keys and values from the Dictionary--->")
for k,v in movies_db.items():
    print(k,"--->",v)

# 4. count the actors in same movies

cast = input("Enter the Actor /Actress name: ")
count = 0 
print(f"Movies of {cast} is:  ")
for k in movies_db:
    if cast in movies_db.get(k):
        
        print(k)
    count+=1

    print(f"{cast} worked in {count} movies.")
    