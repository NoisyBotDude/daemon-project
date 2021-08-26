from typing import Container


def organise_data(data):

    organised_data = {key: value for key,value in data.items() if key != "club core members" or key != "club contact details"}

    member_list = data["club core members"].split(".")
    contact_list = data["club contact details"].split(".")

    club_member = []    
    club_contact = []

    for i in range(len(member_list)):
        member = member_list[i].split(",")
        member_details = {"name": member[0], "designation": member[1]}
        club_member.append(member_details)


    for i in range(len(contact_list)):
        contact = contact_list[i].split(",")
        contact_details = {"name": contact[0], "contact": contact[1]}
        club_contact.append(contact_details)

    data["club core members"] = club_member
    data["club contact details"] = club_contact

    return data
   
    
    