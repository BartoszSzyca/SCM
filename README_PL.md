# Smart Cart Master (SCM)

**Smart Cart Master** (SCM) to zaawansowana aplikacja służąca do zarządzania zakupami spożywczymi, przepisami kulinarnymi oraz produktami w lodówce. Aplikacja umożliwia tworzenie list zakupów, zarządzanie stanem lodówki, śledzenie wartości odżywczych produktów oraz organizowanie przepisów. W przyszłości planowane jest rozszerzenie funkcjonalności o aplikację mobilną oraz wersję webową.

## Spis treści

- [Funkcje](#funkcje)
- [Struktura Projektu](#struktura-projektu)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Plany na Przyszłość](#plany-na-przyszłość)
- [Wymagania Systemowe](#wymagania-systemowe)
- [Autor](#autor)

## Funkcje

- Tworzenie i zarządzanie listą zakupów.
- Zarządzanie produktami spożywczymi w lodówce.
- Organizowanie przepisów kulinarnych.
- Obliczanie wartości odżywczych (makro i mikroelementy).
- Śledzenie daty zakupu i przydatności produktów.
- Obsługa różnych jednostek miary (sztuki, kilogramy, litry, itp.).
- Planowane rozszerzenie o aplikację mobilną i wersję webową.

## Struktura Projektu

```plaintext
    smart_cart_master/
    │
    ├── core/
    │   ├── __init__.py
    │   ├── food.py           # Zarządzanie produktami spożywczymi (opis produktów)
    │   ├── fridge.py         # Zarządzanie produktami w lodówce
    │   ├── shopping_list.py  # Zarządzanie listą zakupów
    │   ├── recipe_list.py    # Zarządzanie listą produktów do gotowania
    │   ├── recipes.py        # Zarządzanie przepisami
    │   ├── nutrition.py      # Obliczenia kaloryczne i wartości odżywcze
    │   └── utils.py          # Pomocnicze funkcje
    │   └── manager.py        # moduł zarządzający
    │
    ├── database/
    │   ├── __init__.py
    │   ├── models.py         # Definicje modeli SQLAlchemy (w tym FoodModel)
    │   ├── database.py       # Konfiguracja bazy danych i sesji oraz operacje na danych
    │   ├── food.db           # Plik bazy danych SQLite
    │   └── migrations/       # Ewentualne migracje bazy danych
    │
    ├── gui/
    │   ├── __init__.py
    │   ├── main_window.py    # Główny interfejs użytkownika (GUI)
    │   ├── shopping_list.py  # Widok listy zakupów
    │   ├── fridge_view.py    # Widok lodówki
    │   ├── recipe_view.py    # Widok przepisów
    │   └── widgets.py        # Niestandardowe widżety GUI
    │
    ├── web/                  # (Do rozwoju w przyszłości)
    │   ├── __init__.py
    │   ├── forms.py          # Formularze (jeśli korzystasz z Django)
    │   └── static/           # Pliki statyczne (CSS, JS, obrazki)
    │   ├── settings.py       # Konfiguracja Django
    │   ├── urls.py           # Routing URL dla aplikacji webowej
    │   ├── views.py          # Widoki webowe
    │   └── models.py         # Modele bazy danych dla Django
    │
    ├── docs/                # Dokumentacja projektu
    │   ├── architecture.md  # Dokumentacja architektury projektu
    │   ├── classes.md       # Opis kluczowych klas i metod
    │   └── usage.md         # Instrukcja użytkowania aplikacji
    │
    ├── main.py               # Główny plik uruchamiający aplikację desktopową
    ├── requirements.txt      # Lista zależności Pythona
    └── README.md             # Opis projektu
```
## Instalacja

   1. **Sklonuj repozytorium**:

      ```bash
      git clone https://github.com/BartoszSzyca/SCM.git
      cd SCM
      ```
   2. **Zainstaluj wymagane zależności**:

      Użyj pip do zainstalowania wszystkich zależności z pliku requirements.txt:

      ```bash 
      pip install -r requirements.txt
      ```
   3. **Konfiguracja bazy danych**:

      Po zainstalowaniu zależności, upewnij się, że plik food.db jest w odpowiednim miejscu w folderze database/. Jeśli baza danych wymaga migracji, uruchom odpowiednie polecenia do zastosowania migracji.

   4. **Uruchom aplikację**:

      W folderze głównym projektu uruchom aplikację za pomocą:

      ```bash
      python main.py
      ```
      
      Powinno to uruchomić aplikację desktopową. Możesz teraz korzystać z funkcji aplikacji, takich jak zarządzanie listą zakupów, lodówką i przepisami.

## Użycie

   1. Tworzenie i zarządzanie listą zakupów:

      W interfejsie użytkownika, przejdź do zakładki "Lista zakupów", aby dodawać, edytować i usuwać produkty. Możesz również zobaczyć podsumowanie kosztów.

   2. Zarządzanie produktami w lodówce:

      Przejdź do zakładki "Lodówka", aby śledzić produkty, ich daty ważności, i warunki przechowywania. Możesz edytować informacje o produktach bezpośrednio z tego widoku.

   3. Organizowanie przepisów:

      W zakładce "Przepisy" możesz dodawać, edytować i usuwać przepisy. Możesz również przeglądać przepisy i dodawać składniki do listy zakupów jednym kliknięciem.

   4. Obliczanie wartości odżywczych:

      W sekcji "Obliczenia" możesz wprowadzać dane dotyczące wartości odżywczych, takich jak kalorie, makro i mikroelementy. Aplikacja automatycznie przelicza wartości na podstawie wprowadzonych danych.

## Plany na Przyszłość

   * Rozwój aplikacji mobilnej i webowej.
   * Integracja z serwisami dostawy, takimi jak UberEats i Glovo.
   * Rozbudowa funkcji analizy diety i planowania posiłków.

## Wymagania Systemowe

   * Python 3.x
   * SQLite (do bazy danych)
   * System operacyjny: Windows, macOS lub Linux

## Autor

   * Bartosz Szyca

## Licencja

   
