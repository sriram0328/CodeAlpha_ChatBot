from nltk.chat.util import Chat,reflections
# nltk => Natural language tool kit . It is an library
# r => used fir reading the string
pairs = [
        [r"hi",["hiiiiiiiii,chatBot here"]],
        [r"hey",["hii there,chatBot is talking"]],
        [r"hello",["hello I'm chatBot"]],
        [r"Tell me about yourself", ["I am an AI language model developed by CodeAlpha, I'm just a basic ChatBot . I use the trained data to answer the user's input"]],
        [r"What is your name?", ["My name is CodeAlpha ChatBot."]],
        [r"How does ChatGPT work?", ["ChatBot works by processing and generating text based on the input it receives,with the trained data"]],
        [r"What can you do?", ["I can assist with a wide range of tasks, including answering questions, providing information, generating text, and engaging in conversation on various topics."]],
        [r"Can you tell me a joke?", ["Why are cricket stadiums so cool?  \n Because every seat has a fan in it!! "]],
        [r"Who created you?", ["I was created by CodeAlpha"]],
        [r"How are you?", ["I'm just a computer program, so I don't have feelings, but I'm here to assist you!"]],
        [r"Can you explain (.*) to me?", ["Sure, I can provide information and explanations on many topics. Please specify the topic you'd like to know about."]],
        [r"What is the weather like?", ["I'm sorry, I don't have real-time access to weather information. You can check a weather website or app for the current forecast in your area."]],
        [r"Can you help me with my homework?", ["I can certainly try! Please provide the details of the homework problem or question you need assistance with."]],
        [r"Do you have feelings?", ["No, I'm just a computer program, so I don't have feelings."]],
        [r"Can you write a story/poem for me?", ["Sure, I can generate a story or poem based on a theme. Please provide more details or a specific request."]],
        [r"Are you human?", ["No, I am an artificial intelligence program created by CodeAlpha."]],
        [r"What languages do you speak?", ["I can understand and generate text in multiple languages, including English, Spanish, French, German, Chinese, and many more."]],
        [r"Can you help me with coding/programming?", ["Yes, I can assist with coding and programming questions. Please provide the specifics of what you need help with."]],
        [r"Can you sing a song?", ["I can't sing, but I can provide lyrics or generate text in a lyrical format if you'd like!"]],
]
chat = Chat(pairs,reflections)
chat.converse()

def quit():
    print("hey, I'm ChatBot ask me something")
if __name__=="__main__":
    quit()
