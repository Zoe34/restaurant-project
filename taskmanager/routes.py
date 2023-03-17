from flask import Flask, render_template
from taskmanager import app, db
from flask_sqlalchemy import SQLAlchemy
from taskmanager.models import Category, Task

