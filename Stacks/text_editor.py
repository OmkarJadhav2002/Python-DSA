def text_editor(text, pattern):
    undo = []
    redo = []

    for i in text:
        undo.append(i)

    for i in pattern:
        if i == "u":
            data = undo.pop()
            redo.append(data)
        else:
            data = redo.pop()
            undo.append(data)

    res = ""
    while len(undo):
        res = undo[-1] + res

        undo.pop()

    return res


if __name__ == "__main__":
    ans = text_editor("Hello", "uuurr")
    print("Solution: ", ans)
