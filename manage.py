import product
import store

def show_prod_array(*args): 
	print ("\n" + ("#" * 20))
	for attr, val in self.__dict__.items():
		print ("{}: {}".format(attr, val))
	print ("#" * 20)
	

product1 = product.Product(1500.00,"BigScreen TV",55,"LG",1200.00,'new')
product2 = product.Product(700.00,"iPhone6S",1,"Apple",400.00,'new')
product3 = product.Product(400.00,"iPhone5",1,"Apple",200.00,'used')
product4 = product.Product(450.00,"XBox",35,"MS",35,'new')
product5 = product.Product(250.00,"wii",15,"EA",50,"like new")
product6 = product.Product(350.00,"PlayStation",22,"Sony",20, "defective")	

product1.displayinfo()
#product2.displayinfo()
#product3.displayinfo()

prods1 = (product1, product2)
		
Store1 = store.Store("Best Buy", "Best Guy")
Store1.add_product(prods1)
Store1.inventory()
Store1.remove_product(prods1)
Store1.inventory()

prods2 = (product4, product5)
Store2 = store.Store("Phil's Electronic Stuff", "Phil Filbert")
Store2.add_product("product4")
Store2.add_product("product5")
Store2.add_product("product6")
Store2.inventory()
Store2.remove_product(product4)
Store2.inventory()


#product1.sell()
#product1.addTax(0.08)
#product1.displayinfo()
#product1.returnItem('opened').displayinfo()
	