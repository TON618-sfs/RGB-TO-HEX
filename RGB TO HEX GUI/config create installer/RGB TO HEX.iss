[Setup]
; Имя программы в установщике и панели управления
AppName=RGB TO HEX
AppVersion=2.0.1a
WizardStyle=modern dynamic
; Папка установки по умолчанию (C:\Program Files\RGB TO HEX)
DefaultDirName={autopf}\RGB TO HEX
LicenseFile="C:\Users\filem\Desktop\RGB-TO-HEX\LICENSE"
DefaultGroupName=RGB TO HEX
; Иконка для удаления в панели управления
UninstallDisplayIcon={app}\RGB TO HEX.exe
Compression=lzma2
SolidCompression=yes
; Куда сохранить готовый файл установки (на Рабочий стол)
OutputDir={userdesktop}
OutputBaseFilename=RGB TO HEX Setup

[Files]
; ЗАМЕНИТЕ "C:\Path\To\Your\..." на реальный путь к вашему .exe на диске
Source: "C:\Users\filem\Desktop\RGB-TO-HEX\dist\RGB TO HEX.exe"; DestDir: "{app}"; Flags: ignoreversion
; Если есть доп. файлы (библиотеки, конфиги), добавьте их сюда:
; Source: "C:\Path\To\Your\settings.ini"; DestDir: "{app}"

[Icons]
; Ярлык в меню «Пуск»
Name: "{group}\RGB TO HEX"; Filename: "{app}\RGB TO HEX.exe"
; Ярлык на рабочем столе (опционально)
Name: "{autodesktop}\RGB TO HEX"; Filename: "{app}\RGB TO HEX.exe"


; --- УДАЛЕНИЕ ВСЕХ ДАННЫХ ПРИ ДЕИНСТАЛЛЯЦИИ ---
[UninstallDelete]
; Удаляет конкретные файлы, созданные программой (например, настройки)
Type: files; Name: "{app}\settings.ini"
Type: files; Name: "{app}\logs.txt"
; Полностью удаляет папку программы, если в ней остались лишние файлы
Type: filesandordirs; Name: "{app}"
