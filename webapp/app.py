from flask import send_file, Flask
from uzman import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/prediction/<my_text>")
def home(my_text):
    prepare()
    return predict(my_text)

@app.route("/export_graph")
def export_graph_from():
    return export_graph()

@app.route("/export_heatmap")
def export_heatmap_from():
    return export_heatmap()

@app.route('/plot', methods=['GET'])
def plot():
#     fig, ax = plt.subplots()
#     ax.plot([1, 2, 3, 4])
    export_heatmap()
    return send_file("heatmap.png")


# @app.route('/plot')
# def plot():
#     fig, ax = plt.subplots()
#     ax.plot([1, 2, 3, 4])
#     return fig_to_response(fig)

# def fig_to_response(fig):
#     png_output = io.BytesIO()
#     FigureCanvas(fig).print_png(png_output)
#     response = make_response(png_output.getvalue())
#     response.headers['Content-Type'] = 'image/png'
#     return response */

if __name__ == '__main__':
    app.run()