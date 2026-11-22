# Wymagania systemu PETVET

## 1. Granica systemu
PETVET wspiera wewnętrzną obsługę przychodni weterynaryjnej. Użytkownikami są opiekunowie (pośrednio, poprzez kontakt z recepcją), recepcjoniści i lekarze weterynarii. System poczty e-mail jest usługą zewnętrzną. Wysyłka e-mail jest planowana i nie występuje jeszcze w aktualnym kodzie.

## 2. Aktorzy i systemy zewnętrzne

| Nazwa | Rodzaj | Potrzeba / odpowiedzialność |
|---|---|---|
| Opiekun zwierzęcia | Aktor ludzki | Zgłasza zwierzę do przychodni, ustala termin i otrzymuje informacje o wizycie. |
| Recepcjonista | Aktor ludzki | Rejestruje opiekunów i zwierzęta, zarządza terminami oraz odnotowuje płatność. |
| Lekarz weterynarii | Aktor ludzki | Przegląda historię pacjenta, realizuje wizytę i zapisuje diagnozę oraz zalecenia. |
| System poczty e-mail | System zewnętrzny | Przyjmuje od PETVET wiadomości z potwierdzeniami lub przypomnieniami i dostarcza je na adres opiekuna. |

> Wymaganie Laboratorium 1 wskazuje minimum 3 aktorów ludzkich i 1 system zewnętrzny. Powyższa tabela spełnia liczbę aktorów ludzkich. Opiekun jest aktorem systemu, nawet jeśli obecna aplikacja jest obsługiwana bezpośrednio przez personel.

## 3. Wersja 0 — bez AI (OBOWIĄZKOWO UZUPEŁNIĆ SAMODZIELNIE)
Instrukcja Laboratorium 1 wymaga, aby każdy członek zespołu najpierw samodzielnie wypisał potrzeby bez użycia AI, a następnie zespół wybrał 10 najważniejszych. Poniższa sekcja jest celowo pozostawiona do uzupełnienia przez Adriana i Macieja. Nie należy kopiować tu historyjek z dalszej części dokumentu.

| ID | Wymaganie zapisane przez zespół bez AI |
|---|---|
| V0-01 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-02 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-03 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-04 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-05 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-06 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-07 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-08 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-09 | [UZUPEŁNIĆ SAMODZIELNIE] |
| V0-10 | [UZUPEŁNIĆ SAMODZIELNIE] |

Data sporządzenia wersji 0: [WPISAĆ]  
Potwierdzenie, że lista powstała przed użyciem AI: [POTWIERDZIĆ]

## 4. Historyjki użytkownika

Priorytety MoSCoW: Must — konieczne; Should — ważne; Could — opcjonalne; Won't — poza zakresem tej wersji. Liczba historyjek Must wynosi 4 (limit z instrukcji: maksymalnie 5).

### R-01 Rejestracja opiekuna (Must)
Jako recepcjonista chcę utworzyć kartę opiekuna z imieniem, nazwiskiem i numerem telefonu, aby móc powiązać z nim zwierzęta i kontaktować się z nim.

- **Zakładając**, że w systemie nie ma jeszcze karty tego opiekuna,
- **Gdy** recepcjonista wprowadzi wymagane dane i zatwierdzi zapis,
- **Wtedy** system zapisze kartę opiekuna z unikalnym identyfikatorem.

**Sytuacja błędna:** gdy wymagane pole jest puste, system nie zapisuje karty i informuje o brakujących danych.

### R-02 Rejestracja zwierzęcia (Must)
Jako recepcjonista chcę utworzyć kartę zwierzęcia i przypisać ją do opiekuna, aby przychodnia mogła prowadzić historię leczenia pacjenta.

- **Zakładając**, że istnieje karta opiekuna,
- **Gdy** recepcjonista poda opiekuna, imię zwierzęcia i gatunek,
- **Wtedy** system zapisze zwierzę z powiązaniem do wskazanego opiekuna.

**Sytuacja błędna:** gdy wskazany opiekun nie istnieje, system odrzuci zapis zwierzęcia.

### R-03 Umówienie wizyty (Must)
Jako recepcjonista chcę umówić wizytę dla zarejestrowanego zwierzęcia u wybranego lekarza, aby zaplanować konsultację.

- **Zakładając**, że zwierzę istnieje, a termin lekarza jest wolny,
- **Gdy** recepcjonista poda lekarza, przyszły termin i powód wizyty,
- **Wtedy** system zapisze wizytę ze statusem „zaplanowana”.

**Sytuacja błędna:** gdy lekarz ma już zaplanowaną wizytę w kolidującym terminie, system odrzuci rezerwację i wyświetli komunikat.

### R-04 Zapis dokumentacji wizyty (Must)
Jako lekarz weterynarii chcę zapisać diagnozę i zalecenia po konsultacji, aby zachować informacje o leczeniu pacjenta.

