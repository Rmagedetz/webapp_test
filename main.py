import streamlit as st
import json
import hmac
import hashlib

# Замените на ваш API токен
API_TOKEN = st.secrets.tg_bot.token


def verify_telegram_auth_data(auth_data, secret_key):
    try:
        auth_data_dict = json.loads(auth_data)
        data_check_string = '\n'.join(f'{k}={v}' for k, v in sorted(auth_data_dict.items()))
        hmac_hash = hmac.new(secret_key, data_check_string.encode('utf-8'), hashlib.sha256).hexdigest()
        return hmac_hash == auth_data_dict.get('hash')
    except Exception as e:
        st.error(f"Ошибка верификации: {e}")
        return False


def main():
    st.title("Ваш Telegram ID")

    # Получите URL-параметры
    auth_data = st.query_params.get('auth_data', '')
    st.write(auth_data)
    if auth_data:
        secret_key = hashlib.sha256(API_TOKEN.encode('utf-8')).digest()
        if verify_telegram_auth_data(auth_data, secret_key):
            auth_data_dict = json.loads(auth_data)
            user_id = auth_data_dict.get('user', {}).get('id', 'Неизвестно')
            st.write(f"Ваш Telegram ID: {user_id}")
        else:
            st.write("Ошибка получения ID")
    else:
        st.write("Ошибка: auth_data не предоставлен")


if __name__ == "__main__":
    main()
