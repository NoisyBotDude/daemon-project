
class ClubDataBase:
    db = None

    @staticmethod
    def initialize(cluster):
        ClubDataBase.db = cluster.db

    @staticmethod
    def count():
        return ClubDataBase.db.clubs.count_documents({})

    @staticmethod
    def add_club(data):
        ClubDataBase.db.clubs.insert_one(data)

    @staticmethod
    def update_club(club, data):
        ClubDataBase.db.clubs.update_one(club, data)

    @staticmethod
    def delete_club(club):
        ClubDataBase.db.clubs.delete_one(club)

    @staticmethod
    def find_club(club):
        return ClubDataBase.db.clubs.find_one(
            {"club name": club},
            {
                "_id": 0
            })

    @staticmethod
    def find_club_name():
        club_names = []
        for name in ClubDataBase.db.clubs.find({}, {"club name": 1, "_id": 0}):
            club_names.append(name)
        return club_names


class AdminDataBase:

    db = None

    @staticmethod
    def initialize(cluster):
        AdminDataBase.db = cluster.db

    @staticmethod
    def add_admin(email, name, password):
        AdminDataBase.db.admins.insert_one({
            "email": email,
            "name": name,
            "password": password
        })

    @staticmethod
    def find_admin(email, password):
        admin_data = AdminDataBase.db.admins.find_one(
            {"email": email}, {"name": 1, "email": 1, "password": 1, "_id": 0})
        return admin_data

    @staticmethod
    def is_registered(email):
        if AdminDataBase.db.admins.find_one({"email": email}):
            return True
        else:
            return False
