from .. import BaseExecutionUnit


class ScriptingExecutionUnit(BaseExecutionUnit):
    def __init__(self, config, work_dir):
        super(ScriptingExecutionUnit, self).__init__(config, work_dir)
