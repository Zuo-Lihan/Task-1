# comment.py

class Comment:
    def __init__(self, id=None, thread_id=None, parent_id=None, body=None, body_is_trimmed=None, author=None, subreddit=None):
        self.id = id
        self.thread_id = thread_id
        self.parent_id = parent_id
        self.body = body
        self.body_is_trimmed = body_is_trimmed
        self.author = author
        self.subreddit = subreddit
