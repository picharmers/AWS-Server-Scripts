#!/usr/bin/python

import boto.datapipeline

class DataPipelineOperations:
	
	def __init__(self):
		self.s3 = boto.datapipeline.connect_to_region('us-east-1')

	def createDataPipeline(self):
		print "Lets create one"
