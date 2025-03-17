import csv
import random
import time

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

def check_player_input(quote:str, user_input:str):
    quote=list(quote)
    user_input=list(user_input)
    quote_len=len(quote)
    user_input_len=len(user_input)
    smallest_len=min(quote_len, user_input_len)



    correct=accuracy=0
    
    #use the smallest length to iterate through
    #Can use color to change color here via quote[char] if possible
    # or just make a new list 
    # green=good, red = wrong

    for char in range(smallest_len):
        if quote[char]==user_input[char]:
            correct+=1
    
    #find difference in extra charcters

    if user_input_len>quote_len:
        correct=-user_input-quote_len
    accuracy=round(correct/quote_len*100,2)
    print("---------------------------------------")
    print("Results:\n")
    print (f'{correct} correct characters')
    print(f'Accuracy: {accuracy}%')    


def main():
    file_name = 'data.csv'
    data = read_csv_file(file_name)
    print("Welcome! Let's play a game of quotes! Type the following quote! \n") 

    play_again=False
    while play_again==False:
        content=get_random_quote(data)
        

        quote=content.get("favorite_quote")
        print(quote)
        start_time=time.perf_counter()
        user_input=input("Input: ")
        end_time=time.perf_counter()
        time_elapsed=round(end_time-start_time,2)

        # have to get words per minute, use user input, go through array, if space-> thats stopping point = one word 
            # wait if its just sapce that dictates words, count how many spaces = thats how many words there are, + 1 for the last word 
            #Double spaces get fucked  FIX!!!!!

        total_words= user_input.count(" ") +1
        words_per_minute= round(total_words/time_elapsed *60,2)

        check_player_input(quote, user_input)
        print(f'Time Elapsed: {time_elapsed} seconds')
        print(f"Words/minute: {words_per_minute} ")
        
        



        play_again=verify_player_input()


        
        


main()






