email = input("Enter your e-mail: ")
if '@' not in email:
    print("Error! e-mail must have @.")
else:
    local, domain = email.split('@')   
    if '.' not in domain:
        print("Error! Domain must have '.' .")
    else:
        main_domain = domain.rsplit('.', 1)[0]
        print(f"Valid e-mail. Domain: '{main_domain}'")

print("-" * 30)

password = input("Enter your password: ")
errors = []
if len(password) < 8:
    errors.append("Password must have at least 8 characters.")
if not any(c.isupper() for c in password):
    errors.append("Password must have at least one uppercase letter.")
if not any(c.isdigit() for c in password):
    errors.append("Password must have at least one digit.")
if errors:
    print("Password is weak:")
    for err in errors:
        print("-", err)
else:
    print("Password is strong.")

print("-" * 30)

date = input("Birthday date (YYYY-MM-DD): ")
parts = date.split('-')
if len(parts) != 3:
    print("Invalid date format.")
else:
    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        print("Error! Date must contain only digits.")
    elif not (1 <= int(month) <= 12):
        print("Error! Month must be between 1 and 12.")
    elif not (1 <= int(day) <= 31):
        print("Error! Day must be between 1 and 31.")
    else:
        formatted_date = f"{int(day):02d}/{int(month):02d}/{int(year):04d}"
        print(f"Formatted date: '{formatted_date}'")