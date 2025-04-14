class Patient:
    def __init__(self, nom, age, urgent):
        self.nom=nom
        self.age=age
        self.urgent=urgent

    def __str__(self):
        return f"Nom: {self.nom}, âge: {self.age}, caractère d'urgence: {self.urgent}"


class Medecin:
    def __init__(self, nom):
        self.nom = nom
    
    def peut_vacciner(self):
        return True
    
    def vaccine(self, patient: Patient):
        return f"Le médecin vaccine le patient {patient.nom}"
    
class MedecinGeneraliste(Medecin):
    def __init__(self, nom):
        super().__init__(nom)

    def peut_vacciner(self, patient: Patient):
        return patient.age > 12
        
    def vaccine(self, patient: Patient):
        if MedecinGeneraliste.peut_vacciner(self, patient) == True:
            return f"Le médecin {self.nom} vaccine le patient {patient.nom}"

class MedecinPediatre(Medecin):
    def __init__(self, nom):
        super().__init__(nom)

    def peut_vacciner(self, patient: Patient):
        return patient.age < 12
        
    def vaccine(self, patient: Patient):
        if MedecinPediatre.peut_vacciner(self, patient) == True:
            return f"Le médecin {self.nom} vaccine le patient {patient.nom}"
        
class Urgentiste(Medecin):
    def __init__(self, nom):
        super().__init__(nom)

    def peut_vacciner(self, patient: Patient):
        return patient.urgent == True
        
    def vaccine(self, patient: Patient):
        if Urgentiste.peut_vacciner(self, patient) == True:
            return f"Le médecin {self.nom} vaccine le patient {patient.nom}"
        

class CentreVaccination:

    file_patient = []
    liste_medecin = []

    def __init__(self, file_patient, liste_medecin):
        self.file_patient = file_patient
        self.liste_medecin = liste_medecin

    def ajouter_patient(self, patient: Patient):
        self.file_patient.append(patient)

    def ajouter_medecin(self, medecin: Medecin):
        self.liste_medecin.append(medecin)

    def traiter(self):
        patient_traite = []
        for patient in self.file_patient:
            for medecin in self.liste_medecin:
                if medecin.peut_vacciner(patient):
                    print(medecin.vaccine(patient))
                    patient_traite.append(patient)
                    break
            else:
                print("Aucun médecin de disponible")

        for patient in patient_traite:
            self.file_patient.remove(patient)

    def taille_file(self):
        return f"Il y a {len(self.file_patient)} patient(s) dans la file"

    def afficher_file(self):
        print("La file d'attente est la suivante :")
        for patient in self.file_patient:
            print(str(patient))


centreVaccination = CentreVaccination([], [])

centreVaccination.ajouter_medecin(MedecinGeneraliste("Dr Martin (généraliste)"))
centreVaccination.ajouter_medecin(MedecinPediatre("Dr Petit (pédiatre)"))
centreVaccination.ajouter_medecin(Urgentiste("Dr Secours (urgentiste)"))

centreVaccination.ajouter_patient(Patient("Eliot", 16, False))
centreVaccination.ajouter_patient(Patient("Léa", 6, True))
centreVaccination.ajouter_patient(Patient("Corentin", 11, False))
centreVaccination.ajouter_patient(Patient("Eude", 85, False))
centreVaccination.ajouter_patient(Patient("Michel", 65, True))



print(centreVaccination.taille_file())
centreVaccination.afficher_file()

centreVaccination.traiter()

centreVaccination.afficher_file()


