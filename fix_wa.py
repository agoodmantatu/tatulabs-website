src = open("E:/TatuLabs/index.html", encoding="utf-8").read()
src = src.replace("91XXXXXXXXXX", "919566698821")
open("E:/TatuLabs/index.html", "w", encoding="utf-8").write(src)
print("WhatsApp number updated")
