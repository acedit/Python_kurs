def on_budget(books,budget):
    rechnik={
        "books_on_budget": 0,
        "loan": 0
        }
    
    books=sorted(books)

    suma=0 #suma na cenite na vsichki knigi v spisuka
    cena=0 #obshta cena na knigite koito moje da si pozvoli s budgeta
    for book in books:
        suma+=book

    for book in books:
        if budget-book>0:
            rechnik["books_on_budget"]+=1
            cena+=book
            budget-=book
        else:
            break

    rechnik["loan"]=suma-cena

    return rechnik
