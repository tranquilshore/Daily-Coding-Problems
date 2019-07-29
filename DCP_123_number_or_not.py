s = "10"
s = "-10"
s = "-10.23"
s = "10.03"
s = "10e3"
s = "-17e23"
s = "-10.54e2.33"
s = "-123.34e-6.34"


#123
def is_positive_integer(s):
	return s.isdigit()
#123.123
def is_positive_real(s):
	if s.count('.')!=1:
		return False
	
	integer_part, decimal_part = s.split('.')
	return is_positive_integer(integer_part) and is_positive_integer(decimal_part)

#-123
def is_negative_integer(s):
	return s.startswith('-') and is_positive_integer(s)

#-123.123
def is_negative_real(s):
	return s.startswith('-') and is_positive_real(s[1:])

#123 or 123.123
def is_positive_number(s):
	return is_positive_integer(s) or is_positive_real(s)

#-123 or -123.123
def is_negative_number(s):
	return is_negative_integer(s) or is_negative_real(s)

#-123.34e-6.34
def is_scientific_number(s):
	if s.count('e')!=1:
		return False 
	
	before_e,after_e = s.split('e')
	return is_positive_number(before_e) or is_negative_number(before_e) and is_negative_number(after_e) or is_negative_number(after_e)

def is_number(s):
	return is_positive_number(s) or is_negative_number(s) or is_scientific_number(s)

print is_number(s)

    
