from wtforms.validators import ValidationError

def clean_data():
	message = 'No spaces or special characters allowed'
	def _clean_data(form, field):
		val = field.data
		if "\'" in val or "\"" in val or "<" in val or '*' in val or '>' in val or " " in val:
			raise ValidationError(message)
	return _clean_data

def clean_data_wspaces():
	def _clean_data(form, field):
		val = field.data
		if "\"" in val or "<" in val or '*' in val or '>' in val:
			raise ValidationError('No special characters allowed')
	return _clean_data