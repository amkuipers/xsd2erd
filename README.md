# xsd2erd
XSD 2 ERD

ChatGPT generated code, until I reached a limit and could not improve it.
Then manually adjusted.

Using mermaid.js to visualise in markdown (without preprocessor).
Reference: https://mermaid.js.org/syntax/entityRelationshipDiagram.html

## Build
The GitHub Action has a step that generates the erDiagram text.

Link: https://github.com/amkuipers/xsd2erd/actions


## Example output

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
    bookType ||--o{ reviewType : reviews
    author ||--o{ bookType : books
    publisher ||--o{ bookType : books


```
