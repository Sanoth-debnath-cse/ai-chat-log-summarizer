import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# download nltk packeges
nltk.download('punkt_tab')
nltk.download("punkt")
nltk.download("stopwords")



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

# Clean sample content
clean_content=re.sub(r'[^A-Za-z0-9\s]', '', content)

# Tokenize and store English stop words
filtered_content=word_tokenize(clean_content)
stop_word = set(stopwords.words("english"))

# Exclude common stop words
filtered_word=[word for word in filtered_content if word not in stop_word]
