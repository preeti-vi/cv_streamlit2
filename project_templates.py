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
        '<img src="' + project_details["img"] + '" style="width:250px;height:150px;">' +
        f'<div style="color: {tcolor}; font-size: 18px; font-family: \'Book Antiqua\';">' +
        project_details["title"] +
        '</div>' +
        f'<div style="margin-top: 15px; color: {tcolor}; font-size: 14px; font-family: \'Book Antiqua\';">' +
        project_details["desc"] +
        '</div></a></body></html>',
        height=260
    )

def proj_section(st, section_header, proj_details):
    st.header(section_header, divider='gray')

    col1, _, col2, _, col3, _, col4 = st.columns([10, 1, 10, 1, 10, 1, 10])

    with col1:
        if len(proj_details) > 0:
            proj_template(st, proj_details[0])
    with col2:
        if len(proj_details) > 1:
            proj_template(st, proj_details[1])
    with col3:
        if len(proj_details) > 2:
            proj_template(st, proj_details[2])
    with col4:
        if len(proj_details) > 3:
            proj_template(st, proj_details[3])

    st.markdown("**View All**")
    # components.html("<a href='#' target='_blank'> View All </a>")


def addProjectsSection(st):
    proj_details = []
    proj_details.append({"img": "https://i.ibb.co/20rGTd32/ai-assist.png",
                         "title": "AI-powered personal assistant",
                         "desc": "A RAG model using Langchain and Google Gemini, OpenAI Embeddings model",
                         "link": "https://ai-cv-assist.streamlit.app/"
                         })

    proj_details.append({"img": "https://i.ibb.co/nMwB30Jy/library-assist.jpg",
                         "title": "AI-powered library assistant",
                         "desc": "An agent-based app using Langchain which utilizes TavilySearch and other tools",
                         "link": "https://library-assist.streamlit.app/"
                         })

    proj_section(st, "Projects", proj_details)



def addPytorchSection(st):
    proj_details = []
    proj_details.append({"img": "https://i.ibb.co/WkCp6M1/LRSchedulers.png",
                         "title": "Template - LR Schedulers",
                         "desc": "Demonstrates use of various LR Schedulers used in PyTorch",
                         "link": "https://preeti-vi.github.io/pages/PyTorch/LR%20Schedulers.html"
                         })
    proj_details.append({"img": "https://i.ibb.co/vXjj5VY/Optimizers.jpg",
                         "title": "Template - Optimizers",
                         "desc": "Demonstrates use of various optimizers available in PyTorch",
                         "link": "https://preeti-vi.github.io/pages/PyTorch/Optimizers.html"
                         })
    proj_details.append({"img": "https://i.ibb.co/NS9CP0Z/bricks.jpg",
                         "title": "Kaggle Competition - Image Classification",
                         "desc": "Training from scratch (81.16% accuracy)",
                         "link": "https://preeti-vi.github.io/pages/PyTorch/kaggle-classification - training-from-scratch.html"
                         })
    proj_details.append({"img": "https://i.ibb.co/D7435W7/2-3blue1brown.png",
                         "title": "Template - LR Schedulers",
                         "desc": "Demonstrates use of various LR Schedulers used in PyTorch",
                         "link": "https://i.ibb.co/D7435W7/2-3blue1brown.png"
                         })

    proj_section(st, "PyTorch 2.x", proj_details)

