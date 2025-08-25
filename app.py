import streamlit as st
import random

st.title("🎲 Guess the Number Game")

# Generate a random number between 1 and 10
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)
    st.session_state.guesses = 0

st.write("I'm thinking of a number between 1 and 10. Can you guess it?")

# User input
guess = st.number_input("Your guess:", min_value=1, max_value=10, step=1)

if st.button("Check"):
    st.session_state.guesses += 1
    if guess == st.session_state.number:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.guesses} tries.")
        # Reset game
        st.session_state.number = random.randint(1, 10)
        st.session_state.guesses = 0
    elif guess < st.session_state.number:
        st.warning("Too low! Try again.")
    else:
        st.warning("Too high! Try again.")


