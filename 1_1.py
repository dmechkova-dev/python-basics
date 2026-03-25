import streamlit as st

st.set_page_config(page_title="Python за 6. клас", page_icon="🐍")

st.title("🚀 Интерактивен Python за 6. клас")
st.sidebar.header("Навигация")
choice = st.sidebar.selectbox("Избери тема:", ["Типове данни & Списъци", "Математически операции", "Цикли (Loops)", "Финален Тест 📝"])

# --- ТЕМА 1: ТИПОВЕ ДАННИ & СПИСЪЦИ ---
if choice == "Типове данни & Списъци":
    st.header("📦 Типове променливи и Списъци")
    
    st.subheader("1. Познай типа на данните")
    col1, col2 = st.columns(2)
    
    with col1:
        val = st.text_input("Въведи нещо (напр. 100, 3.14, 'Здравей' или [1,2,3]):", "100")
        guess = st.selectbox("Какъв според теб е типа?", 
                            ["Избери...", "String (Текст)", "Integer (Цяло число)", "Float (Дробно число)", "List (Списък)"])

    if st.button("Провери моето предположение"):
        user_input = val.strip()
        # Подобрена логика за разпознаване
        if user_input.startswith('[') and user_input.endswith(']'):
            real_type = "list"
        elif user_input.isdigit():
            real_type = "int"
        elif user_input.replace('.', '', 1).isdigit() and "." in user_input:
            real_type = "float"
        else:
            real_type = "str"
        
        type_map = {"str": "String (Текст)", "int": "Integer (Цяло число)", "float": "Float (Дробно число)", "list": "List (Списък)"}
        correct_name = type_map.get(real_type)
        
        if guess == correct_name:
            st.success(f"✅ Браво! '{val}' наистина е {correct_name}.")
        else:
            st.error(f"❌ Грешка. Ти каза '{guess}', но в Python това е {correct_name}.")

    st.divider()
    
    # Секция за Списъци и създаване от текст
    st.subheader("2. Какво е Списък (List)?")
    st.write("Списъкът е подредена колекция от елементи в квадратни скоби `[]`.")
    
    # ТОВА Е НОВАТА ЧАСТ ЗА СЪЗДАВАНЕ НА СПИСЪК ОТ ТЕКСТ:
    st.info("💡 Знаеш ли, че можеш да направиш списък от обикновен текст?")
    user_words = st.text_input("Напиши няколко думи, разделени с интервал:", "котка куче папагал")
    
    if user_words:
        generated_list = user_words.split() # Магията става тук
        st.write("Python превърна твоя текст в този списък:")
        st.code(generated_list)
        st.write(f"Типът на резултата вече е: `{type(generated_list).__name__}`")
        st.write(f"Брой елементи в твоя списък: **{len(generated_list)}**")

    st.divider()
    
    # Индексиране (въпросът с плодовете)
    st.subheader("3. Как намираме елемент в списъка?")
    st.code("plodove = ['ябълка', 'банан', 'портокал']")
    q_index = st.radio("На коя позиция (индекс) е 'ябълка'?", ["index 1", "index 0", "index -1"])
    
    if st.button("Провери индекса"):
        if q_index == "index 0":
            st.success("Точно така! В Python винаги започваме да броим от 0!")
        else:
            st.warning("Почти! Помни правилото: Програмистите винаги започват от НУЛА.")

# --- ТЕМА 2: МАТЕМАТИКА ---
elif choice == "Математически операции":
    st.header("🧮 Математическите суперсили на Python")
    
    st.write("Промени числата А и B, за да видиш как се променят резултатите:")
    col_a, col_b = st.columns(2)
    with col_a:
        a = st.number_input("Въведи число А:", value=10)
    with col_b:
        b = st.number_input("Въведи число B:", value=3)
    
    st.markdown(f"""
    * **Събиране (+):** {a} + {b} = **{a + b}**
    * **Изваждане (-):** {a} - {b} = **{a - b}**
    * **Умножение (*):** {a} * {b} = **{a * b}**
    * **Обикновено деление (/):** {a} / {b} = **{a / b:.2f}**
    * **Целочислено деление (//):** {a} // {b} = **{a // b}** *(Колко цели пъти се събира?)*
    * **Остатък при деление (%):** {a} % {b} = **{a % b}** *(Какво остава накрая?)*
    * **Степенуване (**):** {a} ** {b} = **{a ** b}** *({a} на степен {b})*
    """)
    
    st.divider()
    st.subheader("📝 Кратка проверка: Стани Математик!")
    st.write("Реши задачите, за да видиш дали си разбрал правилата:")

    # Задача 1: Степенуване
    st.write("**Задача 1:** Колко е `3 ** 2`?")
    ans1 = st.number_input("Твоят отговор за 3 на степен 2:", value=0, key="math1")
    if st.button("Провери Задача 1"):
        if ans1 == 9:
            st.success("✅ Точно така! 3 * 3 = 9.")
        else:
            st.error("❌ Не е 9. Помни: 3 на втора степен означава 3 * 3.")

    # Задача 2: Целочислено деление
    st.write("**Задача 2:** Колко е `10 // 4`?")
    ans2 = st.number_input("Твоят отговор за 10 // 4:", value=0, key="math2")
    if st.button("Провери Задача 2"):
        if ans2 == 2:
            st.success("✅ Браво! 4 се събира точно 2 пъти в 10.")
        else:
            st.info("❌ Опитай пак. Колко цели четворки има в 10?")

    # Задача 3: Остатък
    st.write("**Задача 3:** Колко е остатъкът от `11 % 3`?")
    ans3 = st.number_input("Твоят отговор за 11 % 3:", value=0, key="math3")
    if st.button("Провери Задача 3"):
        if ans3 == 2:
            st.success("✅ Супер! 3 * 3 = 9, до 11 остават точно 2.")
        else:
            st.warning("❌ Помисли: 11 делено на 3 е 3 с остатък...?")

    # Задача 4: Умножение и събиране (ред на действията)
    st.write("**Задача 4:** Колко е `2 + 2 * 2`?")
    ans4 = st.number_input("Твоят отговор за 2 + 2 * 2:", value=0, key="math4")
    if st.button("Провери Задача 4"):
        if ans4 == 6:
            st.success("✅ Отлично! Умножението винаги е ПРЕДИ събирането.")
        else:
            st.error("❌ Внимавай! Първо се умножава, после се събира.")

