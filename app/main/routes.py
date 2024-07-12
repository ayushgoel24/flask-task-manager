# app/main/routes.py
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.models import Task
from app.main.forms import TaskForm
from app.main import bp

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('main/index.html', title='Home', tasks=tasks)

@bp.route('/add_task', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, author=current_user)
        db.session.add(task)
        db.session.commit()
        flash('Your task is now live!')
        return redirect(url_for('main.index'))
    return render_template('main/add_task.html', title='Add Task', form=form)

@bp.route('/delete_task/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.author != current_user:
        return redirect(url_for('main.index'))
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/toggle_task/<int:id>', methods=['POST'])
@login_required
def toggle_task(id):
    task = Task.query.get_or_404(id)
    if task.author != current_user:
        return redirect(url_for('main.index'))
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))
