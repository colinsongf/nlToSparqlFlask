#!/usr/bin/env python
import quepy
from flask import Flask, request
from SPARQLWrapper import SPARQLWrapper, JSON
app = Flask(__name__)

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
dbpedia = quepy.install("dbpedia")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getSparql")
def getSparql():
    question = request.args.get('question', ' ')
    target, query, metadata = dbpedia.get_query(question)
    return query

@app.route("/search")
def search():
    query = request.args.get('q', ' ')
    if query:
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
    return results

@app.route("/both")
def both():
    question = request.args.get('question', ' ')
    target, query, metadata = dbpedia.get_query(question)
    print query
    if query:
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        print results
    return results


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

