# Screenshot Organizer

# === KROK 1: Import bibliotek ===
import os       # do plików/folderów
import shutil   # do przenoszenia

# === KROK 2: Zdefiniuj ścieżki ===
desktop_path = os.path.expanduser("~/Desktop")
screenshots_folder = os.path.join(desktop_path, "Screenshoty")

# === KROK 3: Sprawdź czy folder Screenshoty istnieje ===
if not os.path.exists(screenshots_folder):
    os.makedirs(screenshots_folder)
    print("Folder Screenshoty został stworzony!")

# === KROK 4: Znajdź wszystkie pliki na Desktop ===
all_files = os.listdir(desktop_path)

# === KROK 5: Licznik ===
counter = 0

# === KROK 6: Dla każdego pliku ===
for filename in all_files:
    # Sprawdź czy to screenshot
    if filename.startswith("Zrzut ekranu") and filename.endswith(".png"):
        # To jest screenshot!
        
        # Pełne ścieżki
        source = os.path.join(desktop_path, filename)
        destination = os.path.join(screenshots_folder, filename)
        
        # Przenieś
        shutil.move(source, destination)
        
        # Zwiększ licznik
        counter += 1

# === KROK 7: Podsumowanie ===
print(f"Przeniesiono {counter} screenshotów!")