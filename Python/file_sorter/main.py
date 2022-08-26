import os
import shutil
import json
import sys
import pytest
from easygui import *


JSON_DATA = {"file_types": {"zdjęcia": ["gif", "jpg", "png", "jpeg", "tiff", "psd", "raw", "svg"], "exe": ["exe"], "dokumenty": ["pdf", "docx", "doc", "docm"], "Muzyka": ["mp3", "flac"], "Filmy": ["mp4", "avi", "dvd", "flv", "mov", "mpg"], "Niestandardowe": [], "Usuń": []}, "Rozszerzenia": ["gif", "jpg", "png", "jpeg", "tiff", "psd", "raw", "svg", "exe", "pdf", "docx", "doc", "docm", "mp3", "flac", "mp4", "avi", "dvd", "flv", "mov", "mpg", "txt", "odt"]}

class Files:
    file_types = None
    choices = ["Wybierz folder docelowy", "Wybierz folder do posortowania", "Ustawienia Zaawansowane",  "Continue"]
    moved_files = []
    ready_to_continue = False

    def __init__(self, from_folder_path=None, in_folder_path=None):
        self.from_folder = from_folder_path
        self.in_folder = in_folder_path
        self.enlargement = []
        self.file_types = self.read_config_file()
        # self.defualt_json =
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.save_config_file()
        return self

    def move_files(self, file_type_to_move="zdjęcia"):
        for file_name in os.listdir(self.from_folder):
            if isinstance(self.file_types[file_type_to_move], list):
                if self.enlargement_filtr_move(file_name, file_type_to_move):
                    break
            else:
                if self.name_filtr_move(file_name,file_type_to_move):
                    break

    def name_filtr_move(self, file_name, file_type_to_move):
        if self.file_types[file_type_to_move].lower() in file_name.split(".")[0].lower():
            from_file_path = self.from_folder + fr"\{file_name}"
            should_we_break = self.move_file(from_file_path, file_name)
            self.moved_files.append(file_name)
            if should_we_break:
                return True

    def enlargement_filtr_move(self, file_name, file_type_to_move):
        if file_name.split(".")[-1].lower() in self.file_types[file_type_to_move]:
            from_file_path = self.from_folder + fr"\{file_name}"
            should_we_break = self.move_file(from_file_path, file_name)
            self.moved_files.append(file_name)
            if should_we_break:
                return True

    def move_file(self, from_file_path, file_name):
        try:
            shutil.move(from_file_path, self.in_folder)
        except PermissionError as error:
            choices = ["Spróbuj ponownie", "Pomiń", "Zakończ działanie programu"]
            choice = buttonbox(
                f"nie udało sie przenieść pliku {file_name} \n Możliwe rozwiązania \n 1. Zamknij plik jeśli jest otwarty \n 2. Sprawdź czy plik nie znajduje się w folderze docelowym \n treść błędu: {error}",
                "Wykryto Błąd", choices)
            if choice == "Spróbuj ponownie":
                self.move_file(from_file_path, file_name)
            if choice == "Pomiń":
                pass
            if choice == "Zakończ działanie programu":
                return True
        except shutil.Error as error:
            os.remove(fr"{self.in_folder}\{file_name}")
            print(fr"remove {self.in_folder}\{file_name}")
            self.move_file(from_file_path, file_name)

    def select_files_type(self):
        msg = "Wybierz rodzaj plików króre chcesz posortować".center(80, " ")
        title = ""
        choices = [key for key in self.file_types.keys()]
        self.file_type = choicebox(msg, title, choices)
        if self.file_type is None:
            sys.exit(0)
        if self.file_type == "Niestandardowe":
            choice = buttonbox("Wybierz rodzaj filtra który chcesz dodać".center(80, " "), "", ["po nazwie", "po rozszerzeniu", "Anuluj"])
            if choice == "po rozszerzeniu":
                self.add_custom_filtr_enlargement()
            elif choice == "po nazwie":
                self.add_custom_filtr_name()
            elif choice == "Anuluj":
                self.select_files_type()
            elif choice is None:
                sys.exit(0)
        if self.file_type == "Usuń":
            to_remove_list = []
            msg = "Wybierz rozszerzenia które chcesz usunąć".center(80, " ")
            title = "narzędzie filtrów niestandardowych"
            choices = [key for key in self.file_types.keys()]
            choices.remove("Usuń")
            choices.remove("Niestandardowe")
            to_remove_list = multchoicebox(msg, title, choices)
            for to_remove in to_remove_list:
                self.file_types.pop(to_remove)
            self.select_files_type()


        return self.file_type

    def add_custom_filtr_enlargement(self):
        self.add_value_enlargement()
        self.add_key_enlargement()
        self.file_types[self.key] = self.value
        self.select_files_type()

    def add_custom_filtr_name(self):
        self.add_value_name()
        self.add_key_name()
        self.file_types[self.key] = self.value
        self.select_files_type()

    def add_key_enlargement(self):
        key = enterbox("Wprowadź nazwę filtra", "narzędzie filtrów niestandardowych")
        if key == None:
            sys.exit(0)
        if key == "":
            buttonbox("nie wprowadzono tyułu", "", ["Ok"])
            self.add_key_enlargement()
        else:
            print(key)
            self.key = key

    def add_key_name(self):
        key = enterbox("Wprowadź nazwę filtra", "narzędzie filtrów niestandardowych")
        if key is None:
            sys.exit(0)
        if key == "":
            buttonbox("nie wprowadzono tyułu", "", ["Ok"])
            self.add_key_name()
        else:
            print(key)
            self.key = key

    def add_value_name(self):
        value = enterbox("Wprowadź słowo klucz po którym pliki mają być filtrowane", "narzędzie filtrów niestandardowych")
        if value is None:
            sys.exit(0)
        if value == "":
            buttonbox("nic nie wpisano", "", ["Ok"])
            self.add_value_name()
        else:
            print(value)
            self.value = value

    def add_value_enlargement(self):
        value = []
        msg = "Wybierz rozszerzenia które chcesz filtrować".center(80, " ")
        title = "narzędzie filtrów niestandardowych"
        choices = self.enlargement
        value = multchoicebox(msg, title, choices)
        if value == None:
            if buttonbox("nie wybrano rozszerzeń", "", ["Ok"]) is None:
                sys.exit(0)
            self.add_value_enlargement()
        else:
            print(value)
            self.value = value
    def select_folder_from(self):
        self.from_folder = diropenbox("Wybierz Folder")

    def select_folder_in(self):
        self.in_folder = diropenbox("Wybierz Folder")

    def select_folders(self, reply=""):
        msg = "Wybierz Foldery".center(80, " ")
        reply = buttonbox(msg, choices=self.choices)
        if reply is None:
            sys.exit(0)
        msgreplay1 = "folder docelowy - " + self.in_folder if self.in_folder else "Wybierz folder docelowy"
        msgreplay2 = 'folder do posortowania - ' + self.from_folder if self.from_folder else "Wybierz folder do posortowania"
        print(reply)
        if reply == msgreplay1:
            self.select_folder_in()
            self.choices[0] = 'folder docelowy - ' + przeniesienie.in_folder
        if reply == msgreplay2:
            self.select_folder_from()
            self.choices[1] = 'folder do posortowania - ' + przeniesienie.from_folder
        if reply == "Continue":
            if self.in_folder != None and self.from_folder != None and msgreplay2.split(" ")[-1] != \
                    msgreplay1.split(" ")[-1]:
                self.ready_to_continue = True
            else:
                if self.in_folder == None or self.from_folder == None:
                    msgbox("Nie wybrano Folderów".center(80, " "), "", "Ok")
                if msgreplay2.split(" ")[-1] == msgreplay1.split(" ")[-1]:
                    msgbox("Wybrano te same foldery".center(80, " "), "", "Ok")
        if reply == "Ustawienia Zaawansowane":
            self.advanced_settings()

    def advanced_settings(self):
        reply = buttonbox("Ustawienia zaawansowane".center(80, " "), "", ["Dodaj nowe rozszerzenia do bazy programu", "Wróć do Menu"])
        if reply == "Dodaj nowe rozszerzenia do bazy programu":
            self.add_englarment()
        if reply == "Wróć do Menu":
            self.select_folders()
    def add_englarment(self):
        test = True
        englarment = enterbox("Wprowadź rozszerzenie np.(jpg), (docx)")
        for a in self.enlargement:
            if a == englarment:
                test = False
        if test:
            self.enlargement.append(englarment)
            buttonbox("pomyślnie dodano".center(80, " "), "", ["ok"])
            self.advanced_settings()
        else:
            buttonbox("to rozszerzenie znajduje się już w bazie danych".center(80, " "), "", ["ok"])
            self.advanced_settings()

    def read_config_file(self):
        try:
            with open("config.json", encoding='utf-8') as json_data_file:
                data = json.load(json_data_file)
                self.enlargement = data["Rozszerzenia"]
                return data["file_types"]
        except FileNotFoundError as error:
            return self.create_config_file(JSON_DATA)

    def create_config_file(self, jason):
        with open("config.json", "w", encoding='utf-8') as outfile:
            json.dump(jason, outfile)
        with open("config.json", encoding='utf-8') as json_data_file:
            data = json.load(json_data_file)
            self.enlargement = data["Rozszerzenia"]
        return data["file_types"]

    def save_config_file(self):
        print(self.file_types)
        self.file_types.pop("Niestandardowe")
        self.file_types["Niestandardowe"] = []
        self.file_types.pop("Usuń")
        self.file_types["Usuń"] = []
        jason = {"file_types": self.file_types, "Rozszerzenia" : self.enlargement}
        with open("config.json", "w", encoding='utf-8') as outfile:
            json.dump(jason, outfile)

