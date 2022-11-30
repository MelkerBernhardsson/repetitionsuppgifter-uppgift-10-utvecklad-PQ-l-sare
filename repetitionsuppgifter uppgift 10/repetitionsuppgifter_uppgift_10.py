
p=int(input("vad a ditt p varde? "))

q=int(input("vad a ditt q varde? "))

diskriminanten=((p/2)**2)-q 

if diskriminanten == 0:
    print("diskriminanten ar noll du har en losning")

elif diskriminanten < 0:
    print("saknar reell losning")

elif diskriminanten > 0:
    print("du har tva mojliga losningar : ",-p/2-diskriminanten**0.5," och ", -p/2+diskriminanten**0.5)

