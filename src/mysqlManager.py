import mysql.connector
import numpy as np
import Utils

class Image:
    def __init__(self, img: str, image_index: int, blur_type: str):
        self.image_index = image_index
        self.blur_type = blur_type

        vals = img.split(',')
        floatVals = []
        for num in vals:
            floatVals.append(float(num))
        self.img = np.array(floatVals)


    def __str__(self):
        return f"index: {self.image_index}, blur type: {self.blur_type}"

class MySqlWrapper:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="35.247.41.240",
            user="root",
            password="hello",
            database="ee"
        )
    
    def getImage(self, image_index= -1, blur_type="", limit=10):
        cursor = self.db.cursor()
        if image_index == -1 and blur_type == "":
            sql="""
                SELECT img, image_index, blur_type
                FROM images
                LIMIT %s;
            """
            params = [limit]

            cursor.execute(sql, params)

            results = cursor.fetchall()

            return results
        
        if image_index != -1 and blur_type == "":
            sql="""
                SELECT img, blur_type
                FROM images
                WHERE image_index = %s
                LIMIT %s;
            """
            params = [image_index, limit]

            cursor.execute(sql, params)
            results = cursor.fetchall()

            images = []

            for result in results:
                images.append(Image(result[0], image_index, result[1]))

            return images

        if image_index != -1 and blur_type != "":
            sql="""
                SELECT img
                FROM images
                WHERE image_index = %s AND blur_type = %s
                LIMIT %s;
            """
            params = [image_index, blur_type, limit]

            cursor.execute(sql, params)
            results = cursor.fetchall()
            return results
        
        else:
            sql = """
                SELECT img, image_index
                FROM images
                WHERE blur_type = %s
                LIMIT %s;
            """
            params = [blur_type, limit]

            cursor.execute(sql, params)
            results = cursor.fetchall()
            return results

    def updateImage(self, image_index: int, blur_type: str, img: str):
        sql = """
                UPDATE images
                SET img = "%s"
                WHERE image_index = %s AND blur_type = %s;
        """

        params = [img, image_index, blur_type]

        cursor = self.db.cursor()
        cursor.execute(sql, params)

    def insertImage(self, img: str, blur_type: str, image_index: int, value: int):
        sql = """
                INSERT INTO images (img, blur_type, image_index, value)
                VALUES (%s, %s, %s, %s);        
        """

        params = [img, blur_type, image_index, value]

        cursor = self.db.cursor()

        cursor.execute(sql, params)
        self.db.commit()



