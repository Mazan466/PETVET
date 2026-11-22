# PETVET — event storming

> Materiał roboczy przygotowany na podstawie opisu wycinka rzeczywistości i aktualnego kodu. Laboratorium 2 wymaga przeprowadzenia event stormingu bez AI. Zespół powinien zweryfikować, zmienić kolejność i uzupełnić poniższe propozycje podczas ćwiczenia, a następnie udokumentować faktyczny wynik i pytania otwarte.

## 1. Proponowana oś zdarzeń
Zdarzenia zapisano w czasie przeszłym — opisują coś, co się wydarzyło.

| Lp. | Zdarzenie domenowe | Polecenie, które je wywołuje | Aktor / źródło |
|---:|---|---|---|
| 1 | Opiekun zarejestrowany | Zarejestruj opiekuna | Recepcjonista |
| 2 | Zwierzę zarejestrowane | Zarejestruj zwierzę | Recepcjonista |
| 3 | Wizyta zgłoszona | Zgłoś potrzebę wizyty | Opiekun |
| 4 | Dostępność lekarza sprawdzona | Sprawdź termin lekarza | Recepcjonista |
| 5 | Wizyta zaplanowana | Umów wizytę | Recepcjonista |
| 6 | Potwierdzenie wizyty przekazane do wysyłki | Wyślij potwierdzenie | PETVET |
| 7 | Wiadomość e-mail przyjęta przez usługę | Dostarcz wiadomość | System poczty e-mail |
| 8 | Pacjent przyjęty | Potwierdź przybycie | Recepcjonista |
| 9 | Historia pacjenta wyświetlona | Otwórz historię leczenia | Lekarz |
| 10 | Badanie przeprowadzone | Przeprowadź badanie | Lekarz |
| 11 | Diagnoza zapisana | Zapisz diagnozę | Lekarz |
| 12 | Zalecenia zapisane | Zapisz zalecenia | Lekarz |
| 13 | Szczepienie odnotowane | Zapisz szczepienie | Lekarz |
| 14 | Wizyta zrealizowana | Zakończ wizytę | Lekarz |
| 15 | Koszt wizyty ustalony | Rozlicz wykonane usługi | Recepcjonista |
| 16 | Płatność gotówką odnotowana | Odnotuj przyjęcie gotówki | Recepcjonista |
| 17 | Wizyta odwołana | Odwołaj wizytę | Recepcjonista |
| 18 | Historia leczenia uzupełniona | Zapisz dane z wizyty | PETVET |

## 2. Pytania otwarte
1. Czy system wysyła e-mail po każdej rezerwacji, czy tylko przypomnienie przed terminem?
2. Ile czasu przed wizytą wysyłane jest przypomnienie?
3. Co powinno się wydarzyć, gdy usługa poczty e-mail jest niedostępna?
4. Czy opiekun może samodzielnie odwołać wizytę, czy robi to wyłącznie recepcja?
5. Jak długo trwa typowa wizyta i jak wykrywać nakładanie się przedziałów?
6. Czy wizyta może zostać oznaczona jako „nieobecność”?
7. Czy płatność gotówką jest rejestrowana dopiero po zakończeniu wizyty?
8. Czy lekarz może poprawić dokumentację już po zamknięciu wizyty?
9. Czy wymagane jest przechowywanie zgody opiekuna na kontakt e-mail?
10. Co dzieje się, gdy zapis do pliku danych nie powiedzie się?

## 3. Miejsce na wynik rzeczywistego ćwiczenia
- Data i uczestnicy: [UZUPEŁNIĆ]
- Zdarzenia usunięte lub zmienione: [UZUPEŁNIĆ]
- Nowe zdarzenia dodane przez zespół: [UZUPEŁNIĆ]
- Uzgodniona kolejność i wyjątki: [UZUPEŁNIĆ]
- Zdjęcie tablicy / link do tablicy online: [DODAĆ LINK LUB ŚCIEŻKĘ]
