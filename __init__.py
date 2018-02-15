from .test.demo import testfunc

"""
This file contains imported tasks and only one object i.e. plugins

plugin_tasks: This dictionary contains information about all plugins.
              Keys of this dictionary are the names of imported tasks and values
              are their metadata.

              This metadata contains:
                  index:     Used to order tasks (as dict will rearrange items).
                  title:     Title to be displayed.
                  task:      The original task.
                  args (optional):
                    List of arguments to be passed. Each item
                    is a dictionary with key as name of argument
                    and value as a dictionary of metadata.
                    This metadata contains:
                        type:        Type of argument to be passed.
                        default:     Default value if not required.
"""

plugin_tasks = {
    'testfunc': {
        'index': 0,
        'title': 'Test function',
        'task': testfunc,
        'args': [
            {'teststr': {'type': 'str'}},
            {'testlst': {'type': 'list'}},
            {'testdct': {'type': 'dict', 'default': {}}},
            {'testint': {'type': 'int', 'default': []}},
            {'testint': {'type': 'bool', 'default': 0}}
        ]
    }
}
