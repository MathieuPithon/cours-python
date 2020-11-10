"""
module docstring
"""


class Supplier:
    """
    module docstring
    """
    def __init__(self, nom, localisation_usine, nationalité):
        self.nom = nom
        self.localisation_usine = localisation_usine
        self.nationalité = nationalité
        self.historique_achat = []

    def historique_achat_fournisseur(self, achat):
        """
        module docstring
        """
        self.historique_achat.append(achat)

    def funcname(self, parameter_list):
        """
        docstring
        """
