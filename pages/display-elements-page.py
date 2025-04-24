import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
from streamlit_extras.pdf_viewer import pdf_viewer

# Setting up the page configuration.
st.set_page_config(
     page_icon=":material/notes:",
     page_title="Steve's Notes",
     layout="wide",
)

# Remove the anchor icons.
st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

# Remove the watermarks.
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Component: Create tab elements.
text_elements_tab, array_elements_tab, chart_elements_tab, media_elements_tab, special_elements_tab = st.tabs(["Text Display Elements", "Array Display Elements", "Chart Display Elements", "Media Display Elements", "Special Display Elements"])

# Component: Populate tab element.
with text_elements_tab:
     
     # Component: Create column elements.
     col_1, col_2 = st.columns(2)
     
     # Component: Populate column element.
     with col_1:
          
          # Component: Create and populate container element.
          with st.container(border=True):
               
               # Component: Create a title element.
               st.title("The Math Module")

               # Component: Create a header element.
               st.header("Chapter I: Integrals")

               # Component: Create a subheader element.
               st.subheader("Type 1: Definite Integrals.")

               # Component: Create plain text element.
               st.text("Let's explore the definit integral.")

               # Component: Create a latex text element.
               st.latex(r"\int_{a}^{b} f(x) \, dx")

               # Component: Create a markdown text element.
               st.markdown("""
               This LaTeX code represents a definite integral. Let's break down the components:

               * `\int`: This is the integral symbol, representing the operation of integration.
               * `_{a}`: This indicates the lower limit of integration, denoted by the variable 'a'. This is the starting point on the x-axis for the integration.
               * `^{b}`: This indicates the upper limit of integration, denoted by the variable 'b'. This is the ending point on the x-axis for the integration.
               * `f(x)`: This is the integrand, the function of 'x' that we are integrating.
               * `\, dx`: This indicates that the integration is being performed with respect to the variable 'x'. The 'dx' signifies an infinitesimally small change in 'x'.

               **In plain English, this integral represents the signed area between the curve of the function f(x) and the x-axis, from x = a to x = b.**

               If the function f(x) is above the x-axis in the interval [a, b], the integral will yield a positive value representing the area. If the function is below the x-axis, the integral will yield a negative value. If the function crosses the x-axis within the interval, the integral will represent the net signed area.
               """)
     # Component: Populate column element.
     with col_2:
          
          # Component: Create and populate container element.
          with st.container(border=True):
          
          # Component: Create a Code text element.
               st.text("This is how we can generate visualization using Matplotlib.")
               st.code("""
                    import numpy as np
               import pandas as pd
               import matplotlib.pyplot as plt

               # Generate the mathematical data.
               x = np.linspace(3, 15, 30)
               y = np.log(x)

               # Fixed random data generation - shape parameter was incorrectly specified
               data = np.random.randint(low=0, high=100, size=1000)

               # Generate the statistical data.
               df = pd.read_csv("f1_drivers.csv")
               desired_data = df.loc[df["Championships"] >= 2]
               drivers = desired_data["Driver"]
               championships = desired_data["Championships"]

               # Create figures.
               fig_1 = plt.figure(figsize=(8, 3), dpi=300, facecolor="#E5E4E2")
               fig_2 = plt.figure(figsize=(8, 3), dpi=300, facecolor="black")

               # Create axes.
               ax1 = fig_1.add_axes([0.1, 0.1, 0.35, 0.9])
               ax2 = fig_1.add_axes([0.5, 0.1, 0.35, 0.9])
               ax3 = fig_2.add_axes([0.1, 0.1, 0.9, 0.9])

               # Specify the background color.
               ax1.set_facecolor("#E5E4E2")
               ax2.set_facecolor("#E5E4E2")
               ax3.set_facecolor("black")

               # Add the visualizations to the axes.
               ax1.plot(x, y, label='y = log(x)', color='red', linewidth=2, linestyle='-')
               ax2.boxplot(data, labels=["Data"], notch=True)
               ax3.barh(y=drivers.values, width=championships.values, color='purple')

               # Specify axis titles.
               ax1.set_title("y = log(x)")
               ax2.set_title("Data Distribution")
               ax3.set_title("F1 World Champions", color="white")

               # Specify dimension names.
               ax1.set_xlabel("x")
               ax1.set_ylabel("y")
               ax3.set_xlabel("Championships", color="white")
               ax3.set_ylabel("Drivers", color="white")

               # Specify ticks.
               ax3.tick_params(axis='both', colors='white')

               # Specify the grid.
               ax1.grid(True)
               ax2.grid(True)

               # Specify the legends - only add where needed
               ax1.legend()

               # Save the figures.
               fig_1.savefig("data.png", bbox_inches='tight', transparent=True)
               fig_2.savefig("f1_champiopns.png", bbox_inches='tight', transparent=True)

               # Generate the visualizations.
               plt.show()
                    """, language="python", line_numbers=True)

     # Component: Create PDF element.
     pdf_viewer(r"C:\Users\stivi\Downloads\By-law No 2.pdf")

# Component: Populate tab element.
with array_elements_tab:
     
     # Component: Create dynamic array component.
     st.subheader("This is how we create a dynamic array element.")
     df = pd.read_csv(r"C:\Users\stivi\Documents\Python Practice\learning_code\f1_drivers.csv")
     st.dataframe(df)
     
     # Component: Create a static array component.
     st.subheader("This is how we create a static array element.")    
     st.table(df.sort_values(by="Championships", ascending=False)[["Driver", "Nationality", "Championships", "Race_Wins"]].head(15))
     
