contacts = [
    {"name": "James Otieno", "phone": "0712345678", "skills": "Cold Calling, CRM", "city": "Nairobi"},
    {"name": "Sarah Wanjiku", "phone": "0722987654", "skills": "Lead Generation, Email", "city": "Mombasa"},
    {"name": "Brian Kamau", "phone": "0733112233", "skills": "Appointment Setting, Sales", "city": "Athi River"},
    {"name": "Grace Akinyi", "phone": "0744556677", "skills": "Customer Service, HubSpot", "city": "Kisumu"},
    {"name": "David Mutua", "phone": "0755667788", "skills": "LinkedIn Outreach, Follow-up", "city": "Nakuru"}
]

# Add one more contact
contacts.append ({
    "name": "kelvin muoka",
    "phone": "0798989898",
    "skills": "bee keeper",
    "city": "nairobi"
})

#display all contacts
print("===CONTACT BOOK===")
for contact in contacts:
    if contact["city"] == "nairobi":
        print(f" {contact ['name']} | {contact['skills']}")

#summary
print ("===NAIROBI CONTACTS===")
count = 0
for contact in contacts:
    if contact["city"] == "nairobi":
        print (
            f"{contact['name']} | {contact['skills']}")
        count +=1

print(f"\nTotal Nairobi Contacts: {count}")