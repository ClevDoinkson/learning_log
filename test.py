crumb = ["hello my name is lachlan", "hello"]
for x in crumb:
    if len(x) > 20:
        print(f"{x[:15]}...")
    else:
        print(x)