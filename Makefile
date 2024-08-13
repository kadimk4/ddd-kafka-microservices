DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yml
STORAGES_FILE = docker_compose/storages.yml
APP_CONTAINER = main-app

.PHONY: all
all:
	${DC} -f ${STORAGES_FILE} -f ${APP_FILE} ${ENV} up --build -d 

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} 

.PHONY: app-down
app-down:
	${DC} -f  ${APP_FILE} down