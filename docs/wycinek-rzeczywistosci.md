# PETVET — opis wycinka rzeczywistości

## 1. Cel i kontekst
PETVET jest systemem wspierającym pracę przychodni weterynaryjnej zajmującej się profilaktyką, diagnostyką i leczeniem zwierząt domowych, przede wszystkim psów i kotów. Z usług korzystają stali i nowi opiekunowie. W przychodni pracują lekarze weterynarii oraz pracownicy recepcji.

Dane o opiekunach, zwierzętach, terminach, konsultacjach, szczepieniach i płatnościach powinny być dostępne w jednym uporządkowanym miejscu. Celem jest ograniczenie pomyłek przy rejestracji, usprawnienie terminarza lekarzy i zapewnienie dostępu do historii leczenia.

## 2. Główne procesy
1. **Obsługa opiekuna i rejestracja zwierzęcia** — sprawdzenie, czy opiekun i zwierzę mają już karty; w razie potrzeby utworzenie nowych.
2. **Rezerwacja wizyty** — wybór pacjenta, lekarza, terminu i powodu wizyty; sprawdzenie konfliktu terminu.
3. **Przyjęcie i realizacja wizyty** — odczytanie historii, badanie, zapis diagnozy, zaleceń, usług i ewentualnego szczepienia.
4. **Rozliczenie** — ustalenie kosztu wykonanych usług i odnotowanie płatności gotówką.
5. **Kontynuacja leczenia** — przegląd historii, wskazanie kontroli i planowanie przypomnień e-mail.

## 3. Uczestnicy
- **Opiekun zwierzęcia** — przekazuje dane, zgłasza potrzebę wizyty i otrzymuje informacje o terminie.
- **Recepcjonista** — prowadzi rejestrację, terminarz i rozliczenie.
- **Lekarz weterynarii** — realizuje wizytę i prowadzi dokumentację medyczną.
- **Zewnętrzny system poczty e-mail** — planowana usługa do wysyłania potwierdzeń/przypomnień.

## 4. Zakres obecnej aplikacji a zakres docelowy
Obecny kod Python/Tkinter obsługuje dodawanie opiekunów i zwierząt, umawianie i odwoływanie wizyt, zakończenie wizyty, zapis diagnozy i zaleceń, zapis szczepienia, historię leczenia oraz odnotowanie płatności. Dane przechowywane są w lokalnym pliku JSON.

W aktualnym kodzie nie ma jeszcze:
- rzeczywistej wysyłki e-mail;
- mechanizmu logowania i kontroli uprawnień;
- osobnych kart pracowników;
- cennika i pozycji wykonanych usług jako osobnych rekordów;
- rejestrowania terminu kolejnej dawki szczepienia;
- raportów i zestawień;
- pełnej walidacji długości wizyt i nakładania się przedziałów czasowych.

Powyższe funkcje mogą należeć do zakresu docelowego, ale muszą być traktowane jako wymagania do realizacji, a nie jako istniejące możliwości programu.

## 5. Uzgodnione decyzje projektowe
- Nazwa: PETVET.
- Autorzy: Adrian Kuśmirek i Maciej Mazanek.
- Integracja: planowana poczta e-mail.
- Płatność: w zakresie tej wersji wyłącznie gotówka.
- Poziom szczegółowości: średni.
- Zespół: dwie osoby — wymaga potwierdzenia zgody prowadzącego, ponieważ instrukcje laboratoriów wskazują 3–4 osoby.

## 6. Słownik
| Pojęcie | Znaczenie |
|---|---|
| Opiekun | Osoba odpowiedzialna za zwierzę, kontaktująca się z przychodnią i dokonująca płatności. |
| Zwierzę / pacjent | Zwierzę objęte opieką przychodni. |
| Karta opiekuna | Dane identyfikacyjne i kontaktowe opiekuna. |
| Karta zwierzęcia | Dane pacjenta powiązane z opiekunem i historią leczenia. |
| Lekarz | Pracownik prowadzący konsultację i dokumentację leczenia. |
| Wizyta | Zaplanowana lub odbyta konsultacja z terminem, lekarzem, pacjentem i statusem. |
| Historia leczenia | Zestaw zrealizowanych wizyt, diagnoz, zaleceń i szczepień. |
| Szczepienie | Informacja o wykonanym szczepieniu; docelowo również data kolejnej dawki. |
| Płatność | Odnotowanie uregulowania należności; w uzgodnionym zakresie gotówką. |

## 7. Szczegółowy przebieg pracy przychodni według przygotowanego opisu

### 7.1. Obsługa opiekuna i rejestracja zwierzęcia
1. Opiekun zgłasza się osobiście lub telefonicznie.
2. Recepcjonista sprawdza, czy opiekun ma już kartę.
3. Jeśli karta nie istnieje, tworzy ją, zapisując imię, nazwisko i dane kontaktowe.
4. Recepcjonista sprawdza, czy zwierzę jest już zarejestrowane.
5. Jeśli jest to nowy pacjent, tworzy kartę zwierzęcia zawierającą imię, gatunek, rasę, płeć, przybliżoną datę urodzenia i opcjonalny numer mikroczipu.
6. Każde zwierzę ma przypisanego jednego opiekuna głównego.

