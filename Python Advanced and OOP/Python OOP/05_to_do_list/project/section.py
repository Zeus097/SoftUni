from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        searched_task = next((t for t in self.tasks if t.name == task_name), None)
        if searched_task is not None:
            searched_task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        current_len_of_tasks = len(self.tasks)
        for current_task in self.tasks:
            if current_task.completed:
                self.tasks.remove(current_task)
        return f"Cleared {current_len_of_tasks - len(self.tasks)} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]
        for current_task in self.tasks:
            result.append(f"\n{current_task.details()}")
        return ''.join(result)
