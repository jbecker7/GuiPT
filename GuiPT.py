import openai
import re
import tkinter as tk
from PIL import Image, ImageTk

openai.api_key = "sk-key"

def chatbot_gui():
    root = tk.Tk()
    root.title("GuiPT")

    # Open the image file and create a PhotoImage object
    img = Image.open("miku.jpg")
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    title_label = tk.Label(root, text="GuiPT", font=("Helvetica", 30))
    title_label.pack()

    # Create a label widget and set the image attribute
    img_label = tk.Label(root, image=img)
    img_label.pack()


    input_label = tk.Label(root, text="Enter your question:", font=("Helvetica", 24))
    input_label.pack()
    user_input_var = tk.StringVar()
    user_input = tk.Entry(root, font=("Helvetica", 24))
    user_input.pack()
    user_input.bind("<Return>", lambda event: generate_response(user_input.get()))

    send_button = tk.Button(root, text="Send", font=("Helvetica", 24), command=lambda: generate_response(user_input.get()))
    send_button.pack()
    exit_button = tk.Button(root, text="Exit", font=("Helvetica", 24), command=root.destroy)
    exit_button.pack()

    response_label = tk.Label(root, text="Response:", font=("Helvetica", 24))
    response_label.pack()
    global response_text
    response_text = tk.Label(root, font=("Helvetica", 24))
    response_text.pack()
    root.mainloop()

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
    response_text.config(text=message.strip())
  
if __name__ == "__main__":
    chatbot_gui()
