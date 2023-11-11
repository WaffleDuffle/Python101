class Stock:
    def __init__(self, list_stock):
        self.list_stock = []
        for product in list_stock:
            self.list_stock.append(product)

    def add(self, new_product):
        """
        TODO 1:
            * adauga un produs nou in stoc
        
        Args:
            * new_product (Product):    noul produs de adaugat in stoc

        """
        self.list_stock.append(new_product)
    
    def remove(self, product_name):
        """
        TODO 2:
            * sterge din stocul magazinului produsul dat ca parametru
        
        Args:
            * product_name (str):    numele produsului urmeaza a fi sters

        """
        for product in self.list_stock:
            if product_name == product.name:
                self.list_stock.remove(product)
                break
    def view(self):
        """
        TODO 3:
            * returneaza stocul curent

        Returns:
            * [Product]:    lista de produse din stoc
            
        """
        return self.list_stock