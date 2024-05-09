import streamlit as st
import base64

st.set_page_config(layout="wide")

#########################################################
file_ = open("Images/1. MathsIsFun.png", "rb")
contents = file_.read()
data_url_1 = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("Images/2. 3blue1brown.png", "rb")
contents = file_.read()
data_url_2 = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("Images/3. Probability and statistics .png", "rb")
contents = file_.read()
data_url_3 = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("Images/4. NPTEL.png", "rb")
contents = file_.read()
data_url_4 = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("Images/5. Great Learning.png", "rb")
contents = file_.read()
data_url_5 = base64.b64encode(contents).decode("utf-8")
file_.close()

file_ = open("Images/6. OpenCV.png", "rb")
contents = file_.read()
data_url_6 = base64.b64encode(contents).decode("utf-8")
file_.close()

#
# #######################################################
#
col_start, col1, col2, col3, col4, col_end = st.columns([3,1,1,1,1,3])

with col1:
   st.page_link("my_portfolio_3.py", label="Home")
with col2:
   st.page_link("pages/page_1.py", label="Blog")
with col3:
   st.page_link("pages/page_2.py", label="Projects")
with col4:
   st.page_link("http://www.google.com", label="Google")

st.divider()

# Add a script to the HTML header to close the sidebar by default
st.markdown(
    """
    <script>
        const sidebar = document.getElementsByClassName("sidebar-container")[0];
        sidebar.style.display = "none";
    </script>
    """,
    unsafe_allow_html=True
)
###########################################

import streamlit.components.v1 as components

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

<h2 style="text-align: center; color: rgb(81, 0, 12)">Journey to Computer Vision</h2>

<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="data:image/png;base64,""" + data_url_1 + """ " style="width:100%">
  <div class="blacktext">Is maths really a fun... umm... </div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 6</div>
  <img src="data:image/png;base64,""" + data_url_2 + """ " style="width:100%; border: 1px solid rgb(200,200,200);">
  <div class="blacktext">Amazing...</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 6</div>
  <img src="data:image/png;base64,""" + data_url_3 + """ " style="width:100%">
  <div class="blacktext">?????</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">4 / 6</div>
  <img src="data:image/png;base64,""" + data_url_4 + """ " style="width:100%; border: 1px solid rgb(200,200,200);">
  <div class="blacktext">Yuhoo... I did it !!</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">5 / 6</div>
  <img src="data:image/png;base64,""" + data_url_5 + """ " style="width:100%; border: 1px solid rgb(200,200,200);">
  <div class="blacktext">Keep learning... </div>
</div>

<div class="mySlides fade">
  <div class="numbertext">6 / 6</div>
  <img src="data:image/png;base64,""" + data_url_6 + """ " style="width:100%">
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


####################################################

st.header('PyTorch 2.x')
st.divider()