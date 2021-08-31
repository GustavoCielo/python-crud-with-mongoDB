class Post:
    id = 1
    # method to increment id by 1 for each post

    def __init__(
            self,
            created_at: dict,
            updated_at: dict,
            title: str,
            author: str,
            tags: list,
            content: str
            ):
        self.created_at = created_at
        self.updated_at = updated_at
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

# validation for post, containing all keys
# validation for patching invalid posts
# requiring an unexisting post, trying to patch it or delete it
