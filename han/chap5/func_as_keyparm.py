books = [{
  "name": "A",
  "price": 18000
}, {
  "name": "B",
  "price": 26000
}, {
  "name": "C",
  "price": 24000
}]

def test(book):
  return book["price"]

print("lowest")
print(min(books, key=lambda x: x["price"]))

print("highest")
print(max(books, key=lambda x: x["price"]))

books.sort(key=lambda x: x["price"])
print(books)
