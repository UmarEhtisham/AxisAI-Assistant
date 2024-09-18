import streamlit as st

def home():
    st.markdown("""
                <div class="container">
                    <h1 class="elementor-heading-title elementor-size-default">
                        Welcome to Axis AI
                    </h1>
                    <h2 class="elementor-heading-title elementor-size-default">
                        Axis AI the Feature Rich AI Assistance,here to assist you with...
                    </h2>
                </div>
                """,unsafe_allow_html=True)
    cols=st.columns(4,gap='small',vertical_alignment="top")
    # with cols[0]:
    data=[
        {
    'title':'Chat With PDFs',
    'src':"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="50" height="50" style="margin-right: 10px; float: left;">
                                            <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                                            <path d="M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z"/>
                                        </svg>""",
    'description':'Quiz'
        },
        {
    'title':'Quiz',
    'src':"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="50" height="50" style="margin-right: 10px; float: left;">
                                            <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                                            <path d="M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z"/>
                                        </svg>""",
    'description':'Quiz'
        },
        {
    'title':'Quiz',
    'src':"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="50" height="50" style="margin-right: 10px; float: left;">
                                            <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                                            <path d="M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z"/>
                                        </svg>""",
    'description':'Quiz'
        },
        {
    'title':'Quiz',
    'src':"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="50" height="50" style="margin-right: 10px; float: left;">
                                            <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                                            <path d="M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z"/>
                                        </svg>""",
    'description':'Quiz'
        },
        {
    'title':'Quiz',
    'src':"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="50" height="50" style="margin-right: 10px; float: left;">
                                            <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                                            <path d="M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z"/>
                                        </svg>""",
    'description':'Quiz'
        },
    ]

    
    for i,item in enumerate(data):
        
        with cols[i%4]:
            st.markdown(f"""
                        
                        <div class="row">
                        <div class="col-lg-4 col-md-6">
                            <div class="single-feature mb-30">
                                <div class="title d-flex flex-row pb-20">
                                    <figure class="elementor-image-box-img">
                                        {item['src']}
                                    </figure>
                                    <h4>{item['title']}</h4>
                                </div>
                                <p>{item['description']}</p>
                                </div>
                            </div>
                        </div>
                        </div>
                        
                    """, unsafe_allow_html=True)

    
    
    
home()