import streamlit.components.v1 as components

tcolor = None
def set_themecolor(in_tcolor):
    global tcolor
    tcolor = in_tcolor

def proj_template(st, project_details):
    # st.image(project_details["img"])
    components.html(
        '<html><body>' +
        '<a href="' + project_details["link"] + '" target="_blank", style="text-decoration: none;">' +
        '<img src="' + project_details["img"] + '" style="width:250px;">' +
        f'<div style="color: {tcolor}; font-size: 18px; font-family: \'Book Antiqua\';">' +
        project_details["title"] +
        '</div>' +
        f'<div style="margin-top: 15px; color: {tcolor}; font-size: 14px; font-family: \'Book Antiqua\';">' +
        project_details["desc"] +
        '</div></a></body></html>',
        height=250
    )

def proj_section(st, section_header, proj_details):
    st.header(section_header, divider='gray')

    col1, _, col2, _, col3, _, col4 = st.columns([10, 1, 10, 1, 10, 1, 10])

    with col1:
        proj_template(st, proj_details[0])
    with col2:
        proj_template(st, proj_details[1])
    with col3:
        proj_template(st, proj_details[2])
    with col4:
        proj_template(st, proj_details[3])

    components.html("<a href='https://i.ibb.co/D7435W7/2-3blue1brown.png' target='_blank'> View All </a>")


def addPytorchSection(st):
    proj_details = []
    proj_details.append({"img": "https://i.ibb.co/D7435W7/2-3blue1brown.png",
                         "title": "Template - LR Schedulers",
                         "desc": "Demonstrates use of various LR Schedulers used in PyTorch",
                         "link": "https://i.ibb.co/D7435W7/2-3blue1brown.png"
                         })
    proj_details.append({"img": "https://i.ibb.co/D7435W7/2-3blue1brown.png",
                         "title": "Template - LR Schedulers",
                         "desc": "Demonstrates use of various LR Schedulers used in PyTorch",
                         "link": "https://i.ibb.co/D7435W7/2-3blue1brown.png"
                         })
    proj_details.append({"img": "https://i.ibb.co/D7435W7/2-3blue1brown.png",
                         "title": "Template - LR Schedulers",
                         "desc": "Demonstrates use of various LR Schedulers used in PyTorch",
                         "link": "https://i.ibb.co/D7435W7/2-3blue1brown.png"
                         })
    proj_details.append({"img": "https://i.ibb.co/D7435W7/2-3blue1brown.png",
                         "title": "Template - LR Schedulers",
                         "desc": "Demonstrates use of various LR Schedulers used in PyTorch",
                         "link": "https://i.ibb.co/D7435W7/2-3blue1brown.png"
                         })

    proj_section(st, "PyTorch 2.x", proj_details)

