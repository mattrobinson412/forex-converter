from flask import (Flask, request, render_template, session, redirect, flash)

from flask_debugtoolbar import DebugToolbarExtension

from decimal import *

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "NoWayHome"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

from converter import Currency


@app.route('/', methods=["GET", "POST"])
def landing_page():
    """Renders page containing form for the forex converter."""

    return render_template('home.html')


@app.route('/results', methods=["GET", "POST"])
def calculate_conversion():
    """Calculates conversion from initial currency to a
    new one based on the amount given."""

    init = request.form.get('init')
    final = request.form.get('final')
    amt = request.form.get('amount')

    try:
        amount = Decimal(amt)
    except:
        alert = "Please enter a valid number for the amount."
        flash(alert)
        return redirect('/')
    
    try:
        curr = Currency(init)
    except:
        alert = "Please enter a valid currency."
        flash(alert)
        return redirect('/')
    
    try:
        new_curr = Currency(final)
    except:
        alert_2 = "Please enter a valid currency."
        flash(alert_2)
        return redirect('/')

    try:
        converse = curr.convert_amount(init, final, amount)
        converted_val = round(converse, 2)
        converted_sym = curr.currency_symbol(final)   
    except:
        alert_3 = "Sorry! An error arose. Please check your values to see if they are valid."
        flash(alert_3)
        return redirect('/')
    
    return render_template('results.html', conv=converted_val, sym=converted_sym)
    

