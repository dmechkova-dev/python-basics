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
        val = st.text_input("Въведи нещо тук (напр. 5, 3.14, 'Здравей' или [1,2,3]):", "100")
        guess = st.selectbox("Какъв според теб е типа на това, което въведе?", 
                            ["Избери...", "String (Текст)", "Integer (Цяло число)", "Float (Дробно число)", "List (Списък)"])

    if st.button("Провери моето предположение"):
        # Опитваме се да разберем какво е въвел потребителят
        user_input = val.strip()
        
        # 1. Проверка дали е списък (започва с [ и завършва с ])
        if user_input.startswith('[') and user_input.endswith(']'):
            real_type = "list"
        # 2. Проверка за число (цяло)
        elif user_input.isdigit():
            real_type = "int"
        # 3. Проверка за дробно число
        elif user_input.replace('.', '', 1).isdigit() and "." in user_input:
            real_type = "float"
        # 4. Всичко останало е текст
        else:
            real_type = "str"
        
        type_map = {
            "str": "String (Текст)", 
            "int": "Integer (Цяло число)", 
            "float": "Float (Дробно число)", 
            "list": "List (Списък)"
        }
        correct_name = type_map.get(real_type)
        
        if guess == correct_name:
            st.success(f"✅ Браво! Точно така, '{val}' е {correct_name}.")
        else:
            st.error(f"❌ Не съвсем. Ти каза '{guess}', но в Python '{val}' се разпознава като {correct_name}.")
    st.divider()
    st.subheader("2. Какво е Списък (List)?")
    st.write("Списъкът е кутия с много отделения. Използваме квадратни скоби `[]`.")
    items = st.text_input("Напиши 3 любими плода, разделени със запетая:", "ябълка, банан, портокал")
    fruit_list = [i.strip() for i in items.split(",")]
    st.code(f"plodove = {fruit_list}")
    
    q_list = st.radio("Как ще вземем ПЪРВИЯ елемент от списъка в Python?", ["plodove[1]", "plodove[0]", "plodove[първи]"])
    if st.button("Провери за списък"):
        if q_list == "plodove[0]":
            st.success("Правилно! В Python броенето винаги започва от 0.")
        else:
            st.info("Опитай пак! Помни, че програмистите броят от нула.")

# --- ТЕМА 2: МАТЕМАТИКА ---
elif choice == "Математически операции":
    st.header("🧮 Разширени математически действия")
    
    a = st.number_input("Въведи число А:", value=10)
    b = st.number_input("Въведи число B:", value=3)
    
    st.markdown(f"""
    * **Обикновено деление (`/`):** {a} / {b} = **{a/b:.2f}**
    * **Целочислено деление (`//`):** {a} // {b} = **{a//b}** (Колко пъти се събира?)
    * **Остатък при деление (`%`):** {a} % {b} = **{a%b}** (Какво остава накрая?)
    * **Степенуване (`**`):** {a} ** {b} = **{a**b}** ({a} на степен {b})
    """)
    
    st.divider()
    st.subheader("📝 Кратка проверка")
    st.write("Ако имаме `x = 7 % 2`, колко ще бъде `x`?")
    ans_math = st.number_input("Твоят отговор:", value=0)
    if st.button("Провери задачата"):
        if ans_math == 1:
            st.success("Точно така! 7 делено на 2 е 3 с остатък 1.")
        else:
            st.error("Не е 1. Помисли: 2+2+2 = 6. Колко остава до 7?")

# --- ТЕМА 3: ЦИКЛИ ---
elif choice == "Цикли (Loops)":
    st.header("🔄 Магията на циклите")
    st.write("Цикълът ни пести време. Вместо да пишем 100 реда, пишем 2.")
    
    n = st.slider("Колко пъти да завъртим цикъла?", 1, 10, 3)
    for i in range(n):
        st.write(f"🤖 Роботът прави стъпка номер {i}")
        
    st.divider()
    st.subheader("❓ Въпрос за размисъл")
    st.write("Какво ще изпише `range(3)`?")
    ans_loop = st.selectbox("Избери:", ["1, 2, 3", "0, 1, 2, 3", "0, 1, 2"])
    if st.button("Провери цикъла"):
        if ans_loop == "0, 1, 2":
            st.success("Браво!range(3) генерира 3 числа, започвайки от 0 (0, 1, 2).")
        else:
            st.warning("Близо си, но помни: последното число в range() никога не се включва!")

# --- ФИНАЛЕН ТЕСТ ---
elif choice == "Финален Тест 📝":
    st.header("🏆 Стани Python Мастър")
    with st.form("quiz"):
        q1 = st.radio("Кой оператор ни дава САМО остатъка?", ["/", "//", "%", "**"])
        q2 = st.radio("Как се дефинира списък?", ["(1, 2)", "{1, 2}", "[1, 2]"])
        q3 = st.radio("Резултатът от 2 ** 3 е:", ["6", "8", "9"])
        
        submitted = st.form_submit_button("Предай теста")
        if submitted:
            score = 0
            if q1 == "%": score += 1
            if q2 == "[1, 2]": score += 1
            if q3 == "8": score += 1
            
            if score == 3:
                st.balloons()
                st.success(f"Пълен успех! 3/3")
            else:
                st.info(f"Резултат: {score}/3. Провери си грешките и опитай пак!")
