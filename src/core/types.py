from attr import dataclass


class Entry:
    """
    Base class for each type of bookmark
    """
    def __init__(self, **kwargs) -> None:
        self.author = kwargs["author"]
        self.title = kwargs["title"]
        self.tags = kwargs["tags"].split(",")
        self.comment = kwargs["comment"]
        self.url = kwargs.get("url", "")
        self.read = False

    def __str__(self) -> str:
        return "{}\n{}\n{}{}\n{}".format(
                self.title,
                self.author,
                self.url + '\n' if self.url else '',
                ', '.join(self.tags),
                self.comment
                )
class Book(Entry):
    """
    Stores and formats text for podcasts
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.isbn = kwargs["isbn"]

class BlogPost(Entry):
    """
    Stores and formats text for podcasts
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

class Podcast(Entry):
    """
    Stores and formats text for podcasts
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.desc = kwargs["description"]

@dataclass
class Video(Entry):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.url = kwargs["url"]
