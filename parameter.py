class ParameterList:
    """
    Example:
    para_list = ParameterList()
    para_list.add_item(foo=1, bar=2)
    fun(**para_list.get_item())
    """
    def __init__(self):
        self.para = {}

    def add_item(self, **para):
        self.para.update(para)

    def get_item(self):
        return self.para