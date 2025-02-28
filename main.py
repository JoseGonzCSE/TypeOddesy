import csv
import random

#Puts several dictionaries into a list
#Put these into dictionaries and then put them into a list 
#where list[dict{name:value, favorite quote:value}.....] 

def read_csv_file(file_name):
    data=[]
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_dict = {}
            new_dict["name"]= row.get('name')
            new_dict["favorite_quote"]= row.get('favorite_quote')
            data.append(new_dict)
    return data

# print(data) Gets all data
# print(data[0].get("name")) gets name of specific data
# print(data[0].get("favorite_quote")) gets favorite quote of specific data

def get_random_quote(data):
    data_len=len(data)
    random_index=random.randint(0,data_len)

    random_quote=data[random_index]

    return random_quote
    
def verify_player_input():
    correct_input=False
    while correct_input==False:
        userInput=input("Would you like to play again? y/n ")
        lower_input=userInput.lower()
        if lower_input=="y":
            return False
        elif lower_input=="n":
            print("Thanks for Playing!")
            return True
        else:
            print("please Enter a valid input (y/n)")




def main():
    file_name = 'data.csv'
    data = read_csv_file(file_name)
    print("This is the final step")

    play_again=False
    while play_again==False:
        content=get_random_quote(data)
        print(content)

        quote=content.get("name")
        print(quote)



        play_again=verify_player_input()


        
        


main()






