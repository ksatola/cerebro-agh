# cerebro-agh

Aby aktywnie uczestniczyć w warsztatach MLOps w praktyce, potrzebujesz skonfigurowanego środowiska MLOps. Poniżej znajdziesz instrukcję, jak zbudować takie środowisko i przygotować swój komputer do warsztatów.

## I. Przygotowanie środowiska przed warsztatami

### 1. Instalacja wymaganego oprogramowania:
```
1a. Jeżeli używasz systemu MS Windows, zainstaluj Windows Subsystem for Linux (WSL2).
Szczegóły: https://docs.microsoft.com/en-us/windows/wsl/.

1b. Zainstaluj Docker Desktop (w systemie Windows jako administrator):
https://www.docker.com/products/docker-desktop/.
Wejdź do ustawień programu i upewnij się, że ma on do dyspozycji minimum
8GB pamięci RAM.
```

### 2. Pobranie kodu uruchamiającego środowisko MLOps:
```
2a. Uruchom terminal (jeśli używasz MS Windows, wszystkie kolejne czynności
wykonaj w terminalu WSL2) i przejdź do folderu, do którego chcesz pobrać
pliki środowiska MLOps.

$ cd <ścieżka do folderu>

2b. Skopiuj zawartość repozytorium (zostanie utworzony folder
o nazwie cerebro-agh zawierający pliki z repozytorium githuba):

$ git clone https://github.com/ksatola/cerebro-agh.git

2c. Przejdź do folderu cerebro-agh:

$ cd cerebro-agh
```

### 3. Przygotowanie do uruchomienia środowiska MLOps:
```
3a. Uruchom aplikację Docker Desktop (pamiętaj o przydzieleniu
8GB RAM w ustawieniach).

3b. Zaloguj się w Docker Desktop (jeśli nie masz konta,
możesz je bezpłatnie utworzyć).
```

### 4. Uruchomienie środowiska MLOps:
```
4a. W terminalu przejdź do folderu cerebro-agh i uruchom:

$ make

Skrypt pobierze obrazy Docker'a oraz skonfiguruje 3 maszyny wirtualne.
Za pierwszym razem może to potrwać kilka minut. Jeśli wszystko się uda,
w terminalu zobaczysz informacje dotyczące dostępu do poszczególnych
komponentów środowiska. Szczegóły poznasz podczas warsztatów.
```

### 5. Wyłączenie środowiska MLOps:
```
5a. W terminalu przejdź do folderu cerebro-agh i uruchom:

$ make down

Twój system jest gotowy do warsztatów.
```

### 7. Aby kompletnie usunąć środowisko MLOps z komputera:
```
7a. Wyłącz środowisko (patrz punkt 5).

7b. W Docker Desktop usuń wszystkie obrazy, których nazwa zaczyna się
od "gradflow" oraz obraz "mlflow_demo" (jeśli był tworzony).

7c. Usuń folder cerebro-agh utworzony w punkcie 2b.
```

Opisane powyżej środowisko MLOps zostało utworzone na bazie workbench'u zbudowanego przez Natu Lauchande, autora książki pt. Machine Learning Engineering with MLflow (którą polecam wszystkim zainteresowanym MLOps). W trakcie warsztatów, będziemy wykorzystywali pomysł na projekt analityczny zaprezentowany w książce i rozszerzymy go w taki sposób, żeby pasował do koncepcji zaprezentowanych w trakcie wykładu pt. Wstęp do MLOps.


## II. Kod i dodatkowe informacje, które będą nam potrzebne podczas warsztatów

### 0. Pobierz notebooki.
```
$ cd <ścieżka do folderu o nazwie cerebro-agh>
$ git pull
```

### 1. Otwórz Jupyter Lab: http://127.0.0.1:8888/?token=<TOKEN>

### 2. Otwórz MLflow: http://127.0.0.1:5000/#/

### 3. Uruchom w Jupyter Lab Terminal:
```
$ pip install xgboost tensorflow hyperopt evidently pycaret great_expectations
```

### 4. Otwórz drugi terminal na komputerze hoście:
```
$ export DEMO_PATH="/Users/ksatola/git/cerebro-agh"
$ cd $DEMO_PATH

$ pip install mlflow sklearn jupyterlab
$ jupyter lab --no-browser --port=8889

Jupyter: http://127.0.0.1:8889/lab?token=<TOKEN>
```

### 5. Otwórz i uruchom notebook 290
