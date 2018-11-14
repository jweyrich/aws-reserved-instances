#!/usr/bin/env python

from datetime import datetime
from datetime import timedelta
import boto3
import json
import locale
import pytz
import sys

class Reservation:
	def __init__(self):
		self.iid = None
		self.itype = None
		self.icount = None
		self.starts_at = None
		self.ends_at = None
		self.duration = None
		self.payment_type = None
		self.platform = None
		self.fixed_price = None

class EC2Reservation(Reservation):
	def __init__(self, obj):
		self.parse(obj)

	def parse(self, obj):
		self.iid = obj[u'ReservedInstancesId']
		self.itype = obj[u'InstanceType']
		self.icount = obj[u'InstanceCount']

		self.starts_at = obj[u'Start']

		self.ends_at = obj[u'End']

		self.duration = obj[u'Duration'] # in seconds
		self.duration = self.duration / 86400 # seconds to days
		self.duration = self.duration / 365 # days to years
		self.duration = self.duration * 12 # years to months

		self.payment_type = obj[u'OfferingType']

		self.platform = obj[u'ProductDescription']
		self.platform = self.platform.replace(' (Amazon VPC)', '')

		self.fixed_price = obj[u'FixedPrice']

class RDSReservation(Reservation):
	def __init__(self, obj):
		self.multi_az = None
		self.parse(obj)

	def parse(self, obj):
		self.iid = obj[u'ReservedDBInstancesOfferingId']
		self.multi_az = obj[u'MultiAZ']
		self.itype = obj[u'DBInstanceClass'] + ' ' + ('MAZ' if self.multi_az else 'SAZ')
		self.icount = obj[u'DBInstanceCount']

		self.starts_at = obj[u'StartTime']
		self.ends_at = self.starts_at + timedelta(seconds=obj[u'Duration'])

		self.duration = obj[u'Duration'] # in seconds
		self.duration = self.duration / 86400 # seconds to days
		self.duration = self.duration / 365 # days to years
		self.duration = self.duration * 12 # years to months

		self.payment_type = obj[u'OfferingType']

		self.platform = obj[u'ProductDescription']

		self.fixed_price = obj[u'FixedPrice']

def get_rds_reserved_instances(session):
	rds = session.client('rds')
	response = rds.describe_reserved_db_instances() # Does not support Filters yet.

	obj = response[u'ReservedDBInstances']
	if not obj:
		print('Response does not contain reserved RDS instances.')
		exit(1)

	for row in obj:
		state = row[u'State']
		if state != 'active':
			continue

		yield RDSReservation(row)

def get_ec2_reserved_instances(session):
	ec2 = session.client('ec2')
	response = ec2.describe_reserved_instances(Filters=[
			{
				'Name': 'state',
				'Values': [ 'active' ]
			}
		])

	obj = response[u'ReservedInstances']
	if not obj:
		print('Response does not contain reserved EC2 instances.')
		exit(1)

	for row in obj:
		state = row[u'State']
		assert(state == 'active')

		yield EC2Reservation(row)

def print_reserved_instance(obj):
	separator = ','
	print("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (
		obj.iid, separator,
		obj.itype, separator,
		obj.icount, separator,
		datetime.strftime(obj.starts_at, '%d/%m/%Y %H:%M:%S'), separator,
		datetime.strftime(obj.ends_at, '%d/%m/%Y %H:%M:%S'), separator,
		obj.duration, separator,
		obj.payment_type, separator,
		obj.platform, separator,
		str(obj.fixed_price).replace('.',',')))

def main():
	if len(sys.argv) < 2:
		print('Usage: %s <profile_name> <region>' % sys.argv[0])
		exit(1)

	profile_name = sys.argv[1] or 'default'
	region_name = sys.argv[2] or 'sa-east-1'

	locale.setlocale(locale.LC_ALL, 'pt_BR')

	session = boto3.Session(profile_name=profile_name, region_name=region_name)

	for x in get_ec2_reserved_instances(session): print_reserved_instance(x)
	for x in get_rds_reserved_instances(session): print_reserved_instance(x)

if __name__ == "__main__":
    main()
