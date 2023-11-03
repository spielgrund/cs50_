extensions = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".png", ".pdf", ".txt", ".zip"]
mime = ["image/gif", "image/jpg", "image/jpeg", "image/png", "image/pdf", "image/png", "image/pdf", "image/txt", "image/zip"]

prompt = input("file: ")
#prompt = prompt.endswith(extensions)

for i in range(len(extensions)):
    if prompt.endswith(extensions[i]):
        print(mime[i])

#print(prompt)

