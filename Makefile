DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yml
STORAGES_FILE = docker_compose/storages.yml
STORAGES_CONTAINER = mongodb_aboba
APP_CONTAINER = main-app

.PHONY: all
all:
	${DC} -f ${STORAGES_FILE} -f ${APP_FILE} ${ENV} up --build -d 

.PHONY: all-down
all-down:
	${DC} -f ${STORAGES_FILE} -f ${APP_FILE} down

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} 

.PHONY: app-down
app-down:
	${DC} -f  ${APP_FILE} down

.PHONY: storages
storages:
	${DC} -f {STORAGES_FILE} ${ENV} up --build -d

.PHONY: storages-logs
storages-logs:
	${LOGS} ${STORAGES_CONTAINER}

.PHONY: storages-down
storages-down:
	${DC} -f {STORAGES_FILE}

.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} pytest