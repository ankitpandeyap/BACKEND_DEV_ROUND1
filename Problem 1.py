import re
input_no = input()
reg_Exp = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
if re.search(reg_Exp, input_no):
    print("Valid")
else:
    print("Invalid")