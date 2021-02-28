text = "X-DSPAM-Confidence:    0.8475";
Pos = text.find('0')
#print(Pos)
END = text.find('5',Pos)
#print(END)
NUM = text[Pos:]
Ans = float(NUM)
print(Ans)

