from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app.models.book import Add_Book
from app.models.track_history import TrackHistory
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from app import db, bcrypt

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def home():
    return render_template("home.html")

@user_bp.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(Username=form.username.data).first()
        if existing_user:
            flash("⚠️ Username already exists. Please login instead.", "warning")
            return redirect(url_for("user.login_page"))
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(Username=form.username.data, Password=hashed_pw, Role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("user.login_page"))
    return render_template("register.html", data=form)

@user_bp.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(Username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.Password, form.password.data):
            login_user(user)
            flash(f"{user.Role.capitalize()} Login successful!", "success")
            return redirect(url_for("admin.admin_dashboard") if user.Role == "admin" else url_for("user.view_books"))
        flash("Invalid credentials or user not found", "danger")
    return render_template("login.html", data=form)

@user_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("🔒 You have been logged out.", "info")
    return redirect(url_for("user.login_page"))

@user_bp.route("/view_books")
@login_required
def view_books():
    books = Add_Book.query.all()
    return render_template("view_books.html", data=books)

@user_bp.route("/borrow/<int:book_id>")
@login_required
def borrow_book(book_id):
    book = Add_Book.query.get_or_404(book_id)

    if current_user.Role != 'user':
        flash("Access denied", "danger")
        return redirect(url_for("user.view_books"))

    existing_borrow = TrackHistory.query.filter_by(
        username=current_user.Username,
        book_name=book.Book_Name,
        action='borrow'
    ).order_by(TrackHistory.timestamp.desc()).first()

    existing_return = TrackHistory.query.filter_by(
        username=current_user.Username,
        book_name=book.Book_Name,
        action='return'
    ).order_by(TrackHistory.timestamp.desc()).first()

    if existing_borrow and (not existing_return or existing_return.timestamp < existing_borrow.timestamp):
        flash("⚠️ You have already borrowed this book. Please return it first.", "warning")
        return redirect(url_for("user.view_books"))

    history = TrackHistory(
        username=current_user.Username,
        book_name=book.Book_Name,
        author_name=book.Author_Name,
        genre=book.Genre_type,
        action='borrow'
    )
    db.session.add(history)
    book.Status = "Unavailable"
    db.session.commit()
    flash("📚 Book borrowed successfully!", "success")
    return redirect(url_for("user.view_books"))

@user_bp.route("/return/<int:book_id>")
@login_required
def return_book(book_id):
    book = Add_Book.query.get_or_404(book_id)

    if current_user.Role != 'user':
        flash("Access denied", "danger")
        return redirect(url_for("user.view_books"))

    last_borrow = TrackHistory.query.filter_by(
        username=current_user.Username,
        book_name=book.Book_Name,
        action='borrow'
    ).order_by(TrackHistory.timestamp.desc()).first()

    last_return = TrackHistory.query.filter_by(
        username=current_user.Username,
        book_name=book.Book_Name,
        action='return'
    ).order_by(TrackHistory.timestamp.desc()).first()

    if not last_borrow or (last_return and last_return.timestamp > last_borrow.timestamp):
        flash("❌ You haven't borrowed this book or already returned it.", "danger")
        return redirect(url_for("user.view_books"))

    history = TrackHistory(
        username=current_user.Username,
        book_name=book.Book_Name,
        author_name=book.Author_Name,
        genre=book.Genre_type,
        action='return'
    )
    db.session.add(history)
    book.Status = "Available"
    db.session.commit()
    flash("✅ Book returned successfully!", "success")
    return redirect(url_for("user.view_books"))
