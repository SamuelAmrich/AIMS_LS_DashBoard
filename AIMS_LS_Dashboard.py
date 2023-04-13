#!/usr/bin/env python
# coding: utf-8

# # Úvodné Importy

# In[1]:


# Zvacsenie okien prostredia - Odstránit v produkcii

from IPython.core.display import display, HTML
import datetime

display(HTML("<style>.container { width:98% !important; }</style>"))


# In[2]:


# Import vsetkych prerequisities
from requirements import *

# Import vlastnej kniznice
from AIMS_LS_library import *


# # Nastanenie grafiky a iných
# Načítaním z config súborov

# In[3]:


# Nastavenie farebnosti
from config.colours import *

# Nastavenie fontov
from config.fonts import *

# Nastavenie velkosti
from config.sizes import *

# Nastavenie Casovania
from config.timings import *


# # Startovacie nastavenia

# In[4]:


plt.rcParams["ytick.right"] = plt.rcParams["ytick.labelright"] = True
plt.rcParams["ytick.left"] = plt.rcParams["ytick.labelleft"] = False
plt.rcParams.update({"font.size": 50})

plt.rcParams.update({
    "figure.facecolor": (1, 1, 1, 0),
    "axes.facecolor": (1, 1, 1, 0),
    "savefig.facecolor": (1, 1, 1, 0),
})

plt.rcParams["text.color"] = text_colour
plt.rcParams["axes.labelcolor"] = text_colour
plt.rcParams["xtick.color"] = text_colour
plt.rcParams["ytick.color"] = text_colour


# # Vytvorenie DASH prostredia

# In[5]:


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# # Vytvorenie blokov
# 
# Predpŕiprava layout-u pre DASH, kde sa povie kde sa čo nachádza a aké parametre (veľkosť, farbu, a pod.) to má mať.

# In[6]:


# 0 - 0

blok_0_0 = [
    dcc.Graph(id="graph_0_0",
              responsive=True,
              style={
                  "height": "30vh",
                  "width": "60vw"
              })
]


# In[7]:


# 1 - 0

blok_1_0 = [
    html.Img(id="graph_1_0", style={"height": "26vh"}),
    html.P(id="text_1_0",
           style={
               "width": "100%",
               "height": "4vh",
               "background-color": blok_pozadie,
               "color": text_colour,
               "fontSize": text_velkost,
               "textAlign": "center",
               "family": graf_text_font
           })
]


# In[8]:


# 0 - 1

blok_0_1 = [
    html.Img(id="graph_0_1", style={"height": "26vh"}),
    html.P(id="text_0_1",
           style={
               "width": "100%",
               "height": "4vh",
               "background-color": blok_pozadie,
               "color": text_colour,
               "fontSize": text_velkost,
               "textAlign": "center",
               "family": graf_text_font
           })
]


# In[9]:


# 1 - 1

blok_1_1 = [
    html.Img(id="img_1_1", style={"height": "26vh"}),
    html.Img(id="graph_1_1", style={"height": "26vh"}),
    html.P(id="text_1_1",
           style={
               "width": "100%",
               "height": "4vh",
               "background-color": blok_pozadie,
               "color": text_colour,
               "fontSize": text_velkost,
               "textAlign": "center",
               "family": graf_text_font
           })
]


# In[10]:


# 2 - 1

blok_2_1 = [
    html.Img(id="img_2_1",
             style={
                 "height": "26vh",
                 "textAlign": "center",
                 "marginLeft": "auto",
                 "marginRight": "auto"
             }),
    html.P(id="text_2_1",
           style={
               "width": "30vw",
               "height": "4vh",
               "background-color": blok_pozadie,
               "color": text_colour,
               "fontSize": text_velkost,
               "textAlign": "center",
               "family": graf_text_font
           })
]


# In[11]:


# 0 - 2

blok_0_2 = [
    html.Img(id="img_0_2_0",
             style={
                 "width": "15vw",
                 "height": "26vh",
                 "background-color": blok_pozadie
             }),
    html.Img(id="img_0_2_1",
             style={
                 "width": "15vw",
                 "height": "26vh",
                 "background-color": blok_pozadie
             }),
    html.P(id="text_0_2",
           style={
               "width": "30vw",
               "height": "4vh",
               "background-color": blok_pozadie,
               "color": text_colour,
               "fontSize": text_velkost,
               "textAlign": "center",
               "family": graf_text_font
           })
]


# In[12]:


# 1 - 2

