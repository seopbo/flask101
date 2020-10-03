from sqlalchemy import text


class UserDao:
    def __init__(self, database):
        self.db = database

    def insert_user(self, user):
        return self.db.execute(text("""
            INSERT INTO users (
                name,
                email,
                profile,
                hashed_password
            ) VALUES (
                :name,
                :email,
                :profile,
                :password
            )
        """), user).lastrowid

    def get_user_id_and_password(self, email):
        row = self.db.execute(text("""    
            SELECT
                id,
                hashed_password
            FROM users
            WHERE email = :email
        """), {'email' : email}).fetchone()

        return {
            'id'              : row['id'],
            'hashed_password' : row['hashed_password']
        } if row else None

    def insert_follow(self, user_id, follow_id):
        return self.db.execute(text("""
            INSERT INTO users_follow_list (
                user_id,
                follow_user_id
            ) VALUES (
                :id,
                :follow
            )
        """), {
            'id'     : user_id,
            'follow' : follow_id
        }).rowcount

    def insert_unfollow(self, user_id, unfollow_id):
        return self.db.execute(text("""
            DELETE FROM users_follow_list
            WHERE user_id      = :id
            AND follow_user_id = :unfollow
        """), {
            'id'       : user_id,
            'unfollow' : unfollow_id
        }).rowcount

    def save_profile_picture(self, profile_pic_path, user_id):
        return self.db.execute(text("""
            UPDATE users 
            SET profile_picture = :profile_pic_path
            WHERE id            = :user_id
        """), {
            'user_id'          : user_id,
            'profile_pic_path' : profile_pic_path
        }).rowcount

    def get_profile_picture(self, user_id):
        row = self.db.execute(text("""
            SELECT profile_picture
            FROM users
            WHERE id = :user_id
        """), {
            'user_id' : user_id
        }).fetchone()

        return row['profile_picture'] if row else None
