Python script to print a CSV containing the details of all AWS reserved instances in given account and region.

### How to use

	git clone https://github.com/jweyrich/aws-reserved-instances.git
	cd aws-reserved-instances
	virtualenv env
	source env/bin/activate
	pip install -r requirements.txt
	python main.py <profile> <region>
