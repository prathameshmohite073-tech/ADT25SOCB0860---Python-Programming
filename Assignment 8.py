import re

text = "Data about gmails of students abc@email.com, xyz@gmail.com and pqr@edu.in for details."

pattern = r"[a-zA-Z0-9._*+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)
