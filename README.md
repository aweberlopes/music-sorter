# Music Sorter
A Small script to sort a folder of music
**Working only under Windows**

## Usage example
```bash
python3.exe .\main.py <Folder to sort>
python3.exe .\main.py C:\Users\weber\music
```


## Example 
```bash
# Folder Before
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       25.04.2020     11:32              0 Breaking Benjamin - Cold.mp3
-a----       25.04.2020     11:32              0 Breaking Benjamin - Far Away.mp3
-a----       25.04.2020     11:35              0 Galantis - No Money.mp3
-a----       25.04.2020     12:01              0 Linkin Park - Numb.mp3

#Folder After
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       27.04.2020     20:06                Breaking Benjamin
d-----       27.04.2020     20:06                Galantis
d-----       27.04.2020     20:06                Linkin Park

#Log output
PS python3 .\main.py C:\Users\weber\Documents\music\
27-Apr-20 20:08:15 - Start Musik-sorter on PATH: C:\Users\weber\Documents\music\
27-Apr-20 20:08:15 - Check for avaiable folder and files
27-Apr-20 20:08:15 - Start the sorting mechanism
27-Apr-20 20:08:15 - Folder: Breaking Benjamin not found. Create new folder
27-Apr-20 20:08:15 - Move File: Breaking Benjamin - Cold.mp3 to Breaking Benjamin
27-Apr-20 20:08:15 - Move File: Breaking Benjamin - Far Away.mp3 to Breaking Benjamin
27-Apr-20 20:08:15 - Folder: Galantis not found. Create new folder
27-Apr-20 20:08:15 - Move File: Galantis - No Money.mp3 to Galantis
27-Apr-20 20:08:15 - Folder: Linkin Park not found. Create new folder
27-Apr-20 20:08:15 - Move File: Linkin Park - Numb.mp3 to Linkin Park
27-Apr-20 20:08:15 - Music Sorter done
