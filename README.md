# cerebro-agh

```
--------------------------

For English, scroll down.

--------------------------
```

Przed rozpoczęciem pracy z kodem, zachęcam do zapoznania się z wstępem do tematyki MLOps (sesja zaczyna się od 5:23:00): https://www.youtube.com/watch?v=MbbuUJgr0i8.

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


### ----------------------------
# English

## I. Build workshop environment

### 1. Install software:
```
1a. If you are using MS Windows, install Windows Subsystem for Linux (WSL2).
Details: https://docs.microsoft.com/en-us/windows/wsl/.

1b. Install Docker Desktop (in Windows as administrator):
https://www.docker.com/products/docker-desktop/.
Make sure Docker Desktop has at least 8GB of RAM assigned.
```

### 2. Get workshop code:
```
2a. Open your Terminal app, and enter a folder you want to store workshop files:

$ cd <folder path>

2b. Clone the workshop repository to your local system 
(it will create a folder called cerebro-agh with the repo's contents):

$ git clone https://github.com/ksatola/cerebro-agh.git

2c. Move to the cerebro-agh folder:

$ cd cerebro-agh
```

### 3. Prepare to run workshop environment:
```
3a. Run Docker Desktop (remember that it needs 8GB of RAM to run the workshop properly).

3b. You may want to create a free Docker account.
```

### 4. Run workshop environment:
```
4a. In terminal, change you current folder to cerebro-agh and run:

$ make

The script will download base Docker images and builds 3 virtual servers.
It can take a few minutes for the first time.
```

### 5. Shut down the workshop environment:
```
5a. In terminal, change you current folder to cerebro-agh and run:

$ make down

Now you are ready to start the workshop.
```

### 7. To remove completely the workshop environment from your computer:
```
7a. Shut down the workshop environment (see 5).

7b. In Docker Desktop remove all images with the name starting with "gradflow",
and "mlflow_demo" image if created during the workshop.

7c. Delete the cerebro-agh folder created in 2b.
```

The workshop environment has been created based on the book "Machine Learning Engineering with MLflow" by Natu Lauchande. I really recommend this book to anyone interested in MLOps. I have also used the examplary project idea presented in the book extending it to match the MLOps workflow (end-to-end model life-cycle) proposed during the lecture.


## II. Code snippets and additional information for the workshop

### 0. Get Jupyter notebooks:
```
$ cd <path to cerebro-agh folder>
$ git pull
```

### 1. Open Jupyter Lab: http://127.0.0.1:8888/?token=<TOKEN>

### 2. Open MLflow: http://127.0.0.1:5000/#/

### 3. Run in the Jupyter Lab Terminal:
```
$ pip install xgboost tensorflow hyperopt evidently pycaret great_expectations
```

### 4. Open the second terminal sessions in the host (local) computer:
```
$ export DEMO_PATH="/Users/ksatola/git/cerebro-agh"
$ cd $DEMO_PATH

$ pip install mlflow sklearn jupyterlab
$ jupyter lab --no-browser --port=8889

Jupyter: http://127.0.0.1:8889/lab?token=<TOKEN>
```

### 5. Open and run notebook number 290
