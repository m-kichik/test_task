import os
from yolox.data import get_yolox_datadir

print('!!!')
data_dir=os.path.join(get_yolox_datadir(), "VOCdevkit")
print(data_dir)