# --- ТЕМА 3: ЦИКЛИ ---
# --- ТЕМА 3: ЦИКЛИ ---
elif choice == "Цикли (Loops)":
    st.header("🔄 Магията на циклите (for loop)")
    
    st.subheader("1. Как изглежда кодът в Python?")
    st.write("Цикълът `for` се използва, когато искаме да повторим нещо определен брой пъти.")
    
    # Визуализация на кода
    st.code("""
# Пример за стандартен цикъл:
for i in range(5):
    print(i) # Ще изпише: 0, 1, 2, 3, 4
    """, language="python")

    st.divider()

    st.subheader("2. Промяна на интервала (Стъпка)")
    st.write("Знаеш ли, че `range()` може да брои през 2, през 5 или дори назад? Това става с трето число, наречено **стъпка**.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        start = st.number_input("Начало:", value=0)
    with col2:
        stop = st.number_input("Край (до):", value=10)
    with col3:
        step = st.number_input("Стъпка (през колко):", value=2)

    st.write(f"Твоят код в момента изглежда така:")
    st.code(f"for i in range({start}, {stop}, {step}):\n    print(i)")

    if st.button("Стартирай цикъла!"):
        res = list(range(int(start), int(stop), int(step)))
        if res:
            st.success(f"Резултат: {res}")
            for item in res:
                st.write(f"🏃 Стъпка номер: {item}")
        else:
            st.warning("Цикълът не може да започне. Провери дали началото е по-малко от края при положителна стъпка.")

    st.divider()

    st.subheader("📝 Проверка: Разбираш ли стъпката?")
    st.write("Какво ще изведе кодът `range(2, 9, 2)`?")
    
    ans_step = st.selectbox("Избери правилната поредица:", 
                           ["Избери...", "2, 4, 6, 8, 10", "2, 4, 6, 8", "0, 2, 4, 6, 8"])
    
    if st.button("Провери задачата за цикли"):
        if ans_step == "2, 4, 6, 8":
            st.success("✅ Браво! Започваме от 2, броим през 2 и спираме ПРЕДИ 9.")
        elif ans_step == "2, 4, 6, 8, 10":
            st.error("❌ Почти! Но 10 е след края (9), затова не се включва.")
        elif ans_step == "0, 2, 4, 6, 8":
            st.info("❌ Внимавай за началото! Кодът започва от 2, а не от 0.")

    st.info("💡 Съвет: Третото число в `range(начало, край, стъпка)` определя през колко ще броим!")

# --- ФИНАЛЕН ТЕСТ ---
# --- ФИНАЛЕН ТЕСТ ---
elif choice == "Финален Тест 📝":
    st.header("🏆 Стани Python Мастър")
    st.write("Отговори на всички въпроси, за да получиш своята грамота!")

    with st.form("quiz"):
        # Въпрос 1: Оператори
        q1 = st.radio("1. Кой оператор ни дава САМО остатъка от делението?", 
                      ["/", "//", "%", "**"])
        
        # Въпрос 2: Списъци (Индексиране)
        st.divider()
        st.code("plodove = ['ябълка', 'банан', 'портокал', 'киви']")
        q2 = st.radio("2. Кой плод ще се изпише, ако напишем `print(plodove[2])`?", 
                      ["банан", "портокал", "киви", "ябълка"])
        
        # Въпрос 3: Степенуване
        st.divider()
        q3 = st.radio("3. Резултатът от израза `2 ** 3` е:", 
                      ["6", "8", "9", "5"])
        
        # Въпрос 4: Цикли (for loop)
        st.divider()
        st.code("""
for i in range(1, 10, 3):
    print(i)
        """)
        q4 = st.radio("4. Кои числа ще изведе този цикъл?", 
                      ["1, 4, 7, 10", "1, 2, 3", "1, 4, 7", "3, 6, 9"])
        
        # Въпрос 5: Целочислено деление
        st.divider()
        q5 = st.radio("5. Колко е `15 // 4`?", 
                      ["3", "3.75", "4", "2"])

        submitted = st.form_submit_button("Предай теста")
        
        if submitted:
            score = 0
            if q1 == "%": score += 1
            if q2 == "портокал": score += 1
            if q3 == "8": score += 1
            if q4 == "1, 4, 7": score += 1
            if q5 == "3": score += 1
            
            if score == 5:
                st.balloons()
                st.success(f"🎊 НЕВЕРОЯТНО! Ти постигна пълен резултат: {score}/5")
                st.write("Ти вече си истински Python програмист!")
            elif score >= 3:
                st.success(f"Много добре! Твоят резултат е: {score}/5")
                st.write("Почти си готов за мастър ниво!")
            else:
                st.warning(f"Резултат: {score}/5. Не се предавай! Прегледай темите отново и опитай пак.")