blok_1_2 = [
    html.Img(id="img_1_2_0",
             style={
                 "width": "15vw",
                 "height": "26vh",
                 "background-color": blok_pozadie
             }),
    html.Img(id="img_1_2_1",
             style={
                 "width": "15vw",
                 "height": "26vh",
                 "background-color": blok_pozadie
             }),
    html.P(id="text_1_2",
           style={
               "width": "30vw",
               "height": "4vh",
               "background-color": blok_pozadie,
               "color": text_colour,
               "fontSize": text_velkost,
               "textAlign": "center",
               "family": graf_text_font
           })
]


# In[13]:


# 2 - 2

blok_2_2 = [
    html.Img(id="img_2_2_0",
             style={
                 "width": "15vw",
                 "height": "26vh",
                 "textAlign": "center"
             }),
    html.Img(id="img_2_2_1",
             style={
                 "width": "15vw",
                 "height": "26vh",
                 "textAlign": "center"
             }),
    html.P(id="text_2_2",
           style={
               "width": "100%",
               "height": "4vh",
               "background-color": blok_pozadie,
               "color": text_colour,
               "fontSize": text_velkost,
               "textAlign": "center",
               "family": graf_text_font
           })
]


# # Spustenie DASH aplikácie
# Bloky sa pushnu do DASH-u. Taktiež sa tomu nastavia vlastnosti ako poloha, veľkosť, farebnosť a pod.

# In[14]:


app.layout = html.Div([  # zakladny DIV v ktorom su 4 podDIVy - TIMER, PAGE 1, PAGE 2, PAGE 3


    # TIMER - to bude neviditelny blok (iba na test, potom prepisat "display":  "none",)

    html.Div([
        html.Div(id='latest-timestamp', style={"padding": "20px"}),
        dcc.Interval(
            id='interval-component2',
            interval=5 * 1000,  # alebo prepisat na  - interval=Dash_Interval,
            # n_intervals=0
        )
    ], id="timer",
    style={
        "display":  "block",
        "background": uplne_pozadie,
        "color": text_colour,
        "height": "5vh",
        "width": "100vw"
    }),


# PAGE 1 layouut - viditelny hned pri spusteni

    html.Div(
    [
        dcc.Interval(
            id='interval-component',
            interval=Dash_Interval,  # in milliseconds
            n_intervals=0),
        dbc.Row(style={"height": "2.5vh"}),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(blok_0_0,
                             style={
                                 "background-color": blok_pozadie,
                                 "height": "30vh",
                                 "width": "65vw"
                             }),  # " 0 - 0 ", 
                    align="center",
                    width=8,
                ),
                dbc.Col(
                    html.Div(blok_1_0,
                             style={
                                 "background-color": blok_pozadie,
                                 "height": "30vh",
                                 "width": "30vw"
                             }),  # " 1 - 0 ", 
                    align="center",
                    width=4,
                ),
            ],
            align="center",
            justify="evenly",
        ),
        dbc.Row(style={"height": "2.5vh"}),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(blok_0_1,
                             style={
                                 "background-color": blok_pozadie,
                                 "height": "30vh",
                                 "width": "30vw"
                             }),  # " 0 - 1 ", 
                    align="center",
                    width=4,
                ),
                dbc.Col(
                    html.Div(blok_1_1,
                             style={
                                 "background-color": blok_pozadie,
                                 "height": "30vh",
                                 "width": "30vw"
                             }),  # " 1 - 1 ", 
                    align="center",
                    width=4,
                ),
                dbc.Col(
                    html.Div(blok_2_1,
                             style={
                                 "background-color": blok_pozadie,
                                 "height": "30vh",
                                 "width": "30vw"
                             }),  # " 2 - 1 ", 
                    align="center",
                    width=4,
                ),
            ],
            align="center",
            justify="evenly",
        ),
        dbc.Row(style={"height": "2.5vh"}),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(blok_0_2,
                             style={
                                 "background-color": blok_pozadie,
                                 "height": "30vh",
                                 "width": "30vw"
                             }),  #" 0 - 2 ", 
                    align="center",
                    width=4,
                ),
                dbc.Col(
                    html.Div(blok_1_2,
                             style={
                                 "background-color": blok_pozadie,
                                 "height": "30vh",
                                 "width": "30vw"
                             }),  # " 1 - 2 ", 
                    align="center",
                    width=4,
                ),
                dbc.Col(
                    html.Div(blok_2_2,
                             style={
                                 "background-color": blok_pozadie,
                                 "height": "30vh",
                                 "width": "30vw"
                             }),  # " 2 - 2 ", 
                    align="center",
                    width=4,
                ),
            ],
            align="center",
            justify="evenly",
        )
    ], id="page1",
    style={
        "display":  "block",
        "background": uplne_pozadie,
        "height": "100vh",
        "width": "100vw"
    }),

