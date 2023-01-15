# Import the necessary libraries
import openai
import re
import PySimpleGUI as sg

openai.api_key = "key"


def chatbot_gui():
    layout = [  
    [sg.Text("Enter your message: ", font=("Helvetica", 14)), sg.InputText(font=("Helvetica", 14)), sg.Stretch()],
    [sg.Button("Send", font=("Helvetica", 14)), sg.Button("Exit", font=("Helvetica", 14)), sg.Stretch()],
    [sg.Text("Response: ", font=("Helvetica", 14)), sg.Text("", key="response", font=("Helvetica", 14)), sg.Stretch()]
]



    window = sg.Window("GuiPT", layout, auto_size_text=True, default_element_size=(40, 2))

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break

        if event == "Send":
            user_input = values[0]
            response = generate_response(user_input)
            window["response"].update(response)

    window.close()

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

if __name__ == "__main__":
    chatbot_gui()
