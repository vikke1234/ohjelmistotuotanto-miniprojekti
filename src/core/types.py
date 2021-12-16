from attr import dataclass


@dataclass
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
        # Can't do self.url + '\n' if using fstrings
        # pylint: disable=C0209
        return "{}\n{}\n{}{}\n{}".format(
                self.title,
                self.author,
                self.url + '\n' if self.url else '',
                ', '.join(self.tags),
                self.comment
                )
@dataclass
class Book(Entry):
    """
    Stores and formats text for podcasts
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.isbn = kwargs["isbn"]

@dataclass
class BlogPost(Entry):
    """
    Stores and formats text for podcasts
    """


@dataclass
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
