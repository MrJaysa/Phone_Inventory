from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange
from .cleaners import clean_data_wspaces
from App.Model import Store, db


class Form(FlaskForm):
	item 	 = 	StringField(
						validators=[
							DataRequired(),
							clean_data_wspaces()
						]
					)

	price 	=	IntegerField(
					validators=[
						InputRequired(), 
						NumberRange(min=10, max=2000000)
					]
				)
	

	def validate(self):
		if super(Form, self).validate():
			store = Store()
			store.create(
				item = self.item.data,
				price= self.price.data
			)
			store.save()
			return True

		else:
			return False