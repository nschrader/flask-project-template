export PATH := /usr/sbin:$(PATH)

run: dep-mongo
	python3 setup.py develop --user
	python3 entry.py

build:
	python3 setup.py install --user

clean:
	python3 setup.py clean
	rm -rf dist/ build/ db/ log/ *.egg-info/

dep-mongo:
	which mongod
	which mongo
	mkdir -p .db
	mkdir -p .log

run-mongo: dep-mongo
	mongo --eval "quit()" || mongod --fork --logpath .log/mongo --dbpath .db
	echo "Mongo is up"

kill-mongo: dep-mongo
	! mongo --eval "quit()" || mongod --shutdown --logpath .log/mongo --dbpath .db
	echo "Mongo is down"
