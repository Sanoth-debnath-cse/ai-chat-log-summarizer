import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# download nltk packeges
#nltk.download('punkt_tab')
#nltk.download("punkt")
#nltk.download("stopwords")



sample_data="sample.txt"

content=""

with open(sample_data,"r") as file:
    for line in file:
        content+=line.strip()+" "

# Separate messages by speaker
pattern = re.findall(r'(User|AI):\s*(.*?)(?=(?:User|AI):|$)', content, re.DOTALL)


dialogue={}

total_message_count=0

#Formated messages stored into dialogue dict
for user,message in pattern:
    dialogue[user]=dialogue.get(user,[])
    dialogue[user].append(message)
    total_message_count+=1

user_messages_count=len(dialogue["User"])
ai_messages_count=len(dialogue["AI"])

# Clean sample content by removing speaker
clean_content = re.sub(r'(User|AI):\s*', '', content)

# Clean sample content by removing special char
clean_content=re.sub(r'[^A-Za-z0-9\s]', '', clean_content)

# Tokenize and store English stop words
filtered_content=word_tokenize(clean_content.lower())
stop_word = set(stopwords.words("english"))

# Exclude common stop words
filtered_word=[word for word in filtered_content if word not in stop_word]

# Frequency count of filtered words
word_frequency={}

for word in filtered_word:
    word_frequency[word]=word_frequency.get(word,0)+1
    
print(word_frequency)

# Top 5 common frequently used words
most_frequent_5_words=sorted(word_frequency,key=lambda word:word_frequency[word],reverse=True)[:5]
print(most_frequent_5_words)
