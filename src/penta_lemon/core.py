from penta_lemon.const import Const
"""核心类"""
class Xxxv:
    """爻：万物分阴阳"""
    def __init__(self, xxxv_code:Const.XxxvCode):
        self.xxxvCode = xxxv_code

class Yyp:
    """卦：六爻成卦"""
    def __init__(self):
        self.sixXxxv = [] #六爻

    def append_xxxv(self, xxxv):
        if len(self.sixXxxv) >= 6:
            self.sixXxxv.clear() #清空重来
        self.sixXxxv.append(xxxv)
    
    def isCompleted(self):
        return True if len(self.sixXxxv) == 6 else False

    
        

