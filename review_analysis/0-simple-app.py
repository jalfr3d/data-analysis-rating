import justpy as jp

def app():
    wp = jp.QuasarPage()
    # Quasar typography for more styles
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    
    return wp

jp.justpy(app)