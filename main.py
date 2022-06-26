import webview

while True:
    url = input("URL :")
    print("--------------------------")

    window = webview.create_window('Browser', url)

    webview.start()
