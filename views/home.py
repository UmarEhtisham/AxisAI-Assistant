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
    cols=st.columns(5,gap="small",vertical_alignment="center")
    # with cols[0]:
    data=[
        {
    'title':'Quiz',
    'src':'https://www.xevensolutions.com/wp-content/uploads/2023/10/AI-chatbot-development.png',
    'description':'Quiz'
        },
        {
    'title':'Quiz',
    'src':'https://www.xevensolutions.com/wp-content/uploads/2023/10/AI-chatbot-development.png',
    'description':'Quiz'
        },
        {
    'title':'Quiz',
    'src':'https://www.xevensolutions.com/wp-content/uploads/2023/10/AI-chatbot-development.png',
    'description':'Quiz'
        },
        {
    'title':'Quiz',
    'src':'https://www.xevensolutions.com/wp-content/uploads/2023/10/AI-chatbot-development.png',
    'description':'Quiz'
        },
        {
    'title':'Quiz',
    'src':'https://www.xevensolutions.com/wp-content/uploads/2023/10/AI-chatbot-development.png',
    'description':'Quiz'
        },
    ]
    
    for i,item in enumerate(data):
        with cols[i]:
            st.markdown(f"""
                        <div class="col-lg-4 col-md-6">
                            <div class="single-feature mb-30">
                                <div class="title d-flex flex-row pb-20">
                                    <figure class="elementor-image-box-img">
                                        <img loading="lazy" decoding="async" width="50" height="50" 
                                                src={item['src']} class="attachment-full size-full wp-image-4603" alt="">
                                    </figure>
                                    <h4>{item['title']}</h4>
                                </div>
                                <p>{item['description']}</p>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

    
    
    
home()