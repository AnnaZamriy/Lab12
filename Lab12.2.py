def strip_protocol(urls):
    str = []
    for url in urls:
        if url.startswith("http://"):
            str.append(url[7:])
        elif url.startswith("https://"):
            str.append(url[8:])
        else:
            str.append(url)
    return str

N = int(input("Введіть кількість URL-адрес:"))

urls = [input(f"Введіть URL-адресу: ") for i in range(N)]

str = strip_protocol(urls)

for url in str:
    print(url)
