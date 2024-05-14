import streamlit.components.v1 as components
from streamlit_theme import st_theme

tcolor = "rgb(81, 0, 12)"

def app_init(st):
    st.set_page_config(layout="wide",
                       initial_sidebar_state="collapsed")

    theme = st_theme()  # either 'light' or 'dark'
    global tcolor
    if (theme):
        tcolor = "rgb(81, 0, 12)" if theme["base"] == "light" else "rgb(255, 255, 255)"

    return tcolor

def getTopSection(st):
    col_start, col1, col2, col3, col4, col_end = st.columns([3, 1, 1, 1, 1, 3])

    with col1:
        st.page_link("my_portfolio.py", label="Home")
    with col2:
        st.page_link("pages/page_1.py", label="Blog")
    with col3:
        st.page_link("pages/page_2.py", label="Projects")
    with col4:
        st.page_link("http://www.google.com", label="Google")

    st.divider()

    ###########################################

    components.html(
        """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    * {box-sizing: border-box;}
    body {font-family: Verdana, sans-serif;}
    .mySlides {display: none;}
    img {vertical-align: middle;}

    /* Slideshow container */
    .slideshow-container {
      max-width: 600px;
      position: relative;
      margin: auto;
    }

    .blacktext {
      color: rgb(81, 0, 12);
      font-size: 19px;
      font-family: "Comic Sans MS", cursive;
      padding: 1px 1px;
      position: absolute;
      bottom: 8px;
      width: 100%;
      text-align: center;
    }

    /* Caption text white */
    .whitetext {
      color: white - #f2f2f2;
      font-size: 15px;
      padding: 8px 12px;
      position: absolute;
      bottom: 8px;
      width: 100%;
      text-align: center;
    }


    /* Number text (1/3 etc) */
    .numbertext {
      color: #f2f2f2;
      font-size: 12px;
      padding: 8px 12px;
      position: absolute;
      top: 0;
    }

    /* The dots/bullets/indicators */
    .dot {
      height: 15px;
      width: 15px;
      margin: 0 2px;
      background-color: #bbb;
      border-radius: 50%;
      display: inline-block;
      transition: background-color 0.6s ease;
    }

    .active {
      background-color: #717171;
    }

    /* Fading animation */
    .fade {
      animation-name: fade;
      animation-duration: 1.5s;
    }

    @keyframes fade {
      from {opacity: .4} 
      to {opacity: 1}
    }

    /* On smaller screens, decrease text size */
    @media only screen and (max-width: 300px) {
      .text {font-size: 11px}
    }
    </style>
    </head>
    <body>
        <script>
            const sidebar = document.getElementsByClassName("sidebar-container")[0];
            sidebar.style.display = "none";
        </script>

        <div style="color: """ + tcolor + """; font-size: 30px; font-family: 'Book Antiqua'; text-align: center; padding-bottom: 20px;">
            Journey to Computer Vision
        </div>

    <div class="slideshow-container">

    <div class="mySlides fade">
      <div class="numbertext">1 / 6</div>
      <a href="https://i.ibb.co/Gcp7H1Z/1-Maths-Is-Fun.png" target="_blank">
        <img src="https://i.ibb.co/Gcp7H1Z/1-Maths-Is-Fun.png" style="width:100%">
      </a>
      <div class="blacktext">Is maths really a fun... umm... </div>
    </div>

    <div class="mySlides fade">
      <div class="numbertext">2 / 6</div>
      <a href="https://i.ibb.co/D7435W7/2-3blue1brown.png" target="_blank">
        <img src="https://i.ibb.co/D7435W7/2-3blue1brown.png" style="width:100%; border: 1px solid rgb(200,200,200);">
      </a>  
      <div class="blacktext">Eigenvalues... eigenvectors... </div>
    </div>

    <div class="mySlides fade">
      <div class="numbertext">3 / 6</div>
      <a href="https://i.ibb.co/7yjp7Cc/3-Probability-and-statistics.png" target="_blank">
        <img src="https://i.ibb.co/7yjp7Cc/3-Probability-and-statistics.png" style="width:100%">
      </a>  
      <div class="blacktext">?????</div>
    </div>

    <div class="mySlides fade">
      <div class="numbertext">4 / 6</div>
      <a href="https://i.ibb.co/0j2mc7K/4-NPTEL.png" target="_blank">
        <img src="https://i.ibb.co/0j2mc7K/4-NPTEL.png" style="width:100%; border: 1px solid rgb(200,200,200);">
      </a>
      <div class="blacktext">Yuhoo... I did it !!</div>
    </div>

    <div class="mySlides fade">
      <div class="numbertext">5 / 6</div>
      <a href="https://i.ibb.co/qNLPZRW/5-Great-Learning.png" target="_blank">
        <img src="https://i.ibb.co/qNLPZRW/5-Great-Learning.png" style="width:100%; border: 1px solid rgb(200,200,200);">
      </a>  
      <div class="blacktext">Keep learning... </div>
    </div>

    <div class="mySlides fade">
      <div class="numbertext">6 / 6</div>
      <a href="https://i.ibb.co/sHfXSCb/6-Open-CV.png" target="_blank">
        <img src="https://i.ibb.co/sHfXSCb/6-Open-CV.png" style="width:100%">
      </a>
      <div class="blacktext">I am loving it... </div>
    </div>

    </div>
    <br>

    <div style="text-align:center">
      <span class="dot"></span> 
      <span class="dot"></span> 
      <span class="dot"></span>
      <span class="dot"></span> 
      <span class="dot"></span> 
      <span class="dot"></span> 
    </div>

    <script>
    let slideIndex = 0;
    showSlides();

    function showSlides() {
      let i;
      let slides = document.getElementsByClassName("mySlides");
      let dots = document.getElementsByClassName("dot");
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
      }
      slideIndex++;
      if (slideIndex > slides.length) {slideIndex = 1}    
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";  
      dots[slideIndex-1].className += " active";
      setTimeout(showSlides, 2400); // Change image every 2 seconds
    }
    </script>

    </body>
    </html> 

        """,
        height=600,
    )