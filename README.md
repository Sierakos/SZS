# SZS - System zarządzania studentami

Program obsługujący prosty CRUD do zarządzania studentami w systemie. 

Aby pobawić się programem w wersji konsolowej należy:

- zainstalować najnowszą wersję pythona 3
- zainstalować i skonfigurować GIT
- otworzyć kosnole GIT bash

(zalecane)
- utworzyć środowisko wirtualne oraz je włączyc
```
py -m venv env
source env/scripts/activate
```

- pobrać kod
```
git clone https://github.com/Sierakos/SZS.git
```

- pobrać niezbędne biblioteki pythona z pliku requirements.txt
```
pip install -r requirements.txt
```

- włączyć właściwy program
```
cd SZS
py view.py
```

- baze danych w każdym momencie można stworzyć za pomocą komendy
```
py db.py
```