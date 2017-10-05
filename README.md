Client
======

Python Client for the Robo Brain API

## Installation 

In order to use the RoboBrain API, you need to install a few Python packages.

```
    sudo pip install boto
    sudo pip install requests
    sudo pip install filechunkio
```

##  JSON FORMAT:

```json
{
    "feedtype": "Type Of The Feed",
    "text": "Text Caption of the Feed with HashTags",
    "source_text": "Your Project Name",
    "source_url": "Your Project URL",
    "mediashow": [
      "Is 0th image for visualization or for the brain graph ?",
      "Is 1st image for visualization or for the brain graph ?",
      "True or False",
      "True means, it is for visualization"
    ],
    "media": [
      "/your/local/path/to/media0",
      "/your/local/path/to/media1",
      "/your/local/path/to/media2"
    ],
    "mediatype": [
      "Image",
      "Video",
      "Text"
    ],
    "keywords": [
      "Some",
      "Keywords",
      "About",
      "Feed"
    ],
    "mediamap": [
      "#1", (this means 0th media is related to 1st hashtag)
      "#0#1", (this means 1st media is related to 0th and 1st hashtags)
      "#0" (this means 3rd media is related to 0th hashtag)
    ],
    "graphStructure": [
      "has_appearance: #1 ->#0"
      "Edge type and related nodes"
      "It means there exist has_apparance edge from hashtag1 to hashtag0"
    ],
}

```

### Notes:
* If hashtag is multiple number of words use underscore. For example; in order to hash tag feature id 2, use #feature_id_2. We will display them as white spaces
* In all fields; please only use alphanumeric characters, dash ‘-’, and an underscore ’_’ .
* All semantically meaningful entries are nodes(hashtags) and edges should not be hashtagged
* You can only make mediashow True for mediatypes Image and Video
* If you want to hashtag a media but not the concept use #$ instead of #. For example, "#cup has an apperance in #image" is refering to the media not the concept "image"; hence, it should be replaced as "#cup has an apperance in #$image"
* If you are not sure about the edge types, or feed_structure you can use 

```
python batchUpload.py --help
```

## SAMPLE FEED:

```json
{
    "feedtype": "Object Affordance",
    "text": "The position of a #Standing_human while using a #shoe is distributed as #$heatmap_12.",
    "source_text": "Hallucinating Humans",
    "source_url": "http://pr.cs.cornell.edu/hallucinatinghumans/",
    "mediashow": [
      "True",
      "True"
    ],
    "media": [
      "/home/ozan/ilcrf/images/shoe_.jpg",
      "/home/ozan/ilcrf/shoe_12_1.jpg_cr.jpg"
    ],
    "mediatype": [
      "Image",
      "image",
    ],
    "keywords": [
      "Human",
      "Affordance",
      "Object",
      "shoe",
      "Standing"
    ],
    "mediamap": [
      "#1",
      "#0#1#2"
    ],
    "graphStructure": [
      "spatially_distributed_as: #1 ->#2",
      "spatially_distributed_as: #0 ->#2",
      "can_use: #0 ->#1"
    ],
}

```

##  How to Upload Your Feeds to the RoboBrain ?

There are two ways to upload your feeds, you can either use the provided API directly or you can use the batch upload functionality. API provides a function to upload a Python dictionary as a JSON. Batch upload simply traverse the current directory and upload all *.json files in the directory.

You Need (choose one of the ways)
* For Batch Upload: A directory containing all *.json files with correct media paths. Media paths can either be relative to the directory or a global path. We recommend global paths.
* For Direct API Usage: A python script which generates all feeds in the Python dictionary format with correct media paths. Media paths can either be relative to the directory or a global path. We recommend global paths. 
