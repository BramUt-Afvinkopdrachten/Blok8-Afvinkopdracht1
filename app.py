from flask import Flask, render_template, request
import re

from utils import MySQLManager

db_info = {"user": "anonymous", "host": "ensembldb.ensembl.org",
           "port": 3306, "db": "homo_sapiens_core_95_38"}

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def homepage():
    """Zoekt in de ensembldb.ensembl.org database naar een opgegeven
    zoekterm.
    """
    if request.method == "POST":
        if search_term := request.form["search_term"]:
            with MySQLManager(db_info) as cursor:
                cursor.execute(
                    f"select description "
                    f"from gene "
                    f"where description like '%{search_term}%'")
                results = cursor.fetchall()

            results = [re.split(f"({search_term})", result[0])
                       for result in results]

            return render_template("homepage.html", results=results,
                                   search_term=search_term)
    # Returnt homepage zonder resultaten als er geen zoekterm opgegeven
    # is.
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run()
