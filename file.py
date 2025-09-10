# # Writing to file
# with open("pqr.txt", "w") as f:
#     f.write("Hello, this is Akshu writing to a file!")

# print("Data written successfully.")

# #reading file
# with open("pqr.txt", "r") as f:
#     print(f.read())
#     f.close()
    

# #modes in python
# with open("pqr.txt","a") as f:
#     f.write("\n this is appended line")
#     print("data appended successfully")
#     f.close()



# with open("pqr.txt","r") as f:
#     print(f.readline())
#     f.close()


with open("pqr.txt","a+") as f:
    f.seek(0)
    print(f.read())