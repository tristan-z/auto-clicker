init:
	pip3 install -r requirements.txt
	mkdir -p logs
	npm install -g @adobe/jsonschema2md

test:
	cd src && python3 -m unittest

schema:
	rm -f scripts/docs/*.schema.json
	cd src && python3 schema_config.py

schemadocs: schema
	rm scripts/docs/*.md
	jsonschema2md -d scripts/docs -o scripts/docs
	rm -rf out

clean:
	rm logs/*