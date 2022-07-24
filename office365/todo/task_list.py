from office365.directory.extensions.extension import Extension
from office365.entity import Entity
from office365.entity_collection import EntityCollection
from office365.runtime.odata.v4.json_format import V4JsonFormat
from office365.runtime.paths.resource_path import ResourcePath
from office365.todo.task import TodoTask


class TodoTaskList(Entity):
    """A list in Microsoft To Do that contains one or more todoTask resources."""

    def to_json(self, json_format=None):
        return super(TodoTaskList, self).to_json(V4JsonFormat.no_metadata())

    @property
    def extensions(self):
        """The collection of open extensions defined for the task list."""
        return self.properties.get('extensions',
                                   EntityCollection(self.context, Extension,
                                                    ResourcePath("extensions", self.resource_path)))

    @property
    def tasks(self):
        """The tasks in this task list."""
        return self.properties.get('tasks',
                                   EntityCollection(self.context, TodoTask,
                                                    ResourcePath("tasks", self.resource_path)))

    @property
    def entity_type_name(self):
        return "microsoft.graph.todoTaskList"