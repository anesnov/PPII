class TopicsMessages:
    def __init__(self):
        self.topics = {}

    def create_topic(self, topic_id, title, author, content):
        if topic_id in self.topics:
            return "Topic already exists."
        self.topics[topic_id] = {"title": title, "author": author, "content": content, "comments": []}
        return "Topic created successfully."

    def add_comment(self, topic_id, comment, author):
        if topic_id in self.topics:
            self.topics[topic_id]["comments"].append({"author": author, "comment": comment})
            return "Comment added."
        return "Topic not found."

    def edit_topic(self, topic_id, new_title=None, new_content=None):
        if topic_id in self.topics:
            if new_title:
                self.topics[topic_id]["title"] = new_title
            if new_content:
                self.topics[topic_id]["content"] = new_content
            return "Topic updated."
        return "Topic not found."

    def delete_topic(self, topic_id):
        if topic_id in self.topics:
            del self.topics[topic_id]
            return "Topic deleted."
        return "Topic not found."