from datetime import datetime
import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
client = MongoClient(
    os.getenv("DATABASE_URL", int(os.getenv("DATABASE_PORT"))))

db = client[os.getenv("DATABASE_NAME")]


class Post:
    id = 0
    # TODO: find in DB the last id generated and increment from there

    def __init__(
            self,
            title: str,
            author: str,
            tags: list,
            content: str
            ):
        self.id = Post.generate_id()
        self.created_at = datetime.utcnow()
        self.updated_at = Post.update_time()
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    @staticmethod
    def generate_id():

        """Method to generate numeric id for posts"""

        Post.id += 1
        return Post.id

    def update_time():
        Post.updated_at = datetime.utcnow()

    def save(self):

        """Method to save posts in data base in dict format"""
        data = db.posts.insert_one(self.__dict__)
        if data:
            return data

    def get_all():

        """Method to find a post, delete its UID
        from mongo and return a list"""

        data = list(db.posts.find())
        for key in data:
            del key["_id"]
        return data

    def get_post_by_id(requested_id):

        """Method to find a specific post through id received via url params,
        delete its UID from mongo and return a list"""

        data = list(db.posts.find({"id": requested_id}))
        for key in data:
            del key["_id"]
        return data

    def delete_post_by_id(requested_id):

        """method to find post by id and delete it"""

        try:
            data = db.posts.find_one_and_delete({"id": requested_id})
            del data["_id"]
            return True
        except:
            return False
        # TODO: raise exception

    def update_post_by_id(id, post):

        """method to find post via id and update it"""

        try:
            data = db.posts.find_one_and_update({"id": id}, {"$set": post})
            del data["id"]
            return data
        except:
            return {"msg": "Id não encontrado ou chaves inválidas"}, 404

    def serialized(self):

        """Object serialization"""

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "tags": self.tags,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

# validation for post, containing all keys
# validation for patching invalid posts
# requiring an unexisting post, trying to patch it or delete it
