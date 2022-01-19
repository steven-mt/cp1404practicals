import wikipedia

title = input("Enter page title or search phrase: ")
while title != "":
    try:
        print(wikipedia.summary(title))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    page = wikipedia.page(title, auto_suggest=False)
    print(page.title)
    print(page.summary)
    print(page.url)

    title = input("Enter page title or search phrase: ")
