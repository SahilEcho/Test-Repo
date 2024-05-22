from flask import Flask, request, jsonify
app=Flask (__name__)
books=[
       { "id":1,"title":"Harry Potter and the Order of the Phoenix","author":"J.k.Rowling"},
       { "id":2,"title":"The Lord of the Rings: The Fellowship of the Ring","author":"John Ronald Reuel"},
       { "id":3,"title":"Avengers: Endgame","author":"Omid Scobie"}

]
# Get all books
@app.route('/books',methods=['GET'])
def get_books():
    return books

# Get a specific books by id
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return book
        
    return {"error","Book not found"}

# Create a book
@app.route('/books',methods=['POST'])
def create_book():
    new_book={'id':len(books)+1,'title':request.json['title'],'author':request.json['author']}
    books.append(new_book)
    return new_book

# Updates the book

@app.route('/books/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book[id]==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return book 
        return {'error':'Book not found'}
    
    
# Delete the book

@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return{"data":"Book Deleted Successfully"}
        
    return{'error':'Book not found'}


if __name__ == '__main__':
    app.run (debug=True)
    