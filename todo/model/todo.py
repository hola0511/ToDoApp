class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            print("El elemento ya esta en la lista")

    def __str__(self):
        return print(self.code_id, " - ", self.title)


class TodoBook:

    def __init__(self):
        self.todos: dict[int, Todo] = []

    def add_todo(self, title: str, description: str) -> int:
        pass

    def pending_todos(self) -> list[Todo]:
        pass

    def completed_todos(self) -> list[Todo]:
        pass

    def tags_todo_count(self) -> dict[str,int]:
