import mysqlManager
from Utils import saveImage


sql = mysqlManager.MySqlWrapper()

img = sql.getImage(image_index= 62 )

for i in img:
    saveImage(i.img, f"src/img/testfail/{i.blur_type}")