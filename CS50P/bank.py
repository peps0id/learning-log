greeting = input("Greeting: ").strip().lower()

match greeting:
    case "hello" :
        print("$0")
    case greeting if greeting.startswith("h"):
        print("$20")
    case _ :
        print("$100")