# PETVET — model architektury (Laboratorium 2)

> Diagramy są szkicem modelu docelowego. Przed oddaniem zespół powinien je sprawdzić względem zaakceptowanych historyjek i faktycznych decyzji. Nie wpisano technologii innych niż potwierdzone w obecnym rozwiązaniu. W szczególności integracja e-mail jest planowana.

## 1. C4 poziom 1 — diagram kontekstu

```mermaid
flowchart LR
    opiekun([Opiekun zwierzęcia])
    recepcja([Recepcjonista])
    lekarz([Lekarz weterynarii])
    petvet[/"PETVET — system obsługi przychodni"/]
    email[["Zewnętrzny system poczty e-mail"]]

    opiekun -->|przekazuje dane i ustala termin| recepcja
    recepcja -->|rejestruje opiekuna, zwierzę i wizytę| petvet
    lekarz -->|odczytuje historię i zapisuje wynik wizyty| petvet
    petvet -->|przekazuje potwierdzenia i przypomnienia| email
    email -->|dostarcza wiadomości| opiekun
```

### Założenia
1. Opiekun kontaktuje się z przychodnią, a dane do PETVET wprowadza recepcjonista.
2. Lekarz korzysta z PETVET do przeglądania historii i dokumentowania wizyty.
3. System poczty e-mail jest zewnętrzną usługą, której integracja zostanie dopiero wykonana.

### Pytania
1. Czy opiekun w przyszłości będzie korzystał z własnego portalu?
2. Czy potwierdzenia i przypomnienia będą wysyłane automatycznie?
3. Kto zarządza konfiguracją konta pocztowego?

## 2. C4 poziom 2 — diagram kontenerów

```mermaid
flowchart LR
    recepcja([Recepcjonista])
    lekarz([Lekarz weterynarii])

    subgraph system["PETVET — system"]
        app["Aplikacja desktopowa PETVET
interfejs i logika obsługi"]
        json[("Lokalny plik danych JSON")]
        mailmod["Moduł obsługi powiadomień
(planowany)"]
    end

    email[["Zewnętrzny system poczty e-mail"]]

    recepcja -->|wprowadza i odczytuje dane| app
    lekarz -->|przegląda i uzupełnia dokumentację| app
    app -->|odczyt i zapis danych| json
    app -->|zleca wysłanie wiadomości| mailmod
    mailmod -->|przekazuje treść i adres odbiorcy| email
```

### Założenia
1. Aplikacja desktopowa i lokalny plik JSON odpowiadają aktualnemu sposobowi działania programu.
2. Moduł powiadomień jest elementem planowanym, a nie istniejącym w przesłanym kodzie.
3. Nie modelujemy osobnego API ani serwera, ponieważ nie ma ich w obecnym rozwiązaniu ani w uzgodnionym zakresie.

### Pytania
1. Czy plik JSON pozostanie docelowym magazynem danych, czy zostanie zastąpiony bazą danych?
2. Czy wysyłka e-mail będzie realizowana przez serwer SMTP, czy usługę zewnętrznego dostawcy?
3. Czy aplikacja będzie używana na jednym stanowisku, czy przez kilka komputerów?

## 3. Diagram sekwencji — umówienie wizyty, ścieżka główna

```mermaid
sequenceDiagram
    actor R as Recepcjonista
    participant A as Aplikacja PETVET
    participant D as Plik danych JSON

    R->>A: Wybiera zwierzę, lekarza i termin
    A->>D: Odczytuje dane zwierząt i zaplanowanych wizyt
    D-->>A: Zwraca dane
    A->>A: Weryfikuje istnienie zwierzęcia i dostępność lekarza
    A->>D: Zapisuje wizytę ze statusem zaplanowana
    D-->>A: Potwierdza zapis
    A-->>R: Wyświetla potwierdzenie umówienia wizyty
```

## 4. Diagram sekwencji — umówienie wizyty, ścieżka błędu

```mermaid
sequenceDiagram
    actor R as Recepcjonista
    participant A as Aplikacja PETVET
    participant D as Plik danych JSON

    R->>A: Wybiera zwierzę, lekarza i termin
    A->>D: Odczytuje dane zwierząt i zaplanowanych wizyt
    D-->>A: Zwraca dane
    A->>A: Weryfikuje identyfikator zwierzęcia i termin
    alt Zwierzę nie istnieje
        A-->>R: Odrzuca zapis — brak zwierzęcia
    else Termin lekarza jest zajęty
        A-->>R: Odrzuca zapis — termin zajęty
    else Dane terminu są niepoprawne
        A-->>R: Odrzuca zapis — błędne dane
    end
```

### Zgodność z R-03
Ścieżka główna kończy się zapisem wizyty ze statusem „zaplanowana”. Ścieżka błędu obejmuje brak zwierzęcia, zajęty termin i niepoprawne dane terminu. Obecny kod sprawdza konflikt dla tego samego lekarza i identycznego terminu; pełne wykrywanie nakładających się przedziałów wymaga doprecyzowania i ewentualnej zmiany implementacji.

## 5. Diagram sekwencji — zakończenie wizyty i rozliczenie

