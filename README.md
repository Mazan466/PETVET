# PETVET

**System obsługi przychodni weterynaryjnej**

## Zespół
- Adrian Kuśmirek — GitHub: `Kusmir1999`
- Maciej Mazanek — GitHub: `Mazan466`

Nazwa zespołu: **PETVET**  
Temat: system wspierający obsługę przychodni weterynaryjnej zajmującej się profilaktyką, diagnostyką i leczeniem zwierząt domowych, przede wszystkim psów i kotów.

## Cel systemu
PETVET ma porządkować dane opiekunów i zwierząt, terminarz wizyt, dokumentację leczenia, szczepienia oraz rozliczenia. Obecna aplikacja jest prostą aplikacją desktopową w Pythonie z interfejsem Tkinter i lokalnym plikiem JSON.

## Zakres przyjęty w dokumentacji
- rejestracja opiekunów i zwierząt;
- umawianie, odwoływanie i realizacja wizyt;
- zapisywanie diagnoz, zaleceń i szczepień;
- historia leczenia;
- odnotowanie płatności gotówką;
- planowana integracja z zewnętrznym systemem poczty e-mail do przypomnień.

## Struktura
- `docs/wycinek-rzeczywistosci.md` — opis dziedziny i zakresu;
- `docs/wymagania.md` — aktorzy, wersja 0 do uzupełnienia, historyjki i wymagania niefunkcjonalne;
- `docs/ai-log.md` — rejestr pracy z AI i miejsca na rzeczywiste notatki zespołu;
- `docs/zdarzenia.md` — roboczy materiał do event stormingu;
- `docs/architektura.md` — diagramy Mermaid dla Laboratorium 2;
- `docs/log-poprawek.md` — rejestr zmian po weryfikacji i recenzji.

## Ważne decyzje i ograniczenia
1. Zespół liczy obecnie dwie osoby. Instrukcje Laboratorium 1 i 2 podają skład 3–4-osobowy. Należy potwierdzić u prowadzącego, czy dwuosobowy zespół jest dopuszczony.
2. Płatność przyjęta w zakresie projektu: wyłącznie gotówka. Obsługa karty z obecnego kodu nie jest częścią uzgodnionego zakresu i wymaga usunięcia albo jawnej zmiany decyzji.
3. E-mail jest planowaną integracją, a nie funkcją już działającą w aktualnym kodzie.
4. Dokumentacja opisuje docelowy zakres projektu. Nie należy przedstawiać funkcji planowanych jako już zaimplementowanych.

## Uruchomienie obecnej aplikacji
Wymagany Python 3 i biblioteka standardowa (Tkinter). Uruchomienie przykładowo:
```bash
python petvet.py
```
Aplikacja zapisuje dane w pliku `petvet_dane.json` obok skryptu (po poprawnym ustawieniu ścieżki).

## Uzupełnienia na podstawie opisu wycinka rzeczywistości

Dokumenty w katalogu `docs` zostały rozwinięte na podstawie pliku „PETVET_opis_wycinka_rzeczywistosci_Kuśmirek_Mazanek.pdf”. Dodano szczegółowy przebieg pięciu procesów, dane i reguły domenowe, mapowanie historyjek na opis źródłowy oraz logiczny szkic ERD.

Sekcje oznaczone jako wymagające rzeczywistej pracy zespołu pozostają do uzupełnienia: wersja 0 (bez AI), wyniki wywiadu, faktyczny rezultat event stormingu, rzeczywiste poprawki i recenzja krzyżowa. Nie należy wpisywać tam fikcyjnych działań.
