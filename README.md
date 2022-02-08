# wsb-chmury

Aby uruchomić projekt w usłudze Azure App Service sklonuj to repozytorium i wykonaj poniższe kroki w konsoli Bash
z użyciem Azure CLI.


### Używamy stworzonej wcześniej grupy zasobów, w której znajduje się również baza danych:

LOCATION='eastus'
RESOURCE_GROUP_NAME='wsb-grupa'


### Tworzymy plan App Service:

APP_SERVICE_PLAN_NAME='wsb-chmury'    

az appservice plan create \
    --name $APP_SERVICE_PLAN_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --sku B1 \
    --is-linux


### Tworzymy nowy App Service:

APP_SERVICE_NAME='wsb-chmury-123'

az webapp create \
    --name $APP_SERVICE_NAME \
    --runtime 'PYTHON|3.8' \
    --plan $APP_SERVICE_PLAN_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --query 'defaultHostName' \
    --output table


### Uzyskujemy URL do wdrożenia przez Git

az webapp deployment source config-local-git \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --output tsv


### Pobierz poświadczenia wdrożenia dla aplikacji.

az webapp deployment list-publishing-credentials \
    --name $APP_SERVICE_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --query "{Username:publishingUserName, Password:publishingPassword}" \
    --output table

### Skonfiguruj zdalne repozytorium Git wskazujące na platformę Azure. Użyj URL uzyskanego w poprzednim kroku.

git remote add azure <uzyskane url>


### Wypchnij pliki

git push azure master:master

### Aplikacja jest gotowa

http://wsb-chmury-123.azurewebsites.net