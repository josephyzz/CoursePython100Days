# Catching except

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The Key {error_message} does not exist.")
# # When no Exception occurs
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height < 3:
    raise ValueError("Human Height should not be over 3 meters.")


bmi = pow(weight / height, 2)
print(bmi)
