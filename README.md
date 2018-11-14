Python script to print a CSV containing the details of all AWS reserved instances in given account and region.

### How to use

	git clone https://github.com/jweyrich/aws-reserved-instances.git
	cd aws-reserved-instances
	virtualenv env
	source env/bin/activate
	pip install -r requirements.txt
	python main.py <profile> <region>

### Example of output

	45b31f28-bb14-4f5f-8a24-be53a433fdca,t2.small,1,04/01/2017 17:00:00,29/09/2019 15:04:43,36,All Upfront,Linux/UNIX,0,0
	3e8b81eb-9df6-499a-95aa-ac1622300195,m4.xlarge,1,14/06/2017 13:00:00,29/09/2019 16:16:44,36,All Upfront,Linux/UNIX,0,0
	69f7e658-faac-4e5b-a471-ebf6d8b9afb4,t2.medium,1,02/08/2018 14:24:03,02/08/2019 14:24:02,12,No Upfront,Windows,0,0
	3974a868-bf38-46a6-80d0-2dfc9867940d,t2.large,1,12/07/2018 17:56:06,12/07/2019 17:56:05,12,No Upfront,Windows,0,0
	83cb273a-89bb-4074-8d4a-9f16daa50062,t2.medium,1,05/10/2017 13:00:00,29/09/2019 16:16:45,36,All Upfront,Linux/UNIX,0,0
	ff481f27-d0eb-4316-8f73-2ddc445bde58,t2.micro,1,14/06/2017 13:00:00,29/09/2019 15:04:44,36,All Upfront,Linux/UNIX,0,0
	b06f67f3-04f5-4a14-867b-9214837e3263,db.t2.micro SAZ,1,29/09/2016 16:50:08,29/09/2019 16:50:08,36,All Upfront,mysql,202,0
	23ca5080-2ad2-4e8d-970e-e3fcddb3231b,db.t2.medium SAZ,1,29/09/2016 17:23:55,29/09/2019 17:23:55,36,All Upfront,mysql,781,0
	3fd44004-5e02-46e7-a887-429f81d87e2b,db.r3.2large SAZ,1,29/09/2016 17:26:21,29/09/2019 17:26:21,36,All Upfront,aurora-mysql,2657,0
