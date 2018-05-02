export PATH := /usr/sbin:$(PATH)

run:
	python3 setup.py develop --user
	python3 entry.py

build:
	python3 setup.py install --user

clean:
	python3 setup.py clean
	rm -rf dist/ build/ db/ log/ *.egg-info/

dep-mongo:
	which mongod
	mkdir -p db
	mkdir -p log

run-mongo: dep-mongo
	mongod --fork --logpath log/mongo --dbpath db

kill-mongo: dep-mongo
	mongod --shutdown --logpath log/mongo --dbpath db
