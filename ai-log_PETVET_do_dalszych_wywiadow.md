# Dziennik pracy z AI — PETVET

> Dziennik wywiadów z symulowanymi interesariuszami (role odgrywa AI). Pytania zespołu są **skróconymi parafrazami**, a odpowiedzi AI — **streszczeniami**, nie dosłownym zapisem rozmowy. Pełny zapis wywiadu jest przechowywany osobno. Nieuzupełnione pola pozostawiono celowo do samodzielnej analizy.

## 1. Wywiady z klientem AI

**Zespół:** Adrian Kuśmirek, Maciej Mazanek  
**Projekt:** PETVET  
**Cel:** zebranie i stopniowe doprecyzowanie wymagań systemu przychodni weterynaryjnej.

### Rozmowa 1 — kierownik przychodni (wywiad wstępny)

**Rozmówca:** kierownik przychodni weterynaryjnej, symulowany przez AI.  
**Charakter rozmowy:** wstępne rozpoznanie problemów i potrzeb; szczegóły wymagają dalszej weryfikacji.

| Nr | Pytanie zespołu (skrócone) | Odpowiedź klienta AI (streszczenie) |
|---:|---|---|
| 1 | Jakich funkcji brakuje w obecnym systemie i czego oczekują pracownicy? | Dane są rozproszone, a część zadań wykonywana ręcznie. Potrzebne są sprawna rejestracja, harmonogram wizyt, historia leczenia, dokumentacja, kontrola płatności i prosty interfejs. Przydatne byłyby przypomnienia. |
| 2 | Na czym zależy Państwu przy rejestracji opiekunów i zwierząt? | Szybkie dodawanie opiekuna (imię, nazwisko, telefon, e-mail) i zwierzęcia (imię, gatunek, rasa, wiek/data urodzenia), przypisanie wielu zwierząt do opiekuna, edycja, wyszukiwanie i unikanie duplikatów. |
| 3 | Jakie problemy mają lekarze z obecnym programem i co chcieliby usprawnić? | Trudno szybko znaleźć historię leczenia; dokumentacja zajmuje dużo czasu. Lekarze chcą podglądu wizyt i szczepień, wpisywania diagnoz i zaleceń, dziennego harmonogramu i zachowania historii po zakończeniu wizyty. |
| 4 | Czy system wykrywający konflikty wizyt, przypominający e-mailem i obsługujący płatności spełni potrzeby? Czy są inne wymagania? | Klient chce komunikatów o kolizjach, przypomnień e-mail (najlepiej dzień przed wizytą), prostego rozliczania **gotówką** i statusu opłacenia. Dodatkowo podkreśla bezpieczeństwo danych i prostotę obsługi. Pyta o zachowanie danych po awarii. |

**Zakończenie rozmowy (nie liczymy jako pytania nr 5):** Zespół zapewnił, że dane nie powinny znikać po zamknięciu programu ani awarii, oraz zadeklarował prosty interfejs. Klient podziękował, nie zgłosił na tym etapie dalszych wymagań i zapowiedział możliwość doprecyzowania szczegółów. Są to deklaracje i oczekiwania, **nie dowód wdrożenia zabezpieczeń**.

**Najważniejsze ustalenia z pierwszej rozmowy:** rejestracja opiekunów i zwierząt, planowanie wizyt i wykrywanie kolizji, historia leczenia i szczepień, diagnozy i zalecenia, rozliczenia gotówkowe, trwały zapis danych, czytelny interfejs. Przypomnienia e-mail są pożądane, ale ich termin wdrożenia nie został rozstrzygnięty; płatności kartą i potwierdzanie obecności nie są wymagane na start.

#### Refleksja zespołu po rozmowie 1 — do samodzielnego wypełnienia

**O co nie zapytaliśmy, a powinniśmy? (maksymalnie 3 kwestie):**

1. [UZUPEŁNI ZESPÓŁ]
2. [UZUPEŁNI ZESPÓŁ]
3. [UZUPEŁNI ZESPÓŁ]

**Dlaczego wracamy do rozmowy / co chcemy wyjaśnić?**  
[UZUPEŁNI ZESPÓŁ]

### Rozmowa 2 — wywiad uzupełniający (do przeprowadzenia)

**Rozmówca / rola:** [UZUPEŁNIĆ]  
**Data:** [UZUPEŁNIĆ]

| Nr | Pytanie zespołu (skrócone) | Odpowiedź klienta AI (streszczenie) |
|---:|---|---|
| 1 | [UZUPEŁNIĆ] | [UZUPEŁNIĆ] |
| 2 | [UZUPEŁNIĆ] | [UZUPEŁNIĆ] |
| 3 | [UZUPEŁNIĆ] | [UZUPEŁNIĆ] |
| 4 | [UZUPEŁNIĆ] | [UZUPEŁNIĆ] |
| 5 | [UZUPEŁNIĆ] | [UZUPEŁNIĆ] |
| 6 | [UZUPEŁNIĆ] | [UZUPEŁNIĆ] |

**O co nie zapytaliśmy? (maksymalnie 3 kwestie, tylko jeśli potrzebne):**

1. [UZUPEŁNI ZESPÓŁ]
2. [UZUPEŁNI ZESPÓŁ]
3. [UZUPEŁNI ZESPÓŁ]

### Kolejne rozmowy z użytkownikami systemu (opcjonalnie)

**Rozmowa 3 — recepcja (symulacja AI):** [DATA / PYTANIA / ODPOWIEDZI — DO UZUPEŁNIENIA]  
**Rozmowa 4 — lekarz weterynarii (symulacja AI):** [DATA / PYTANIA / ODPOWIEDZI — DO UZUPEŁNIENIA]

