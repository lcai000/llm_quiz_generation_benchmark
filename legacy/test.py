from quiz_format import format_question

with open("example.txt","r") as f:
    q = f.read()
t = ""
t=t+'\n'+q+'\n'+q
# print(t)
print(format_question(str(t)))