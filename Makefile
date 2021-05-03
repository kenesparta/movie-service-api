prepare:
	cp -n src/movie_service/config.py.example src/movie_service/config.py
	cp -n src/robot_service/config.py.example src/robot_service/config.py
	cp -n ./etc/psql/.env.example ./etc/psql/.env

down:
	docker-compose down --remove-orphans --volumes --rmi local

dc:
	docker-compose down --remove-orphans --volumes --rmi local
	docker-compose up --build --remove-orphans --detach --force-recreate
	@sleep 10

import-movies:
	curl http://127.0.0.1:8090/movie/import\?s\=Avengers\&page\=1\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Avengers\&page\=2\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Car\&page\=1\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Car\&page\=2\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Fast\&page\=1\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Fast\&page\=2\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Ice\&page\=1\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Ice\&page\=2\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Toy\&page\=1\&apikey=${API_KEY}
	curl http://127.0.0.1:8090/movie/import\?s\=Toy\&page\=2\&apikey=${API_KEY}

rate:
	curl http://127.0.0.1:8091/rate
	curl http://127.0.0.1:8091/best

# Get the best 5 movies from the queue
get-movies:
	curl http://127.0.0.1:8090/movie