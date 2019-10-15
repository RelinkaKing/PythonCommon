import os
from shutil import copyfile

source=r"C:\Users\Raytine\Desktop\temp_path"+"/log.log"
target=r"C:\Users\Raytine\Desktop\temp_path"+"/log2.log"
copyfile(source,target)