with Files() as przeniesienie:
    while przeniesienie.ready_to_continue is False:
        przeniesienie.select_folders()
    file_type = przeniesienie.select_files_type()
    przeniesienie.move_files(file_type)
    tekst = ""
    for file_name in przeniesienie.moved_files:
        tekst = tekst + "-" + file_name + "\n"
    msgbox(f"Przeniesiono pliki:\n\n{tekst}".center(80, " "), ok_button="Ok")



#TODO
# bledy:
# 1: zamykanie programu
# 2. dodanie do menu gl "configuracja zaawansowana" z dodatkowymi wyborami. // bardziej zzaawanowana klasa to wiecej pracy
# 3. nowe fuknkcje lub klasa
# 5. zapisaywanie nowej konfiguracji.
# 6. dodanie szybkiego uruchamiania
# 7. ew testy automatyczne # opcjonalnie
# ----------------------------------------------------------------------------------------------------------------------
# 1. główne krainy geograficzne afryki
# 2. Zróżnicowanie klimatu afryki, cechy charakterystyczne klimataów str 55
# 3. passaty
# 4. Przyczyny pustynienia sachelu
# 5. co się uprawia w afryce 68, 69 str
# 6. Podsumowanie 72 str
# 7. Czyniki utrudniające rozwój większości państw afryki