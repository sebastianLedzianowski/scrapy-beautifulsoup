from mongoengine import Document, StringField, ReferenceField, ListField


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

    def to_dict(self):
        return {
            'fullname': self.fullname,
            'born_date': self.born_date,
            'born_location': self.born_location,
            'description': self.description
        }


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=2)
    quote = StringField(required=True)

    def to_dict(self):
        return {
            'tags': self.tags,
            'author': self.author.to_dict(),
            'quote': self.quote
        }
