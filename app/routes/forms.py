from flask_wtf import Form
from wtforms import IntegerField,SelectField,FloatField,SubmitField
from wtforms.validators import DataRequired,InputRequired
from app.utils import db_utils

class LoanForm(Form):

    amount_Credit_Request = FloatField(label='Amount Credit Request',validators=[InputRequired(),DataRequired("Should be a value > 0")])
    familyMembers = IntegerField(label='Family Members',validators=[InputRequired()])
    clientAge = SelectField(label="Client's Age",choices=db_utils.get_categorical_values('clientAge'))
    gender = SelectField(label='Gender',choices=db_utils.get_categorical_values('gender'))
    maritalStatus = SelectField(label='Marital Status',choices=db_utils.get_categorical_values('maritalStatus'))
    economicSector = SelectField(label='Economic Sector',choices=db_utils.get_categorical_values('economicSector'))
    economicSector = SelectField(label='Economic Sector',choices=db_utils.get_categorical_values('economicSector'))
    education = SelectField(label='Client Education',choices=db_utils.get_categorical_values('Education'))
    idType = SelectField(label='Client ID Type', choices = db_utils.get_categorical_values('idType'))
    AddressDistrict = SelectField(label='Address District',choices=db_utils.get_categorical_values('AddressDistrict'))
    amountbracket = SelectField(label='Amount Bracker',choices=db_utils.get_categorical_values('amountbracket'))
    branch = SelectField(label='Branch',choices=db_utils.get_categorical_values('branch'))
    Currency = SelectField(label='Currency',choices=db_utils.get_categorical_values('currency'))
    InterestRate = SelectField(label='Interest Rate',choices=db_utils.get_categorical_values('InterestRate',table_name='D_Interest'))
    newRepeated = SelectField(label= 'Loan New or Repeated?',choices=db_utils.get_categorical_values('newRepeated'))
    Product = SelectField(label='Product',choices = db_utils.get_categorical_values('product'))
    Purpose = SelectField(label='Purpose',choices = db_utils.get_categorical_values('purpose'))
    submit_button = SubmitField("PREDICT")