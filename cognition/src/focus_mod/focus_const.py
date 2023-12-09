# cognition/src/focus_mod/focus_const.py

"""
The `Focus` module is the most, well, focused module, lol.
It's the least abstract and used for handling specific, short-term task.
Performing immediate actions in response to input it receives from the `Global` and `Independent` modules, the `Focus` module is sort of the "hands" of the agent, taking actions following the global and personal consideration from the previous modules.
"""


class FocusConstants:
    # Constants relevant to the performance of specific tasks
    TASK_PRIORITY_THRESHOLD = 5  # Priority level at which tasks become urgent
