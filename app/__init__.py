"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="postgres:dpg-chaaqc3hp8u791gvvjsg-a.oregon-postgres.render.com",
        database="todo_list_mg00",
        user="todo_list_mg00_user",
        password="2ooNGKsMJVHe5oHzdM97mwjsqvMVwpZl")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
