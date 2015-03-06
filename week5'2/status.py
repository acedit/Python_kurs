def status_count(students):

    rechnik={
        "finalized": [],
        "not_finalized": []
    }

    for spisuk in students:

        if spisuk["status"]=="finalized":
            rechnik["finalized"]+=[spisuk["name"]]

        else:
            rechnik["not_finalized"]+=[spisuk["name"]]

    return rechnik

