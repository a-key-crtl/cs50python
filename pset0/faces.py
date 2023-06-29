def main():
    face = input("Make a face: ")
    result = convert(face)
    print(result)

def convert(face):
    face1 = face.replace(":)","🙂")
    face2 = face1.replace(":(", "🙁")
    return face2

main()