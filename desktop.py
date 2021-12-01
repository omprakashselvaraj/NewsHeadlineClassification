import pickle
from tkinter import *
import string
from nltk.corpus import stopwords
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize

path='Pickle Files/nhp.pkl'
model = pickle.load(open(path, 'rb'))
path1='Pickle Files/tfidf.pkl'
vector=pickle.load(open(path1,'rb'))
  
root = Tk()
root.geometry("300x300")
root.title(" Q&A ")
  
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    all_list = [char for char in INPUT if char not in string.punctuation]
    clean_str = ''.join(all_list)
    clean_str = word_tokenize(clean_str)
    tokens_without_sw = [' '.join(word for word in clean_str if not word in stopwords.words())]
    print(tokens_without_sw)
    vect = vector.transform(tokens_without_sw).toarray()
    my_prediction = model.predict(vect)
    val=my_prediction[0]
    dic={1:"Politics",2:"Technology",3:"Entertainment",4:"Bussiness"}
    Output.insert(END, dic[val])

    
      
l = Label(text = "Enter your News Story ")
inputtxt = Text(root, height = 10,width = 25,bg = "light yellow")
  
Output = Text(root, height = 5, width = 25, bg = "light cyan")
  
Display = Button(root, height = 2,width = 20, text ="Show",command = lambda:Take_input())
  
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
  
mainloop()