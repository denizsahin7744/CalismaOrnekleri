note=100
text = ""
if note > 80:
    text+="A"
elif note > 60:
    text+="B"
elif note >50:
    text +="C"
if text =="A" and note>90:
    text+="A"
elif text =="A" and note>80:
    text+="B"
elif text =="B" and note>70:
    text+="B"
elif text =="B" and note>60:
    text+="C"
elif text =="C" and note>50:
    text+="C"
print(text if note>50 else "CC")