from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = next((c for c in self.categories if c.id == category_id), None)
        if category is not None:
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = next((t for t in self.topics if t.id == topic_id), None)
        if topic is not None:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = next((d for d in self.documents if d.id == document_id), None)
        if document is not None:
            document.file_name = new_file_name

    def delete_category(self, category_id) -> None:
        category = next((c for c in self.categories if c.id == category_id), None)
        if category is not None:
            self.categories.remove(category)

    def delete_topic(self, topic_id) -> None:
        topic = next((t for t in self.topics if t.id == topic_id), None)
        if topic is not None:
            self.topics.remove(topic)

    def delete_document(self, document_id) -> None:
        document = next((d for d in self.documents if d.id == document_id), None)
        if document is not None:
            self.documents.remove(document)

    def get_document(self, document_id) -> Document:
        document = next((d for d in self.documents if d.id == document_id), None)
        if document is not None:
            return document

    def __repr__(self):
        return '\n'.join([d.__repr__() for d in self.documents])
