import time
import json
my_json = 'C:\\Users\\jonzm\\OneDrive\\Desktop\\Projects\\Coding\\Calander\\Dates.JSON'

#making function
def int_input(prompt: str = ""):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Please enter an integer.")
            continue

#opening json
with open("C:\\Users\\jonzm\\OneDrive\\Desktop\\Projects\\Coding\\Calander\\Dates.JSON") as f:
    data = json.load(f)


print('------------------------------------------------')
print('Welcome To Jon Zmudas Calendar Application.')
time.sleep(0.5)
print('Loading JSON File')
time.sleep(0.5)
command_prompt = input('1 ) Next\n2 ) Calendar\n3 ) Clear\nWhat command would you like to enter? ')
if command_prompt == "next":    
    input_dict = dict()
    user_input = input('What would you like to add to your calendar? ')
    input_dict.update({f"user_input": user_input})
    input_date = int_input('What day would you like to set that too? (1-365)) ')
    #making sure input_date is within 1-365
    if 0 <= input_date <= 365:
        print('Setting up your Calendar.')
    else:
        print('Please pick a number 1-365.')  
    input_dict.update({f"input_date": input_date})
    data["entries"].append(input_dict)

if command_prompt == "calendar":
    for entry in data["entries"]:
        print("-------------------------------------")
        print(entry["user_input"])
        print(entry["input_date"])

if command_prompt == "clear":
    print("Clearing calendar.")
    sample = {}
    with open('Dates.JSON', 'w') as fp:
        json.dump({"entries":[]} , fp)
#dumping data of json
with open("C:\\Users\\jonzm\\OneDrive\\Desktop\\Projects\\Coding\\Calander\\Dates.JSON", "w") as f:
    json.dump(data, f)















