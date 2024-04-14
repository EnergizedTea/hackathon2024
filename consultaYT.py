import webbrowser

def buscar_en_youtube(consulta):
    url = f"https://www.youtube.com/results?search_query={consulta}&sp=CAASAhAB,EgIQAg%3D%3D"
    webbrowser.open(url)
