from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book():
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookReqest(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=3)
    author: str = Field(min_lenfth=1)
    description: str = Field(min_lenfth=1, max_length=1000)
    rating: int = Field(gt=0, lt=6)

    class Config:
        schema_extra = {
            'example': {
                "title": "A new Book",
                "author": "Umesh",
                "description": "A description of a book ",
                "rating": 5
            }
        }


BOOKS = [
    Book(1, 'Computer', 'Umesh', 'A very nice Book', 4),
    Book(2, 'A Moon', 'Aku', 'A very Good Book', 5),
    Book(3, 'A King', 'Raj', 'A great Book', 4),
    Book(4, 'La-net', 'Huzefa', 'meri job', 3),
    Book(5, 'One piace', 'Oda', 'World best anime', 5),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get('/book/{book_id}')
async def read_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get('/book/')
async def read_book_by_rating(rating: int):
    book_to_return = []
    for book in BOOKS:
        if book.rating == rating:
            book_to_return.append(book)
    return book_to_return


@app.post("/create-book")
async def create_book(book_request: BookReqest):
    newBook = Book(**book_request.dict())
    BOOKS.append(find_book_id(newBook))
    return {"status": "Done"}


def find_book_id(book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book


@app.put('/book/update')
async def update_book(book: BookReqest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book # type: ignore
            return {"status": "Done"}

    return {"status": "fail"}


@app.delete("/book/{book_if}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return {"status": "Done"}

    return {"status": "fail"}
