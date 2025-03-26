import streamlit as st
import csv
import random
import time

#for local use
#from dotenv import load_dotenv 

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
    
# verify_player_input() for terminal stuffs:
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
    quote_chars = list(quote)
    input_chars = list(user_input)
    min_length = min(len(quote_chars), len(input_chars))
    
    correct = sum(1 for i in range(min_length) if quote_chars[i] == input_chars[i])
    
    # Penalize extra characters
    if len(input_chars) > len(quote_chars):
        correct -= (len(input_chars) - len(quote_chars))
    
    accuracy = round(correct/len(quote_chars)*100, 2) if quote_chars else 0
    st.progress(correct/len(quote_chars),text=f"**Correct characters:** {correct}/{len(quote_chars)}")
    st.write(f'**Accuracy:** {accuracy}%')  

def Gemini(quote:str,author:str):
    #load_dotenv()
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API_KEY is not set! Please make sure it's added in Streamlit Cloud Secrets.")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"Where is this quote from, give brief information about the book and author? The author is {author} and the quote is: {quote}"
    )
    st.write(response.text)




def main():
    st.title("⌨️ Quote Typing Speed Test ⌨️")
    
    # Initialize session state
    if 'game_state' not in st.session_state:
        st.session_state.game_state = {
            'playing': False,
            'start_time': None,
            'quote': None,
            'author': None,
            'user_input': ''
        }

    file_name = 'data.csv'
    data = read_csv_file(file_name)

    # Start new game
    if not st.session_state.game_state['playing']:
        content = get_random_quote(data)
        st.session_state.game_state.update({
            'playing': True,
            'quote': content['favorite_quote'],
            'author': content['name'],
            'start_time': None,
            'user_input': ''
        })

    # Display quote
    st.subheader("Type the following quote!")
    st.write(st.session_state.game_state['quote'])

    if not st.session_state.game_state['start_time']:
        st.session_state.game_state['start_time'] = time.perf_counter()

    # Text input with controlled state
    user_input = st.text_input(
        "Your input:",
        value=st.session_state.game_state['user_input'],
        key='user_input',
        placeholder="Begin typing here..."
    )
    
    

    # Submit button
    if st.button("✅ Check Result") and user_input:
        with st.container(border=True):
            # Calculate results
            end_time = time.perf_counter()
            start_time = st.session_state.game_state['start_time'] or end_time
            time_elapsed = max(1, round(end_time - start_time-2, 2))
            
            # Update results
            st.subheader("🏆 Your Preformance:")
            check_player_input(st.session_state.game_state['quote'], user_input)
            
            word_count = len(user_input.strip().split())
            wpm = round((word_count / time_elapsed) * 60, 2)

            cols = st.columns(2)
            cols[0].metric("⏱️ Time",f'{time_elapsed}s')
            cols[1].metric('🚀 WPM', f'{wpm}')

            st.divider()
            st.subheader("📚 About the Quote")
            with st.spinner("Thinking...", show_time=True):
                Gemini(st.session_state.game_state['quote'], st.session_state.game_state['author'])

        
        

if __name__ == "__main__":
    main()