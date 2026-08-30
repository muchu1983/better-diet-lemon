import time
import random
from lemon64.core.const import XxxvCode
from lemon64.core.core import Xxxv

class TimeDrivenXxxvGen:

    def getXxxv(self) -> Xxxv:
        # 用时间戳+微妙级时间做种子，增加离散度
        seed = int(time.time() * 1000000)
        random.seed(seed)
        #delay wait 6/15
        delay = random.uniform(0.006, 0.015)
        time.sleep(delay)
        # 限定只在 XxxvCode 里随机
        xxxvCode = random.choice([
            XxxvCode.OLD_BDEM,
            XxxvCode.OLD_BAYT,
            XxxvCode.YOUNG_BDEM,
            XxxvCode.YOUNG_BAYT
        ])
        return Xxxv(xxxvCode)
