from flask import Flask, render_template, request, flash,session, redirect
import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = "chicken123"



@app.route('/')
def show_form():
    """Displays form to convert currency"""
    return render_template('currency_form.html')

@app.route('/convert', methods=['POST'])
def submit_form():
    """Handles form submission"""
    currencyFrom = request.form['from'].upper()
    currencyTo = request.form['to'].upper()
    Amount = float(request.form.get['amount'])
    # if not Amount:
    #    flash ("must enter numerical value")
    #    return redirect('/')
    
    
    
    valid_currency_codes = requests.get('http://api.exchangerate.host/list?access_key=0b39e76fdf15c90ece4e1736d13383cd')
    all_currencies = valid_currency_codes.json()['currencies']
    if len(currencyFrom) == 0 or len(currencyTo) == 0:
       flash("must input data in all spaces")
       return redirect('/')
    
    elif currencyFrom not in all_currencies:
       flash("'from' currency not in database")
       return redirect('/')
    #  raise KeyError(" 'from' currency not in database")
    elif currencyTo not in all_currencies:
        flash(" 'to' currency not in database")
        return redirect('/')

    #  raise KeyError(" 'to' currency not in database")
    elif not isinstance(Amount, float):
       flash("must enter a proper numerical amount")
       return redirect('/')

      # raise ValueError("must enter a proper numerical amount")

    else: 
     url = requests.get(f'http://api.exchangerate.host/convert?access_key=0b39e76fdf15c90ece4e1736d13383cd&from={currencyFrom}&to={currencyTo}&amount={Amount}')
    Result = url.json()['result']
    roundedResult = round(Result,2)
    return render_template('currency_form.html', currency_from=currencyFrom, currency_to=currencyTo, amount=Amount, conversion_result=roundedResult)
    
 

  

   
