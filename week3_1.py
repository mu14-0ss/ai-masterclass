def print_contact(contact):
    print(f"{contact['name']} | {contact['skills']} | {contact['city']}")

contacts = [
    {"name": "John", "city": "nairobi", "skills": "Python"},
    {"name": "Grace", "city": "mombasa", "skills": "Design"}
]

for contact in contacts:
    print_contact(contact)  # reuse the same code