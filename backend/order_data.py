import sheets_api

class CustomerData:
    def __init__(self, timestamp, email, delivery_method, payment_method, legal_entity, cif, company, registration_number,
                 last_name, first_name, address, county, city, postal_code, phone, delivery_to_other_address=False,
                 alt_last_name=None, alt_first_name=None, alt_address=None, alt_county=None, alt_city=None,
                 alt_postal_code=None, alt_phone=None):
        self.timestamp = timestamp
        self.email = email
        self.delivery_method = delivery_method
        self.payment_method = payment_method
        self.legal_entity = legal_entity
        self.cif = cif
        self.company = company
        self.registration_number = registration_number
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.county = county
        self.city = city
        self.postal_code = postal_code
        self.phone = phone
        self.delivery_to_other_address = delivery_to_other_address
        self.alt_last_name = alt_last_name
        self.alt_first_name = alt_first_name
        self.alt_address = alt_address
        self.alt_county = alt_county
        self.alt_city = alt_city
        self.alt_postal_code = alt_postal_code
        self.alt_phone = alt_phone

    def to_list(self):
        # Define the order of columns
        columns = [
            self.timestamp, self.email, self.delivery_method, self.payment_method, self.legal_entity, self.cif,
            self.company, self.registration_number, self.last_name, self.first_name, self.address, self.county,
            self.city, self.postal_code, self.phone, self.delivery_to_other_address, self.alt_last_name,
            self.alt_first_name, self.alt_address, self.alt_county, self.alt_city, self.alt_postal_code, self.alt_phone
        ]
        # Convert to a list
        return columns

# USAGE TESTS

if __name__ == '__main__':
    # Example usage:
    customer = CustomerData("2023-08-31", "customer@example.com", "Express", "Credit Card", "Legal Entity", "123456", 
                        "Company ABC", "7890", "Doe", "John", "123 Main St", "County A", "City X", "12345", 
                        "555-123-4567", True, "Smith", "Jane", "456 Secondary St", "County B", "City Y", "54321", 
                        "555-987-6543")

    # Generate a list for the Google Sheet
    data_list = customer.to_list()

    # Print the generated list
    print(data_list)
    # Create a customer with missing alternative address information
    customer1 = CustomerData("2023-09-01", "customer1@example.com", "Standard", "PayPal", False,  None, 
                            None, None, "1234", "Smith", "Alice", "456 Park Ave", "County C", "City Z", "67890", 
                            "555-555-5555")

    # Create a customer with no alternative address
    customer2 = CustomerData("2023-09-02", "customer2@example.com", "Express", "Credit Card", "Legal Entity", "456789", 
                            "Company DEF", "5678", "Brown", "Bob", "789 Oak St", "County D", "City W", "45678", 
                            "555-111-2222", False)

    # Create a customer with missing contact information
    customer3 = CustomerData("2023-09-03", "customer3@example.com", "Standard", "Bank Transfer", "Individual", None, 
                            None, None, "Johnson", "Eve", "890 Elm Rd", "County E", "City V", "23456", "0723660642")

    # Generate lists for each customer's data
    data_list1 = customer1.to_list()
    data_list2 = customer2.to_list()
    data_list3 = customer3.to_list()

    # Print the generated lists
    print(data_list1)
    print(data_list2)
    print(data_list3)

    sheets_api.Add_Raw_Order_Data(data_list)
    sheets_api.Add_Raw_Order_Data(data_list1)
    sheets_api.Add_Raw_Order_Data(data_list2)
    sheets_api.Add_Raw_Order_Data(data_list3)

