file_name = input("File Name: ")

if file_name.endswith("gif"):
        print("image/gif")
elif file_name.endswith("jpg"):
        print("image/jpg")
elif file_name.endswith("jpeg"):
        print("image/jpeg")
elif file_name.endswith("png"):
        print("image/png")
elif file_name.endswith("pdf"):
        print("image/pdf")
elif file_name.endswith("txt"):
        print("image/txt")
elif file_name.endswith("zip"):
        print("image/zip")
else:
        print("application/octet-stream")