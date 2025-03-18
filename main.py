import csv
import random
import time
from dotenv import load_dotenv
import os
from google import genai



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
    random_index=random.randint(0,data_len-1)

    random_quote=data[random_index]

    return random_quote
    
def verify_player_input():
    correct_input=False
    while correct_input==False:
        userInput=input("\nWould you like to play again? y/n ")
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

def Gemini(quote:str,author:str):
    load_dotenv()

    client = genai.Client(api_key=os.getenv('API_KEY'))
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"Where is this quote from, give brief information about the book and author? The author is {author} and the quote is: {quote}"
    )
    print(response.text)



def main():
    file_name = 'data.csv'
    data = read_csv_file(file_name)
    print("Welcome! Let's play a game of quotes! Type the following quote! \n") 
    

    play_again=False
    while play_again==False:
        content=get_random_quote(data)
        

        quote=content.get("favorite_quote")
        author=content.get("name")
        print(quote)
        start_time=time.perf_counter()
        user_input=input("Input: ")
        end_time=time.perf_counter()
        #max to avoid div by 0
        time_elapsed=max(1,round(end_time-start_time,2))

        
        word_count=user_input.strip()
        if not word_count:
            total_words = 0
        else:
            total_words = len(word_count.split())
        words_per_minute= round(total_words/time_elapsed *60,2)


        check_player_input(quote, user_input)
        print(f'Time Elapsed: {time_elapsed} seconds')
        print(f"Words/minute: {words_per_minute} ")

        print("---------------------------\n AI more info: \n")
        Gemini(quote,author)
        



        play_again=verify_player_input()


main()






