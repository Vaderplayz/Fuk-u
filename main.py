import json
import datetime
def appendData(data, filename="bills.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent = 4)
def checkDate():
    month1 = [1, 3, 5, 7, 8, 10, 12]
    month = [2, 4, 6, 9, 11]
    total = 0
    if int(datetime.datetime.now().strftime("%m")) in month1 and len(json.load(open("bills.json"))['bills']) == 31:
        """
        with open("bills.json") as f:
            obj = json.load(f)
            obj['bills'].clear()
            json.dumps(obj, sort_keys=True, indent=4)
        """
        for i in range(0, len(json.load(open("bills.json"))['bills'])):
            total = total + float(json.load(open("bills.json"))['bills'][i]['price'])
        print(f"Your total this month: {total}$")
    elif len(json.load(open("bills.json", "r"))['bills']) == 30 and int(datetime.datetime.now().strftime("%m")) in month:
        """
        with open("bills.json") as f:
            obj = json.load(f)
            obj['bills'].clear()
            json.dumps(obj, sort_keys=True, indent=4)
        """
        for i in range(0, len(json.load(open("bills.json"))['bills'])):
            total = total + float(json.load(open("bills.json"))['bills'][i]['price'])
        print(f"Your total this month: {total}$")
def purchase(item, price):
    try:
        with open("bills.json") as bills:
            content = {"date_of_purchase": str(datetime.datetime.now().strftime("%A %B, %d")), "name": item, "price": price}
            data = json.load(bills)
            data['bills'].append(content)
        appendData(data)
        status = "Item has been added"
    except (ValueError, IndexError):
        status = "An error has occured. Please try again later"
    return status
def main():
    while True:
        checkDate()
        with open("price.json", "r") as price:
            data = json.loads(price.read())
            print("Our current offers")
        for i in range(0, len(data['list'])):
            print(f"[{i}] {data['list'][i]['name']}: {data['list'][i]['price']}$")
        try:
            item = int(input("Enter index: "))
            print(purchase(data['list'][item]['name'], float(data['list'][item]['price'])))
        except IndexError:
            print("That item is non-existant")
if __name__ == "__main__":
    main()
