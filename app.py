import streamlit as st
import speech_recognition as sr
import random
import gtts
from io import BytesIO

# Banco de respostas do professor virtual
respostas_voz = {
    "hello": ["Hi! How are you?", "Hello! What's up?", "Hey there!"],
    "how are you": ["I'm fine, thanks! And you?", "Doing great! How about you?"],
    "what's your name": ["I'm your AI Language Teacher!", "Call me AI Teacher!"],
    "hola": ["¡Hola! ¿Cómo estás?", "¡Hola! ¿Qué tal?"],
    "cómo estás": ["Estoy bien, gracias. ¿Y tú?", "¡Todo bien! ¿Y tú?"],
}

# Função para gerar áudio da resposta
def gerar_audio_resposta(texto, idioma='en'):
    tts = gtts.gTTS(texto, lang=idioma)
    audio_bytes = BytesIO()
    tts.save(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# Criando a interface com Streamlit
st.title("🎧 AI Language Teacher - Web App")

st.write("🔹 Este é um assistente de idiomas interativo. Você pode falar ou digitar uma pergunta!")

# Entrada de texto
user_input = st.text_input("Digite sua pergunta aqui:")
if user_input:
    resposta = respostas_voz.get(user_input.lower(), ["Desculpe, não entendi."])
    resposta_escolhida = random.choice(resposta)
    
    st.write(f"🧠 Resposta: {resposta_escolhida}")

    idioma_resposta = "en" if "how" in user_input or "hello" in user_input else "es"
    
    audio_file = gerar_audio_resposta(resposta_escolhida, idioma_resposta)
    st.audio(audio_file, format="audio/mp3")

