import getpass
def check_password(password):
  if len(password)<8:
    return "WEAK","Password must contain at least 8 characters."
  has_upper=any(char.isupper() for char in password)
  has_digit=any(char.isdigit() for char in password)
  has_symbol=any(not char.isalnum() for char in password)

  if not (has_upper and has_digit and has_symbol):
   return "WEAK", "Include uppercase letters, numbers and symbols."
  else:
   return "STRONG", "Your password is strong."

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("          PASSWORD STRENGTH CHECKER     ")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
password=getpass.getpass("Enter your password : ")
strength,message= check_password(password)
print("\nPassword Strength :",strength)
print("Result :",message)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

