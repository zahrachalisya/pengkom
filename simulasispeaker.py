# Judul: program simulasi speaker
# deskripsi program mensimulasikan bluetooth speaker yang bisa terhubung dengan 3 device sekaligus, speaker memprioritaskan input wire lalu prioritas sesuai koneksi pertama bluetooth.

# KAMUS
# i = int
# vol = int array
# prioritas = int
# cara_koneksi = str
# device nyala wired = bool
# song = int
# playlist = str array
# nama_lagu str
# nama_device = str
# Tambah_lagu = str (yes/no jadi bisa diganti bool)

# Sub program menampilkan data
# Data
def data(): 
    print(f"volume : {vol[prioritas]}")
    print(f"wired: {wired}")
    for i in range(3):
        print(f"channel ke-{i} {device[i]}")

# Sub program menampilkan kalau lagu/suara main
# Sound
def play_sound():
    if wired == False:
        print(f"playing {playlist[song]} from ke-{prioritas} at {vol[prioritas]}")
    else:
        print(f"playing {playlist[song]} from wired at {vol[prioritas]}")

#Algoritma

#definisi variable dan inisiasi array
prioritas = -1
vol = [0 for i in range(4)]
wired = False
device = [False for i in range(3)]
nyala = [False for i in range(4)]
song = 0
playlist =["auto_generated song"]

#pilih aksi yang dilakukan (simulasi orang yang berinteraksi dengan device atau speaker)
do = input("Mau Ngapain? (play, pause, next, back, vol_up, vol_down , connection, default, playlist, reset, data, off): ")
while do != "off":

    if do == "play": #aksi 1 membuat device memberi signal ke speaker
        data()
        if wired == True:
            play_sound()
        else:
            i = int(input("input suara dari device mana: "))
            if device[i] == True: 
                if prioritas == -1:
                    prioritas = i
                play_sound()
                nyala[i] = True
            else:
                print("no device connected in that channel, go to connection to connect device")
       
    elif do == "pause": #aksi 2 menghentikan input dari device
        for i in range(3):
            if nyala[i] == True and wired== False: #list semua channel yang sedang memberi input
                print(f"koneksi yang memberi input adalah koneksi: {i}")
        i = int(input("mau pause device mana"))
        nyala[i] = False
        print(f"input dari koneksi {i} berhenti")
        if nyala[0] == True: #speaker haya dapat meerima satu input walau terhubung ke bergaai device. saat mati device selajutya mejadi yag iput(signalnya diterima)
            prioritas = 0
            print(f"diterima input dari koneksi {prioritas}")
        elif nyala[1] == True: 
            prioritas = 1
            print(f"diterima input dari koneksi {prioritas}")
        elif nyala[1] == True: 
            prioritas = 2
            print(f"diterima input dari koneksi {prioritas}")
        else:
            prioritas = -1
            print("no device playing")

    elif do == "next": #aksi 3 meambah indeks untuk playlist
        song += 1
        if len(playlist)<song:
            song = 0
        play_sound()

    elif do == "back": #aksi 4 menguragi indeks utuk playlist
        song += -1
        if song<0:
            song = 0
        play_sound()    

    elif do == "vol_up": #aksi 5 peningkatan volume dengan 10 sebagai terbesar. volume disimpan dalam device buka speaker jadi hanya dapat diubah jika terhubug
        if vol[prioritas] < 10 and prioritas != -1: 
            vol[prioritas] += 1
            print(f"volume speaker: {vol[prioritas]}")
        else: # prioritas == -1
            print("no device connected")
        
    elif do == "vol_down": #aksi 6 penguragan volume degan 0 sebagai terkecil
        if vol[prioritas] > 0 and prioritas != -1:
            vol[prioritas] += -1
            print(f"volume speaker: {vol[prioritas]}")
        elif prioritas != -1:
            print("no device connected")
        else:
            (f"volume speaker: {vol[prioritas]}")
        
    elif do == "connection": #aksi 7 Speaker dapat konek lewat cabel atau bluetooth serta bisa putus
        print(f"current connection {wired} and device bluetooth: ")
        for i in range(3):
            print(f"channel ke-{i} {device[i]}") 
        cara_koneksi = input("mau terhubung dengan cabel/bluetooth atau mau disconnect_cabel/disconnect_bluetooth: ") # input mau connect atau disconnect 
        if cara_koneksi == "cabel": # jika terhubung cabel
            wired = True
            prioritas = 3
            print("cabel terhubung")
        elif cara_koneksi == "bluetooth": # jika ingin terhubung bluetooth (melihat jika ada device yang dikenal denna asumsi bahwa speaker mennyimpan data volumenya)
            i = int(input("mau terhubung channel koneksi berapa: "))
            nama_device= input("nama device (yang pernah terhubung sebelumnya: hp-an, au3player, :)")
            if nama_device == "hp-an":
                vol[i] = 4
            elif"au3player":
                vol[i] = 9
            elif nama_device == ":)":
                vol[i] = 3
            device[i] = True
            print(f"terhubung koneksi {i}")
        elif cara_koneksi =="disconnect_cabel": # jika ingin putus dari cabel (playlist dan volume itu disimpan bukan dalam speaker sendiri tetapi dari hp atau device yang terhubung. speaker dapat menghakses data tersebut hanya saat terkonseksi)
            wired = False
            playlist =["auto_generated song"]
            print("cabel terputus")
        elif cara_koneksi == "disconnect_bluetooth": # jika ingin putus koneksi bluetooth (playlist dan volume itu disimpan bukan dalam speaker sendiri tetapi dari hp atau device yang terhubung. speaker dapat menghakses data tersebut hanya saat terkonseksi)
            i = int(input("mau disconnect channel koneksi berapa: "))
            device[i] = False
            playlist =["auto_generated song"]
            print(f"terputus koneksi {i}")

    elif do == "playlist": #aksi 8 device dapat menerima input playlist lagu, posisi indeks 0 dianggap lagu/suara standarnya
        tambah = "yes"
        while tambah != "no": #looping untuk memasukan lagu dalam playlist
            nama_lagu = input("masukkan nama lagu yang di queue " )
            playlist.append(nama_lagu)
            tambah = input("masih mau tambah lagu? (ya/no) " )

    elif do ==  "default": #aksi 9 asumsi speaker pernah terhubung ke device (menyimpan channel koneksi dan volume)
        wired = False
        device[1] = True
        vol[1] = 5
        data()
       
    elif do == "reset": #aksi 10 menghilangkan semua koneksi dan volume dari 
        device = [False for i in range(3)]
        vol = [0 for i in range (4)]
        playlist =["auto_generated song"] 
        data()
        
    elif do == "data": #aksi 11 memanggil prosedur data
        data()
    else:  
        print("no matching order")
    do = input("Mau Ngapain? (play, pause, next, back, vol_up, vol_down , connection, default, playlist, reset, data, off): ")

print("speaker mati") #aksi 12
