# ERD Example

should produce something like;

```mermaid
erDiagram
    bookType {
        string isbn
        string title
        int author_id
        int publisher_id
        date published_date
        decimal price
        reviews reviews
    }
    reviewType {
        int id
        string book_isbn
        string reviewer
        int rating
        string comments
        date review_date
    }
    author {
        int id
        string name
        date birthdate
        string nationality
        books books
    }
    publisher {
        int id
        string name
        string address
        books books
    }
    bookType ||--o{ reviewType : contains
    author ||--o{ bookType : contains
    publisher ||--o{ bookType : contains


```
