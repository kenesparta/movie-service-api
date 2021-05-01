prepare:
	cp -n src/movie_service/config.py.example src/movie_service/config.py
	cp -n src/robot_service/config.py.example src/robot_service/config.py
	cp -n ./etc/psql/.env.example ./etc/psql/.env

dc:
	docker-compose down --rmi local
	docker-compose up -d --build --remove-orphans

dc-dev:
	docker-compose down
	docker-compose up -d --build
