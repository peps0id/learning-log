extension = input("File name: ").lower()
match extension:
    case extesion if extension.endswith("gif"):
        print("image/gif")
    case extesion if extension.endswith("jpg"):
        print("image/jpeg")
    case extesion if extension.endswith("jpeg"):
        print("image/jpeg")
    case extesion if extension.endswith("png"):
        print("image/png")
    case extesion if extension.endswith("pdf"):
        print("application/pdf")
    case extesion if extension.endswith("txt"):
        print("text/plain")
    case extesion if extension.endswith("zip"):
        print("application/gif")
    case _ :
        print("application/octet-stream")