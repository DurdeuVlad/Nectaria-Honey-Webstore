import time
from flask import Flask, render_template, request, redirect, url_for
from order_data import CustomerData
import sheets_api

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        email = request.form['email']
        delivery_method = request.form['delivery_method']
        payment_method = request.form['payment_method']
        legal_entity = request.form.get('legal_entity') == 'on'
        cif = request.form['cif']
        company = request.form['company']
        registration_number = request.form['registration_number']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        address = request.form['address']
        county = request.form['county']
        city = request.form['city']
        postal_code = request.form['postal_code']
        phone = request.form['phone']
        delivery_to_other_address = request.form.get('delivery_to_other_address') == 'on'
        alt_last_name = request.form['alt_last_name']
        alt_first_name = request.form['alt_first_name']
        alt_address = request.form['alt_address']
        alt_county = request.form['alt_county']
        alt_city = request.form['alt_city']
        alt_postal_code = request.form['alt_postal_code']
        alt_phone = request.form['alt_phone']

        # Create a CustomerData object with the form data
        customer = CustomerData(timestamp, email, delivery_method, payment_method, legal_entity, cif, company,
                                registration_number, last_name, first_name, address, county, city, postal_code, phone,
                                delivery_to_other_address, alt_last_name, alt_first_name, alt_address, alt_county,
                                alt_city, alt_postal_code, alt_phone)

        # Assuming you have a sheets_api function to add the data to Google Sheets
        sheets_api.Add_Data(customer.to_list())

        # Redirect to a thank you page or display a success message
    message = "Your order was successfully placed!"

    return render_template('test_form_full.html', message="")

if __name__ == '__main__':
    app.run()
