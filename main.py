from tkinter import *
from chatterbot import ChatBot
import pyttsx3
import speech_recognition as s
import threading

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


from chatterbot.trainers import ListTrainer

bot = ChatBot("My Bot")
convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Tuba I am a female bot created by Yogii',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'what is the capital of india?',
    'Delhi is the capital of India',
    'dont talk to me ',
    'i will talk to you',
    'are you intelligent?',
    'Yes i am intelligent',
    'Where do you live ?',
    'I live in Bharunda',
    'what you do?',
    'I do chatting',
    'Are you single or Married?',
    'married',

    'Say something',
    'No, you say something',

    'In which language you talk?',

    ' I mostly talk in english',
    'what you do in free time?',
    'I memorize things in my free time',
    'ok bye take care see you again',
    'bye'

]
trainer = ListTrainer(bot)
trainer.train(convo)

def take_query():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print('your bot is listening try to speak')
    with s.Microphone as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language= 'eng-in')
            question_field.delete(0,END)
            question_field.insert(0, query)
            askbot()
        except Exception as e:
            print(e)



def askbot():
    query = question_field.get()
    answers = bot.get_response(query)

    text_area.insert(END, "you:" + query+'\n\n')
    text_area.insert(END, "Bot:" + str(answers)+'\n\n')
    engine.say(answers)
    engine.runAndWait()

    question_field.delete(0,END)
    text_area.yview(END)


root = Tk()
root.geometry('500x570+100+30')
root.resizable(0,0)
root.title('ChatBot created by Yogii')
root.config(bg = "lavender blush")

pic = PhotoImage(file = 'pic.png')
picture_label = Label(root, image = pic, bg = "lavender blush")
picture_label.pack(pady = 5)

center_frame = Frame(root)
center_frame.pack()

scroll_bar = Scrollbar(center_frame)
scroll_bar.pack(side = RIGHT, fill = Y)

text_area = Text(center_frame, font = ("times new roman", 28, "bold"),width = 80, height = 10, yscrollcommand = scroll_bar.set,bg = "floral white")
text_area.pack(side = LEFT, fill = BOTH)

question_field = Entry(root, font = ("verdana", 25, "bold"), bg = "floral white")
question_field.pack(fill = X, pady = 10)

ask_image = PhotoImage(file = "ask.png")
ask_button = Button(root, image = ask_image, bd= 0, bg = 'lavender blush', activebackground = 'lavender blush', cursor = 'hand2',command = askbot)
ask_button.pack()

def enter_function(event):
    ask_button.invoke()


root.bind('<Return>',enter_function)

def repeat():
    while True:
        take_query()


t1 = threading.Thread(target=repeat)
t1.start()


root.mainloop()