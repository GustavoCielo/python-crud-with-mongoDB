from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


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
        self.updated_at = datetime.utcnow()
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    @staticmethod
    def generate_id():
        """Method to generate numeric id for posts"""
        Post.id += 1
        return Post.id

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
        try:
            data = db.posts.find_one_and_delete({"id": requested_id})
            del data["_id"]
            return True
        except:
            return False

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
