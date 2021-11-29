nilai = [{'nim' : 'A01', 'nama' : 'AGUSTINA', 'mid' : 50, 'uas' : 80}, 
         {'nim' : 'A02', 'nama' : 'BUDI',     'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'CHICHA',   'mid' : 100,'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'DONNA',    'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'FATIMAH',  'mid' : 70, 'uas' : 100}]
print("=" * 40)
print("NIM".ljust(10), "NAMA".ljust(10), "N.MID".ljust(10), "N.UAS".ljust(10))
print("_" * 40)

for data in nilai :
    print (data["nim"].ljust(10),data["nama"].ljust(10),str(data["mid"]).ljust(10),str(data["uas"]).ljust(10))
print("_" * 40)
