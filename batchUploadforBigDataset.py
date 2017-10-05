from RoboBrainClient.RoboBrainAPI import RoboBrainAPI
import json

import re
import glob
import pprint
import sys
import getopt
import pprint

RoboAPIUserName = 'RobotLearningMember'
RoboAPIPass = 'PASS'
S3KEY = 'S3_KEY'
S3SECRET = 'S3_SECRET'

URL = "http://robobrain.me:3000/api/feeds/"



#Please change your user name
userHandle = 'userName'

colorred = "\033[01;31m{0}\033[00m"
colorgrn = "\033[1;36m{0}\033[00m"

def main(argv):
    if len(argv)>0:
        try:
            opts, args = getopt.getopt(argv,"h")
        except getopt.GetoptError:
            print "Usage:"
            print "\t"," batchUpload.py -h for help"
            print "\t"," batchUpload.py fro pushing all .json files in the directory"
            sys.exit(2)
        for opt,arg in opts:
            if opt == '-h':
                print colorgrn.format("Robo Brain Feed Uploader")
                print colorgrn.format("\t Supported Edge Types:")
		pprint.pprint( ['is_type_of','has_appearance','has_3dshape','has_part','can_perform_action','can_be_object_of','is_trajectory_of','uses_feature','sub_task_of','similar_to','corresponds_to','spatially_distributed_as.activity','spatially_distributed_as','can_use','is_synonym_of','is_grounded_as_action_sequence','verb_object','pobj','adjectives','adverbial_modifier','sequence-representation'])

    else:
        #Connect to the API
        rC = RoboBrainAPI(RoboAPIUserName ,RoboAPIPass,S3KEY,S3SECRET,userHandle)

        # Posting a feed
        #Batch Upload
        for file in glob.glob("*.json"):
            json_data=open(file).read()
            data = json.loads(json_data)
            rC.addFeed(data)
            print colorgrn.format("Feed Added to the Queue:")
            print "\t", data
            print colorgrn.format("Attempt to push feeds to the Brain")
            rC.push2Brain(URL)

if __name__ == "__main__":
    main(sys.argv[1:])
