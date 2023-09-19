import numpy as np
import pandas as pd







with open("spam.csv","r")as file:
    data=file.readlines()

data.pop(0)
labels=[]
messages=[]

#assign labels and messages to separate lists
for line in data:
    comma_loc=line.find(",")
    labels.append(line[:comma_loc])
    messages.append(line[comma_loc+1:])

#create a list of words that define whether the email is spam or not
spamwords=["free","buy","win","lottery","jackpot","urgent","package","expiring","expired","competition", "login", "log in"]


#create an empty dataframe
features=np.zeros((len(messages),len(spamwords)))

#loop through messages and turn it all to lower case
for i,msg in enumerate(messages):
    msg=msg.lower()
    #loop through spawmrds count the occurences of a spamword in the iterated message
    for j,word in enumerate(spamwords):
        word_count=msg.count(word)
        features[i,j]=word_count
labels=np.array(labels)
labels=labels.reshape((-1,1))

dataset=np.hstack((features,labels))

df=pd.DataFrame(dataset)
spamwords.append("label")
pd=df.to_csv("spam_dataset.csv",header=spamwords)