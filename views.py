"""
Routes and views for the flask application.
"""
import mysql.connector
from datetime import datetime
#from flask import render_template
from FWInvetorySystem import app
from flask import Flask, render_template, request
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask import render_template
from FWInvetorySystem import app
#mysql.connector database connection
msqldb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="ims"
)
sqlcursor = msqldb.cursor()
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/Invoice')
def Invoice():
    """Renders the home page."""
    return render_template(
        'Invoice.html',
        title='Invoice Page',
        year=datetime.now().year,
    )


@app.route('/sales')
def sales():
    """Renders the home page."""
    return render_template(
        'sales.html',
        title='sales Page',
        year=datetime.now().year,
    )


@app.route('/Purchase')
def Purchase():
    """Renders the home page."""
    return render_template(
        'Purchase.html',
        title='Purchase Page',
        year=datetime.now().year,
    )




@app.route('/Register')
def Register():
    """Renders the home page."""
    return render_template(
        'Registration.html',
        title='Registration Page',
        year=datetime.now().year,
    )

@app.route('/customer.')
def customer():
    """Renders the home page."""
    return render_template(
        'customer.html',
        title='customer. Page',
        year=datetime.now().year,
    )

@app.route('/search.')
def search():
    """Renders the home page."""
    return render_template(
        'search.html',
        title='search. Page',
        year=datetime.now().year,
    )



@app.route('/SearchPurchase.')
def SearchPurchase():
    """Renders the home page."""
    return render_template(
        'SearchPurchase.html',
        title='SearchPurchase. Page',
        year=datetime.now().year,
    )


@app.route('/SearchSales')
def SearchSales():
    """Renders the home page."""
    return render_template(
        'SearchSales.html',
        title='SearchSales. Page',
        year=datetime.now().year,
    )


@app.route('/SearchInvoice')
def SearchInvoice():
    """Renders the home page."""
    return render_template(
        'SearchInvoice.html',
        title='SearchInvoice. Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/Userregistration', methods=['GET', 'POST'])
def Userregistration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        country = request.form['country']
        cursor = msqldb.cursor()
        cursor.execute("INSERT INTO registration(username, password, email, phone, address, city, state, zip, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (username, password, email, phone, address, city, state, zip, country))
        msqldb.commit()
        cursor.close()
        return redirect(url_for('Userregistration'))
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        cursor = msqldb.cursor()
        msql="SELECT * FROM registration WHERE username = '" + user +  "' and password= '" + password + "'"  
        cursor.execute(msql)
        account = cursor.fetchone()
        if account:
            msg = 'Logged in successfully !'
            return render_template('Home.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html')





@app.route('/CustomerReg', methods=['GET', 'POST'])
def CustomerReg():
    if request.method == 'POST':
        Fullname = request.form['Fullname']
        Address = request.form['Address']
        City = request.form['City']
        State = request.form['State']
        Zip = request.form['Zip']
        Country = request.form['Country']
        Email = request.form['Email']
        Phone = request.form['Phone']
        Username = request.form['Username']
       
        cr = msqldb.cursor()
        cr.execute("INSERT INTO customer (Fullname, Address, City, State, Zip, Country, Email, Phone, Username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Fullname, Address, City, State, Zip, Country, Email, Phone, Username))
        msqldb.commit()
        cr.close()
        return redirect(url_for('CustomerReg'))
    return render_template('Home.html')
  


#Search customer by username
@app.route('/searchCustomer', methods=['GET', 'POST'])
def searchCustomer():
    if request.method == 'POST':
        search = request.form['search']
        cur = msqldb.cursor()
        
        msql="SELECT * FROM customer WHERE fullname like '%" + search+ "%'"
        cur.execute(msql)
        cust = cur.fetchall()
        if cust:
            #userDetails = cur.fetchall()
            return render_template('searchResult.html', userDetails=cust)
        else:
            msg = 'No Record Found'
            return render_template('searchResult.html', msg=msg)
        cur.close()
    return render_template('search.html')

@app.route('/PurchaseSave', methods=['GET', 'POST'])
def PurchaseSave():
    if request.method == 'POST':
        productID = request.form['productID']
        productName = request.form['productName']
        price = request.form['price']
        quantity = request.form['quantity']
        total = request.form['total']
        date = request.form['date']
        cr = msqldb.cursor()
        cr.execute("INSERT INTO purchase (productID, productName, price, quantity, total, date) VALUES (%s, %s, %s, %s, %s, %s)", (productID, productName, price, quantity, total, date))
        msqldb.commit()
        cr.close()
        return redirect(url_for('PurchaseSave'))
    return render_template('purchase.html')


@app.route('/salesSave', methods=['GET', 'POST'])
def salesSave():
    if request.method == 'POST':
        product = request.form['product']
        price = request.form['price']
        quantity = request.form['quantity']
        total = request.form['total']
        date = request.form['date']
        cr = msqldb.cursor()
        cr.execute("INSERT INTO sales (product, price, quantity, total, date) VALUES (%s, %s, %s, %s, %s)", (product, price, quantity, total, date))
        msqldb.commit()
        cr.close()
        return redirect(url_for('salesSave'))
    return render_template('sales.html')



@app.route('/InvoiceeSave', methods=['GET', 'POST'])   
def InvoiceeSave():
    if request.method == 'POST':
        CustomerUsername = request.form['CustomerUsername']
        product = request.form['product']
        quantity = request.form['quantity']
        Amount = request.form['Amount']
        date = request.form['date']
        cr = msqldb.cursor()
        cr.execute("INSERT INTO invoice (CustomerUsername, product, quantity, Amount, date) VALUES (%s, %s, %s, %s, %s)", (CustomerUsername, product, quantity, Amount, date))
        msqldb.commit()
        cr.close()
        return redirect(url_for('InvoiceeSave'))
    return render_template('invoice.html')

#Search customer by username
@app.route('/searchsl', methods=['GET', 'POST'])
def searchsl():
    if request.method == 'POST':
        search = request.form['search']
        cur = msqldb.cursor()
        
        msql="SELECT * FROM sales WHERE product like '%" + search+ "%'"
        cur.execute(msql)
        sale = cur.fetchall()
        if sale:
            #userDetails = cur.fetchall()
            return render_template('searchsalesResult.html', userDetails=sale)
        else:
            msg = 'No Record Found'
            return render_template('searchsaleResult.html', msg=msg)
        cur.close()
    return render_template('search.html')

@app.route('/searchInvoiceData', methods=['GET', 'POST'])
def searchInvoiceData():
    if request.method == 'POST':
        search = request.form['search']
        cur = msqldb.cursor()
        
        msql="SELECT * FROM invoice WHERE CustomerUsername like '%" + search+ "%'"
        cur.execute(msql)
        sale = cur.fetchall()
        if sale:
            #userDetails = cur.fetchall()
            return render_template('searchinvoiceResult.html', userDetails=sale)
        else:
            msg = 'No Record Found'
            return render_template('searchinvoiceResult.html', msg=msg)
        cur.close()
    return render_template('search.html')


@app.route('/searchpurchaseproduct', methods=['GET', 'POST'])
def searchpurchaseproduct():
    if request.method == 'POST':
        search = request.form['search']
        cur = msqldb.cursor()
        
        msql="SELECT * FROM purchase WHERE productName like '%" + search+ "%'"
        cur.execute(msql)
        sale = cur.fetchall()
        if sale:
            #userDetails = cur.fetchall()
            return render_template('searchpurchaseproduct.html', userDetails=sale)
        else:
            msg = 'No Record Found'
            return render_template('searchpurchaseproduct.html', msg=msg)
        cur.close()
    return render_template('search.html')