# PAGE 2 .. upravit podla potreby
html.Div([
    html.H1("PAGE2"),
    html.H1("Upravit podla potreby... Text , video, info, graphs, etc."),

], id='page2', style={'display': 'none',
                      "background": uplne_pozadie,
                      "height": "100vh",
                      "color": text_colour,
                      "width": "100vw"}),

# PAGE 3 .. upravit podla potreby
html.Div([
    html.H1("PAGE3"),
    dcc.Graph(id='graph3', style={'display': 'none'}),
    html.H1("Upravit podla potreby")

], id='page3', style={'display': 'none',
                      "background": uplne_pozadie,
                      "height": "100vh",
                      "color": text_colour,
                      "width": "100vw"})

# koniec zakladneho DIVu

],id='container',
style={
        "background": uplne_pozadie,
        "color": text_colour,
        "height": "100vh",
        "width": "100vw"}
)

# update DIVov podla timera

@app.callback(
    [Output(component_id='latest-timestamp', component_property='children'),
     Output(component_id='page1', component_property='style'),
     Output(component_id='page2', component_property='style'),
     Output(component_id='page3', component_property='style'),
     Output('interval-component2', 'n_intervals'),
     ],
    [Input('interval-component2', 'n_intervals')]
)
def update_timestamp(n):
    if n % 3 == 1:
        return [html.Span(f"{n}counts - active page :1 Last updated: {datetime.datetime.now()}")], {
            'display': 'block'}, {'display': 'none'}, {'display': 'none'}, n
    elif n % 3 == 2:
        return [html.Span(f"{n}counts - active page :2 Last updated: {datetime.datetime.now()}")], {
            'display': 'none'}, {'display': 'block'}, {'display': 'none'}, n
    else:
        return [html.Span(f"{n}counts - active page :3 Last updated: {datetime.datetime.now()}")], {
            'display': 'none'}, {'display': 'none'}, {'display': 'block'}, n





    # # Delené funkcie
# Vytvorenie callback-u na obnovu DASH-u. Funkcie ktoré načítajú parquet a vytvoria grafiky, obrázky, grafy a texty. 

# In[15]:


# 0 - 0 DEMAND


@app.callback([
    Output("graph_0_0", 'figure'),
], Input('interval-component', 'n_intervals'))
def update_0_0(n):
    dataframe = pd.read_parquet("dataframes/dataframe.parquet.gzip")

    fig_0_0 = go.Figure()

    fig_0_0.layout = {
        "width": 580,
        "height": 315,
        "title": {
            "text": "Meranie NEUTRON",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": {
                "color": graf_nazov,
                "size": graf_nazov_velkost,
                "family": graf_text_font
            }
        },
        "template": "simple_white",
        "plot_bgcolor": blok_pozadie,
        "paper_bgcolor": blok_pozadie,
        "margin": {
            "l": 20,
            "r": 20,
            "t": 20,
            "b": 20
        },
        "showlegend": True,
        "legend": {
            "x": 0,
            "y": 1,
            "bgcolor": graf_legend_pozadie,
            "bordercolor": graf_legend_okraj,
            "borderwidth": 1,
            "font": {
                "family": graf_text_font,
                "size": graf_legenda_velkost,
                "color": graf_legend_text
            }
        },
        "xaxis": {
            "color": graf_os_text,
            "linecolor": graf_os,
            "title": "Čas",
            "ticklen": 5,
            "zeroline": False,
            "rangeslider": {
                "visible": False
            },
            "tickfont": {
                "color": graf_os,
                "size": graf_os_velkost,
                "family": graf_text_font
            },
            "titlefont": {
                "color": graf_os,
                "size": graf_os_velkost,
                "family": graf_text_font
            }
        },
        "yaxis": {
            "color": graf_os_text,
            "linecolor": graf_os,
            "title": "Hustota neutrónov",
            "ticklen": 5,
            "zeroline": False,
            "tickfont": {
                "color": graf_os,
                "size": graf_os_velkost,
                "family": graf_text_font
            },
            "titlefont": {
                "color": graf_os,
                "size": graf_os_velkost,
                "family": graf_text_font
            }
        },
    }

    fig_0_0.add_trace(
        go.Scatter(
            x=dataframe["Time"],
            y=dataframe["Neutron_monitor"],
            line={
                "color": graf_seria1,
                "width": 1,
                "dash": "solid",
            },
            mode="lines",
            name="NEUTRON",
            marker={"color": graf_seria1},
        ))

    return [fig_0_0]


