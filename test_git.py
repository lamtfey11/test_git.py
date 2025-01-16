import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Загрузка предобученной модели нейронной сети
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Функция для обработки сообщений
conversation_history = []
def process_message():
    user_input = user_input_field.get()
    if not user_input.strip():
        return

    # Добавление сообщения пользователя в историю чата
    chat_display.insert(tk.END, f"Вы: {user_input}\n")

    # Обработка сообщения нейронной сетью
    global conversation_history
    conversation_history.append({"role": "user", "content": user_input})
    bot_response = chatbot(user_input)
    response_text = bot_response[0]['generated_text']

    # Добавление ответа в историю чата
    chat_display.insert(tk.END, f"Игра: {response_text}\n")

    # Очистка поля ввода
    user_input_field.delete(0, tk.END)

# Создание GUI
root = tk.Tk()
root.title("Игра с нейронной сетью")

# Поле чата
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state="normal")
chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Поле для ввода текста
user_input_field = tk.Entry(root, width=40)
user_input_field.grid(row=1, column=0, padx=10, pady=10)

# Кнопка для отправки
send_button = tk.Button(root, text="Отправить", command=process_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Запуск приложения
root.mainloop()