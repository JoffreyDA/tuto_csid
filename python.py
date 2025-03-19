"""
Module principal avec plusieurs fonctionnalités pour gérer des véhicules.
"""

class Vehicule:
    """Classe de base représentant un véhicule."""
    def __init__(self, marque: str, modele: str, vitesse: int = 0) -> None:
        self.marque = marque
        self.modele = modele
        self.vitesse = vitesse
    
    def description(self):
        """Affiche les informations du véhicule."""
        return f"{self.marque} {self.modele}, vitesse : {self.vitesse} km/h"

    def accelerer(self, vitesse: int):
        """Accélère le véhicule."""
        self.vitesse += vitesse
        return f"{self.marque} {self.modele} accélère de {vitesse} km/h, vitesse actuelle : {self.vitesse} km/h"


class Voiture(Vehicule):
    """Classe de base pour les voitures."""
    pass


class VoitureThermique(Voiture):
    """Classe représentant une voiture thermique."""
    def __init__(self, marque: str, modele: str, vitesse: int = 0) -> None:
        super().__init__(marque, modele, vitesse)
        self.type_energie = "thermique"


class VoitureElectrique(Voiture):
    """Classe représentant une voiture électrique."""
    def __init__(self, marque: str, modele: str, vitesse: int = 0) -> None:
        super().__init__(marque, modele, vitesse)
        self.type_energie = "electrique"


class Scooter(Vehicule):
    """Classe de base pour les scooters."""
    pass


class ScooterThermique(Scooter):
    """Classe représentant un scooter thermique."""
    def __init__(self, marque: str, modele: str, vitesse: int = 0) -> None:
        super().__init__(marque, modele, vitesse)
        self.type_energie = "thermique"


class ScooterElectrique(Scooter):
    """Classe représentant un scooter électrique."""
    def __init__(self, marque: str, modele: str, vitesse: int = 0) -> None:
        super().__init__(marque, modele, vitesse)
        self.type_energie = "electrique"


if __name__ == "__main__":
    voiture_thermique = VoitureThermique("Peugeot", "208")
    voiture_electrique = VoitureElectrique("Tesla", "Model 3")
    scooter_thermique = ScooterThermique("Yamaha", "XMAX")
    scooter_electrique = ScooterElectrique("NIU", "NQi")

    print(voiture_thermique.description())
    print(voiture_electrique.description())
    print(scooter_thermique.description())
    print(scooter_electrique.description())
    
    voiture_thermique.accelerer(20)
    print(voiture_thermique.description())