# Component: Populate tab element.     
with chart_elements_tab:
     
     # Generate the mathematical data.
     x = np.linspace(3, 15, 30)
     y = np.log(x)
     statistical_data = np.random.randint(low=0, high=100, size=1000)

     # Generate the statistical data.
     dataf = pd.read_csv(r"C:\Users\stivi\Documents\Python Practice\streamlit_app\database\f1_drivers.csv")
     desired_data = dataf.loc[dataf["Championships"] >= 3].sort_values(by="Championships")
     drivers = desired_data["Driver"]
     championships = desired_data["Championships"]

     # Create figures.
     fig_1 = plt.figure(figsize=(8, 3), dpi=900, facecolor="#E5E4E2")
     fig_2 = plt.figure(figsize=(8, 3), dpi=900, facecolor="#E5E4E2")

     # Create axes.
     ax1 = fig_1.add_axes([0.1, 0.1, 0.35, 0.9])
     ax2 = fig_1.add_axes([0.5, 0.1, 0.35, 0.9])
     ax3 = fig_2.add_axes([0.1, 0.1, 0.9, 0.9])

     # Specify the background color.
     ax1.set_facecolor("#E5E4E2")
     ax2.set_facecolor("#E5E4E2")
     ax3.set_facecolor("#E5E4E2")

     # Add the visualizations to the axes.
     ax1.plot(x, y, label='y = log(x)', color='#515a5a', linewidth=2, linestyle='-')
     ax2.boxplot(statistical_data, labels=["Data"], notch=True)  # Fixed: using statistical_data
     ax3.barh(y=drivers.values, width=championships.values, color='#515a5a')

     # Specify axis titles and other properties
     ax1.set_title("y = log(x)")
     ax2.set_title("Data Distribution")
     ax3.set_title("F1 World Champions", color="black")

     ax1.set_xlabel("x")
     ax1.set_ylabel("y")
     ax3.set_xlabel("Championships", color="black")
     ax3.set_ylabel("Drivers", color="black")

     ax3.tick_params(axis='both', colors='black')

     ax1.grid(True)
     ax2.grid(True)
     ax3.grid(True)

     ax1.legend()

     # Create the chart elements
     st.pyplot(fig_1)
     st.pyplot(fig_2)

     # Clear the current figures to prevent memory issues
     plt.close(fig_1)
     plt.close(fig_2)

# Component: Populate tab element.
with media_elements_tab:
     
     # Component: Create column elements.
     col_1, col_2 = st.columns(2)
     col_3, col_4 = st.columns(2)
     
     # Component: Populate column element.
     with col_1:
          with st.container(border=True):
               # Component: Create internal image element.
               with open(r"C:\Users\stivi\Documents\Python Practice\streamlit_app\assets\steve.jpg", "rb") as internal_image:
                    internal_image = internal_image.read()
                    st.image(internal_image, caption="This is Steve", use_container_width=True)
     
     # Component: Populate column element.
     with col_2:
          with st.container(border=True):
               # Component: Create external image element.
               st.image(r"https://olmsted.org/wp-content/uploads/2023/06/Main-Quad-from-Palm-Dive-by-Linda-Cicero.png", caption="This is his dream school", use_container_width=True)
     
     # Component: Populate column element.
     with col_3:
          with st.container(border=True):
               with open(r"C:\Users\stivi\Documents\Python Practice\streamlit_app\assets\sample_video.mp4", "rb") as internal_video:
                    internal_video = internal_video.read()
                    st.video(internal_video, autoplay=False, loop=False)

     # Component: Populate column element.
     with col_4:
          with st.container(border=True):
                    st.video(r"https://www.youtube.com/watch?v=pz6wfRN0q_k", autoplay=False, loop=False)
     
     # Component: Add internal audio element.
     with open(r"C:\Users\stivi\Documents\Python Practice\streamlit_app\assets\simple-piano-reverse-logo-201061.mp3", "rb") as internal_audio:
          internal_audio = internal_audio.read()
          st.audio(internal_audio, autoplay=False, loop=False)

# Component: Populate tab element.
with special_elements_tab:
     
     # Component: Create a map element.
     st.text("This is a type of map we can generate:")
     map_data = {'lat': [40.231092,], 'lon': [20.359585,]}
     loc = pd.DataFrame(map_data)
     st.map(loc, zoom=15, size=15)
     
     # Component: Create a map element.
     st.text("This is another type of map that we can generate:")
     coordinates = [40.231092, 20.359585]  # Store coordinates in a variable for consistency
     m = folium.Map(location=coordinates, zoom_start=17)  # Adjusted zoom level
     folium.Marker(coordinates, popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)
     st_data = st_folium(m, width="100%", height=400)  # Changed width to percentage

     # Component: Create divider element.
     st.divider()

     # Component:Create metric element.
     left, center, right = st.columns(3)
     
     with left:
          st.metric("Speed", "175 kmh", delta=10, border=True)
     with center:
          st.metric("G-Force", "2.5", delta=-3, border=True)
     with right:
          st.metric("Tire Pressure", "35 psi", delta=0, border=True)
     
     # Component: Create an info box element.
     st.text("In Streamlit, we can create information box elements:")
     st.info("Please provide your personal details below.", icon=":material/info:")
     
     # Component: Create a warning box element.
     st.text("In Streamlit, we can create warning box elements:")
     st.warning("Note: the file cannot be edited after it has been uploaded.", icon=":material/warning:")
     
     # Component: Create a success box element.
     st.text("In Streamlit, we can create success box elements:")
     st.success("Your answers are now saved.", icon=":material/task_alt:")
     
     # Component: Create an error box element.
     st.text("In Streamlit, we can create error box elements:")
     st.error("The server is not responding.", icon=":material/error:") 
     
     # Component: Create a link button element.
     st.link_button(
          label="Explore More Streamlit Components",
          url="https://streamlit.io/components",
          icon=":material/web_stories:",
          use_container_width=True
     )