- **Zakładając**, że istnieje zaplanowana wizyta,
- **Gdy** lekarz uzupełni diagnozę i zatwierdzi zakończenie wizyty,
- **Wtedy** system zapisze diagnozę i zalecenia oraz zmieni status wizyty na „zrealizowana”.

**Sytuacja błędna:** gdy wskazana wizyta nie istnieje albo nie ma statusu „zaplanowana”, system nie pozwoli jej zakończyć.

### R-05 Historia leczenia (Should)
Jako lekarz weterynarii chcę wyświetlić historię zrealizowanych wizyt zwierzęcia, aby zapoznać się z wcześniejszym leczeniem.

- **Zakładając**, że zwierzę jest zarejestrowane,
- **Gdy** lekarz wybierze pacjenta,
- **Wtedy** system wyświetli chronologicznie zrealizowane wizyty wraz z diagnozami i zaleceniami.

### R-06 Odwołanie wizyty (Should)
Jako recepcjonista chcę odwołać zaplanowaną wizytę, aby zwolnić termin, z którego opiekun nie skorzysta.

- **Zakładając**, że wizyta ma status „zaplanowana”,
- **Gdy** recepcjonista wybierze polecenie odwołania,
- **Wtedy** system zmieni status wizyty na „odwołana”.

### R-07 Odnotowanie płatności gotówką (Should)
Jako recepcjonista chcę odnotować przyjęcie gotówki za zrealizowaną wizytę, aby zachować informację o rozliczeniu.

- **Zakładając**, że wizyta została zrealizowana i nie jest opłacona,
- **Gdy** recepcjonista potwierdzi przyjęcie gotówki,
- **Wtedy** system zapisze metodę płatności „gotówka” i oznaczy wizytę jako opłaconą.

### R-08 Ewidencja szczepienia (Should)
Jako lekarz weterynarii chcę zapisać informację o szczepieniu wykonanym podczas wizyty, aby uzupełnić dokumentację profilaktyki pacjenta.

- **Zakładając**, że trwa rejestrowanie realizacji wizyty,
- **Gdy** lekarz poda nazwę lub opis szczepienia,
- **Wtedy** system zapisze tę informację w dokumentacji wizyty.

### R-09 Przypomnienie e-mail (Could)
Jako recepcjonista chcę wysłać opiekunowi przypomnienie o nadchodzącej wizycie pocztą e-mail, aby ograniczyć liczbę nieobecności.

- **Zakładając**, że opiekun ma poprawny adres e-mail i wyraził zgodę na kontakt,
- **Gdy** zostanie uruchomione wysłanie przypomnienia,
- **Wtedy** system przekaże wiadomość do zewnętrznego systemu poczty e-mail.

**Uwaga:** integracja jest planowana; funkcja nie jest obecnie zaimplementowana.

### R-10 Zestawienie wizyt (Won't)
Jako kierownik przychodni chcę generować zestawienie liczby wizyt w wybranym okresie, aby analizować obciążenie placówki.

- **Zakładając**, że w systemie znajdują się wizyty z różnych dni,
- **Gdy** kierownik wybierze zakres dat,
- **Wtedy** system docelowo wyświetli liczbę wizyt w tym okresie.

**Uzasadnienie Won't:** funkcja nie jest priorytetem dla obecnej wersji i nie występuje w aktualnym kodzie.

## 5. Wymagania niefunkcjonalne

Poniższe wartości są proponowanymi celami dla niewielkiej, lokalnej aplikacji desktopowej. Zespół powinien je zaakceptować i zweryfikować na rzeczywistym sprzęcie.

| ID | Obszar i wymaganie mierzalne | Sposób sprawdzenia |
|---|---|---|
| NF-01 | Przy bazie do 1 000 opiekunów, 2 000 zwierząt i 10 000 wizyt wyświetlenie listy lub historii powinno trwać maksymalnie 2 s w 95% prób. | 20 pomiarów na testowym zbiorze danych. |
| NF-02 | Zapis pojedynczego rekordu do lokalnego pliku danych powinien zakończyć się w maksymalnie 1 s dla bazy o rozmiarze do 10 MB. | 20 pomiarów czasu zapisu. |
| NF-03 | Po poprawnym zapisie dane muszą pozostać dostępne po zamknięciu i ponownym uruchomieniu aplikacji w 100% prób testowych. | 20 cykli zapis–zamknięcie–uruchomienie–odczyt. |
| NF-04 | Aplikacja powinna umożliwiać obsługę podstawowych funkcji na ekranie o rozdzielczości co najmniej 1366 × 768 pikseli bez ucięcia głównych przycisków. | Test interfejsu na ekranie o podanej rozdzielczości. |
| NF-05 | Każda próba zapisu niepoprawnej daty, nieistniejącego identyfikatora lub ujemnego kosztu musi zostać odrzucona w 100% przygotowanych testów walidacyjnych. | Zestaw minimum 15 testów danych błędnych. |
| NF-06 | Kopia pliku danych powinna być wykonywana co najmniej raz na dobę w docelowym środowisku pracy. | Kontrola procedury kopii zapasowej i daty ostatniej kopii. |

