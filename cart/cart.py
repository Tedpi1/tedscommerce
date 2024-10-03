class Cart:
    def __init__(self, request):
        self.session = request.session
        
        # get the current session data or initialize a new one
        cart=self.session.get('session_key')
        
        # create new session if it doesn't exist
        if 'session_key' not in request.session:
            cart=self. session['session_key']={}
            
        # make sure that its availabel to all page in a websie
        self.cart = cart
    
    def add(self, product):
        product_id=str(product.id)

        # if product already exist in cart  
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]={
                'price':str(product.price),
            }
        self.session.modified=True   