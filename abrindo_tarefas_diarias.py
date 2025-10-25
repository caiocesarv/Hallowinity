import os
import time

# Lista de programas que irei abrir na automação 
apps = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

print("Invocando os programas do além... 🧙‍♂️")
for app in apps:
    os.startfile(app)
    time.sleep(2)
print("Todos os feitiços foram lançados!")
