init:
	pip3 install -r requirements.txt
	mkdir -p logs

test:
	cd src && python3 -m unittest

clean:
	rm logs/*