```mermaid
sequenceDiagram
    actor L as Lekarz weterynarii
    actor R as Recepcjonista
    participant A as Aplikacja PETVET
    participant D as Plik danych JSON

    L->>A: Wybiera zaplanowaną wizytę
    A->>D: Odczytuje wizytę
    D-->>A: Zwraca dane wizyty
    A-->>L: Wyświetla dane pacjenta
    L->>A: Wprowadza diagnozę, zalecenia i szczepienie
    A->>D: Zapisuje dane i status zrealizowana
    D-->>A: Potwierdza zapis
    A-->>L: Potwierdza zakończenie wizyty
    R->>A: Wybiera zrealizowaną wizytę do rozliczenia
    A-->>R: Wyświetla koszt wizyty
    R->>A: Potwierdza przyjęcie gotówki
    A->>D: Zapisuje metodę płatności gotówka
    D-->>A: Potwierdza zapis płatności
    A-->>R: Wyświetla potwierdzenie
```

## 5. Maszyna stanów wizyty

```mermaid
stateDiagram-v2
    [*] --> Zaplanowana: umów wizytę
    Zaplanowana --> Zrealizowana: zakończ wizytę
    Zaplanowana --> Odwolana: odwołaj wizytę
    Zrealizowana --> Oplacona: odnotuj płatność gotówką
    Odwolana --> [*]
    Oplacona --> [*]
```

### Reguły przejść
- Wizytę zaplanowaną można zrealizować albo odwołać.
- Nie można odwołać wizyty już zrealizowanej.
- Płatność można odnotować dopiero po realizacji wizyty.
- W uzgodnionym zakresie metoda płatności to gotówka.
- Stany „Odwolona” i „Oplacona” są końcowe w tym uproszczonym modelu. Jeżeli przyjmiecie inne reguły, zaktualizujcie diagram.

## 6. Kontrola spójności
Przed zatwierdzeniem diagramów sprawdźcie:
- czy wszyscy aktorzy z `wymagania.md` występują na diagramie kontekstu;
- czy system e-mail jest oznaczony jako zewnętrzny;
- czy każda strzałka ma opis czynności lub przepływu;
- czy sekwencja odpowiada kryteriom akceptacji R-03;
- czy pokazano ścieżkę błędu;
- czy maszyna stanów nie dopuszcza niedozwolonych przejść;
- czy nazwy są językiem domeny przychodni, a nie nazwami klas i tabel.

## 7. Diagram ERD — encje wskazane w opisie wycinka rzeczywistości

Poniższy diagram jest modelem pojęciowym wynikającym z encji i relacji wymienionych w przygotowanym opisie PETVET. Nie jest jeszcze projektem fizycznej bazy danych. Aplikacja w obecnej wersji zapisuje dane lokalnie w pliku JSON.

```mermaid
erDiagram
    OPIEKUN ||--o{ ZWIERZE : "opiekuje się"
    ZWIERZE ||--o{ WIZYTA : "ma"
    PRACOWNIK ||--o{ WIZYTA : "prowadzi jako lekarz"
    WIZYTA ||--o{ WIZYTA_USLUGA : "obejmuje"
    USLUGA ||--o{ WIZYTA_USLUGA : "jest wykonana jako"
    WIZYTA ||--o{ SZCZEPIENIE : "może obejmować"
    WIZYTA ||--o| PLATNOSC : "jest rozliczana przez"

    OPIEKUN {
        int id_opiekuna PK
        string imie
        string nazwisko
        string dane_kontaktowe
    }
    ZWIERZE {
        int id_zwierzecia PK
        int id_opiekuna FK
        string imie
        string gatunek
        string rasa
        string plec
        date przyblizona_data_urodzenia
        string numer_microczipu
    }
    PRACOWNIK {
        int id_pracownika PK
        string dane_pracownika
        string rola
    }
    WIZYTA {
        int id_wizyty PK
        int id_zwierzecia FK
        int id_lekarza FK
        datetime termin
        string powod
        string status
        string objawy
        string rozpoznanie
        string zalecenia
    }
    USLUGA {
        int id_uslugi PK
        string nazwa
        decimal cena
    }
    WIZYTA_USLUGA {
        int id_wizyty FK
        int id_uslugi FK
        decimal cena_w_chwili_wykonania
    }
    SZCZEPIENIE {
        int id_szczepienia PK
        int id_wizyty FK
        string nazwa_szczepionki
        date data_podania
        date termin_kolejnej_dawki
    }
    PLATNOSC {
        int id_platnosci PK
        int id_wizyty FK
        decimal kwota
        date data_platnosci
        string sposob_platnosci
    }
```

### Uwagi do ERD
- Relacja Opiekun–Zwierzę jest typu jeden do wielu; każde zwierzę ma jednego opiekuna głównego.
- Relacja Zwierzę–Wizyta jest typu jeden do wielu.
- Każda wizyta ma jednego lekarza; encja Pracownik przechowuje również informację o roli.
- Wizyta i Usługa są połączone encją pośrednią Wizyta_Usługa, ponieważ jedna wizyta może obejmować wiele usług.
- Płatność powiązano z wizytą jako relację zero lub jedna do jednej w uproszczonym modelu. Jeśli dopuszczone będą raty lub wiele płatności do jednej wizyty, relację trzeba zmienić.
- Pola i klucze są propozycją modelu logicznego. Opis źródłowy nie określa wszystkich typów danych ani zasad identyfikatorów.
