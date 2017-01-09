# Creating a datapack

Multimodal data recordings in repovizz2 are represented as *datapacks*, a collection of the data files to-be-uploaded accompanied by a hierarchical structure that describes them.

Each datapack consists of the following:

* a datapack JSON document that adheres to the [repovizz2 datapack JSON schema](https://raw.githubusercontent.com/repovizz/repovizz2doc/master/datapack_schema.json)
* a list of files to be uploaded

In order to upload a repovizz datapack, the user needs to provide all of the above and follow the guide in [Uploading, Retrieving, Editing datapacks](https://github.com/repovizz/repovizz2doc/blob/master/Presentation.ipynb).

In the rest of this guide, we will walk through the process of creating a datapack JSON document, and preparing the files to be uploaded.

## Creating the datapack JSON

We'll use an example datapack that includes the datapack JSON document along with a list of data files.

### Example datapack

This example datapack contains a multimodal recording carried out using [Thalmic Labs' MYO](https://www.myo.com/), together with video from a handheld camera. The following data files are present inside the datapack:

<center>

Filename | Description
---------|------------
video.mp4 | video recording from a handheld camera
emg.json | 8-channel muscle activity (EMG) data 
accelerometer.json | 3-axis accelerometer data
gyroscope.json | 3-axis gyroscope data 
orientation.json | 3-axis orientation data

</center>

The video file is in standard H.264 MP4 format, while the sensor data are stored inside json arrays. Let's take a look at the corresponding datapack JSON document:

	{
		"info": {
			"keywords": [
				"MYO", "video", "accelerometer", "gyroscope"
			],
			"description": "Short datapack of MYO data coupled with video and audio.",
			"name": "MYO_various",
			"author": "panpap"
		},
		"children": [{
			"class": "data",
			"name": "Video",
			"text": "Handheld camera",
			"link": "video.mp4",
			"mime": "video/mp4; charset=binary"
		}, {
			"class": "container",
			"name": "EMG",
			"text": "",
			"children": [{
				"class": "data",
				"name": "EMG",
				"text": "8-channel EMG data from the MYO armband",
				"link": "emg.json",
				"mime": "text/plain; charset=us-ascii"
			}]
		}, {
			"class": "container",
			"name": "IMU",
			"text": "Inertial Measurement Unit (IMU) data from the MYO armband",
			"children": [{
				"class": "data",
				"name": "Accelerometer",
				"text": "3-dimensional (XYZ) acceleration data",
				"link": "accelerometer.json",
				"mime": "text/plain; charset=us-ascii"
			}, {
				"class": "data",
				"name": "Gyroscope",
				"text": "3-dimensional (XYZ) gyroscope data",
				"link": "gyroscope.json",
				"mime": "text/plain; charset=us-ascii"
			}, {
				"class": "data",
				"name": "Orientation",
				"text": "3-dimensional (yaw, pitch, roll) orientation calculated from quaternion data",
				"link": "orientation.json",
				"mime": "text/plain; charset=us-ascii"
			}]
		}]
	}

As you can see, the document contains two top-level objects:

* An *"info"* object which holds metadata about the datapack (name, author, description, keywords)
* A *"children"* object which holds an array with a hierarchical structure for the contents of the datapack.

Within the *children* array, datapack contents are hierarchically organized using two classes of nodes: **data** nodes that hold pointers to data files, and **container** nodes that can be used to construct a tree-like structure the leaves of which point to the data included in the datapack. The class of each node is specified through the *class* property.

The structure from the example datapack can be seen below:
<center><img src="https://dl.dropboxusercontent.com/u/8191579/repovizz2_example_datapack_graph.png" width="300"></center>

### Container nodes
Container nodes, as the name suggests, contain other nodes! They can be used to give structure to your datapack, like the way in which muscle activity (EMG) and movement (IMU) data have been placed in two different container nodes in the example above. Each container node stores some metadata about itself through the *name* and *text* properties, while the children nodes are placed inside the node's *children* array property.

### Data nodes
Data nodes hold links to data files along with some metadata information about the data itself, such as *name*, *text* and *link* (which specifies the name of the file associated with the node). 

## Verifying the datapack JSON
In order to verify that the datapack JSON you have generated is valid, you can use the datapack schema found [here](https://raw.githubusercontent.com/repovizz/repovizz2doc/master/datapack_schema.json). A detailed documentation of that schema can be found [here](http://lbovet.github.io/docson/index.html#https://raw.githubusercontent.com/repovizz/repovizz2doc/master/datatype_schema.json).
