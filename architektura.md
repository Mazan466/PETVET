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
