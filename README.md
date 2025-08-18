# Library Management System
   🔗 **Live Demo**: [Click here to try the app](https://full-stack-library-management-system-2.onrender.com/)
## Overview

The Library Management System is a web-based application built using Python and Flask. It provides functionality for managing books, users, and borrowing/returning operations in a library. The system includes role-based access control, allowing administrators to manage books and track history, while regular users can borrow and return books. The application ensures secure user authentication and integrates with a MySQL database for data storage.

---

## Features

### User Roles
- **Admin**: Can add, update, delete books, view and clear track history, and access the admin dashboard.
- **User**: Can view available books, borrow and return books, and access their borrowing history.

### Book Management
- Add new books with details such as name, author, genre, status, and ID.
- Update existing book details.
- Delete books from the library.

### Borrowing and Returning
- Users can borrow books if available and return them when done.
- Prevents borrowing the same book multiple times without returning it first.
- Tracks borrowing and returning actions with timestamps.

### Track History
- Logs all borrowing and returning actions for administrative review.
- Allows admins to clear the track history.

### Authentication
- Secure user registration and login using hashed passwords (bcrypt).
- Role-based access control ensures restricted access to admin functionalities.

### Responsive Design
- Built with Bootstrap for a responsive and user-friendly interface.
- Optimized for both desktop and mobile devices.

---

## Technologies Used

### Backend
- **Python**: Core programming language.
- **Flask**: Web framework for routing, templates, and handling requests.
- **Flask-Bcrypt**: For secure password hashing.
- **Flask-Login**: For user authentication and session management.

### Frontend
- **HTML/CSS**: For structuring and styling web pages.
- **Bootstrap**: For responsive design and pre-built UI components.

### Database
- **MySQL**: Relational database for storing user, book, and track history data.
- **SQLAlchemy**: ORM for database interaction.

---

## Installation

### Prerequisites
- Python 3.x
- MySQL database
- A virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/PradeepPradeep1234/library-management-system.git
   cd library-management-system
   
2. Install dependencies:  
pip install -r requirements.txt

### Usage

Admin:

    1. Log in as an admin.
    2. Navigate to the admin dashboard to manage books and track history.
    3. Add, update, or delete books as needed.
    4. View and clear borrowing/returning history.

User:

    1.Log in as a user.
    2.Browse the list of available books.
    3.Borrow books and return them when done.

### Database Schema

User:

    1.id: Primary key.
    2.Username: Unique username.
    3.Password: Hashed password.
    4.Role: User role (admin or user).

Add Book:

    1.id: Primary key.
    2.Book_Name: Name of the book.
    3.Author_Name: Author of the book.
    4.Status: Availability status (Available, Checked Out, Reserved).
    5.Book_id: Unique book ID.
    6.Genre_type: Genre of the book.

TrackHistory:

    1.id: Primary key.
    2.username: Username of the user.
    3.book_name: Name of the book.
    4.author_name: Author of the book.
    5.genre: Genre of the book.
    6.action: Action performed (borrow or return).
    7.timestamp: Timestamp of the action.

### Security

   1. Passwords are securely hashed using bcrypt.
   2. Role-based access control ensures restricted access to admin functionalities.
   3. Prevents unauthorized borrowing or returning of books.

---
### Future Enhancements

1. Add email notifications for borrowing and returning books.
2. Implement advanced search and filtering for books.
3. Add support for multiple libraries.
4. Enhance reporting and analytics for admins.

---
### Contact
For any questions or feedback, please contact:

   - GitHub: [PradeepPradeep1234](https://github.com/PradeepPradeep1234)