# In[16]:


# 1 - 0 DEMAND


@app.callback([
    Output("graph_1_0", 'src'),
    Output("text_1_0", 'children'),
], Input('interval-component', 'n_intervals'))
def update_1_0(n):

    dataframe = pd.read_parquet("dataframes/dataframe.parquet.gzip")
    Boltek_EF = np.array(dataframe["Boltek_EF"])[n]  #Nahradiť n za -1
    Boltek_EF = np.round(Boltek_EF, Boltek_EF_round)

    fig, ax = plt.subplots(figsize=(8.18, 22.88))
    bar = ax.bar(" ", Boltek_EF, width=0.5, align="edge")
    ax.set_ylim([0, 250_000])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().set_visible(False)
    plt.locator_params(axis="y", nbins=5)
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.tick_params(which="major", length=100, width=20, direction="inout")
    ax.tick_params(which="minor", length=25, width=5, direction="in")
    bar = gradientbars(bar)
    plt.close()

    #graph_1_0 = fig2img(fig)
    graph_1_0 = fig_to_uri(fig)
    text_1_0 = f" [{Boltek_EF:_} V] "

    return [graph_1_0, text_1_0]


# In[17]:


# 0 - 1 DEMAND


@app.callback([
    Output("graph_0_1", 'src'),
    Output("text_0_1", 'children'),
], Input('interval-component', 'n_intervals'))
def update_0_1(n):

    dataframe = pd.read_parquet("dataframes/dataframe.parquet.gzip")
    Temperature = np.array(dataframe["Temperature"])[n]  #Nahradiť n za -1
    Temperature = np.round(Temperature, Temperature_round)

    fig, ax = plt.subplots(figsize=(8.18, 22.88))
    bar = ax.bar(" ", Temperature, width=0.5, align="edge")
    ax.set_ylim([-50, 50])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().set_visible(False)
    plt.locator_params(axis="y", nbins=5)
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.tick_params(which="major", length=100, width=20, direction="inout")
    ax.tick_params(which="minor", length=25, width=5, direction="in")
    bar = gradientbars(bar)
    plt.close()

    graph_0_1 = fig2img(fig)
    text_0_1 = f" [{Temperature:_} °C] "

    return [graph_0_1, text_0_1]


# In[18]:


# 1 - 1 DEMAND


@app.callback([
    Output("img_1_1", 'src'),
    Output("graph_1_1", 'src'),
    Output("text_1_1", 'children'),
], Input('interval-component', 'n_intervals'))
def update_1_1(n):

    dataframe = pd.read_parquet("dataframes/dataframe.parquet.gzip")
    Wind_speed = np.array(dataframe["Wind_speed"])[n]  #Nahradiť n za -1
    Wind_speed = np.round(Wind_speed, Wind_speed_round)

    fig, ax = plt.subplots(figsize=(8.18, 22.88))
    bar = ax.bar(" ", Wind_speed, width=0.5, align="edge")
    ax.set_ylim([0, 100])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().set_visible(False)
    plt.locator_params(axis="y", nbins=5)
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.tick_params(which="major", length=100, width=20, direction="inout")
    ax.tick_params(which="minor", length=25, width=5, direction="in")
    bar = gradientbars(bar)
    plt.close()
    graph_1_1 = fig2img(fig)

    if -999 < Wind_speed <= 5.5:
        img_1_1 = Image.open("assets/veterny_tunel_0.png")
    elif 5.5 < Wind_speed <= 11:
        img_1_1 = Image.open("assets/veterny_tunel_1.png")
    elif 11 < Wind_speed <= 16:
        img_1_1 = Image.open("assets/veterny_tunel_2.png")
    elif 16 < Wind_speed <= 22:
        img_1_1 = Image.open("assets/veterny_tunel_3.png")
    else:
        img_1_1 = Image.open("assets/veterny_tunel_4.png")

    text_1_1 = f" [ {Wind_speed:_} km/h | {Wind_speed:_} m/s | {Wind_speed:_} uzol ] "

    return [img_1_1, graph_1_1, text_1_1]


