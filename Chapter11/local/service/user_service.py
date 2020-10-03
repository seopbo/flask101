import os
import jwt
import bcrypt

from datetime import datetime, timedelta


class UserService:
    def __init__(self, user_dao, config):
        self.user_dao = user_dao
        self.config = config

    def create_new_user(self, new_user):
        new_user['password'] = bcrypt.hashpw(
            new_user['password'].encode('UTF-8'),
            bcrypt.gensalt()
        )

        new_user_id = self.user_dao.insert_user(new_user)

        return new_user_id

    def login(self, credential):
        email = credential['email']
        password = credential['password']
        user_credential = self.user_dao.get_user_id_and_password(email)

        authorized = user_credential and bcrypt.checkpw(password.encode('UTF-8'),
                                                        user_credential['hashed_password'].encode('UTF-8'))

        return authorized

    def generate_access_token(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
        }
        token = jwt.encode(payload, self.config.JWT_SECRET_KEY, 'HS256')

        return token.decode('UTF-8')

    def follow(self, user_id, follow_id):
        return self.user_dao.insert_follow(user_id, follow_id)

    def unfollow(self, user_id, unfollow_id):
        return self.user_dao.insert_unfollow(user_id, unfollow_id)

    def get_user_id_and_password(self, email):
        return self.user_dao.get_user_id_and_password(email)

    def save_profile_picture(self, picture, filename, user_id):
        profile_pic_path_and_name = os.path.join(self.config.UPLOAD_DIRECTORY, filename)  # 1
        picture.save(profile_pic_path_and_name)  # 2
        return self.user_dao.save_profile_picture(profile_pic_path_and_name, user_id)  # 3

    def get_profile_picture(self, user_id):
        return self.user_dao.get_profile_picture(user_id)