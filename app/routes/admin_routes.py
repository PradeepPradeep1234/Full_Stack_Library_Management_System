from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models.book import Add_Book
from app.models.track_history import TrackHistory
from app import db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin_dashboard")
@login_required
def admin_dashboard():
    if current_user.Role != "admin":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for("user.view_books"))
    return render_template("admin_page.html")

@admin_bp.route("/add_books", methods=["GET", "POST"])
@login_required
def add_books():
    if current_user.Role != "admin":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for("user.view_books"))

    if request.method == "POST":
        obj = Add_Book(
            Book_Name=request.form["b_name"],
            Author_Name=request.form["a_name"],
            Status=request.form["status"],
            Book_id=request.form["b_id"],
            Genre_type=request.form["b_genre"]
        )
        db.session.add(obj)
        db.session.commit()
        flash("✅ Book Added Successfully!", "success")
        return redirect(url_for('admin.admin_dashboard'))
    return render_template("add_book.html")

@admin_bp.route("/update_books_list")
@login_required
def update_books_list():
    if current_user.Role != "admin":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for("user.view_books"))
    books = Add_Book.query.all()
    return render_template("update_books_list.html", books=books)

@admin_bp.route("/update_book/<int:id>", methods=["GET", "POST"])
@login_required
def update_books(id):
    if current_user.Role != "admin":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for("user.view_books"))
    obj = Add_Book.query.get_or_404(id)
    if request.method == "POST":
        obj.Book_Name = request.form["b_name"]
        obj.Author_Name = request.form["a_name"]
        obj.Status = request.form["status"]
        obj.Book_id = request.form["b_id"]
        obj.Genre_type = request.form["b_genre"]
        db.session.commit()
        flash("✏️ Book updated successfully.", "info")
        return redirect(url_for('user.view_books'))
    return render_template("update_book.html", data=obj)

@admin_bp.route("/delete")
@login_required
def delete_books():
    if current_user.Role != "admin":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for("user.view_books"))
    obj = Add_Book.query.all()
    return render_template("delete_books.html", data=obj)

@admin_bp.route("/delete_books/<int:id>", methods=["GET", "POST"])
@login_required
def del_books(id):
    if current_user.Role != "admin":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for("user.view_books"))
    obj = Add_Book.query.get_or_404(id)
    db.session.delete(obj)
    db.session.commit()
    flash("🗑️ Book deleted successfully.", "info")
    return redirect(url_for('admin.delete_books'))

@admin_bp.route("/track_history")
@login_required
def track_history():
    if current_user.Role != "admin":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for("user.view_books"))
    history = TrackHistory.query.order_by(TrackHistory.timestamp.desc()).all()
    return render_template("track_history.html", history=history)

@admin_bp.route("/clear_track_history", methods=["POST"])
@login_required
def clear_track_history():
    if current_user.Role != "admin":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for("user.view_books"))
    TrackHistory.query.delete()
    db.session.commit()
    flash("🧹 Track history cleared successfully.", "info")
    return redirect(url_for("admin.track_history"))
