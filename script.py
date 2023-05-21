import os

for item in os.listdir():
    if '.' not in item:
        for pth in os.listdir(item):
            if "." not in pth:
                with open(item+"/"+pth+"/index.html", "r") as file:
                    data = file.read()
                    print(data)
                with open(item+"/"+pth+"/index.html", "w") as file:
                    file.write(data.replace('window.close();', r'window.location.replace("https://csemoodle.tint.edu.in/")'))