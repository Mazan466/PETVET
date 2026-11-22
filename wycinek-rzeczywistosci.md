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
