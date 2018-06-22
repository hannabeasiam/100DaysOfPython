attendees = ["Hanna", "Kevin", "Stefan"]

# Add value in the list
attendees.append("Ashley")
# Add list to list
attendees.extend(["Greg", "Jiran"])

optional_invitees = ["ederm", "malica"]
potential_attendees = attendees + optional_invitees

print("There are", len(attendees), "attendees currently. ")

for attendee in attendees:
    print(attendee)

to_line = ", ".join(attendees)  # join convert list -> string
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("Cc: " + cc_line)

split_test = to_line.split(", ")    # split convert string -> list
print(split_test)