> Jeśli przeprowadzicie te rozmowy, dopiszcie tabelę pytań i odpowiedzi w formacie użytym wyżej. Nie przedstawiajcie symulacji AI jako wywiadu z rzeczywistym pracownikiem.

### Ocena wywiadów — podsumowanie po zakończeniu rozmów

- **O co nie zapytaliśmy, a powinniśmy:** [UZUPEŁNI ZESPÓŁ na podstawie refleksji po rozmowach]
- **Czy klient udzielił sprzecznych odpowiedzi:** [UZUPEŁNI ZESPÓŁ]
- **Jakie nowe wymagania dodaliśmy i dlaczego:** [UZUPEŁNI ZESPÓŁ po porównaniu z wersją 0]
- **Jakie sugestie odrzuciliśmy i dlaczego:** [UZUPEŁNI ZESPÓŁ]

---

## 2. Łowca luk — trzy historyjki Must

**Status: ćwiczenie nie zostało przeprowadzone w tym wywiadzie.** Poniższe obszary są listą do przyszłej analizy, a nie wynikami 15 wygenerowanych i ocenionych przypadków dla każdej historyjki.

### R-01 Rejestracja opiekuna

Do sprawdzenia m.in.: duplikat osoby, brak telefonu, błędny format telefonu, bardzo długie dane, polskie znaki, przerwanie formularza, awaria zapisu, ponowne kliknięcie zapisu, spacje na początku i końcu, nieoczekiwane znaki, pusty ciąg po usunięciu spacji, istniejący opiekun o tym samym nazwisku, brak uprawnień, uszkodzony plik danych, brak miejsca na dysku.

| Przypadek | Decyzja: kryterium / nowe wymaganie / odrzucenie | Uzasadnienie |
|---|---|---|
| [UZUPEŁNIĆ po przeprowadzeniu ćwiczenia — 15 przypadków] | | |

### R-02 Rejestracja zwierzęcia

Do sprawdzenia m.in.: nieistniejący opiekun, brak imienia, brak gatunku, nieznany gatunek, duplikat zwierzęcia, wiele zwierząt jednego opiekuna, brak rasy, błędny numer mikroczipu, bardzo długie pole, anulowanie formularza, awaria zapisu, usunięcie opiekuna, niezgodny identyfikator, uszkodzony plik, brak miejsca na dysku.

| Przypadek | Decyzja: kryterium / nowe wymaganie / odrzucenie | Uzasadnienie |
|---|---|---|
| [UZUPEŁNIĆ po przeprowadzeniu ćwiczenia — 15 przypadków] | | |

### R-03 Umówienie wizyty

Do sprawdzenia m.in.: termin w przeszłości, zajęty termin, nakładające się przedziały o różnej długości, nieistniejące zwierzę, brak lekarza, pusty powód, błędny format daty, termin poza godzinami pracy, równoczesna próba rezerwacji, odwołana wizyta w tym samym terminie, zmiana czasu, brak zapisu do pliku, awaria aplikacji, niepoprawny identyfikator, brak dostępności poczty e-mail.

| Przypadek | Decyzja: kryterium / nowe wymaganie / odrzucenie | Uzasadnienie |
|---|---|---|
| [UZUPEŁNIĆ po przeprowadzeniu ćwiczenia — 15 przypadków] | | |

## 3. Porównanie wersji 0 i wyników pracy z AI

- Liczba wymagań z wersji 0, które pozostały: **[DO USTALENIA po zestawieniu z faktyczną wersją 0]**.
- Liczba wymagań dodanych po wywiadzie: **[DO USTALENIA po zestawieniu z faktyczną wersją 0]**.
- Liczba sugestii AI odrzuconych jako nieuzasadnione: **[DO USTALENIA po ocenie zespołu]**.

### Refleksja — dokładnie trzy zdania (propozycja do zatwierdzenia przez zespół)

1. AI pomogło doprecyzować potrzeby recepcji i lekarzy oraz wymagania dotyczące dokumentacji, terminów i bezpieczeństwa danych.
2. Propozycje płatności kartą i potwierdzania obecności przez e-mail wykraczały poza uzgodniony zakres pierwszej wersji.
3. W wywiadzie nie rozstrzygnięto szczegółowych zasad edycji zakończonych wizyt, wysyłania powiadomień ani odzyskiwania danych po awarii.

## 4. Rejestr użycia AI

| Data | Zadanie | Co wygenerowało AI | Co sprawdził/poprawił zespół |
|---|---|---|---|
| [DATA WYWIADU — DO WPISANIA] | Wywiad z klientem AI | Odpowiedzi w roli kierownika przychodni na 4 główne pytania oraz odpowiedź końcowa | Zespół prowadził rozmowę, przedstawiał propozycje i zadeklarował zabezpieczenie danych; weryfikacja wymagań w dokumentacji pozostaje do potwierdzenia |
| 2026-11-22 | Uporządkowanie wywiadu w ai-log.md | Cytaty wypowiedzi zespołu, streszczenia odpowiedzi klienta, tabela ustaleń i szkic oceny wywiadu | [DO POTWIERDZENIA przez zespół po przeglądzie pliku] |
| [DATA] | Analiza luk dla trzech historyjek Must | [NIE PRZEPROWADZONO w tej rozmowie] | [DO UZUPEŁNIENIA] |
| [DATA] | Modelowanie Lab 2 | [NIE DOKUMENTOWANO w tej rozmowie] | [DO UZUPEŁNIENIA] |