### 7.2. Rezerwacja terminu
1. Recepcjonista sprawdza terminarz wybranego lekarza.
2. Uzgadnia z opiekunem dzień i godzinę.
3. Tworzy wizytę powiązaną ze zwierzęciem i lekarzem.
4. Zapisuje powód zgłoszenia, termin i status wizyty.
5. System nie powinien dopuścić do dwóch wizyt u tego samego lekarza w tym samym czasie.
6. Wizyta może zostać przełożona lub odwołana. Przypomnienie e-mail jest funkcją planowaną.

### 7.3. Przyjęcie i realizacja wizyty
1. Recepcja potwierdza przybycie pacjenta.
2. Lekarz otwiera kartę zwierzęcia i historię leczenia.
3. Lekarz zapisuje objawy, rozpoznanie i zalecenia.
4. Do wizyty można przypisać wykonane usługi, np. badanie, szczepienie lub drobny zabieg.
5. Przy szczepieniu zapisywana jest nazwa/opis szczepionki i data podania; opis docelowy przewiduje także termin kolejnej dawki.
6. Po zakończeniu badania lekarz oznacza wizytę jako zrealizowaną.

### 7.4. Rozliczenie
1. Recepcja otrzymuje listę usług wykonanych podczas wizyty.
2. Należność jest ustalana na podstawie cennika.
3. W opisie źródłowym przewidziano gotówkę lub kartę, jednak dla aktualnego zakresu projektu PETVET przyjęto wyłącznie płatność gotówką.
4. System powinien umożliwić wystawienie potwierdzenia zapłaty.
5. Za wizytę odwołaną lub nieodbytą nie tworzy się rozliczenia za niewykonane usługi.

### 7.5. Kontynuacja leczenia i przypomnienia
1. Lekarz może wskazać zalecany termin kontroli.
2. Recepcja może na tej podstawie umówić kolejną wizytę.
3. System powinien pozwolić sprawdzić planowane szczepienia i wizyty kontrolne.
4. Przypomnienie e-mail może być wysłane, jeśli opiekun wyraził zgodę na taką formę kontaktu.
5. Historia leczenia jest dostępna uprawnionym pracownikom.

## 8. Dane i encje wskazane w opisie
| Encja | Najważniejsze informacje wynikające z opisu |
|---|---|
| Opiekun | Imię, nazwisko, dane kontaktowe. |
| Zwierzę | Imię, gatunek, rasa, płeć, przybliżona data urodzenia, opcjonalny numer mikroczipu, opiekun główny. |
| Pracownik | Dane pracownika i rola; opis wskazuje recepcję i lekarzy oraz ograniczenie dostępu według roli. |
| Wizyta | Termin, powód zgłoszenia, status, zwierzę, lekarz, opis medyczny. |
| Usługa | Nazwa i cena w cenniku. |
| Wizyta_Usługa | Powiązanie wizyty z wykonanymi usługami oraz cena z chwili wykonania. |
| Szczepienie | Podana szczepionka, data podania, opcjonalny termin kolejnej dawki. |
| Płatność | Kwota, data i sposób opłacenia; w zakresie projektu metoda gotówkowa. |

## 9. Reguły i ograniczenia wynikające z opisu
- Jeden opiekun może mieć wiele zwierząt.
- Jedno zwierzę ma jednego opiekuna głównego.
- Jedno zwierzę może mieć wiele wizyt.
- Każda wizyta dotyczy jednego zwierzęcia i jednego lekarza.
- Jedna wizyta może obejmować wiele usług.
- Nie wolno zapisać dwóch wizyt u tego samego lekarza w tym samym czasie.
- Nieobecność lub odwołanie wizyty nie powoduje naliczenia opłat za niewykonane usługi.
- Przypomnienia e-mail wymagają zgody opiekuna.
- Dostęp do danych opiekunów i dokumentacji medycznej powinien być ograniczony rolą pracownika.

## 10. Kwestie wymagające doprecyzowania
- Dokładny zakres danych kontaktowych opiekuna i to, które z nich są obowiązkowe.
- Czy termin wizyty ma określony czas trwania i jak wykrywane są nakładające się przedziały.
- Jakie dokładnie statusy wizyty są obsługiwane, w tym czy „nieobecność” jest osobnym statusem.
- Czy potwierdzenie rezerwacji jest wysyłane automatycznie, czy wysyłane jest wyłącznie przypomnienie.
- Z jakim wyprzedzeniem wysyłane jest przypomnienie e-mail.
- Czy cennik i potwierdzenie zapłaty będą częścią aktualnej wersji aplikacji.
- Jak szczegółowo ma być realizowana kontrola uprawnień pracowników.
