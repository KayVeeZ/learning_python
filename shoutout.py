import win32com.client as wcl
speaker = wcl.Dispatch("SAPI.SpVoice")
l = []
z ='y'
while z!='done':
    a = input("Type the name you want a shoutout to or type 'Done' to start shoutouts : ")
    l.append(a)
    z = a.lower()
else:
    l.remove('done')
    for person in l:
        print(f"Shoutout to {person}")
        speaker.Speak(f"Shoutout to {person}")

c = input('Thanks for using me! Press Enter to continue...')

