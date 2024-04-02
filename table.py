import win32com.client as wcl
speaker = wcl.Dispatch("SAPI.SpVoice")
a = int(input("Please enter the number whose table you want to see: "))
for i in range(1,11):
    
    if i == 1:
        print("Bhosadike multiply by 1 bhi janega?")
        speaker.Speak("Bhosadike multiply by 1 bhi janega?")
        pass
    elif i!=10:
        print(a, "X", i, "=", a * (i))
        speaker.Speak(f"{a} multiplied by {i} equals {a*i}" )
    elif i == 10:
        print("Gand mara gaya 10 ka")
        speaker.Speak("Gand mara gaya 10 ka")
        break
    
