from django.db import models
# Create your models here.
import uuid
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename=filename[0:-(len(ext)+1)]
    filename = '{0}_{1}.{2}'.format(filename,uuid.uuid4().hex[:8],ext)
    # return the whole path to the file
    #instance.user.id
    return "imgs/{0}/{1}".format(uuid.uuid4().hex[:8], filename)

def count_path(instance, filename):
    global count
    ext = filename.split('.')[-1]
    filename=filename[0:-(len(ext)+1)]
    count = 1
    filename = '{0}_{1}.{2}'.format(filename,count,ext)
    #count = count+1
    # return the whole path to the file
    #instance.user.id
    return "imgs/{0}".format(filename)
global count
count = 1
class Img(models.Model):
    # upload_to指定图片上传的途径，如果不存在则自动创建
    # 相对于MEIDA_ROOT
    #img_url = models.ImageField(upload_to=user_directory_path) 
    img_url = models.ImageField(upload_to=count_path)