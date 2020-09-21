print('MENU: \n1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen')

try:
    choice = int(input())
    if not 1 <= choice < 5:
        print('Geen valide optie.')
except:
    print('Geen valide optie.')

def aantal_kluizen_vrij():
    return len(vrije_kluizen())

def kluis_openen():
    kluisopenen = 'kluis' + input('Kluisnummer: ') + ' ' + input('Kluiscode: ')
    for kluis in lees_kluizen():
            if kluis == kluisopenen:
                print('Combinatie klopt!')
                exit()
    print('Combinatie klopt niet.')

def vrije_kluizen():
    kluisnummers = ['kluis1', 'kluis2', 'kluis3', 'kluis4', 'kluis5', 'kluis6', 'kluis7', 'kluis8', 'kluis9', 'kluis10', 'kluis11', 'kluis12']

    for kluis_en_code in lees_kluizen():
        try:
            kluisnummers.remove(kluis_en_code.split(" ")[0])
        except ValueError:
            continue
    return kluisnummers

def nieuwe_kluis():
    kluisnummers = vrije_kluizen()
    if kluisnummers:
        print('Er is een kluis beschikbaar!')
        code = input('Voer vier cijfer code in: ')
        print('Je hebt ' + str(kluisnummers[0]) + ' gekregen!')
        kluizen = open('fa_kluizen.txt', 'a')
        kluizen.write( kluisnummers[0] + ' ' + code + '\n')
        kluizen.close()
    else:
        print('Er is geen kluis beschikbaar.')

def lees_kluizen():
    kluizen = open('fa_kluizen.txt', 'r')
    kluisrijen = kluizen.read().splitlines()
    kluizen.close()
    return kluisrijen


if choice == 1:
    print('Er zijn nog ' + str(aantal_kluizen_vrij()) + ' kluizen beschikbaar.')
elif choice == 2:
    nieuwe_kluis()
elif choice == 3:
    kluis_openen()
elif choice == 4:
    kluis_teruggeven()
