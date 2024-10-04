from odoo import models, fields, api

class ApiModelCreateMulti(models.Model):
    _name = 'ma.api.model.create.multi'
    _description = "The @api.model decorator in Odoo is used to define methods that can be called on the model level, allowing operations like creating multiple records at once."
    name = fields.Char(string='Name')
    city_name= fields.Char(string="City Name")
    city_people = fields.Integer(string='Population')

    @api.model_create_multi
    def create(self, vals_list):
        records = super(ApiModelCreateMulti, self).create(vals_list)
        for record in records:
            if record.city_name:
                self._increment_city_people(record.city_name)

        return records

    def _increment_city_people(self, city_name):
        # Search for all records with the specified city_name
        records = self.search([('city_name', '=', city_name)])
        for record in records:
            record.city_people += 1  # Increment city_people by 1

    @api.model
    def create_multiple_records(self,*args):
        data = [
            {'name': 'Raj', 'city_name': 'Ahmedabad', 'city_people': 0},
            {'name': 'Aditi', 'city_name': 'Surat', 'city_people': 0},
            {'name': 'Vikram', 'city_name': 'Vadodara', 'city_people': 0},
            {'name': 'Sneha', 'city_name': 'Rajkot', 'city_people': 0},
            {'name': 'Kunal', 'city_name': 'Gandhinagar', 'city_people': 0},
            {'name': 'Priya', 'city_name': 'Bhavnagar', 'city_people': 0},
            {'name': 'Ravi', 'city_name': 'Junagadh', 'city_people': 0},
            {'name': 'Neha', 'city_name': 'Anand', 'city_people': 0},
            {'name': 'Manish', 'city_name': 'Nadiad', 'city_people': 0},
            {'name': 'Meera', 'city_name': 'Dahod', 'city_people': 0},
            {'name': 'Akash', 'city_name': 'Palanpur', 'city_people': 0},
            {'name': 'Isha', 'city_name': 'Morbi', 'city_people': 0},
            {'name': 'Rohan', 'city_name': 'Navsari', 'city_people': 0},
            {'name': 'Pooja', 'city_name': 'Gandhinagar', 'city_people': 0},
            {'name': 'Jay', 'city_name': 'Valsad', 'city_people': 0},
            {'name': 'Sanjay', 'city_name': 'Bharuch', 'city_people': 0},
            {'name': 'Nisha', 'city_name': 'Surendranagar', 'city_people': 0},
            {'name': 'Tarun', 'city_name': 'Kutch', 'city_people': 0},
            {'name': 'Geeta', 'city_name': 'Mehsana', 'city_people': 0},
            {'name': 'Rajesh', 'city_name': 'Gandhinagar', 'city_people': 0},
            {'name': 'Anjali', 'city_name': 'Sabarmati', 'city_people': 0},
            {'name': 'Aarav', 'city_name': 'Godhra', 'city_people': 0},
            {'name': 'Kavita', 'city_name': 'Vapi', 'city_people': 0},
            {'name': 'Deepak', 'city_name': 'Diu', 'city_people': 0},
            {'name': 'Simran', 'city_name': 'Dwarka', 'city_people': 0},
            {'name': 'Harsh', 'city_name': 'Gir Somnath', 'city_people': 0},
            {'name': 'Maya', 'city_name': 'Bhuj', 'city_people': 0},
            {'name': 'Ritik', 'city_name': 'Sihor', 'city_people': 0},
            {'name': 'Sonia', 'city_name': 'Wadhwan', 'city_people': 0},
            {'name': 'Vishal', 'city_name': 'Bardoli', 'city_people': 0},
            {'name': 'Riya', 'city_name': 'Khambhalida', 'city_people': 0},
            {'name': 'Aditya', 'city_name': 'Narmada', 'city_people': 0},
            {'name': 'Divya', 'city_name': 'Dahod', 'city_people': 0},
            {'name': 'Nitin', 'city_name': 'Patan', 'city_people': 0},
            {'name': 'Kiran', 'city_name': 'Kheda', 'city_people': 0},
            {'name': 'Amit', 'city_name': 'Banswara', 'city_people': 0},
            {'name': 'Chaitali', 'city_name': 'Madhavpur', 'city_people': 0},
            {'name': 'Himanshu', 'city_name': 'Dharampur', 'city_people': 0},
            {'name': 'Shivani', 'city_name': 'Amreli', 'city_people': 0},
            {'name': 'Abhishek', 'city_name': 'Ankleshwar', 'city_people': 0},
            {'name': 'Ritika', 'city_name': 'Bhuj', 'city_people': 0},
            {'name': 'Gaurav', 'city_name': 'Vijapur', 'city_people': 0},
            {'name': 'Lavanya', 'city_name': 'Bhavnagar', 'city_people': 0},
            {'name': 'Dev', 'city_name': 'Jamnagar', 'city_people': 0},
            {'name': 'Rachna', 'city_name': 'Gandhidham', 'city_people': 0},
            {'name': 'Shreyas', 'city_name': 'Upleta', 'city_people': 0},
            {'name': 'Shweta', 'city_name': 'Kankrej', 'city_people': 0},
            {'name': 'Rahul', 'city_name': 'Sihor', 'city_people': 0},
            {'name': 'Ayesha', 'city_name': 'Ranavav', 'city_people': 0},
            {'name': 'Sunny', 'city_name': 'Talaja', 'city_people': 0},
            {'name': 'Tanya', 'city_name': 'Lathi', 'city_people': 0},
            {'name': 'Pankaj', 'city_name': 'Sihor', 'city_people': 0},
            {'name': 'Anupama', 'city_name': 'Bardoli', 'city_people': 0},
            {'name': 'Nakul', 'city_name': 'Shahibaug', 'city_people': 0},
            {'name': 'Meenal', 'city_name': 'Vapi', 'city_people': 0},
            {'name': 'Samir', 'city_name': 'Kutch', 'city_people': 0},
            {'name': 'Chirag', 'city_name': 'Veraval', 'city_people': 0},
            {'name': 'Surbhi', 'city_name': 'Rajkot', 'city_people': 0},
            {'name': 'Vimal', 'city_name': 'Jasdan', 'city_people': 0},
            {'name': 'Aarushi', 'city_name': 'Rapar', 'city_people': 0},
            {'name': 'Niraj', 'city_name': 'Bhuj', 'city_people': 0},
            {'name': 'Palak', 'city_name': 'Surendranagar', 'city_people': 0},
            {'name': 'Neelam', 'city_name': 'Mehsana', 'city_people': 0},
            {'name': 'Yash', 'city_name': 'Talaja', 'city_people': 0},
            {'name': 'Vidya', 'city_name': 'Bharuch', 'city_people': 0},
            {'name': 'Shailesh', 'city_name': 'Palanpur', 'city_people': 0},
            {'name': 'Nayana', 'city_name': 'Upleta', 'city_people': 0},
            {'name': 'Ashok', 'city_name': 'Jamnagar', 'city_people': 0},
            {'name': 'Kavish', 'city_name': 'Kutch', 'city_people': 0},
            {'name': 'Diya', 'city_name': 'Himmatnagar', 'city_people': 0},
            {'name': 'Keshav', 'city_name': 'Bhavnagar', 'city_people': 0},
            {'name': 'Swati', 'city_name': 'Navsari', 'city_people': 0},
            {'name': 'Bharat', 'city_name': 'Diu', 'city_people': 0},
            {'name': 'Tanvi', 'city_name': 'Gandhinagar', 'city_people': 0},
            {'name': 'Jayesh', 'city_name': 'Sihor', 'city_people': 0},
            {'name': 'Priti', 'city_name': 'Bharuch', 'city_people': 0},
            {'name': 'Vijay', 'city_name': 'Vadodara', 'city_people': 0},
            {'name': 'Priyanka', 'city_name': 'Ahmedabad', 'city_people': 0},
            {'name': 'Hardik', 'city_name': 'Rajkot', 'city_people': 0},
            {'name': 'Simran', 'city_name': 'Bhuj', 'city_people': 0},
            {'name': 'Devika', 'city_name': 'Surat', 'city_people': 0},
            {'name': 'Nitesh', 'city_name': 'Navsari', 'city_people': 0},
            {'name': 'Kiran', 'city_name': 'Kutch', 'city_people': 0},
            {'name': 'Parul', 'city_name': 'Gandhinagar', 'city_people': 0},
            {'name': 'Ravina', 'city_name': 'Vadodara', 'city_people': 0},
        ]
        self.create(data)