## 6. Założenia, ograniczenia i pytania otwarte

### Założenia
- Jedno zwierzę ma jednego głównego opiekuna.
- Wizyta dotyczy jednego zwierzęcia i jednego lekarza.
- W obecnej wersji płatność jest odnotowywana jako gotówka.
- Poczta e-mail jest integracją planowaną, nie działającą.
- Aplikacja jest lokalną aplikacją desktopową.

### Pytania otwarte do rozstrzygnięcia
1. Czy adres e-mail i zgoda na kontakt będą obowiązkowymi polami karty opiekuna?
2. Czy potwierdzenie rezerwacji ma być wysyłane od razu, czy tylko przypomnienie przed wizytą?
3. Ile godzin lub dni przed wizytą należy wysyłać przypomnienie?
4. Czy system ma blokować nakładające się przedziały wizyt, uwzględniając czas trwania wizyty?
5. Czy recepcjonista może edytować diagnozę po zakończeniu wizyty?
6. Czy w przyszłości dopuszczamy płatności kartą, mimo że obecny zakres obejmuje tylko gotówkę?

## 7. Weryfikacja INVEST
Historyjki należy sprawdzić w zespole pod kątem: niezależności, negocjowalności, wartości, możliwości oszacowania, małego rozmiaru i testowalności. Kryteria akceptacji zapisano w formacie Zakładając/Gdy/Wtedy, jednak ostateczne potwierdzenie INVEST należy do zespołu.

## 8. Pokrycie wymagań opisem wycinka rzeczywistości

Poniższa tabela wiąże wymagania z konkretnymi procesami opisanymi w dokumencie „PETVET — opis wycinka rzeczywistości”. Ułatwia sprawdzenie, czy historyjki mają uzasadnienie w przygotowanym opisie.

| ID / obszar | Uzasadnienie w opisie wycinka rzeczywistości |
|---|---|
| R-01 Rejestracja opiekuna | Proces „Obsługa opiekuna i rejestracja zwierzęcia”: sprawdzenie karty opiekuna i utworzenie jej z imieniem, nazwiskiem oraz danymi kontaktowymi. |
| R-02 Rejestracja zwierzęcia | Proces rejestracji zwierzęcia: karta pacjenta, dane identyfikacyjne i przypisanie opiekuna głównego. |
| R-03 Umówienie wizyty | Proces „Rezerwacja terminu wizyty”: wybór lekarza, terminu i powodu zgłoszenia oraz kontrola dostępności lekarza. |
| R-04 Zapis dokumentacji wizyty | Proces „Przyjęcie pacjenta i wykonanie wizyty”: zapis objawów, rozpoznania, zaleceń i oznaczenie wizyty jako zrealizowanej. |
| R-05 Historia leczenia | Opis wskazuje możliwość wyświetlenia wcześniejszych wizyt i udostępniania historii leczenia uprawnionym pracownikom. |
| R-06 Odwołanie wizyty | Proces rezerwacji przewiduje odwoływanie i przekładanie wizyt oraz aktualizację statusu. |
| R-07 Płatność gotówką | Proces „Rozliczenie i zakończenie wizyty” przewiduje obliczenie należności i zapis płatności; gotówka jest metodą przyjętą w zakresie tej wersji projektu. |
| R-08 Ewidencja szczepienia | Proces realizacji wizyty przewiduje zapis podanej szczepionki, daty podania i ewentualnego terminu kolejnej dawki. |
| R-09 Przypomnienie e-mail | Proces kontynuacji leczenia przewiduje przypomnienie o wizycie lub szczepieniu, jeśli opiekun wyraził zgodę na kontakt e-mail. |
| R-10 Zestawienie wizyt | W opisie zakresu wymieniono proste zestawienia liczby wizyt i wykonanych usług; w tej wersji historyjka pozostaje poza zakresem (Won't). |

### Funkcje opisane w źródle, które nie mają osobnej historyjki
- Przełożenie terminu wizyty — opisane w procesie rezerwacji; warto dodać osobną historyjkę, jeśli funkcja ma być osobno oceniana.
- Potwierdzenie przybycia pacjenta — czynność recepcji przed wizytą.
- Przypisanie do wizyty wykonanych usług — potrzebne do późniejszego rozliczenia.
- Ustalenie należności na podstawie cennika i wystawienie potwierdzenia zapłaty — opisane w procesie rozliczenia.
- Wyszukiwanie planowanych szczepień i terminów kontroli — opisane w procesie kontynuacji leczenia.
- Ograniczenie dostępu do danych według roli pracownika — wymaganie dotyczące ochrony danych; obecny kod nie realizuje pełnego mechanizmu uprawnień.

Uwaga: lista powyżej wynika z przygotowanego opisu, ale nie oznacza, że wszystkie te funkcje są już zaimplementowane. Zakres aktualnego kodu i zakres docelowy należy nadal rozróżniać.
