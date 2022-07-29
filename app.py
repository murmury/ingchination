# from web.streamlit_pages import some_page # import your pages here
from web.streamlit_pages.multipage import MultiPage

# Create an instance of the app 
app = MultiPage()

# Add all your application here
# app.add_page("샘플 페이지", some_page.app)

# The main app
app.run()