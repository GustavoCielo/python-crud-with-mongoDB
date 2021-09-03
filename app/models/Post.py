from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


class Post:
    id = 0
    # method to increment id by 1 for each post
    # find in DB the last uid generated and increment from there

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
        Post.id += 1
        return Post.id

    def save(self):
        data = db.posts.insert_one(self.__dict__)
        if data:
            return data

    def serialized(self):
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
