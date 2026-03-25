pip install streamlit
import streamlit as st

st.set_page_config(page_title="Python за 6. клас", page_icon="🐍")

st.title("🚀 Приключение в света на Python!")
st.write("Добре дошли, млади програмисти! Нека научим основите заедно.")

# Меню встрани
choice = st.sidebar.selectbox("Избери тема:", ["Типове данни", "Математика", "Цикли (Loops)"])

if choice == "Типове данни":
    st.header("📦 Типове променливи")
    st.write("Променливите са като кутии, в които пазим информация.")
    
    name = st.text_input("Напиши името си:", "Робот")
    age = st.number_input("Напиши годините си:", value=12)
    
    if st.button("Покажи типа!"):
        st.success(f"Твоето име '{name}' е тип **String** (текст)")
        st.info(f"Твоите години {age} са тип **Integer** (цяло число)")

elif choice == "Математика":
    st.header("🧮 Аритметични действия")
    num1 = st.number_input("Число А:", value=10)
    num2 = st.number_input("Число B:", value=5)
    
    st.write(f"**{num1} + {num2} = {num1 + num2}**")
    st.write(f"**{num1} - {num2} = {num1 - num2}**")
    st.write(f"**{num1} * {num2} = {num1 * num2}**")
    st.write(f"**{num1} / {num2} = {num1 / num2}**")

elif choice == "Цикли (Loops)":
    st.header("🔄 Цикли")
    st.write("Цикълът `for` повтаря нещо много пъти.")
    
    times = st.slider("Колко пъти да повторя?", 1, 10, 5)
    word = st.text_input("Какво да кажа?", "Python е супер!")
    
    if st.button("Старт!"):
        for i in range(times):
            st.write(f"{i+1}. {word}")
