import os
import math
from filechunkio import FileChunkIO

import boto
from boto.s3.connection import S3Connection
#from boto.s3.connection import OrdinaryCallingFormat

from boto.s3.key import Key

class Upload:
    def __init__(self,apikey,secret):
        self.apikey = apikey
        self.apisecret = secret
        self.conn = boto.connect_s3(apikey, secret)#,calling_format=OrdinaryCallingFormat())
        self.b = self.conn.get_bucket('feedmedia')


    def upload(self,localPath,keyName):
        source_size = os.stat(localPath).st_size
        
        k = Key(self.b)
        k.key = keyName
        mp = self.b.initiate_multipart_upload(k)
        
        chunk_size = 52428800
        chunk_count = int(math.ceil(source_size / chunk_size))
        
        for i in range(chunk_count +1):
            offset = chunk_size * i
            bytes = min(chunk_size, source_size - offset)
            with FileChunkIO(localPath, 'r', offset=offset,bytes=bytes) as fp:
                mp.upload_part_from_file(fp, part_num=i + 1)
    
        mp.complete_upload()