# In[19]:


# 2 - 1 DEMAND


@app.callback([
    Output("img_2_1", 'src'),
    Output("text_2_1", 'children'),
], Input('interval-component', 'n_intervals'))
def update_2_1(n):

    dataframe = pd.read_parquet("dataframes/dataframe.parquet.gzip")
    Wind_direction = np.array(
        dataframe["Wind_direction"])[n]  #Nahradiť n za -1
    Wind_direction = np.round(Wind_direction, Wind_direction_round)

    img_2_1 = Image.open("assets/Hora.png")
    draw = ImageDraw.Draw(img_2_1)
    draw.polygon(
        ((150, 130 - 60), (100, 130 + 60 * np.sin(np.radians(Wind_direction))),
         (200, 130 + 60 * np.sin(np.radians(Wind_direction)))),
        fill="red",
        outline=255)

    Wind_direction_temp = int((Wind_direction / 22.5) + .5)
    directions = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW",
        "WSW", "W", "WNW", "NW", "NNW"
    ]
    smery = ["S", "SV", "V", "JV", "J", "JZ", "Z", "SZ"]
    Wind_direction_dir = directions[(Wind_direction_temp % 16)]
    Wind_direction_smer = smery[(Wind_direction_temp % 8)]

    text_2_1 = f" [ {Wind_direction:_} ° | {Wind_direction_smer} | {Wind_direction_dir} ] "

    return [img_2_1, text_2_1]


# In[20]:


# 0 - 2 DEMAND


@app.callback([
    Output("img_0_2_0", 'src'),
    Output("img_0_2_1", 'src'),
    Output("text_0_2", 'children'),
], Input('interval-component', 'n_intervals'))
def update_0_2(n):

    dataframe = pd.read_parquet("dataframes/dataframe.parquet.gzip")
    Pressure = np.array(dataframe["Pressure"])[n]  #Nahradiť n za -1
    Humidity = np.array(dataframe["Humidity"])[n]  #Nahradiť n za -1
    Pressure = np.round(Pressure, Pressure_round)
    Humidity = np.round(Humidity, Humidity_round)

    Pressure_angle = np.radians((Pressure - 100) * 60)
    img_0_2_0 = Image.open("assets/Tlakomer.png")
    draw_0_2_0 = ImageDraw.Draw(img_0_2_0)
    draw_0_2_0.polygon(((361 - 250 * np.cos(Pressure_angle),
                         361 - 250 * np.sin(Pressure_angle)), (361 - 20, 365),
                        (361 + 20, 355)),
                       fill="white",
                       outline=255)

    Humidity_angle = np.radians((Humidity - 25))
    img_0_2_1 = Image.open("assets/Vlhkomer.png")
    draw_0_2_1 = ImageDraw.Draw(img_0_2_1)
    draw_0_2_1.polygon(((361 - 250 * np.cos(Humidity_angle),
                         361 - 250 * np.sin(Humidity_angle)), (361 - 20, 365),
                        (361 + 20, 355)),
                       fill="white",
                       outline=255)

    text_0_2 = f" [ {Pressure:_} Kps | {Humidity:_} %] "
    return [img_0_2_0, img_0_2_1, text_0_2]


# In[21]:


# 1 - 2 DEMAND


@app.callback([Output("text_1_2", 'children')],
              Input('interval-component', 'n_intervals'))
def update_1_2(n):

    dataframe = pd.read_parquet("dataframes/dataframe.parquet.gzip")
    Solar_radiation = np.array(
        dataframe["Solar_radiation"])[n]  #Nahradiť n za -1
    Solar_radiation = np.round(Solar_radiation, Solar_radiation_round)

    text_1_2 = f" [ {Solar_radiation:_} W/m^2 ]    [ {Solar_radiation:_} W] "

    return [text_1_2]


# In[22]:


# 2 - 2 TO Delete


@app.callback([Output("text_2_2", 'children')],
              Input('interval-component', 'n_intervals'))
def update_2_2(n):

    dataframe = pd.read_parquet("dataframes/dataframe.parquet.gzip")
    Sevan = np.array(dataframe["Sevan"])[n]  #Nahradiť n za -1
    Sevan = np.round(Sevan, Sevan_round)

    text_2_2 = f" [ {Sevan:_}  castic/min] "

    return [text_2_2]


# # Spustenie DASH servera live

# In[23]:


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)

