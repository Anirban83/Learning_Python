# Exploring different string formats and functions

# Using single and double quotes
message = "India is playing in the final."
print(message)
message = 'The final match is at Eden Gardens.'
print(message)
message = "This is India's first ever final match."
print(message)
message = 'The name of the tournament is "World Series".'
print(message)

# Bad code
# message = 'This is Mr.Fuller's final match as umpire.'
# print(message)

# Changing Case
first_name = "mr. kishan"
last_name = "yadav"
address = "10 sherwood street"
city = "LONDON"

print(first_name.capitalize())
print(last_name.upper())
print(address.title())
print(city.lower())
print(first_name)

# Formatted strings
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}"
print(message)

# Adding whitespaces (tabs and newlines)
print("Language\tPython")
print("Languages:\n\tPyhton\n\tDotNet\n\tAngular")

# Removing whitespaces
message = "   This sentence has spaces at the begining and end.     "
print(message.rstrip())
print(message.lstrip())
print(message.strip())

# Removing prefix and suffix
python_url = "https://wiki.python.org/moin/BeginnersGuide"
python_filename = "strings.py"
print(python_url.removeprefix("https://"))
print(python_filename.removesuffix(".py"))
