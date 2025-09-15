from flask import Blueprint, render_template, redirect, url_for, request
from .models import Meal, PlannedMeal
from .forms import MealForm
from . import db
from .utils import generate_grocery_list

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    meals = Meal.query.all()
    return render_template('index.html', meals=meals)

@bp.route('/add', methods=['GET', 'POST'])
def add_meal():
    form = MealForm()
    if form.validate_on_submit():
        meal = Meal(name=form.name.data, ingredients=form.ingredients.data)
        db.session.add(meal)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_meal.html', form=form)

@bp.route('/plan', methods=['GET', 'POST'])
def plan():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meals = Meal.query.all()
    if request.method == 'POST':
        # Remove old plan
        PlannedMeal.query.delete()
        db.session.commit()
        for day in days:
            meal_id = request.form.get(day)
            if meal_id:
                planned = PlannedMeal(day=day, meal_id=int(meal_id))
                db.session.add(planned)
        db.session.commit()
        return redirect(url_for('main.view_plan'))
    return render_template('plan.html', days=days, meals=meals)

@bp.route('/view_plan')
def view_plan():
    planned = PlannedMeal.query.all()
    # organize by day
    plan_by_day = { p.day: p.meal for p in planned }
    return render_template('view_plan.html', plan=plan_by_day)

@bp.route('/grocery')
def grocery():
    planned = PlannedMeal.query.all()
    grocery_list = generate_grocery_list(planned)
    return render_template('grocery.html', groceries=grocery_list)
