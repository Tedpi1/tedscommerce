from  .cart import Cart

# create context precessor inorder our cart can work with all templates
def cart(request):
    return {'cart': Cart(request)}