# try:
#     file = open("a_file.txt")
#     a_dictionary = {
#         "key": "value"
#     }
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message: #obtains the error message
#     print(f"the key {error_message} does not exist.")
# else: #this is going to happen if everything in try works out.
#     content = file.read()
#     print(f"all the contents are: {content}")
# finally: #happens after else... not use that often.
#     # file.close()
#     # print("\nfile has been closed")
#     raise KeyError("This is an error that i made up") #forces an error.

height = float(input("Height: "))
weight = float(input("Weight: "))

bmi = weight / height **2
print(bmi)

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

#json is java script object notation

#TODO json.dump() json.load() json.update()