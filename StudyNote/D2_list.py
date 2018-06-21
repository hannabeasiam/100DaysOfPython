attendees = ["Hanna", "Kevin", "Stefan"]

# Add value in the list
attendees.append("Ashley")
# Add list to list
attendees.extend(["Greg", "Jiran"])

optional_invitees = ["ederm", "malica"]
potential_attendees = attendees + optional_invitees

print("There are", len(attendees), "attendees currently. ")
