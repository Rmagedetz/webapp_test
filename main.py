import streamlit as st

# Получение параметров из URL
query_params = st.experimental_get_query_params()
tg_id = query_params.get('tg_id', [None])[0]

# Отображение Telegram ID
st.title('Streamlit App')
if tg_id:
    st.write(f'Telegram ID: {tg_id}')
else:
    st.write('Telegram ID not provided.')

if tg_id == "12345":
    st.write("вы вошли")
# Пример вывода других данных
st.write('This is your Streamlit app with Telegram integration.')
