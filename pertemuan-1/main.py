#print = output data ke terminal
print("Hello, World!")
print("=" * 20)
#tipe data python
name = "made suryana"  #string (teks)
age = 20               #integer (bilangan bulat)
married = False      #boolean (True/False)
print(f"Name: {name}, umur: {age} tahun")
namabali = ["wayan", "made", "kadek", "putu"]  #list (daftar)
print(namabali)
# fungsi di awali dengan def
# def nama_fungsi(parameter):
def halo(name, city):
    print(f"Halo, nama saya {name}, saya dari {city}")
    print("-" * 20)
# pemanggilan nama fungsi diluar blok fungsi/def
halo("wayan koster", "singaraja")
halo("nyoman sureca", "denpasar")