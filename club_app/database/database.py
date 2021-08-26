
class DataBase:
    db = None

    @staticmethod
    def initialize(cluster):
        DataBase.db = cluster.db
    
    @staticmethod
    def add_club(data):
        DataBase.db.clubs.insert_one(data)

    @staticmethod
    def update_club(club, data):
        DataBase.db.clubs.update_one(club, data)

    @staticmethod
    def delete_club(club):
        DataBase.db.clubs.delete_one(club)

    @staticmethod
    def find_club(club):
        return DataBase.db.clubs.find_one({ "club name": club})

    @staticmethod
    def find_club_name(club):
        return Database.db.clubs.find_one({ "club name": club}) 


