"""Reading list: our team project.

What happens where:
- main.py      the web part: which address shows what (the "routes")
- storage.py   where the books are kept
- templates/   the HTML page
- static/      the stylesheet and two pictures
"""

from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import storage

HERE = Path(__file__).parent

app = FastAPI(title="Reading list")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")

# (finished books needed, name of the achievement)
ACHIEVEMENTS = [
    (1, "First book"),
    (5, "Bookworm"),
    (10, "Double digits"),
    (15, "Page turner"),
    (20, "Shelf filler"),
    (25, "Library builder"),
]


def achievements(finished_count):
    """All achievements, each marked as earned or not."""
    result = []
    for books_needed, name in ACHIEVEMENTS:
        earned = finished_count >= books_needed
        result.append({"books": books_needed, "name": name, "earned": earned})
    return result


@app.get("/")
def show_page(request: Request):
    """The start page: the three columns and the achievements."""
    finished = storage.books_with_status("finished")
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "want": storage.books_with_status("want"),
            "reading": storage.books_with_status("reading"),
            "finished": finished,
            "achievements": achievements(len(finished)),
        },
    )


@app.post("/add")
def add(title: str = Form(...), author: str = Form(...)):
    """The form on the start page sends its fields here."""
    storage.add_book(title.strip(), author.strip())
    # Back to the start page. 303 tells the browser: load it with GET.
    return RedirectResponse("/", status_code=303)


@app.post("/move/{book_id}")
def move(book_id: int, status: str = Form(...)):
    """A button on a book sends the new column here."""
    if status in ("want", "reading", "finished"):
        storage.move_book(book_id, status)
    return RedirectResponse("/", status_code=303)


@app.post("/delete/{book_id}")
def delete(book_id: int):
    """The "Remove" button on a book sends its id here."""
    storage.delete_book(book_id)
    return RedirectResponse("/", status_code=303)
